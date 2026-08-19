# birdclef-papers

A curated, automatically-updated collection of papers on **bird sound recognition**, bioacoustics, passive acoustic monitoring, and related animal-sound topics — covering the BirdCLEF / LifeCLEF competition era (2016 onwards) and growing every day.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from multiple indexes via their public APIs:
  - [arXiv](https://arxiv.org/) — preprints in cs, eess, and q-bio.
  - [Semantic Scholar](https://www.semanticscholar.org/) — broad coverage of journals and conferences not on arXiv.
  - [DBLP](https://dblp.org/) / [CEUR-WS](https://ceur-ws.org/) — LifeCLEF and BirdCLEF workshop working-notes.
  - [bioRxiv](https://www.biorxiv.org/) (via [Crossref](https://www.crossref.org/)) — ecology and bioacoustics preprints.
  - [Papers With Code](https://paperswithcode.com/) — community-curated ML papers.
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull recently submitted papers.
- Results are filtered with a negative-keyword blacklist plus a positive animal-acoustics relevance gate (birds, mammals, insects, reptiles, amphibians).
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- For arXiv papers, converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- For Semantic Scholar entries, an open-access PDF is converted with marker when one is available.
- bioRxiv, CEUR-WS working-notes, and Papers With Code entries without a fetchable source are written as metadata-only stubs (title, authors, abstract).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.
- When the paper's [Hugging Face page](https://huggingface.co/papers) links a GitHub repo, it is recorded as `github_repo` in the frontmatter.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata (`github_repo`, …) + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

```bash
# Install the pinned Prettier used by the pipeline, CI, and pre-commit
npm ci

# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2016-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch BirdCLEF Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2016 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Search terms

Papers are discovered by querying each source with the keyword sets below.

**arXiv** · `BirdCLEF` · `bird sound recognition` · `bird call recognition` · `bird song recognition` · `bird species identification audio` · `bird vocalization classification` · `avian sound classification` · `bioacoustics deep learning` · `passive acoustic monitoring birds` · `soundscape bird` · `bird audio detection` · `bird species classification spectrogram` · `ecoacoustics machine learning` · `bird call detection` · `LifeCLEF bird` · `BirdNET` · `xeno-canto` · `avian bioacoustics` · `bird acoustic identification` · `automated bird identification` · `bird sound classification deep learning` · `bird species acoustic` · `soundscape ecology machine learning` · `wildlife acoustic monitoring` · `ornithology deep learning` · `bird audio neural network` · `avian call classification` · `bird sound event detection` · `bird sound dataset` · `PAM birds` · `bird species recognition neural` · `mel spectrogram bird classification`

**Semantic Scholar** · `BirdCLEF` · `bird sound recognition` · `bird vocalization classification` · `avian bioacoustics deep learning` · `passive acoustic monitoring birds` · `LifeCLEF bird` · `BirdNET bird identification` · `bird call classification neural network` · `bird species audio identification` · `soundscape ecology bird machine learning` · `ecoacoustics bird deep learning` · `automated bird species recognition`

**DBLP / CEUR-WS** · `BirdCLEF` · `LifeCLEF bird` · `bird sound recognition CLEF` · `avian sound classification CLEF` · `bird species identification audio CLEF` · `passive acoustic monitoring LifeCLEF`

**bioRxiv** · `BirdCLEF bird sound` · `bird vocalization bioacoustics` · `passive acoustic monitoring birds` · `bird call classification` · `avian acoustic deep learning` · `bird species audio identification` · `soundscape ecology bird` · `ecoacoustics bird species`

**Papers With Code** · `BirdCLEF` · `bird sound recognition` · `bird vocalization` · `bioacoustics bird` · `passive acoustic monitoring birds` · `avian sound classification`

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 30 papers (30 of 1633 total). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [PAMalytics: a no-code application for structured validation of bioacoustic detections](https://doi.org/10.64898/2026.08.14.744822)

**Alastair Pickering, Santiago Martinez Balvanera, Nicholas Brown, Sareach Chea et al.** · 2026-08-14

<details>
<summary>Abstract</summary>

1. Passive acoustic monitoring (PAM) is increasingly used for ecological research, biodiversity monitoring, assessment, and reporting. Automated species classifiers make it feasible to process large audio datasets but generate numerous detections that often need validation before use in downstream analyses or formal outputs. 2. Method development in PAM has focused on classifier building and downstream models that account for imperfect detection, yet the practical step between these - post-classification validation - remains weakly supported and is often implemented through ad hoc workflows. This increases manual handling, creates scope for transcription or consolidation errors, limits transparency and makes it difficult to document what was reviewed. 3. We introduce PAMalytics, an open-source, no-code, local browser-based application to support post-classification validation as a standardised workflow stage. PAMalytics ingests detections from any classifier, allows users to define how detections are sampled for review, and presents selected detections alongside their spectrograms with audio playback in one unified interface. Sampling strategy and review decisions are tracked alongside reviewer identity improving traceability and reproducibility across the validation workflow. 4. Case studies with Conservation International Cambodia and Imperial College London demonstrate PAMalytics in two validation settings. In Cambodia, gibbon predictions from a large, uneven dataset were sampled within sites, with likely classifier errors prioritised for validation. At Imperial, Amazon bird detections were sampled across each species’ classifier-confidence range before biodiversity metrics were derived. In both cases, PAMalytics reduced manual handling and validation time. By turning an ad hoc step into an accessible, structured workflow for conservation practitioners, PAMalytics fills a practical gap in the PAM bioacoustics pipeline and strengthens the link between automated detections and evidence used in biodiversity monitoring and reporting.

</details>

#### [How Passive Acoustic and Traditional Monitoring Estimate Bird Diversity Across Habitats](https://doi.org/10.1002/rse2.70098)

**Jarek Scanferla, Julia Seeber, G. Brambilla, M. Brambilla et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Bird monitoring techniques have evolved substantially in recent years. While the most common protocols remain the point count and transect survey, new technologies such as passive acoustic monitoring (PAM) are becoming increasingly popular. As more monitoring programs adopt PAM, it is crucial to understand how comparable it is with classical monitoring derived data. We compared diversity indices (i.e., species richness, Shannon diversity and Jaccard index) derived from both classical (by means of observer‐based point counts) and passive acoustic (by means of recording devices) monitoring and developed a novel estimated Shannon index based on PAM, using species‐specific confidence thresholds and detection rates. We applied the protocols at 126 sites in a heterogeneous landscape within the Italian Alps, enabling us to investigate for the first time whether the effectiveness of different monitoring schemes depends on the habitat type. We show that PAM captured approximately twice as many species as the classical point count method. The species richness estimated by both protocols was strongly correlated (r s = 0.71), but with major differences between habitat types. The difference was greater in diversity hotspots such as wetlands and meadows and lower in alpine habitats. The novel PAM‐based Shannon index was very reliable and yielded similar results to the observer‐based Shannon index, illustrating its effectiveness. Species composition differed significantly between the two protocols (average Jaccard index = 0.38). Although this study highlights the additional information that PAM can provide, bird counts remain essential as they offer further insights (e.g., breeding status) and not all species can be captured by PAM (e.g., acoustically indistinguishable). As point counts are time‐ and cost‐efficient, they will continue to play an important role in bird monitoring. Our results highlight the strengths and weaknesses of each approach and provide recommendations for future monitoring programs.

</details>

#### [Investigating Quantum-Embedded Transformers on Classical Datasets for Cross-Modality Classification](https://arxiv.org/abs/2608.06846)

**Hao-Yuan Chen** · 2026-08-07

<details>
<summary>Abstract</summary>

We test whether a parameterized quantum circuit (PQC) improves a hybrid quantum-classical model's performance on classical datasets, using an interface-matched classical map as the control while holding all other components fixed. Our architecture, Quantum-Embedded Attention (QEA), uses a learnable projector to compress backbone features into an $n_q$-dimensional angle vector, a shallow PQC to map those angles to one- and two-qubit Pauli expectations, and a classical attention decoder to produce class logits. We hypothesized the PQC would improve accuracy or seed-to-seed stability over a classical map with matched input/output dimensions. We test this with an interface-matched $2\times2$ factorial on Breast Cancer Wisconsin at $n_q\in\{4,8\}$, independently swapping the PQC for a classical map and the attention decoder for a linear head, across five paired seeds per cell. Three of four paired quantum-minus-classical $95\%$ confidence intervals include zero; the fourth, a $+1.63$ percentage-point contrast for the attention decoder at $n_q=4$, reverses sign at $n_q=8$ and does not survive correction across the four contrasts. The experiment thus shows no consistent PQC contribution and cannot establish equivalence. A five-dataset cross-modality grid shows comparable accuracy on AG~News, Breast Cancer Wisconsin, and BirdCLEF but a large deficit on CIFAR-10; these cells are not interface-matched and are interpreted descriptively. We report all planned canonical runs, distinguish current Pauli-readout results from legacy probability-readout experiments, and analyze bottleneck, simulation, finite-shot, and noise limitations. The results do not establish a quantum advantage; they demonstrate why controlled component attribution is necessary before crediting a hybrid model's performance to its quantum layer.

</details>

#### [BirdCODE: Detecting bird communication at scale](https://doi.org/10.64898/2026.07.31.742086)

**Anthony Fine, Benjamin Hoffman, David Robinson, Marius Miron et al.** · 2026-08-05

<details>
<summary>Abstract</summary>

Deep learning-based animal sound identification is regularly applied to large audio datasets for ecological monitoring and citizen science, but existing methods lack the fine temporal resolution required to extract insights into animal communication from these same datasets. Here we introduce Bird Communication Detector (BirdCODE), a deep learning model that detects and classifies the vocalizations of over 9000 bird species with precise temporal boundaries, a several hundredfold increase the number of species over previous bioacoustic sound event detection models. In extensive benchmarking, BirdCODE achieves state-of-the-art performance in detection and classification of bird sounds. Applying BirdCODE to 1.3M citizen-science recordings, we present four case studies of how BirdCODE-computed sound event boundaries can be used to carry out phylogenetic analyses, to describe geographic and temporal variation in acoustic communication, and to characterize cross-species interactions. Together, these demonstrate how BirdCODE can enable large-scale, data-driven studies of bird communication. Model code, weights, and predictions are publicly available.

</details>

#### [An Automated Population Monitoring Framework for Larus ridibundus in Kunming City Based on Improved YOLOv8 and ByteTrack](https://www.mdpi.com/1424-8220/26/15/4948/pdf?version=1785913116)

**Yonglin Che, Yucheng Zeng, Zhaoxiang Ma, Qian Xia et al.** · 2026-08-05

<details>
<summary>Abstract</summary>

The Larus ridibundus (L. ridibundus), a prominent part of Kunming’s landscape, attracts many tourists and boosts the local tourism industry. Effective population monitoring of this species matters for wetland environment evaluation, biodiversity conservation, and ecological civilization construction. Currently, L. ridibundus population statistics mainly rely on manual methods, which are labor-intensive and inefficient. To overcome these limits, we propose a deep learning (DL) framework. It automatically recognizes and counts L. ridibundus by combining CDSP2-YOLOv8n with ByteTrack, aiming to efficiently monitor their population metrics. Our framework uses the optimized YOLOv8n model to achieve excellent multi-object detection for this species. It also uses ByteTrack to effectively reduce target loss from occlusion or overlap during the birds’ flight, providing a sophisticated DL approach for population monitoring. Experimental results show the modified CDSP2-YOLOv8n model works well on the collected L. ridibundus multi-object detection dataset. Its mAP@0.5, mAP@0.5:0.95, Precision, and Recall reach 0.9705, 0.6557, 0.9685, and 0.9496, respectively. When combined with ByteTrack, the proposed framework achieved a Multiple Object Tracking Accuracy (MOTA) of 89.7% and a Multiple Object Tracking Precision (MOTP) of 83.5%. It also demonstrated superior performance in terms of IDF1, Mostly Tracked (MT), Mostly Lost (ML), and Identity Switches (IDSs). Compared to manual counting, our framework has an average accuracy of 91.58%, greatly enhancing the efficiency and accuracy of L. ridibundus population monitoring. In summary, we successfully achieved the automated recognition and counting of L. ridibundus. The proposed method accurately identifies and consistently tracks individual birds, enabling effective population counting. It provides a novel and comprehensive technical approach for the monitoring and conservation of this species and demonstrates promising potential for practical applications.

</details>

#### [Transfer Learning for Avian Bioacoustics under Sparse Positive Labels](https://arxiv.org/abs/2608.03977)

**Dhyey Patel, Yunting Yin** · 2026-08-04

<details>
<summary>Abstract</summary>

Passive acoustic monitoring is an important tool for biodiversity assessment and wildlife conservation because it supports continuous and non-invasive monitoring of species across large spatial and temporal scales. Robust monitoring remains challenging because many datasets contain sparse positive labels, where species presences may be confirmed while unannotated species cannot be assumed absent. In this work, we study transfer learning under sparse positive labels using BirdCLEF+ 2026 as a target benchmark and BirdCLEF 2021, iNatSounds, WABAD, and BirdSet as external bioacoustic sources. We introduce a multi-source reliability framework that models heterogeneous bioacoustic datasets as distinct supervision sources with differing reliability. Our approach achieves 0.584 macro average precision and 0.860 macro AUC on public BirdCLEF+ 2026 validation labels while outperforming naive source pooling strategies. The strongest gains arise from passive acoustic monitoring datasets and biologically informed source selection. Our findings suggest that transfer learning in bioacoustics is fundamentally a weak supervision and negative transfer problem.

</details>

#### [Developing a low‐cost drone‐based method for deploying and retrieving autonomous recording units in inaccessible areas](https://doi.org/10.1002/wsb.70044)

**Akshit R. Suthar, Jared A. Elmore, E. Buchholtz, T. Folk et al.** · 2026-07-29

<details>
<summary>Abstract</summary>

Autonomous Recording Units (ARUs) are increasingly used in research to support passive acoustic monitoring, but deployment in remote or inaccessible locations remains logistically challenging. Traditional manual placement is labor‐intensive, time‐consuming, potentially hazardous, and often limited to habitat edges, creating sampling biases and restricting spatial coverage. To address placement limitations in wetland systems, we developed and field‐tested a low‐cost, lightweight floating platform paired with a drone‐based deployment and retrieval system. The drone‐deployable ARU platform, constructed from inexpensive, off‐the‐shelf materials (~US $21 per unit), weighed ~560 g and was mounted with an ARU (AudioMoth) at ~1.2 m above water. The platform was designed for stability, portability, and compliance with Federal Aviation Administration Part 107 regulations. Field trials were conducted across 50 operations in various types of historical rice‐field impoundments along the South Carolina coast, which provide critical habitat for secretive marsh birds such as rails (e.g ., Rallus, Laterallus , and Porzana ) and bitterns (e.g ., Botaurus and Ixobrychus ). All 50 deployments and retrievals were successful, demonstrating the robustness of the method under diverse hydrologic and vegetative conditions. Deployment times were significantly shorter than retrieval times (median 6 vs. 9 min), with retrieval requiring greater precision for hook engagement. Operation times scaled predictably with distance: deployment increased by 0.93 min/100 m (R 2 = 0.94) and retrieval by 1.17 min/100 m (R 2 = 0.95). No platform damage or displacement was observed, as emergent vegetation was likely providing natural anchoring. Our approach offers an affordable and effective solution for expanding ARU coverage in large, inaccessible wetlands, reducing sampling bias and enhancing biodiversity monitoring. With continued advances in drone payload capacity, battery endurance, and beyond‐visual‐line‐of‐sight flight regulations, our workflow could be adapted for deploying multi‐sensor platforms (e.g., ARUs, eDNA samplers, water and air quality sensors, plant sample collectors, insect traps, and trail cameras) to support integrated biodiversity monitoring in challenging landscapes worldwide.

</details>

#### [Phylogenetic signal in marine mammal and bird vocalizations captured by audio foundation models: the limited benefit of domain-specific pretraining](https://arxiv.org/abs/2607.22458) · [📄 Read](papers/2026/2607.22458.md)

**Víctor Rincón Yepes** · 2026-07-24

<details>
<summary>Abstract</summary>

Do learned audio embeddings encode structure that nobody told them to encode? We probe four large pretrained audio models (AST, CLAP, BEATs-bio and BirdNET) with a downstream task none of them saw during training: recovering phylogenetic distance from species vocalizations. If the geometry of the embedding space tracks the tree of life, the representation is picking up something deeper than the labels the model was optimized for. We run Mantel tests across two independent radiations. In 32 marine mammal species (1,754 recordings from the Watkins Marine Mammal Sound Database) the foundation models recover strong phylogenetic signal within the 26 cetaceans (CLAP r=0.82, BEATs-bio r=0.82, AST r=0.74; all p<0.001), among the highest acoustic-phylogenetic correlations reported for any taxon. Hand-crafted MFCC features (105d) find nothing (r=0.040, p=0.338). The gap survives after PCA-projecting every embedding down to 105 dimensions, so it is not an artefact of representation size. It also survives a partial Mantel test controlling for dominant frequency (partial Mantel r=0.404, keeping 97% of the variance explained), so it is not just pitch in disguise. We repeat the analysis on 20 bird species using the Jetz et al. (2012) phylogeny, and this time add BirdNET, a classifier trained end-to-end on around 6,000 bird species. The general-purpose foundation models recover the signal again (AST r=0.55, CLAP r=0.52). The unexpected result is that neither BirdNET nor the bioacoustic BEATs-bio beat them (r around 0.32 to 0.36). Matching the training domain to the target taxon does not, by itself, help. Pretrained audio embeddings carry evolutionary information across two independent radiations, and domain-specific pretraining is not required for it to emerge.

</details>

#### [Ultra-Compact CNN Architectures for Tropical Bird Audio Detection on Microcontrollers](https://arxiv.org/abs/2607.19721) · [📄 Read](papers/2026/2607.19721.md)

**Muhammad Mun'im Ahmad Zabidi, Mohd Yamani Idna Idris, Norisma Idris** · 2026-07-22

<details>
<summary>Abstract</summary>

Passive acoustic monitoring of tropical biodiversity is bottlenecked by the storage and battery cost of continuously recording soundscapes in which bird vocalisations typically occupy less than 10% of the audio. Autonomous recording units built on low-power microcontrollers (typically ARM Cortex-M with $\leq$256 kB of RAM) address this by triggering only on likely-positive segments, but the on-device options are unsatisfying: coarse frequency-energy triggers such as Goertzel filters flood SD cards with false positives at $\sim$71% precision, whereas neural detectors developed for temperate single-species tasks are either too large to deploy or transfer poorly to species-rich tropical settings. We present DrongoNet, a family of three INT8 CNN detectors sized for this envelope and validated on a 50,000-clip, 1,677-species Southeast Asian tropical dataset (SEABAD). The headline model, DrongoNet-Micro (919 parameters, 6.26 kB, 0.9810 AUC, 98.3\% mean recall at τ = 0.35), is a drop-in replacement for the Goertzel trigger used in commodity field recorders: at α = 0.10 tropical prevalence it captures 8 pp more bird vocalisations than Goertzel and extends a 32 GB card from $\sim$28 to $\sim$45 days of monitoring. DrongoNet-Nano (5.09 kB) bounds the ultra-low-flash extreme; DrongoNet-Edge (33.06 kB, 0.9991 AUC) targets Linux SBCs. On SEABAD, Micro matches a retrained TinyChirp CNN-Mel baseline within 0.1 pp AUC at 28$\times$ fewer parameters, confirming that the family is deployment-agnostic across mel-spectrogram bird corpora but requires per-environment retraining. Full INT8 quantisation costs $<$0.12% AUC across all three variants.

</details>

#### [MetaPerch: Learning from metadata for bioacoustics foundation models](https://arxiv.org/abs/2607.14072) · [📄 Read](papers/2026/2607.14072.md)

**Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer** · 2026-07-15

<details>
<summary>Abstract</summary>

Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary supervision signals, allowing the model to leverage species-metadata correlations in its learned representation. Auxiliary metadata losses provide additional information beyond vocalizations alone that can encourage a richer, more robust representation that generalizes better to species distribution and acoustic domain shifts -- important challenges for deployment in real-world passive acoustic monitoring (PAM) settings. We introduce MetaPerch, a new foundation model that achieves strong species identification performance across multiple challenging domains and present an extensive empirical study of the effects of 9 diverse metadata sources on 17 bioacoustic datasets.

</details>

#### [Two-stage fine-tuning of HuBERT for multi-label bird species recognition in overlapping acoustic environments](https://doi.org/10.1007/s11047-026-10080-x) · [📄 Read](papers/2026/ss:14d1d80453003d899c213b311888b5851d79682f.md)

**Hailemariam Abebe Endalamaw, Chuan-Kai Yang** · 2026-07-13

<details>
<summary>Abstract</summary>

Automated recognition of bird species from audio is critical for biodiversity monitoring, yet it remains difficult in practice because field recordings often contain multiple birds vocalizing at the same time, strong environmental noise, and limited labeled data. Most existing systems either assume single-species recordings, require clean inputs, or depend on manually engineered preprocessing, such as source separation. This work introduces a novel two-stage fine-tuning framework that adapts a large self-supervised speech model (HuBERT) to the highly non-speech, polyphonic, multi-label setting of wild bird soundscapes. The proposed approach departs from conventional direct fine-tuning by using a two-stage curriculum. In Stage 1, HuBERT is fine-tuned on clean single-species recordings to learn discriminative, species-specific acoustic representations without interference. In Stage 2, the model is then transferred and further fine-tuned on synthetically constructed overlapping vocalizations, enabling it to generalize to real noisy soundscapes where multiple species co-occur. This two-stage adaptation strategy bridges the acoustic gap between human speech pretraining and avian bioacoustics, and allows robust multi-label prediction directly on overlapping audio without requiring explicit source separation. Extensive experiments on ten bird species show that the proposed two-stage HuBERT achieves an F1-score of 0.94 on overlapping recordings, outperforming (i) HuBERT variants trained only on clean or overlapping audio, and (ii) state-of-the-art CNN, RNN, graph-based, and transformer baselines reported in prior studies. These results demonstrate that two-stage self-supervised adaptation is an effective and scalable direction for real-time, multi-species bird monitoring in complex natural environments.

</details>

#### [Farmland bird diversity requires heterogeneity between and within habitats](https://doi.org/10.1007/s10980-026-02406-y) · [📄 Read](papers/2026/ss:57f26f0b3df3ca38f7872a92640ee3b0605a4193.md)

**M. K. Kasten, Thomas Hiller, Sara Tassoni, Rosalie Böhmer et al.** · 2026-07-01

<details>
<summary>Abstract</summary>

Birds are declining worldwide, with farmland birds disproportionately affected. Most studies on farmland birds focus on single habitat types, yet agriculturally dominated landscapes are mosaics composed of multiple habitat types like arable land, grassland, forests, and orchards. We aimed to understand how these habitat types jointly shape farmland bird diversity, particularly regarding local and landscape drivers of alpha and beta diversity. We used passive acoustic monitoring to survey farmland bird communities in 14 mosaic agricultural landscapes (1 km2) in southern Germany that differ in habitat diversity. In total, 224 autonomous recording units were deployed in a grid-based design with sampling intensity proportional to habitat area. Using BirdNET and manual validation, we identified 54 bird species from 2016 h of recordings collected over 4.5 months. Local species richness (alpha diversity) increased with habitat heterogeneity at both local and landscape scales. Arable sites showed the lowest alpha diversity but comparatively high within-habitat beta diversity, whereas orchards supported high alpha but low within-habitat beta diversity. Beta diversity was highest between habitat types, especially between forests and arable land, reflecting strong contrasts in their structural complexity. Generalized dissimilarity modelling showed that local predictors were more important than landscape-level predictors in explaining bird beta diversity. Habitat associations of bird species were largely consistent with ecological expectations: bird species adapted to dense vegetation occurred mainly in forest-dominated sites, while open-habitat species were associated with arable land. Species with decreasing population trends occurred across all major habitat types. At the landscape scale, gamma diversity increased strongly with landscape diversity. Maintaining habitat heterogeneity at multiple spatial scales is critical to conserve farmland bird diversity.

</details>

#### [Bird Species Detection from Audio Signals Using Transfer Learning](https://doi.org/10.22214/ijraset.2026.82931) · [📄 Read](papers/2026/ss:daad1ca06c669d654d6b7f6824a827ce251fcb3b.md)

**Trishika K, D. R** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic identification of bird species from audio recordings is an important task in ecological research and biodiversity monitoring. This study proposes a deep learning-based framework that analyzes bird sounds using signal processing and transfer learning techniques. Audio signals are first transformed into frequency-based representations such as Fast Fourier Transform (FFT) and spectrograms. The use of pre-trained networks enhances learning efficiency and improves classification performance. A comparative evaluation between FFT features and spectrogram inputs reveals that spectrogram-based representations capture richer acoustic patterns, leading to better accuracy. The proposed system demonstrates reliable performance and can be effectively used in real-time environmental monitoring applications

</details>

#### [Differential response variability of black-capped chickadees to wingbeat sounds and vocalizations.](https://doi.org/10.1242/bio.062598) · [📄 Read](papers/2026/ss:c95cd32cfc9f5239e8a22e12e1eb15120b17bc70.md)

**P. Sahu, K. Nottebrock, J. Ratch, Sarah M L Smeltz et al.** · 2026-06-11

#### [Time-frequency localization of bird calls in dense soundscapes](https://arxiv.org/abs/2606.10407) · [📄 Read](papers/2026/2606.10407.md)

**Simen Hexeberg, Fanghui Tong, H. Vishnu, M. Chitre** · 2026-06-09

<details>
<summary>Abstract</summary>

Passive acoustic monitoring enables large-scale observation of wildlife, but most bioacoustic classifiers only predict species presence in a time window without localizing vocalizations precisely in time or frequency, limiting downstream analyses. We formulate bird vocalization detection as an object detection task on spectrograms and train YOLO11 models to localize bird calls in dense tropical soundscapes from Singapore. We additionally introduce an open-source browser-based annotation tool and propose Intersection over Minimum (IoMin), an evaluation metric that better handles ambiguous acoustic boundaries than standard IoU and is better suited to the problem at hand. The best YOLO model nearly doubles baseline performance on in-distribution soundscapes from Singapore (81.8% vs. 42.1% IoMin@50 F1-score) while still outperforming the baseline on unseen out-of-distribution recordings from Hawaii (58.6% vs. 48.6%). These results suggest that object detection frameworks are a promising approach to time-frequency localization of animal vocalizations in complex soundscapes.

</details>

#### [MyGardenBird: A Machine-Learning-Ready Bird Sound Dataset for Twelve Common Malaysian Birds](https://arxiv.org/abs/2606.06975) · [📄 Read](papers/2026/2606.06975.md)

**Muhammad Mun'im Ahmad Zabidi, Mohd Yamani Idna Idris, Norisma Idris** · 2026-06-05

<details>
<summary>Abstract</summary>

Bioacoustic datasets from tropical regions remain limited, in part due to the absence of reproducible workflows for aggregating recordings from public archives. We present \textbf{MyGardenBird}, a curated dataset of bird vocalisations representing twelve common species across Peninsular Malaysia and the Indo-Malayan region. Recordings were sourced from Xeno-canto and processed through species-level filtering, manual spectrogram segmentation, and quality control checks. The primary release comprises 7,200 manually validated audio clips (16 kHz, 16-bit PCM mono WAV), balanced at 600 three-second clips per species (6.0 hours total) derived from 1,381 distinct recordings. Metadata includes geospatial coordinates, vocalisation categories, and signal-to-noise ratio (SNR) values (range: 0.83--59.18 dB; mean: 15.80 dB). A supplementary 44.1 kHz version is also provided. To mitigate data leakage, dataset partitions are defined at the source-recording level. Baseline classification experiments using convolutional neural networks on Mel-spectrograms achieved test accuracies of 92--96\%, indicating strong interspecies separability. Limitations include reliance on single-annotator curation; however, validation with BirdNET confirmed label consistency. MyGardenBird is openly available at https://doi.org/10.5281/zenodo.20306877 under a CC BY-NC-SA 4.0 licence. Complete preprocessing code accompanies the release to support reproducibility and future expansion.

</details>

#### [Forest type consistently shapes bird communities across seasons: Insights from passive acoustic monitoring](https://doi.org/10.1016/j.foreco.2026.123617) · [📄 Read](papers/2026/ss:4aef9a45ee1ab4f290b3e1e656ed4e4764478720.md)

**E. S. Felgentreff, David Singer, Markus Bernhardt-Römermann** · 2026-06-01

#### [BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks](https://arxiv.org/abs/2605.28739) · [📄 Read](papers/2026/2605.28739.md)

**Tirtharaj Dash** · 2026-05-27

<details>
<summary>Abstract</summary>

Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two features. We show two consequences of this design: First, the architecture is sparse by construction: at most $2/d$ of the weights in each BIR layer are active, where $d$ is the input dimension. Second, the model is interpretable: every trained unit keeps a stable symbolic identity, so rules can be read off the network without surrogate models. Unlike most neurosymbolic models, BIRDNet does not consume an external rule base; its structural prior is mined from the data. We evaluate BIRDNet on six transcriptomic and proteomic benchmarks. Our results show that BIRDNet stays within 0.02 AUROC of the strongest dense baseline, at a small accuracy cost, while using up to $96\times$ fewer active parameters than an architecture-matched dense MLP. First-layer rules recover known biological signatures across multiple cancer subtypes and tissue types, including canonical amplicons, lineage-defining co-expression modules, and immune-infiltration markers. Data and code are available at: https://github.com/MAHI-Group/BIRDNet.

</details>

#### [Traditional bioacoustic analyses and machine-learning methods indicate weak vocal dimorphism in four Cerrado antbird species](https://doi.org/10.1007/s10336-026-02415-3) · [📄 Read](papers/2026/ss:12379b125ff15f24f100784104a481d031179a5e.md)

**Enrico L. Breviglieri, L. S. M. Sugai, Guilherme Sementili-Cardoso, R. J. Donatelli et al.** · 2026-05-27

#### [Individual Bird Identification by Modeling Temporal Structure in Bioacoustic Embeddings](https://doi.org/10.64898/2026.05.21.727031) · [📄 Read](papers/2026/ss:65101fceb335efcb16d0624d15424e554fc4997a.md)

**J. Gallego, J. Martínez, J. D. López** · 2026-05-26

#### [SEABAD: A Tropical Bird Activity Detection Dataset for Passive Acoustic Monitoring](https://arxiv.org/abs/2605.20853) · [📄 Read](papers/2026/2605.20853.md)

**Muhammad Mun'im Ahmad Zabidi, Mohd Yamani Idna Idris, Norisma Idris** · 2026-05-20

<details>
<summary>Abstract</summary>

Passive acoustic monitoring (PAM) enables large-scale biodiversity assessment, but continuous recording generates large amounts of non-informative audio, creating challenges for storage, power consumption, and long-term edge deployment. Bird audio detection (BAD), which identifies bird vocalizations, can reduce this burden by filtering irrelevant recordings before downstream analysis. However, most BAD systems are trained on temperate datasets despite tropical soundscapes being denser, more species-rich, and acoustically unpredictable. To address this gap, we introduce SEABAD (Southeast Asian Bird Activity Detection), a dataset of 50,000 curated three-second clips from Southeast Asian soundscapes, evenly balanced between bird-present and bird-absent samples. The dataset spans 1,677 bird species and is standardized to 16 kHz mono audio for embedded and low-power inference. We developed a dual-branch curation pipeline: a six-stage positive-label workflow applied to Xeno-Canto recordings, alongside six source-specific negative-label extractions from environmental datasets. These procedures reduced class imbalance by 13.7% (Gini coefficient: 0.601 to 0.519). A manual audit of 1,000 positive clips confirmed 97.8% +/- 0.9% labeling accuracy. Baseline experiments using MobileNetV3-Small achieved 99.57% +/- 0.25% accuracy and 0.9985 +/- 0.0002 AUC across three random seeds. SEABAD and the full curation pipeline are publicly released to support tropical BAD research and energy-efficient acoustic monitoring.

</details>

#### [An Adaptive Audiovisual Fusion Method Based on Prediction Confidence for Fine Granularity Bird Species Recognition](https://doi.org/10.3390/app16105113) · [📄 Read](papers/2026/ss:0420bb273644e6322ff18037a54b409fb73d9914.md)

**Xinliang Xu, Qiming Liu, Xin Wen, Hengye Zhao et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

To address the inherent limitations of single-modality approaches in fine-grained bird species recognition, this paper proposes an adaptive audiovisual fusion method based on prediction confidence. The proposed framework comprises three core components: an image classification branch, an audio classification branch, and a confidence–adaptive fusion module. The image branch employs EfficientNet-B3 to extract fine-grained visual features through compound scaling and squeeze-and-excitation (SE) attention. The audio branch utilizes ResNet-50 to classify Mel spectrograms converted from bird vocalizations, incorporating a dense sampling inference strategy to fully exploit complete audio information. For multimodal integration, a confidence–adaptive fusion strategy is introduced that jointly considers information entropy and probability gap to dynamically assess the reliability of each modality’s prediction, thereby assigning fusion weights at the sample level without any additional trainable parameters. Experiments on the SSW60 multimodal bird recognition dataset show that the image branch achieves a Top-1 accuracy of 91.55%, outperforming ResNet-50 (89.75%) and VGG-16 (83.81%); the audio branch reaches 68.20%, surpassing AST (63.29%) and VGG-16 (53.48%); and the fused model attains 95.30% Top-1 accuracy, a 3.75 percentage-point improvement over the image-only baseline and a 0.21 percentage-point gain over the learning-based TMC fusion baseline without introducing any trainable parameters, confirming the effectiveness of the proposed method.

</details>

#### [From video to behaviour: An

LSTM
‐based approach for automated nest behaviour recognition in the wild](https://doi.org/10.1111/2041-210x.70325) · [📄 Read](papers/2026/ss:ecee39a27fe1b14c7ac50e00573719fb2fee28a7.md)
**Liliana R. Silva, André C. Ferreira, Irene Martínez-Baquero, Arlette Fauteux et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

Studies of animal behaviour usually rely on direct observations or manual annotations of video recordings. However, such methods can be very time‐consuming and error‐prone, leading to sub‐optimal sample sizes. Recent advances in deep learning show great potential to overcome such limitations. Nevertheless, most currently available behavioural recognition solutions remain focused on captivity settings. Here, we present a deployment‐focused framework to guide researchers in building behavioural recognition systems from video data, using Long Short‐Term Memory (LSTM) networks to classify behavioural sequences across consecutive frames. LSTMs allowed us to: (1) monitor nest activity by detecting the birds' presence and simultaneously classifying the type of trajectory: i.e. nest‐chamber entrance or exit; and (2) identify the behaviour performed: building, aggression or sanitation. Our framework achieved comparable error rates to human annotators while greatly outperforming them in speed. Model performance improved with challenging training instances and remained robust even with modest sample sizes. LSTM also outperformed YOLO (‘You Only Look Once’), highlighting the critical role of temporal sequence information in behavioural analysis. We demonstrate that our approach is replicable across three bird species and applicable to deployment videos, highlighting its value as a generalisable and transferable tool for long‐term studies in the wild.

</details>

#### [Identification of Erroneous Locations and Restoration of Tracks Distorted as a Result of the Spoofing of Signals from Global Navigation Satellite Systems](https://doi.org/10.19074/1814-8654-2026-52-36-70) · [📄 Read](papers/2026/ss:5d6a0dd7a5cf2f11302410a74e574ccd8971fc86.md)

**I. Karyakin** · 2026-05-03

<details>
<summary>Abstract</summary>

Global Navigation Satellite Systems (GNSS) serve as a fundamental tool in modern movement ecology; however, the transnational use of electronic warfare (EW) systems poses a critical threat to telemetry research. Targeted jamming and spoofing of navigation signals result in massive spatiotemporal track distortions, rendering raw data unsuitable for population and spatial analyses. This article analyzes existing data-cleaning tools (in R and Python) and presents three author-developed cascading algorithms (in Python) for automated anomaly identification and true trajectory reconstruction. The proposed methodology integrates deterministic kinematic heuristics (iterative filters for speed and turning angle, and an adaptive spatial deviation) with unsupervised (Isolation Forest) and supervised (Random Forest) machine learning algorithms. The reconstruction of lost route segments is carried out using time-weighted linear interpolation. Testing the algorithms on telemetry data from 26 birds of prey across four species demonstrated the high efficacy of the hybrid approach during periods of active directional migration (the filtering efficiency of distorted locations averaged 98.7±2.2%). At the same time, the algorithms showed limitations when processing data from stationary areas (nesting, wintering, and prolonged stopovers), where anomaly recognition efficiency decreased significantly (to 69.6±45.2%).

</details>

#### [Multi-grained detail-enhanced and patch-aware network based on bird sound recognition](https://doi.org/10.1016/j.engappai.2026.114274) · [📄 Read](papers/2026/ss:00250364001d845f9685fa621cf1c0a856f52a62.md)

**Lin Duan, Li-dong Yang, Dawei Niu, Yong Guo et al.** · 2026-05-01

#### [Predicting the ecological condition of grazed Australian landscapes using satellite-derived indices, patch metrics, and passive acoustic monitoring of birds](https://doi.org/10.1016/j.ecolind.2026.114862) · [📄 Read](papers/2026/ss:e16f5b192f8eb1bcce9ee3d1c5e24f98621fe81a.md)

**David K. Tucker, M. D. Scarpelli, Callan Alexander, Susan Fuller et al.** · 2026-05-01

#### [TABMON

: Design and deployment of a transnational passive acoustic monitoring network for European birds](https://doi.org/10.1111/2041-210x.70308) · [📄 Read](papers/2026/ss:dbb1a1f72d44f6b8aba4693b66bcb742793e2453.md)
**B. Cretois, Carolyn M. Rosten, J. Wiel, Cynthia Barile et al.** · 2026-04-23

<details>
<summary>Abstract</summary>

Ecological surveys are often fragmented, costly and limited in scale, leading to large and long‐standing knowledge gaps which threaten our ability to properly safeguard biodiversity. Passive acoustic monitoring (PAM) has promised to deliver automated biodiversity monitoring, but networks are rarely deployed on scales that can offer truly novel insights due to scalability and standardization challenges around collecting, managing, analysing and sharing data. Here we present the Transnational Acoustic Biodiversity Monitoring Network (TABMON), a standardized deployment of 108 autonomous sensors across Norway, the Netherlands, France and Spain along a continental bird migration route. Audio is recorded continuously, uploaded in near real‐time and processed through an automated analysis pipeline designed to support expert validation and the generation of datasets for deriving Essential Biodiversity Variables (EBVs). TABMON provides a methodological blueprint for transnational, networked PAM deployments and highlights both the opportunities and current limitations of near real‐time acoustic biodiversity monitoring at continental scales.

</details>

#### [BAGEL: Benchmarking Animal Knowledge Expertise in Language Models](https://arxiv.org/abs/2604.16241) · [📄 Read](papers/2026/2604.16241.md)

**Jiacheng Shen, Masato Hagiwara, Milad Alizadeh, Ellen Gilsenan-McMahon et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Large language models have shown strong performance on broad-domain knowledge and reasoning benchmarks, but it remains unclear how well language models handle specialized animal-related knowledge under a unified closed-book evaluation protocol. We introduce BAGEL, a benchmark for evaluating animal knowledge expertise in language models. BAGEL is constructed from diverse scientific and reference sources, including bioRxiv, Global Biotic Interactions, Xeno-canto, and Wikipedia, using a combination of curated examples and automatically generated closed-book question-answer pairs. The benchmark covers multiple aspects of animal knowledge, including taxonomy, morphology, habitat, behavior, vocalization, geographic distribution, and species interactions. By focusing on closed-book evaluation, BAGEL measures animal-related knowledge of models without external retrieval at inference time. BAGEL further supports fine-grained analysis across source domains, taxonomic groups, and knowledge categories, enabling a more precise characterization of model strengths and systematic failure modes. Our benchmark provides a new testbed for studying domain-specific knowledge generalization in language models and for improving their reliability in biodiversity-related applications.

</details>

#### [bacpipe: a Python package to make bioacoustic deep learning models accessible](https://arxiv.org/abs/2604.11560) · [📄 Read](papers/2026/2604.11560.md)

**Vincent S. Kather, Sylvain Haupert, Burooj Ghani, Dan Stowell** · 2026-04-13

<details>
<summary>Abstract</summary>

1. Natural sounds have been recorded for millions of hours over the previous decades using passive acoustic monitoring. Improvements in deep learning models have vastly accelerated the analysis of large portions of this data. While new models advance the state-of-the-art, accessing them using tools to harness their full potential is not always straightforward. Here we present bacpipe, a collection of bioacoustic deep learning models and evaluation pipelines accessible through a graphical and programming interface, designed for both ecologists and computer scientists. Bacpipe is a modular software package intended as a point of convergence for bioacoustic models. 2. Bacpipe streamlines the usage of state-of-the-art models on custom audio datasets, generating acoustic feature vectors (embeddings) and classifier predictions. A modular design allows evaluation and benchmarking of models through interactive visualizations, clustering and probing. 3. We believe that access to new deep learning models is important. By designing bacpipe to target a wide audience, researchers will be enabled to answer new ecological and evolutionary questions in bioacoustics. 4. In conclusion, we believe accessibility to developments in deep learning to a wider audience benefits the ecological questions we are trying to answer.

</details>

#### [DeepForestSound: a multi-species automatic detector for passive acoustic monitoring in African tropical forests, a case study in Kibale National Park](https://arxiv.org/abs/2604.08087) · [📄 Read](papers/2026/2604.08087.md)

**G. Dubus, Th'eau d'Audiffret, Claire Auger, Raphaël Cornette et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Passive Acoustic Monitoring (PAM) is widely used for biodiversity assessment. Its application in African tropical forests is limited by scarce annotated data, reducing the performance of general-purpose ecoacoustic models on underrepresented taxa. In this study, we introduce DeepForestSound (DFS), a multi-species automatic detection model designed for PAM in African tropical forests. DFS relies on a semi-supervised pipeline combining clustering of unannotated recordings with manual validation, followed by supervised fine-tuning of an Audio Spectrogram Transformer (AST) using low-rank adaptation, which is compared to a frozen-backbone linear baseline (DFS-Linear). The framework supports the detection of multiple taxonomic groups, including birds, primates, and elephants, from long-term acoustic recordings. DFS was trained on acoustic data collected in the Sebitoli area, in Kibale National Park, Uganda, and evaluated on an independent dataset recorded two years later at different locations within the same forest. This evaluation therefore assesses generalization across time and recording sites within a single tropical forest ecosystem. Across 8 out of 12 taxons, DFS outperforms existing automatic detection tools, particularly for non-avian taxa, achieving average AP values of 0.964 for primates and 0.961 for elephants. Results further show that LoRA-based fine-tuning substantially outperforms linear probing across taxa. Overall, these results demonstrate that task-oriented, region-specific training substantially improves detection performance in acoustically complex tropical environments, and highlight the potential of DFS as a practical tool for biodiversity monitoring and conservation in African rainforests.

</details>

</details>
<!-- PAPERS_TABLE_END -->

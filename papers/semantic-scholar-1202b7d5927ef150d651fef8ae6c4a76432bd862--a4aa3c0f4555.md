---
identifier: semantic_scholar:1202b7d5927ef150d651fef8ae6c4a76432bd862
title: Towards the Acoustic Monitoring of Birds Migrating at Night
authors:
  - H. Pamula
  - Agnieszka Pocha
  - M. Kłaczyński
published: "2019-06-18T00:00:00+00:00"
url: https://biss.pensoft.net/article/36589/download/pdf/
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

![](semantic-scholar-1202b7d5927ef150d651fef8ae6c4a76432bd862--a4aa3c0f4555.figures/figure-1.webp)

![](semantic-scholar-1202b7d5927ef150d651fef8ae6c4a76432bd862--a4aa3c0f4555.figures/figure-2.webp)

#### Conference Abstract

# **Towards the Acoustic Monitoring of Birds Migrating at Night**

#### Hanna Pamula , Agnieszka Pocha , Maciej Klaczynski ‡ § ‡

- ‡ AGH University of Science and Technology in Krakow, Faculty of Mechanical Engineering and Robotics, Department of Mechanics and Vibroacoustics, al. Mickiewicza 30 30-059, Krakow, Poland
- § Jagiellonian University, Faculty of Mathematics and Computer Science, Institute of Computer Science and Computational Mathematics, Department of Machine Learning, Łojasiewicza Street 6, 30-348, Krakow, Poland

Corresponding author: Hanna Pamula ([pamulah@agh.edu.pl](mailto:pamulah@agh.edu.pl))

Received: 28 May 2019 | Published: 18 Jun 2019

Citation: Pamula H, Pocha A, Klaczynski M (2019) Towards the Acoustic Monitoring of Birds Migrating at Night.

Biodiversity Information Science and Standards 3: e36589.<https://doi.org/10.3897/biss.3.36589>

#### **Abstract**

Every year billions of birds migrate between their breeding and wintering areas. As birds are an important indicator in nature conservation, migratory bird studies have been conducted for many decades, mostly by bird-ringing programmes and direct observation. However, most birds migrate at night, and therefore much information about their migration is lost. Novel methods have been developed to overcome this difficulty; including thermal imaging, radar, geolocation techniques, and acoustic recognition of bird calls.

Many bird species are detected by their characteristic sounds. This method of identification occurs more often than by direct observation, and therefore recordings are widely used in avian research. The commonly used approach is to record the birds automatically, and to manually study the bird sounds in the recordings afterwards (Furnas and Callas 2015, Frommolt 2017). However, the tagging of recordings is a tedious and time-consuming process that requires expert knowledge, and, as a result, automatic detection of flight calls is in high demand. The first experiments towards this used energy thresholds or template matching (Bardeli et al. 2010, Towsey et al. 2012), and later on the machine and deep learning methods were applied (Stowell et al. 2018). Nevertheless, not many studies have focused specifically on night flight calls (Salamon et al. 2016, Lostanlen et al. 2018). Such acoustic monitoring could complement daytime avian research, especially when the field recording station is close to the bird-ringing station, as it is in our project.

2 Pamula H et al

In this study, we present the initial results of a long-term bird audio monitoring project using automatic methods for bird detection. Passive acoustic recorders were deployed at a narrow spit between a lake and the Baltic sea in Dąbkowice, West Pomeranian Voivodeship, Poland. We recorded bird calls nightly from sunset till sunrise during the passerine autumn migration for 3 seasons. As a result, we collected over 3000 hours of recordings each season. We annotated a subset of over 50 hours, from different nights with various weather conditions. As avian flight calls are sporadic and short, we created a balanced set for training - recordings were divided into partially overlapping 500-ms clips, and we retained all clips containing calls and created about the same number of clips without bird sounds. Different signal representations were then examined (e.g. mel-spectrograms and multitaper). Afterwards, various convolutional neural networks were checked and their performance was compared using the area under the receiver operating characteristic curve (AUC) measure. Moreover, an initial attempt was made to take advantage of the transfer learning from image classification models. The results obtained by the deep learning methods are promising (AUC exceeding 80%), but higher bird detection accuracy is still needed. For a chosen bird species – Song thrush ( _Turdus philomelos_) – we observed a correlation between calls recorded at night and birds caught in the nets during the day. This fact, as well as the promising results from the detection of calls from long-term recordings, indicate that acoustic monitoring of nocturnal birds has great potential and could be used to supplement the research of the phenomenon of seasonal bird migration.

#### **Keywords**

acoustic monitoring, night flight calls, bird call detection, bioacoustics

## **Presenting author**

Hanna Pamula

#### **Presented at**

Biodiversity_Next 2019

### **Funding program**

AGH University of Science and Technology, Grant Number: 16.16.130.942

#### **References**

- Bardeli R, Wolff D, Kurth F, Koch M, Tauchert K-, Frommolt K- (2010) Detecting bird sounds in a complex acoustic environment and application to bioacoustic monitoring. Pattern Recognition Letters 31 (12): 1524‑1534. [https://doi.org/10.1016/](https://doi.org/10.1016/j.patrec.2009.09.014) [j.patrec.2009.09.014](https://doi.org/10.1016/j.patrec.2009.09.014)
- Frommolt K (2017) Information obtained from long-term acoustic recordings: applying bioacoustic techniques for monitoring wetland birds during breeding season. Journal of Ornithology 158 (3): 659‑668. <https://doi.org/10.1007/s10336-016-1426-3>
- Furnas B, Callas R (2015) Using automated recorders and occupancy models to monitor common forest birds across a large geographic region. The Journal of Wildlife Management 79 (2): 325‑337. <https://doi.org/10.1002/jwmg.821>
- Lostanlen V, Salamon J, Farnsworth A, Kelling S, Bello JP (2018) Birdvox-Full-Night: A Dataset and Benchmark for Avian Flight Call Detection. 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) [https://](https://doi.org/10.1109/icassp.2018.8461410) [doi.org/10.1109/icassp.2018.8461410](https://doi.org/10.1109/icassp.2018.8461410)
- Salamon J, Bello JP, Farnsworth A, Robbins M, Keen S, Klinck H, Kelling S (2016) Towards the Automatic Classification of Avian Flight Calls for Bioacoustic Monitoring. PLOS ONE 11 (11). <https://doi.org/10.1371/journal.pone.0166866>
- Stowell D, Wood M, Pamuła H, Stylianou Y, Glotin H (2018) Automatic acoustic detection of birds through deep learning: The first Bird Audio Detection challenge. Methods in Ecology and Evolution 10 (3): 368‑380. <https://doi.org/10.1111/2041-210x.13103>
- Towsey M, Planitz B, Nantes A, Wimmer J, Roe P (2012) A toolbox for animal call recognition. Bioacoustics 21 (2): 107‑125. <https://doi.org/10.1080/09524622.2011.648753>

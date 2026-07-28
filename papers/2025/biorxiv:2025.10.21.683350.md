---
arxiv_id: biorxiv:2025.10.21.683350
title:
  Decoding the physicochemical basis of taxonomy preferences in protein design
  models
authors:
  - Laura Dillon
  - Aaron Maiwald
  - Oliver Crook
submitted: "2025-10-21"
categories: []
arxiv_url: https://doi.org/10.1101/2025.10.21.683350
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-28T07:07:25+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Abstract Protein design models have transformed protein engineering by enabling computational exploration of sequence spaces far exceeding experimental capacity. Yet different models applied to identical structures generate divergent outputs. These systematic differences reflect training data characteristics rather than random variation, but their patterns and malleability remain uncharacterised. We quantified how training data modality shapes systematic preferences across six architectures. Structure-conditioned models retain minimal unexplained taxonomic variance ( &lt; 3%) after controlling for measurable protein properties, while sequence-only models show substantial residual taxonomic dependence (19-25%). This difference stems from distinct preference patterns: Structure-conditioned models favour compactness and stability, properties enriched in experimentally tractable structures; sequence-only models bias reflect organism identity more heavily when evaluating sequence quality. These systematic preferences constrain design space exploration in predictable ways. Generated sequences converge toward model-specific biophysical profiles, with both input template properties and training-derived preferences jointly determining outcomes. Fine-tuning demonstrates these patterns are malleable: training ProteinMPNN on alkaline-adapted proteins redirects preferences toward elevated isoelectric points and basic residue content while preserving structural compatibility. Systematic bias characterisation enables both prediction of design outcomes and strategic modification for target applications. As protein design tackles increasingly complex challenges, understanding how training procedures encode systematic preferences becomes essential for reliable engineering.

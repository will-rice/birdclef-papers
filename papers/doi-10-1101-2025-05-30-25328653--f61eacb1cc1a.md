---
arxiv_id: biorxiv:2025.05.30.25328653
title:
  "Revisiting VERTIGO and VERTIGO-CI: Identifying confidentiality breaches and
  introducing a statistically sound, efficient alternative"
authors:
  - Marie-Pier Domingue
  - Jean-François Ethier
  - Jean-Philippe Morissette
  - Simon Lévesque
  - Anita Burgun
  - Félix Camirand Lemyre
submitted: "2025-05-31"
categories: []
arxiv_url: https://doi.org/10.1101/2025.05.30.25328653
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-28T07:07:38+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Abstract Background Health Data Research Network Canada is tasked with facilitating large-scale health data research, such as statistical analyses that integrate, within a single model, data collected by different organizations, each holding distinct subsets of features corresponding to the same individuals, thereby forming a vertical data partition. To support logistic regression analyses in this setting, we assessed two recently proposed algorithms, VERTIGO and VERTIGO-CI, which enable parameter estimation and confidence interval computation, respectively, with respect to three aspects: the risk of re-identifying patient feature data, communication efficiency, and the extent to which model interpretability is preserved. This study has three main objectives: (1) highlighting confidentiality issues that arise with VERTIGO-CI, as well as those that may occur with VER-TIGO when a data node holds only binary covariates; (2) reducing the number of required communication rounds; and (3) proposing an alternative (RidgeLog-V) to VERTIGO that excludes the intercept from the penalty term, which VER-TIGO otherwise includes. Methods We inspected the quantities exchanged in the original algorithms and used linear algebra to identify reverse-engineering procedures that the coordinating center could employ to reconstruct raw data. We also analyzed the objective function of the optimization problem, leading to the proposal of an alternative formulation that requires only a single round of communication while allowing the intercept to be excluded from the penalty term. Results We showed that, when the VERTIGO-CI algorithm is executed, the coordinating center can reconstruct all individual-level data using simple vectormatrix operations. When the VERTIGO algorithm is executed and a data node has binary covariates only, the coordinating center may be able to recover individual data when parameter estimates are shared. We adapted the VERTIGO algorithm to reduce the number of communications and proposed a variant that excludes the intercept from the penalty term. Conclusions While the use of VERTIGO-CI, or of VERTIGO with binary covariates does not involve directly sharing raw data, confidentiality breaches may arise through reverse-engineering, illustrating that that the distributed nature of an algorithm does not inherently guarantee data privacy. This work also proposed a new algorithm (RidgeLog-V) that reduces operational costs and enhances model interpretability.

---
arxiv_id: ss:d0b7189298683f06a3c82d5781f55f5f8df4d99d
title:
  "From video to behaviour: an LSTM-based approach for automated nest behaviour
  recognition in the wild"
authors:
  - Liliana R. Silva
  - André C. Ferreira
  - Irene Martínez-Baquero
  - Arlette Fauteux
  - C. Doutrelant
  - R. Covas
submitted: "2026-02-25"
categories: []
arxiv_url: https://www.biorxiv.org/content/biorxiv/early/2024/10/25/2024.10.25.620052.full.pdf
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-28T07:07:14+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Studies of animal behaviour usually rely on direct observations or manual annotations of video recordings. However, such methods can be very time-consuming and error-prone, leading to sub-optimal sample sizes. Recent advances in deep-learning show great potential to overcome such limitations, nevertheless, most currently available behavioural recognition solutions remain focused on captivity settings. Here, we present a deployment-focused framework to guide researchers in building behavioural recognition systems from video data, using Long Short-Term Memory (LSTM) networks to classify behavioural sequences across consecutive frames. LSTMs allowed to: 1) monitor nest activity by detecting the birds’ presence and simultaneously classifying the type of trajectory: i.e., nest-chamber entrance or exit; and 2) identify the behaviour performed: building, aggression or sanitation. Using our framework, we outperformed human annotators when jointly considering error and speed. Model performance improved with challenging training instances, and remained robust even with modest sample sizes. LSTM also outperformed YOLO (“You Only Look Once”), highlighting the critical role of temporal sequence information in behavioural analysis. We demonstrate that our approach is replicable across three bird species and applicable to deployment videos, highlighting its value as a generalizable and transferable tool for long-term studies in the wild. DATA AVAILABILITY Scripts, models, and data required to reproduce this work are available on Zenodo (DOIs: 10.5281/zenodo.18681623 and 10.5281/zenodo.18695178).

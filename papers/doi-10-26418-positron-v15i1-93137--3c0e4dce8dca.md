---
arxiv_id: ss:463b7909593621646053527943ef5e2aa96f09b6
title:
  Automatic Recognition of Pelung and Canary Bird Sounds Using Machine Learning
  and Signal Enhancement
authors:
  - Dyah Kurniawati
  - N. Kadarisman
  - Sumarna Sumarna
  - Agus Purwanto
submitted: "2025-05-31"
categories: []
arxiv_url: https://doi.org/10.26418/positron.v15i1.93137
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

Bird sound classification is a valuable tool in ecological monitoring and species identification, particularly for non-invasive assessment in natural environments. However, challenges such as limited labeled data and environmental noise often reduce the reliability of classification models. This study presents a lightweight bird sound classification pipeline that integrates signal preprocessing, audio augmentation, and machine learning to address these issues. Two bird species with distinct vocal characteristics, Pelung (a crossbreed involving Bangkok chickens) and Canary (Serinus canaria), were used as case subjects. A total of 40 original 2-second audio clips were extracted from longer field recordings, then processed through frame-based energy attenuation, bandpass filtering (1–8 kHz), and RMS normalization. Ten augmentation techniques were applied to each original file to improve generalization, generating 400 augmented files for model training. Feature extraction was performed using 13-dimensional Mel Frequency Cepstral Coefficients (MFCCs), and Principal Component Analysis (PCA) was used to visualize the effect of filtering. Classification was conducted using a Support Vector Machine (SVM) with a radial basis function (RBF) kernel. Results showed that filtering improved classification accuracy from 90% to 95% on the original data. Furthermore, using only augmented data for training and original data for testing yielded 100% classification accuracy, demonstrating excellent generalization. This study highlights the effectiveness of combining adaptive preprocessing and augmentation for reliable bird sound classification under limited and noisy conditions.

---
arxiv_id: ss:fe9100eb09c15e3dad38ac3cb92200ee5cb6b8fd
title:
  Lightweight MCU Implementation (Under 512KB Flash and 256KB RAM) of Neural
  Networks for Bird Call Classification
authors:
  - Jingwei Chen
  - Terry Tao Ye
submitted: "2025-08-13"
categories: []
arxiv_url: https://doi.org/10.1109/HPCC67675.2025.00161
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-28T07:07:33+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Neural network implementation on resourceconstrained MCUs for edge devices had always been a challenging task, where both the computation logics as well as parameter storage have to be counted and utilized efficiently. In this paper, we propose techniques including lightweight architectural modifications, mixed-precision quantization, and knowledge distillation to implement a complete neural network under tightly budgeted hardware resources. An optimized SqueezeNet network, called BirdCallNet is constructed for bird call classification and used as a case study to demonstrate these techniques. The bird call Mel spectrograms are resized to $112 \times 112$ single-channel inputs, and the model was quantized (with symmetric quantization for weights and asymmetric quantization for activations) through ONNX Runtime from FP32 to INT8. The architecture is refined by replacing standard convolutions with time-frequency separable convolutions and integrating efficient channel attention (ECA) blocks, further improving performance under tight constraints. The BirdCallNet can be successfully executed on a 32-bit microcontroller (STM32H743IIT6) with only $\mathbf{5 1 2 K B}$ (around $\mathbf{4 3 8 K B}$) flash and 256 KB (around 228 KB) of RAM, with the performance comparable to other implementations with much more hardware overhead. A Python-based GUI is built that allows audio files to be transformed into Mel spectrograms for real-time processing. The techniques proposed in this paper could be used as guidelines for neural network implementation on edge devices.

---
arxiv_id: biorxiv:2025.08.11.669530
title: "BATSY4-PRO: An Open-Source Multichannel Ultrasound Recorder for Field Bioacoustics"
authors:
  - Ravi Umadi
submitted: "2025-08-15"
categories: []
arxiv_url: https://doi.org/10.1101/2025.08.11.669530
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

A bstract Behavioural studies of acoustic communication in animals—particularly echolocating bats—require lightweight, power-efficient recording systems robust under field conditions. High-frequency multichannel recordings typically use consumer-grade audio interfaces and laptops, limiting portability and reproducibility. Recent advances in embedded microcontrollers and MEMS microphones enable the development of compact, affordable, open-source alternatives, yet such platforms remain underutilised for multichannel ultrasonic research. To address this gap, I developed B atsy4 -P ro , a four-channel ultrasonic recorder based on the Teensy 4.1 microcontroller. The system uses WM8782 analogue-to-digital converters for synchronised 192 kHz audio recording to microSD storage. The firmware enables customisation of buffering, triggering, and recording modes and durations. The system weighs under 150 g and operates from a 5 V DC supply for reliable field deployment. A key feature is real-time heterodyne monitoring via an integrated digital-to-analogue converter, providing audible down-conversion of ultrasonic calls through headphones. This allows researchers to assess activity during deployment and make informed decisions about when to record, thereby improving data relevance and experimental efficiency without additional bat detectors or spectrogram systems. Performance was validated using synthetic bat calls and field recordings of free-flying bats. Analysis of 368 echolocation calls yielded a median maximum-channel SNR of 27.3 dB, matching that obtained with a professional-grade audio interface. The four-channel array enabled three-dimensional localisation via time-difference-of-arrival methods. Monte Carlo simulations were used to quantify localisation uncertainty as a function of source position and motion. Within the evaluated near-field region (&lt;4 m), localisation accuracy was governed primarily by array geometry and range. Source velocity did not influence median localisation error; however, increasing flight speed systematically altered the shape of error distributions, increasing the occurrence of larger deviations beyond narrow accuracy thresholds. Together, these results provide practical guidance for selecting array geometry and defining usable operating volumes in experiments involving moving sound sources. B atsy4 -P ro provides an accessible platform for multichannel ultrasonic recording in behavioural and ecological research. Through open hardware, documented firmware, and performance characterisation, this system reduces technical barriers and promotes the adoption of spatial acoustic methods in field studies.

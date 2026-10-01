---
identifier: semantic_scholar:7b1e09cca08290f3504f5409fd85db21126d29ae
title: An AI-based Wild Animal Detection System and Its Application
authors:
  - Congtian Lin
  - Jiangning Wang
  - Liqiang Ji
published: "2023-09-11T00:00:00+00:00"
url: https://biss.pensoft.net/article/112456/download/pdf/
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

![](semantic-scholar-7b1e09cca08290f3504f5409fd85db21126d29ae--628ac5bd39b5.figures/figure-1.webp)

![](semantic-scholar-7b1e09cca08290f3504f5409fd85db21126d29ae--628ac5bd39b5.figures/figure-2.webp)

#### Conference Abstract

# **An AI-based Wild Animal Detection System and Its Application**

Congtian Lin , Jiangning Wang , Liqiang Ji ‡,§ ‡ ‡

- ‡ Institute of Zoology, Chinese Academy of Sciences, Beijing, China
- § National Basic Science Data Center, Beijing, China

Corresponding author: Congtian Lin [\(linct@ioz.ac.cn](mailto:linct@ioz.ac.cn)), Liqiang Ji [\(ji@ioz.ac.cn](mailto:ji@ioz.ac.cn))

Received: 09 Sep 2023 | Published: 11 Sep 2023

Citation: Lin C, Wang J, Ji L (2023) An AI-based Wild Animal Detection System and Its Application. Biodiversity Information Science and Standards 7: e112456. <https://doi.org/10.3897/biss.7.112456>

## **Abstract**

Rapid accumulation of biodiversity data and development of deep learning methods bring the opportunities for detecting and identifying wild animals automatically, based on artificial intelligence. In this paper, we introduce an AI-based wild animal detection system. It is composed of acoustic and image sensors, network infrastructures, species recognition models, and data storage and visualization platform, which go through the technical chain learned from Internet of Things [\(IOT\)](https://handle.itu.int/11.1002/1000/11559) and applied to biodiversity detection. The workflow of the system is as follows:

- 1. **Deploying sensors for different detection targets.** The acoustic sensor is composed of two microphones for picking up sounds from the environment and an edge computing box for judging and sending back the sound files. The acoustic sensor is suitable for monitoring birds, mammals, chirping insects and frogs. The image sensor is composed of a high performance camera that can be controlled to record surroundings automatically and a video analysis edge box running a model for detecting and recording animals. The image sensor is suitable for monitoring waterbirds in locations without visual obstructions.
- 2. **Adopting different networks according to signal availability**. Network infrastructures are critical for the detection system and the task of transferring data collected by sensors. We use the existing network when 4/5G signals are available, and build special networks using Mesh Networking technology for the areas without signals. Multiple network strategies lower the cost for monitoring jobs.

2 Lin C et al

- 3. **Recognizing species from sounds, images or videos.** AI plays a key role in our system. We have trained acoustic models for more than 800 Chinese birds and some common chirping insects and frogs, which can be identified from sound files recorded by acoustic sensors. For video and image data, we also have trained models for recognizing 1300 Chinese birds and 400 mammals, which help to discover and count animals captured by image sensors. Moreover, we propose a special method for detecting species through features of voices, images and niche features of animals. It is a flexible framework to adapt to different combinations of acoustic and image sensors. All models were trained with labeled voices, images and distribution data from Chinese species database, [ESPECIES](http://portal.especies.cn).
- 4. **Saving and displaying machine observations.** The original sound, image and video files with identified results were stored in the data platform deployed on the cloud for extensible computing and storage. We have developed visualization modules in the platform for displaying sensors on maps using [WebGIS](http://www.webgis.com/) to show curves of the number of records and species for each day, real time alerts from sensors capturing animals, and other parameters.

For storing and exchanging records of machine observations and information of sensors, and models and key nodes of network, we have proposed a collection of data fields extended from [Darwin Core](https://www.tdwg.org/standards/dwc/) and built up a data model to represent where, when and which sensors observe which species. The system has been applied in several projects since last year. For example, we have deployed 50 sensors across the city of Beijing for detecting birds, and now they have harvested more than 300 million records and detected 320 species, filling the data gaps of Beijing birds from taxonomic coverage to time dimension effectively. Next steps will focus on improving AI models for identifying species with higher accuracy, popularizing this system in biodiversity detection, and building up a mechanism for sharing and publishing machine observations.

# **Keywords**

artificial intelligence, machine observation, workflow, sensor

# **Presenting author**

Congtian Lin

#### **Presented at**

TDWG 2023

## **Acknowledgements**

We thank Yan Han, members of Institute of Zoology, CAS, for their contributions on collecting data. This job is supported by the Strategic Priority Research Program of the Chinese Academy of Sciences(Grant No. XDA19050202).

## **Hosting institution**

Institute of Zoology, CAS

# **Conflicts of interest**

The authors have declared that no competing interests exist.

---
identifier: dblp:conf/clef/Northcott14
title: Participation of Group SCS to LifeCLEF Bird Identification Challenge 2014
authors:
  - James Northcott
published: "2014-01-01T00:00:00+00:00"
url: https://ceur-ws.org/Vol-1180/CLEF2014wn-Life-Northcott2014.pdf
source: dblp
doi: null
arxiv_id: null
categories: []
---

# **Participation of group SCS to LifeCLEF bird identification challenge 2014**

James Northcott

Sales.info@wildflowersuk.com

## **1 Tasks performed**

Using the automatic call detection system based on the spectrogram correlation method within Ishmael v2.3 bi-acoustic analysis freeware [2]. Manually generated synthetic kernel [3] was created for a total of 14 audio test records and each kernel was then cross-correlated with spectrograms from the full set of 9688 audio training files. Only top 501 predictions included as per max requested. Probability not calculated by system so figure shown was an arbitrary detection function.

## **2 Main objectives of experiment**

To establish how well the spectrogram correlation automatic detection within Ishmael v2.3 [1] would perform on various birdcalls.

#### **3 Approach used**

Each test audio record requiring approx 12 hours to process. Therefore time and processing constraints limited to processing of only 14 test audio records.

The system for determining probability rank compares test audio record with all sounds within every record of the training data. Therefore initial results include multiple duplicates of the same species. In order to meet with the task requirement of 501 maximum predictions, duplicate species had to be removed, to leave only the highest prediction for each species.

# **4 Resources used**

Ishmael v2.3 http://www.bioacoustics.us/ishmael.html [1]

#### **5 Results obtained**

An overall score of zero was obtained (see graph below) which was last when compared to the other 29 submitted runs.

![](_page_1_Figure_4.jpeg)

### **6 Analysis of the results**

As mentioned in 3 above the time and processing constraints with this method limited the analysis to just 14 of the 4339 test audio records.

With these limitations, I suspect it would not have been possible to achieve an overall score above zero. As yet it has not been possible to make any assessment of where my predictions scored for the 14 audio test records that were analyzed.

## **7 Perspectives for future work**

By participating in the LifeCLEF 2014 Bird Task, I was hoping to the demonstrate that spectrogram correlation can be very useful for the automatic detection of certain bird calls. At the same time, I think my participation also demonstrates the limitations of freely available software currently available. Hopefully this may lead to improvements of existing software or the development of new software. I would consider the most useful improvements to be as follows:

- Improved detection algorithms and accuracy of automatic detection
- Improved method for quick and easy creation of synthetic kernels
- Possible combining of Spectrogram correlation with other detection methods such as energy summation to provide a more robust and accurate detection system
- More powerful and speedier processing capability.

# **Bibliography**

- 1. David K. Mellinger, Ishmael 2.3, http://www.bioacoustics.us/ishmael.html
- _2._ David K. Mellinger, Ishmael 1.0 User's guide : automatic detection
- 3. Mellinger and Clarke, 2000, construction of kernels, and their performance*.*

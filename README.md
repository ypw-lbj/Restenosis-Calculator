# Value of machine learning approach for predicting in-stent restenosis in coronary artery disease patients implanted with drug-eluting stents
![Python 3.6](https://img.shields.io/badge/python-3.7-DodgerBlue.svg?style=plastic)

## Setup
* Python 3.7.6
* scikit-learn 0.22.2

Clone this repository somewhere with:

    git clone https://github.com/ypw-lbj/Restenosis-Calculator.git
    cd Restenosis-Calculator/

Then from the base directory of this repository, install all dependencies with:

    pip install -r requirements.txt

## Data preparation
Data preparation  in this study consists of missing data imputation, data normalization, and data cleaning.

<div align=center>  <img src="images/all-abnormal.svg" alt="abnormal" width="1000" align="bottom" /> </div>
*Overview of the proposed Plug-and-Play (PnP) adaption framework for generalizing gaze estimation to a new domain.*

## Feature Rank and Selection

<div align=center>  <img src="images/featureRank.svg" alt="featureRank" width="1000" align="bottom" /> </div>
*Overview of the proposed Plug-and-Play (PnP) adaption framework for generalizing gaze estimation to a new domain.*

<div align=center>  <img src="images/featureSelect.svg" alt="featureSelect" width="800" align="bottom" /> </div>
*Overview of the proposed Plug-and-Play (PnP) adaption framework for generalizing gaze estimation to a new domain.*

## Software
we developed a calculator software based on ML model to predict ISR risk stratification, which only used the best combination of 8 features selected in the ML model. According to the predict score of this calculator, patients would be stratified in low or high risk of arising ISR at the cutoff operating point.

<div align=center>  <img src="images/figure4_1.jpg" alt="figure4_1" width="1000" align="bottom" /> </div>
*Overview of the proposed Plug-and-Play (PnP) adaption framework for generalizing gaze estimation to a new domain.*

## Demo
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/vt5fpE0bzSY)
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://www.bilibili.com/video/BV1Ur4y1U72X?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.6)

## Contact

If you have any questions, feel free to E-mail me via: `yinpengwei@stu.hit.edu.cn`

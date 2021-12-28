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
Data preparation in this study consists of missing data imputation, data normalization, and **data cleaning**.<br>
Isolation Forest was used to distinguish outliners, its corresponding code see file `abnormal_detect.py`. <br>
The following picture is an example figure, using PCA dimensionality reduction for visual display so that readers can understand the purpose of data cleaning. The red points indicate the abnormal data which were cleared out, and the white points indicate normal data which were included for analysis. There were 3 data in ISR group and 10 data in NISR group were cleaned.
<div align=center>  <img src="images/all-abnormal.svg" alt="abnormal" width="1000" align="bottom" /> </div>
<div align=center>  2D Example Image for Data Clean </div>
 

## Feature Rank and Selection
Features were selected and ranked by the contributions to outcome in every iterative decision process of the classifier, and its corresponding code see file `feature_select.py`. <br>.
<div align=center>  <img src="images/featureRank.svg" alt="featureRank" width="1000" align="bottom" /> </div>
<div align=center>  Feature Rank </div>

Relationship between the area under the curve (AUC) and number of features used to classify the dataset using LightGBM.
<div align=center>  <img src="images/featureSelect.svg" alt="featureSelect" width="800" align="bottom" /> </div>
<div align=center>  Feature Selection </div>

## Software and Demo
To better apply to clinical practice of this model, we developed the ML model as a restenosis calculator, where patients could be discriminated at high or low risk for arising ISR according to the cutoff operating point. This study calculated the sensitivity and specificity of all points on the ROC curve, and the point with the best sensitivity and specificity was assigned as the cutoff operating point. 

The video below is a result display, it contains two examples of high risk and low risk.
<div align=center>  <img src="images/anli_speed.gif" alt="anli_speed" width="800" align="bottom" /> </div>

If you want to use this software, please go to link https://github.com/ypw-lbj/Restenosis-Calculator/releases/tag/v1.1.0 and download the `RestenosisCalculator_v1.1.zip` file.
## Contact

If you have any questions, feel free to E-mail me via: `yinpengwei@stu.hit.edu.cn`

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 22:10
# @Author  : ypw
# @Email   : 1043773117@qq.com
# @File    : feature_select.py
# @Software: win10 3.7.6
import numpy as np
import lightgbm as lgb
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import RFE,RFECV,train_test_split
def select_feature(X, Y):
    Classifier = lgb.LGBMClassifier(importance_type='gain')
    importance_list = Classifier.fit(X, Y).feature_importances_
    score_list = []
    for i in range(1, X.shape[1]+1, 1):
        X_wrapper = RFE(Classifier, n_features_to_select=i,\
                    step=1).fit_transform(X, Y)
        score = cross_val_score(Classifier, X_wrapper,\
                Y, cv=10, scoring='roc_auc').mean()
        score_list.append(score)
    plt.figure(figsize=[20, 5])
    plt.plot(range(1, X.shape[1]+1, 1), score_list)
    plt.xticks(range(1, X.shape[1]+1, 1))
    plt.show()
def main():
    X = np.load('train_file')  # after data abnormal detecting
    Y = np.load('label_file')
    select_feature(X, Y)
if __name__ == '__main__':
main()

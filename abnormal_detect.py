#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 21:17
# @Author  : ypw
# @Email   : 1043773117@qq.com
# @File    : abnormal_detect.py
# @Software: win10 3.7.6
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets
from sklearn.ensemble import IsolationForest
def abnormal_visualization(X_ISR, X_NISR):
    for data in [X_ISR, X_NISR]:
        tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
        X = tsne.fit_transform(data)
        clf = IsolationForest(n_estimators=100, max_samples='auto', random_state = 1, max_features=1.0, contamination= 0.05, bootstrap=False)
        preds = clf.fit_predict(X)
        index_inliers = np.where(preds==1)
        index_outliers = np.where(preds==-1)
        larger_x = (X[:, 0].max() - X[:, 0].min()) * 0.05
        larger_y = (X[:, 1].max() - X[:, 1].min()) * 0.05
        xx, yy = np.meshgrid(
                np.linspace(X[:, 0].min()-larger_x, X[:, 0].max()+larger_x, 50),\
                np.linspace(X[:, 1].min()-larger_y, X[:, 1].max()+larger_y, 50))
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        fig, ax = plt.subplots(figsize=(16, 9))
        plt.title("Data With Isolation Forest Abnorm Detection", fontsize = 40, loc='center')
        plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)
        inl = plt.scatter(X[index_inliers][:, 0], X[index_inliers][:, 1], c='white', s=30, edgecolor='k')
        outl = plt.scatter(X[index_outliers][:, 0], X[index_outliers][:, 1], c='red',s=70, edgecolor='k')
        plt.axis('tight')
        plt.tick_params(labelsize=30)
        plt.xlim((X[:, 0].min()-larger_x, X[:, 0].max()+larger_x))
        plt.ylim((X[:, 1].min()-larger_y, X[:, 1].max()+larger_y))
        plt.legend([inl, outl],["normal", "abnormal"], loc="upper right", prop={'size': 40})
        plt.show()
def abnormal_detect(X, Y):
    clf = IsolationForest(n_estimators=121, max_samples=9, contamination=0.05, max_features=1.0, bootstrap=False,\
           n_jobs=None, random_state=None, verbose=0)
    preds = clf.fit_predict(X)
    indexs, value = np.where(np.array(preds).reshape(-1,1)==1)
    X = X[indexs]
    Y = Y[indexs]
    return X, Y
def main():
    X_ISR = np.load('X_ISR_file')
    Y_ISR = np.load('Y_ISR_file')
    X_NISR = np.load('X_NISR_file')
    Y_NISR = np.load('Y_NISR_file')
    abnormal_visualization(X_ISR, X_NISR)
    X_ISR, Y_ISR = abnormal_detect(X_ISR, Y_ISR)
    X_NISR, Y_NISR = abnormal_detect(X_NISR, Y_NISR)
if __name__ == '__main__':
    main()

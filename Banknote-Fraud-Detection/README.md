# Banknote Fraud Classification - Decision Trees from Scratch

To view the notebook without downloading anything, [go here](https://nbviewer.jupyter.org/github/Unique-Divine/Banknote-Fraud-Detection/blob/master/Banknote%20Fraud%20-%20Decision%20Tree.ipynb).

## Summary: ##
The goal of this project was to develop accurate predictive models to solve a binary classification problem, detecting  fraudulent banknotes. I figured that classifying the banknotes with decision trees written from scratch could serve as an effective technical exercise.
 
 
## Data Description:
The data was downloaded from [this source](https://archive.ics.uci.edu/ml/datasets/banknote+authentication#).
> Extracted from images were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object, gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

#### Dataset Attributes:
1. variance of Wavelet Transformed image (continuous)
2. skewness of Wavelet Transformed image (continuous)
3. curtosis of Wavelet Transformed image (continuous)
4. entropy of image (continuous)
5. class (integer)

## Next Step / To-Do:
* The decision tree is done, but I'd like to try to implement a random forest using the decision tree class. 
* Afterward, I'll turn this entire repo into a tutorial, so people won't have to struggle as much as I did to understand some of these concepts.   

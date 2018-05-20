Sentiment Analysis

Python for Data science #sentiment analyse using tensorflow#CNN#NLP#BOW 

Motivation: 
This Sentiment analysis challenge was for Datalogue recruiting
Goal: Write a neural network that can classify sentiments using a corpus in ./data/
HOWTO: Details on how to deploy these models and run them see INSTALL.md.
You can track the progress and completed tasks of this project here: Progress
I will be keeping track of my explorations and observations in this README for anyone else who wants to explore# ML-CNN-NLP-SentimentAnalyse

Requirements:
Python 3.4.3
Numpy 1.12.0
Matplotlib 1.4.3
Pandas 0.16.2
nltk 3.0.3
Scikit-learn 0.16.1
Theano 0.8.2/Tensorflow 1.0.0
Keras 1.2.2


Dataset & Preprocessing:
Currently the only supported dataset is the one provided by the Bag of Words Meets Bags of Popcorn challenge, instructions how to obtain and preprocess it can be found here
The Kaggle dataset contains 25,000 labeled examples of movie reviews. Positive movie reviews are labeled with 1, while negative movie reviews are labeled with 0. The dataset is split into 20,000 training and 5,000 validation examples

Training the network:
The model can be trained across multiple GPUs to speed up the computations. In order to start the training:
Execute

python train.py ( <== Use all available GPUs )
or
CUDA_VISIBLE_DEVICES=0,1 python train.py ( <== Use only GPU 0, 1 )

Authors:
Abonia Sojasingarayar (aboniaa@gmail.com)

*Python for Data science #sentiment analyse using tensorflow#CNN#NLP#BOW *

*Motivation: 
This project focus on a bit research towards machine learning concepts.The best businesses understand sentiment of their customers – what people are saying, how they’re saying it, and what they mean. Sentiment Analysis is the domain of understanding these emotions with software, and it’s a must-understand for developers and business leaders in a modern workplace. As with many other fields, advances in Deep Learning have brought Sentiment Analysis into the foreground of cutting-edge algorithms. Today we use natural language processing, statistics, and text analysis to extract, and identify the sentiment of text into positive, negative, or neutral categories.
I will be keeping track of my explorations and observations in this README for anyone else who wants to explore# ML-CNN-NLP-SentimentAnalyse*


Requirements:
Python 3.4.3
Numpy 1.12.0
Matplotlib 1.4.3
Pandas 0.16.2
nltk 3.0.3
Scikit-learn 0.16.1
Theano 0.8.2/Tensorflow 1.0.0
Keras 1.2.2

NOTE:I advise better to go with Anaconda navigator which will provide you 1000+ datascience packages.

IDE:
Atom(best for me)
Jupyter

Dataset & Preprocessing:
Currently the only supported dataset is the one provided by the Bag of Words Meets Bags .

Training the network:
The model can be trained across multiple GPUs to speed up the computations. In order to start the training:
Execute

python train.py ( <== Use all available GPUs )
or
CUDA_VISIBLE_DEVICES=0,1 python train.py ( <== Use only GPU 0, 1 )


*Twitter Sentiment Analyse*
This let you do sentiment analyse with tweets of public profiles in twitter.I used tweepy and textblob packages for to use twitter api and sentiment polarity and subjectivity prediction based on analysing the text in the tweets.

Author:
Abonia Sojasingarayar (aboniaa@gmail.com)

#!usr/bin/env python  
#-*- coding: utf-8 -*-  
  
import sys  
#import os  
import time  
from sklearn import metrics  
import numpy as np  
import cPickle as pickle  

reload(sys)  
sys.setdefaultencoding('utf8')  
  
# Multinomial Naive Bayes Classifier  
def naive_bayes_classifier(train_x, train_y):  
    from sklearn.naive_bayes import MultinomialNB  
    model = MultinomialNB(alpha=0.01)  
    model.fit(train_x, train_y)  
    return model  
  
  
# KNN Classifier  
def knn_classifier(train_x, train_y):  
    from sklearn.neighbors import KNeighborsClassifier  
    model = KNeighborsClassifier()  
    model.fit(train_x, train_y)  
    return model  
  
  
# Logistic Regression Classifier  
def logistic_regression_classifier(train_x, train_y):  
    from sklearn.linear_model import LogisticRegression  
    model = LogisticRegression(penalty='l2')  
    model.fit(train_x, train_y)  
    return model  
  
  
# Random Forest Classifier  
def random_forest_classifier(train_x, train_y):  
    from sklearn.ensemble import RandomForestClassifier  
    model = RandomForestClassifier(n_estimators=8)  
    model.fit(train_x, train_y)  
    return model  
  
  
# Decision Tree Classifier  
def decision_tree_classifier(train_x, train_y):  
    from sklearn import tree  
    model = tree.DecisionTreeClassifier()  
    model.fit(train_x, train_y)  
    return model  
  
  
# GBDT(Gradient Boosting Decision Tree) Classifier  
def gradient_boosting_classifier(train_x, train_y):  
    from sklearn.ensemble import GradientBoostingClassifier  
    model = GradientBoostingClassifier(n_estimators=200)  
    model.fit(train_x, train_y)  
    return model  
  
  
# SVM Classifier  
def svm_classifier(train_x, train_y):  
    from sklearn.svm import SVC  
    model = SVC(kernel='rbf', probability=True)  
    model.fit(train_x, train_y)  
    return model  
  
# SVM Classifier using cross validation  
def svm_cross_validation(train_x, train_y):  
    from sklearn.grid_search import GridSearchCV  
    from sklearn.svm import SVC  
    model = SVC(kernel='rbf', probability=True)  
    param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001]}  
    grid_search = GridSearchCV(model, param_grid, n_jobs = 1, verbose=1)  
    grid_search.fit(train_x, train_y)  
    best_parameters = grid_search.best_estimator_.get_params()  
    for para, val in best_parameters.items():  
        print para, val  
    model = SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)  
    model.fit(train_x, train_y)  
    return model  

#def read_data(data_file):  
    #import gzip  
    #f = gzip.open(data_file, "rb")  
    #train, val, test = pickle.load(f)  
    #f.close()  
    #train_x = train[0]  
    #train_y = train[1]  
    #test_x = test[0]  
    #test_y = test[1]  
    #return train_x, train_y, test_x, test_y 
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
def review_to_words(raw_review):

    review_text = BeautifulSoup(raw_review).get_text()#remove HTML tags
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)#remove punctuation
    words = letters_only.lower().split()# convert to lower letters and split to word
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if w not in stops]#remove stopwords
    
    #from nltk.stem.snowball import SnowballStemmer
    #stemmer = SnowballStemmer("english")
    #meaningful_words = stemmer.stem(meaningful_words)
    return " ".join(meaningful_words)

import pandas as pd
if __name__ == '__main__':  
    #data_file = "labeledTrainData.tsv"  
    #thresh = 0.5  
    model_save_file = None  
    model_save = {}  
    
    test_classifiers = ['LR'] 
    #test_classifiers = ['NB', 'KNN', 'LR', 'RF', 'DT', 'SVM', 'SVMCV','GBDT']  
    classifiers = {#'NB':naive_bayes_classifier,   
                  #'KNN':knn_classifier,  
                   'LR':logistic_regression_classifier,  
                   #'RF':random_forest_classifier,  
                   #'DT':decision_tree_classifier,  
                  #'SVM':svm_classifier,  
                #'SVMCV':svm_cross_validation,  
                 #'GBDT':gradient_boosting_classifier  
    }  
      
    print 'reading training and testing data...'  
    train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    test = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3)

    num_reviews = train["review"].size
    #sentiment_train = train["sentiment"].values

    clean_train_reviews = []
    print "cleaning training data..."
    for i in xrange(0, num_reviews):
        if ((i+1)%5000 == 0):
            print "review %d of %d" %(i+1, num_reviews)
        clean_train_reviews.append(review_to_words(train['review'][i]))
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    print 'extracting features on training set...'
    vectorizer = TfidfVectorizer(analyzer="word",tokenizer=None,preprocessor=None,stop_words=None,max_features=20000,
                                 sublinear_tf=True, ngram_range=(1,2))
    train_data_features = vectorizer.fit_transform(clean_train_reviews)
    #train_data_features = train_data_features.toarray()
    #train_data_features = np.asarray(train_data_features)
    #split clean_train_reviews into train and test set
    from sklearn.cross_validation import train_test_split
    train_x, test_x, train_y, test_y = train_test_split(train_data_features, train['sentiment'], test_size=0.25, random_state=0)
    num_train, num_feat = train_x.shape  
    num_test, num_feat = test_x.shape  
    is_binary_class = (len(np.unique(train_y)) == 2)  
    print '******************** Data Info *********************'  
    print '#training data: %d, #testing_data: %d, dimension: %d' % (num_train, num_test, num_feat)  
      
    for classifier in test_classifiers:  
        print '******************* %s ********************' % classifier  
        start_time = time.time()  
        model = classifiers[classifier](train_x, train_y)  
        print 'training time : %fs!' % round(time.time() - start_time, 3)  
        predict = model.predict(test_x)
        if model_save_file != None:  
            model_save[classifier] = model  
        if is_binary_class:  
            precision = metrics.precision_score(test_y, predict)  
            recall = metrics.recall_score(test_y, predict)  
            print 'precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall)  
        accuracy = metrics.accuracy_score(test_y, predict)  
        print 'accuracy: %.2f%%' % (100 * accuracy)
        from sklearn.metrics import roc_auc_score
        auc = roc_auc_score(test_y, model.predict_proba(test_x)[:,1])
        print 'auc: %.2f%%' % (100 * auc)
        
    if model_save_file != None:  
        pickle.dump(model_save, open(model_save_file, 'wb'))  

    clean_test_reviews = []
    num_test_reviews = test["review"].size
    print "cleaning test data..."
    for i in xrange(0, num_test_reviews):
        if ((i+1)%5000 == 0):
            print "review %d of %d" %(i+1, num_test_reviews)
        clean_test_reviews.append(review_to_words(test['review'][i]))
    
    #extracting features on test set
    test_data_features = vectorizer.transform(clean_test_reviews)

    #results predicting on test set and create a submission
    print 'ready to submission results...'
    t1 = time.time() 
    results = model.predict_proba(test_data_features)
    #results = results.tolist()
    print 'predicting time : %fs!' % round(time.time() - start_time, 3)
    output = pd.DataFrame(data={"id":test["id"], "sentiment":results[:, 1]})
    output.to_csv("LR_bow.csv", index=False, quoting=3) 
    print 'sucessful submission!'

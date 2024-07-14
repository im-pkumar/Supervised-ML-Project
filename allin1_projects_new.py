#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np
import os
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, mean_absolute_error, confusion_matrix
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, LabelEncoder, OrdinalEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
rm_stopword = stopwords.words("english")


# ### Height and Weight

def htnwt(height):
    df = pd.read_csv(f"{os.getcwd()}/train_hw.csv")
    df.drop('Id',axis=1,inplace=True)
    X = df[['height']]
    y = df['weight']

    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7,test_size=0.3,random_state=21)
    from sklearn.linear_model import LinearRegression
    pf = PolynomialFeatures(degree=2)
    X_new_train = pf.fit_transform(X_train)
    lr = LinearRegression()
    lr.fit(X_new_train,y_train)
    h = pf.transform(height)
    pred = lr.predict(h)
    return pred


# ### BigMart Sales Predictions

def bigmrt():
    df_train = pd.read_csv(f"{os.getcwd()}/train_bgmrt.csv")
    df_train.fillna(df_train.Item_Weight.mean(), inplace=True)
    df_train.drop(["Item_Identifier", "Outlet_Establishment_Year", "Outlet_Size"], axis = 1, inplace = True)
    col = ["Item_Fat_Content", "Item_Type", "Outlet_Identifier", "Outlet_Location_Type", "Outlet_Type"]
    global bgle
    for c in col:
        bgle = LabelEncoder()
        df_train[c] = bgle.fit_transform(df_train[c])
    X = df_train.iloc[:, :-1].values
    y = df_train.iloc[:, -1].values
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, train_size = 0.75, random_state = 11)
    global ss
    ss = StandardScaler()
    Xt_train = ss.fit_transform(X)
    #Xt_test = ss.transform(X_test)
    from sklearn.ensemble import AdaBoostRegressor
    global abr
    abr = AdaBoostRegressor(n_estimators = 8, loss = 'linear', random_state = 15)
    abr.fit(Xt_train, y)

def pred_bigmrt(X_test):
    global bgle, ss
    X_test = bgle.transform(X_test)
    Xt_test = ss.transform(X_test)
    global abr
    pred = abr.predict(Xt_test)
    return pred


#### BBC News Category Predictions


def text_cleaning(doc):
        doc = doc.lower()
        doc = re.sub(f"[{string.punctuation}]", "", doc)
        doc_splt = doc.split()
        newdoc = []
        wnl = WordNetLemmatizer()
        for token in doc_splt:
            if token not in rm_stopword:
                newdoc.append(wnl.lemmatize(token))
        return " ".join(newdoc)

def bbcnews():
    df_train = pd.read_csv(f"{os.getcwd()}/train_bbc.csv")
    X_train = df_train.Text.values
    corpus_train = list(map(text_cleaning, X_train))
    yt_train = df_train['Category'].values
    
    global tv
    tv = TfidfVectorizer()
    corpus_t_train = tv.fit_transform(corpus_train).toarray()
    global model_mb
    model_mb = MultinomialNB()
    model_mb.fit(corpus_t_train, yt_train)
    
def pred_bbcnews(sample_test_X):
    global tv
    sample_test_X = list(map(text_cleaning, sample_test_X))
    sample_test_X = tv.transform(sample_test_X).toarray()
    global model_mb
    pred = model_mb.predict(sample_test_X)
    return pred


# ### Rotten Tomatos Movies sentiment analysis


def rt():
    df = pd.read_csv(f"{os.getcwd()}/train_rt.tsv", delimiter="\t")
    df.drop(['PhraseId', 'SentenceId'], inplace =  True, axis=1)
    ret = RegexpTokenizer(r"[a-zA-Z0-9]+")
    global cv
    cv = CountVectorizer(lowercase = True, stop_words = 'english', tokenizer = ret.tokenize)
    X = cv.fit_transform(df['Phrase'])
    y = df['Sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,train_size=0.8,random_state=22)
    global mb_rt
    mb_rt = MultinomialNB()
    mb_rt.fit(X_train,y_train)
    print("Training Score: ",mb_rt.score(X_train,y_train))
    print("Testing Score: ",mb_rt.score(X_test,y_test))

def pred_rt(X_test):
    global cv, mb_rt
    X_test = cv.transform(X_test)
    pred = mb_rt.predict(X_test)
    return pred


# ### Loan Approval Prediction

def loan_apprv():
    df = pd.read_csv(f"{os.getcwd()}/train_loan_approval.csv")
    df.drop(['Loan_ID', 'Loan_Amount_Term'], axis = 1, inplace = True)
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
    df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])
    df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
    df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
    X = df[['Gender', 'Married', 'Dependents',	'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Credit_History', 'Property_Area']]
    y = df['Loan_Status']

    c = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

    global enc
    enc = OrdinalEncoder(handle_unknown = 'use_encoded_value', unknown_value = -1)
    X[c] = enc.fit_transform(X[c])

    from imblearn.over_sampling import SMOTE
    smote = SMOTE()
    X_new, y_new = smote.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size = 0.3, random_state = 15)
    global ss_la
    ss_la = StandardScaler()
    X_train = ss_la.fit_transform(X_train)
    X_test = ss_la.transform(X_test)
    from sklearn.ensemble import RandomForestClassifier
    global model_rfc
    model_rfc = RandomForestClassifier(n_estimators=18, bootstrap=True, max_features=7, max_samples=145)
    model_rfc.fit(X_train,y_train)

    pred_test = model_rfc.predict(X_test)
    acs_test= accuracy_score(y_test,pred_test)
    acs_train = accuracy_score(y_train,model_rfc.predict(X_train))
    print("Accuracy Score Train:", acs_train)
    print("Accuracy Score Test:", acs_test)

def pred_loan_apprv(X_test):
    global model_rfc, ss_la, enc
    c = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    X_test[c] = enc.fit_transform(X_test[c])
    x_test = X_test.iloc[:,:].values
    X_t_test = ss_la.transform(x_test)
    pred = model_rfc.predict(X_t_test)
    return pred


# ### IMDb Movies Reviews Sentiment Analysis and prediction

def imdb():
    df = pd.read_csv(f"{os.getcwd()}/train_imdb.csv")
    X = df['review'].values
    y = df['sentiment'].values

    X_train,X_test,y_train,y_test = train_test_split(X, y, train_size = 0.5, test_size = 0.5, random_state = 25)
    reg = RegexpTokenizer("[a-zA-Z0-9+]")
    global cv_imdb
    cv_imdb = CountVectorizer(lowercase=True, stop_words = "english", tokenizer = reg.tokenize)
    Xt_train = cv_imdb.fit_transform(X_train).toarray()
    Xt_test = cv_imdb.transform(X_test).toarray()
    global mb_imdb
    mb_imdb = MultinomialNB()
    mb_imdb.fit(Xt_train, y_train)

    pred = mb_imdb.predict(Xt_test)
    acs_train = accuracy_score(y_train, mb_imdb.predict(Xt_train))
    acs_test = accuracy_score(y_test, pred)

    print("Accuracy Score Training: ", acs_train)
    print("Accuracy Score Test: ", acs_test)

def pred_imdb(X_test):
    global cv_imdb, mb_imdb
    X_test = cv_imdb.transform(X_test)
    pred = mb_imdb.predict(X_test)
    return pred


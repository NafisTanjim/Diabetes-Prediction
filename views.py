from pickle import GET

from django.shortcuts import *
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def home(request):
    return render(request ,"home.html")
def predict(request):
    return render(request ,"predict.html")
def result (request):
    return render(request , "predict.html")

    data = pd.read_csv(r"/content/drive/MyDrive/Moury/diabetes.csv")

    X = diabetes.drop("outcome", axis=1)
    Y = diabetes['outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


    mlp = MLPClassifier(random_state=2)
    mlp.fit(X_train, Y_train)

    val1 = float (request, GET['n1'])
    val2 = float(request, GET['n2'])
    val3 = float(request, GET['n3'])
    val4 = float(request, GET['n4'])
    val5 = float(request, GET['n5'])
    val6 = float(request, GET['n6'])
    val7 = float(request, GET['n7'])
    val8 = float(request, GET['n8'])

    pred = mlp.predict([[val1,val2 ,val3,val4,val5,val6,val7,val8]])
    result2=""
    if  predict[1]:
        result2 = "Positive"
    else:
        result2 = "Negative"
    result(result2)


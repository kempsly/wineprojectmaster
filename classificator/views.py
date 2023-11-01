from django.shortcuts import render, redirect
from django.http import HttpResponse

import pandas as pd
from .backup import model
from sklearn.preprocessing import StandardScaler


# Create your views here.
def handler_view(request):
    result = [-1]
    if request.method == 'POST':
        fa = request.POST.get('fixed acidity')
        va = request.POST['volatile acidity']
        ca = request.POST['citric acid']
        rs = request.POST['residual sugar']
        ch = request.POST['chlorides']
        fsd = request.POST['free sulfur dioxide']
        tsd = request.POST['total sulfur dioxide']
        dens = request.POST['density']
        ph = request.POST['pH']
        sulp = request.POST['sulphates']
        alc = request.POST['alcohol']
        df = pd.DataFrame(columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                                   'chlorides', 'free sulfur dioxide', 'total sulfur dioxide'
            , 'density', 'pH', 'sulphates', 'alcohol'])

        df2 = {'fixed acidity': float(fa), 'volatile acidity': float(va), 'citric acid': float(ca),
               'residual sugar': float(rs),
               'chlorides': float(ch), 'free sulfur dioxide': float(fsd), 'total sulfur dioxide': float(tsd)
            , 'density': float(dens), 'pH': float(ph), 'sulphates': float(sulp), 'alcohol': float(alc)}

        data = df._append(df2, ignore_index=True)
        result = prediction(data)
    else:
        result = [-1]
    return render(request, "classificator/my-model.html", {'response': result[0]})


def prediction(data):
    data = StandardScaler().fit_transform(data)
    res = model.predict(data)
    print(res)
    return res
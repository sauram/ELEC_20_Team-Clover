from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from sklearn.externals import joblib
from django.views.generic.base import TemplateView
import math
from .models import data
from datetime import date,datetime


def prediction():
    sk=joblib.load('../Downloads/model.pkl')
    input1 = open('../Desktop/input.txt').read()
    error_msg="File is empty"
    if input1=="":
        return render(request ,'error.html',{'msg':error_msg})
    input=input1.split()
    #k=sk.predict([[input[0],input[1],input[2],input[3],input[4],input[5],input[6], input[7]]])
    k=sk.predict([input])
    k=math.exp(k) -1
    #orm=NameForm()
    #form=Edata(request.POST)

    todayf=date.today()
    #todayf=today.strftime("%B %d, %Y")
    ctimef=datetime.now()
    #ctimef=ctime.strftime("%H:%M:%S")


    fire=0
    if k>4.4:
        fire=1
    f1=data.objects.all()[::-1][0]
    
    if (str(f1.a) != input[0]) or (str(f1.b)!=input[1]) or (str(f1.c)!=input[2]) or (str(f1.d)!=input[3]) or (str(f1.e)!=input[4]) or (str(f1.f)!=input[5]) or (str(f1.g)!=input[6]) or (str(f1.h)!=input[7]):
        data1=data(a=input[0], b=input[1], c=input[2], d=input[3],today=todayf,time=ctimef,area=k,fire=1)
        data1.save()
    return fire


def enter(request):

    fire=prediction()  
    f=data.objects.all()[::-1]
    f1=f[0]
    f2=f[1]
    f3=f[2]
    args = {'f1':f1,'f2':f2,'f3':f3}
    output=open('../Desktop/output.txt','w')
    output.write(str(fire))
    return render(request ,'enter.html',args)

def list(request):

    fire=prediction()
    f3=data.objects.all()[::-1]
    args = {'f3':f3}
    output=open('../Desktop/output.txt','w')
    output.write(str(fire))
    return render(request ,'history.html',args)

class home(TemplateView):
    fire=prediction()
    template_name='home.html'

class about(TemplateView):
    fire=prediction()
    template_name='about.html'

        
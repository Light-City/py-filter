from django.shortcuts import render
import datetime
# Create your views here.
class Animal(object,):
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

def query(request):
    l=["存","正","参"]
    d={'name':'见','age':12,'sex':'M'}
    c=Animal('alex','M')
    test='world'
    test1='hello kitty'
    t=datetime.datetime.now()
    e=[]
    a='<a href=''>click</a>'
    return render(request,'index.html',locals())

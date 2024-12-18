from django.shortcuts import render,HttpResponse
from home import models

def home(req):
    return render(req,'home.html')
def home1(req):
    return HttpResponse("<h1>Home</h1>")
def about(req):
    return render(req,'about.htm')
def contact(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        content=req.POST['content']
        print(name,email,content)
        instance=models.Contact(name=name,email=email,content=content)
        instance.save()
        print("saved")
    return render(req,'contact.htm')
def projects(req):
    return render(req,"projects.htm")

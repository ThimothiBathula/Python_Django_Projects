from django.shortcuts import render,HttpResponse

def home(req):
    return render(req,'home.html')
def home1(req):
    return HttpResponse("<h1>Home</h1>")

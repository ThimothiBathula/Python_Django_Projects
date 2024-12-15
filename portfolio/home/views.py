from django.shortcuts import render,HttpResponse

def home(req):
    return render(req,'home.html')
def home1(req):
    return HttpResponse("<h1>Home</h1>")
def about(req):
    return HttpResponse("About")
def contact(req):
    return render(req,'contact.htm')
def projects(req):
    return HttpResponse("Projects")

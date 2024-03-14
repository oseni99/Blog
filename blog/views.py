from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "blog/index.html")

def posts(request):
    pass 

def posts_details(request):
    pass 



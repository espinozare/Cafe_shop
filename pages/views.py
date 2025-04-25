from django.shortcuts import render

# Create your views here.


# Create your views here.
def home(request):
    return render(request,"pages/home.html")

def about(request):
    return render(request,"pages/about.html")

def store(request):
    return render(request,"pages/store.html")
from django.shortcuts import render

def index(request):
    return render(request, 'blogs/index.html')

# Create your views here.

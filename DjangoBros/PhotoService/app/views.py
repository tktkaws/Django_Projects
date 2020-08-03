from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    return render(request, 'app/index.html')

from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def sobre_nos(request):
    return render(request, 'sobre_nos.html')

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def about(request):
    return render(request, 'about.html')
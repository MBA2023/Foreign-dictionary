from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    print(request)
    return render(request, "home.html")

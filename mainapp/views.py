from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    print(request)
    return render(request, "home.html")

def words_list(request):
    print(request)
    return render(request, "words_list.html")

def add_word(request):
    print(request)
    if request.method == "GET":
        return render(request, "add_word.html")

    else:
        print(request.POST)
        #with open("dictionary.txt", "a", encoding="utf-8") as file:
        #file.write(word1 + "-" + word2 + "\n")


def index(request):
    print(request)
    return render(request, "index.html")

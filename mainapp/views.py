from django.shortcuts import render, redirect
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
        print("первый принт", request)
        print("2 принт", request.POST)
        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.writelines(f"New word: {request.POST['new_word']}, Translation: {request.POST['translation']}, Language: {request.POST['language']} \n")
        return redirect(add_word)


def index(request):
    print(request)
    return render(request, "index.html")

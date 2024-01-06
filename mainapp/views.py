from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):
    return render(request, "home.html")

def words_list(request):
    file = open("dictionary.txt", "r", encoding="utf-8").read().splitlines()
    words_dictionary = {}
    for line in file:
        word1, word2 = line.split("-")
        words_dictionary[word1] = word2
    print(words_dictionary)
    for word in words_dictionary:
        print(word)

    return render(request, "words_list.html", words_dictionary)

def add_word(request):
    if request.method == "GET":
        return render(request, "add_word.html")

    else:
        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.writelines(f"{request.POST['word1']}-{request.POST['word2']}\n")
        return redirect(add_word)


def index(request):
    print(request)
    return render(request, "index.html")

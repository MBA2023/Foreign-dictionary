from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):
    return render(request, "home.html")

def words_list(request):
    file = open("dictionary.txt", "r", encoding="utf-8").read().splitlines()
    print(file)
    posts = []
    for line in file:
        part1, part2 = line.split(",")
        print(f"{part1}=")
        print(f"{part2}=")
        part11, part22 = part1.split(":")
        part33, part44 = part2.split(":")
        posts.append({part11:part22, part33:part44})
    print(posts)
    for word in posts:
        print(word)

    return render(request, "words_list.html", { 'words_dictionary': posts})

def add_word(request):
    if request.method == "GET":
        return render(request, "add_word.html")

    else:
        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.writelines(f"Word:{request.POST['word1']},Translation:{request.POST['word2']}\n")
        return redirect("/add_word")


def index(request):
    print(request)
    return render(request, "index.html")

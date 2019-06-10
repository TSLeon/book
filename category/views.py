from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index2.html')


def book(request, num):
    f = open('spider/novels/圣墟/简介.txt', 'r')
    resume = f.read()
    f.close()
    f = open('spider/novels/圣墟/第一章 沙漠中的彼岸花.txt', 'r')
    temp = f.readlines()
    f.close()
    contents = []
    temps = ''
    i = 0
    for content in temp:
        if i == 5:
            contents.append(temps)
            temps = ''
        else:
            i = i + 1
            temps = temps + content
    context = {
        'resume': resume,
        'contents': contents,
    }
    return render(request, 'index2.html', context=context)

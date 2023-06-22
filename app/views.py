from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'priya','age':5}
    return render(request,'wish.html',d)


def condition(request):
    d={'a':5}
    return render(request,'condition.html',d)

from django.shortcuts import render

def home(request):
    return render(request, 'contact.html')

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = val1 + val2

    return render(request, "success.html", {'result' : res})
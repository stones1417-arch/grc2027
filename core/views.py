from django.shortcuts import render

def home(request):
    # يعرض: C:\Users\stone\grc2027\templates\home.html
    return render(request, "home.html")

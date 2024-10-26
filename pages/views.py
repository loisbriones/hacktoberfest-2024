from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {})

def pdf(request):
    return render(request,"pages/pdf.html",{})
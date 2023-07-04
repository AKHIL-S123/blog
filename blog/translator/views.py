from django.shortcuts import render
from .import translate

# Create your views here.

def translator_view(request):
    if request.method == "POST":
        ginput =request.POST["my_textarea"]
        output =translate.language(ginput)
        return render(request,'translator.html',{'a':output,'b':ginput})
    else:
        return render(request,"translator.html")

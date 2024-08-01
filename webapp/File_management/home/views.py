from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('title')
        description = data.get('description')
        myfile = request.FILES
        image = myfile.get('image')
        text_file = myfile.get('text_file')
        pdf_file = myfile.get('pdf_file')
        Document.objects.create(title=name,
            description=description,
            image=image,
            text_file=text_file,
            pdf_file=pdf_file)
        return redirect('/')
    else:
        documents = Document.objects.all()
    return render(request, "home.html",{'documents': documents})
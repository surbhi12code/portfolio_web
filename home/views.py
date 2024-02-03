from django.shortcuts import render,HttpResponse
from home.models import contactModel

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    # return HttpResponse("This is my about(/about)")
     return render(request,'about.html')
def projects(request):
    # return HttpResponse("This is my projects(/projects)")
     return render(request,'projects.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        txt=request.POST['txt']
        print(name,email,txt)
        ins=contactModel(name=name, email=email, txt=txt)
        ins.save()
        print("Data written to db")
    # return HttpResponse("This is my contact(/contact)")
    return render(request,'contact.html')


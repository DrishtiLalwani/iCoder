from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request): 
    return render(request, 'home/home.html')

def about(request): 
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content=request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.warning (request, "jo bhi error ho")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
  

    return render(request, 'home/contact.html')

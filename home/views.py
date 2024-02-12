from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
# Create your views here.
def home(request): 
    return render(request, 'home/home.html')

def about(request): 
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method=='POST':
        s_no= request.POST['s_no']
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content=request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.error (request, "Fill the complete details correctly details!!")
        else:
            contact=Contact(s_no=s_no,name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success (request, "Thank you for contacting us! \n We will get back to you soon.")
  

    return render(request, 'home/contact.html')

def signup(request):
    if request.method=='POST':
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        if len(username)< 10 or len(username)>10:
            messages.error(request,"username should be of 10 characters")
            return redirect("home")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"username not valid")
            return redirect("home")
        
        if len(pass1)<8:
            messages.error(request,"Password shoul be atleast 8 characters long")
            return redirect("home")


        if pass2!=pass1:
            messages.error(request,"passwords do not match")
            return redirect("home")
    
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'You have been registered successfully!!')
        
        return redirect("home")
    else:
        return HttpResponse("404 - Not Found")
    
def handlelogin(request):
    if request.method=="POST":
        
        data = request.POST
        loginusername = data.get("loginusername")
        loginpassword  = data.get("loginpassword")
        print(loginpassword, loginusername)
        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        print("................")

        if user is  not None:

            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
    else:
        return HttpResponse("404 - Page Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("home")
 







from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'home/home.html', context)

def about(request): 
    return render(request, 'home/about.html')

def search(request):
    query=request.POST['query']
    if len(query)>60:
        allPosts=Post.objects.none()
    else: 
        allPoststitle= Post.objects.filter(title__icontains= query)
        allPostscontent= Post.objects.filter(content__icontains= query)
        allPostsauthor= Post.objects.filter(author__icontains= query)
        allPosts1=allPoststitle.union(allPostscontent)
        allPosts=allPosts1.union(allPostsauthor)

    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)

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

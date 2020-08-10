from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import Query,Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        querqy=Query(name=name, email=email,query=query)
        querqy.save()
        messages.success(request, 'Profile details updated.')
        return redirect('contact')
    return render(request,'contact.html')
def blog(request,slug):
    post=Post.objects.filter(slug=slug)[0]
    context={'post':post}
    return render(request,'blog.html',context)
def search(request):
    query = request.GET.get('query')
    alltitle =Post.objects.filter(title__icontains=query)
    allcontent = Post.objects.filter(content__icontains=query)
    if len(query) < 1 or len(query) >255:
        allPosts=[]
        messages.error(request,'No search results found')
    else:
        allPosts=list(alltitle)+list(allcontent)
    if len(allPosts)==0:
        messages.error(request,'No blogs found')
    context={'allPosts':allPosts,'query':query}
    return render(request,'search.html',context)
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        print(password)
        user=User.objects.create_user(username=username,email=email,password=password)
        user.first_name=firstname
        user.last_name=lastname
        messages.success(request,"Succesfully signed up")
        return render(request,'index.html',{'type':'success'})
    else:
        return HttpResponse("error 404 not found")
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is  not None:
            login(request,user)
            messages.success(request,'Logged in successfully')
            return render(request,'index.html',{'type':'success'})
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'index.html',{'type':'danger'})
    else:
        return HttpResponse('404 not found')
def logoutuser(request):
    logout(request)
    messages.info(request,'Logged out successfully')
    return render(request,'index.html',{'type':'success'})
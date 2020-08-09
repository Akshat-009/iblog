from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import Query,Post
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
    else:
        allPosts=list(alltitle)+list(allcontent)
    context={'allPosts':allPosts,'query':query}
    return render(request,'search.html',context)
    

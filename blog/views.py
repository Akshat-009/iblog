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

def blog(request):
    return render(request,'blog.html')
def search(request):
    query = request.GET.get('query')
    alltitle =Post.objects.filter(title__icontains=query)
    allcontent = Post.objects.filter(content__icontains=query)
    
    allPosts=list(alltitle)+list(allcontent)
    context={'allPosts':allPosts}
    return render(request,'search.html',context)
    

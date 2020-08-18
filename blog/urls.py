from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path('add',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('blog/<str:slug>',views.blog,name="blog"),
    path('search',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('postcomments/<str:slug>',views.postcomment,name="postcomments"),
    path('postreply/<str:slug>/<str:id>',views.postreply,name="postreply"),
    path('user/<str:name>',views.user,name="user"),
]

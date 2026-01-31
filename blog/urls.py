from django.urls import path
from . import views 

urlpatterns = [
	path('',views.blog,name='blog'),
	path("create/",views.create_post, name="create_post"),
	path('<slug:slug>/',views.blog_detail, name='blog_detail'),
	
	
]


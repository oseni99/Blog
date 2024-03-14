from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage, name="startig_page"),
    path("posts",views.posts, name="posts-page"),
    path("posts/<slug:slug>",views.posts_details,name="detail-posts" )
]

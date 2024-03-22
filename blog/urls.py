from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage, name="starting-page"),
    path("posts",views.posts, name="posts-page"),
    path("posts/<slug:slug>",views.posts_details,name="detail-posts" ) #localhost/posts/<slug>(particular_posts)
]

from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomepageView.as_view(), name="starting-page"),
    path("posts",views.PostView.as_view(), name="posts-page"),
    path("read-later", views.ReadLaterView.as_view(),name="read-later"),
    path("posts/<slug:slug>",views.PostDetailsView.as_view(),name="detail-posts" ),
    #localhost/posts/<slug>(particular_posts)
]

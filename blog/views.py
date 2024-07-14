from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.urls import reverse




# def get_dates(post):
#     return post["date"]
the_posts = Post.objects.all()
sorted_posts = Post.objects.all().order_by("-date")[:3]
# Create your views here.

class HomepageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "my_posts"
    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data

# def homepage(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "my_posts":latest_posts
#     })

class PostView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]
    def get_queryset(self):
        data =  super().get_queryset()
        return data
    

# def posts(request):
#     sorted_posts =  Post.objects.all().order_by("-date")
#     return render(request, "blog/all_posts.html",{
#         "all_posts": sorted_posts
#     })

class PostDetailsView(View):
    def is_stored_posts(self, request, post_id):
        stored_posts = request.session.get("stored_posts") #get the saved posts from session
        if stored_posts is not None:
            is_saved_later = post_id in stored_posts
        else:
            is_saved_later = False
        return is_saved_later
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
       
        return render(request,"blog/post-details.html",{
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm,
            "comments":post.comments.all().order_by("-date_ct"),
            "saved_later":self.is_stored_posts(request, post.id)
            })

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("detail-posts",args=[slug]))
        return render(request,"blog/post-details.html",{
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":comment_form,
            "comments":post.comments.all,
            "saved_later":self.is_stored_posts(request, post.id)
            })
    
    # def get_context_data(self, **kwargs) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm
    #     return context
    
# def posts_details(request,slug):  #localhost/posts/particularposts
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-details.html", {
#         "post":identified_post,
#         "post_tags":identified_post.tags.all()
#     })
class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None or len(stored_posts) == 0:
            return render(request,"blog/stored_posts.html",{
                "posts":[],
                "has_posts":False
                })
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            return render(request,"blog/stored_posts.html",{
                "posts":posts,
                "has_posts":True
                })
    def post(self,request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post-id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
            
        return HttpResponseRedirect("/")


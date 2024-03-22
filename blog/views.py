import datetime
from django.shortcuts import render


the_posts = [
    {"slug":"Traveling-on-vacation",
     "image":"greece.jpg",
     "author":"Oluwatosin",
     "date": datetime.datetime(2024,3,19),
     "title":"Traveling to Greece",
     "excerpt":"""From having a passport that makes it hard for me to travel aroundthe woorld to getting a visa that gives me the chance is so amazing""",
     "content":""" Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora quos deleniti illum cumque inventore quaerat! Quod veritatis quos aliquid cumque ipsum, necessitatibus numquam aliquam, est animi autem consequatur, voluptatibus commodi?
       Ratione amet officiis sit voluptatem assumenda perspiciatis quidem rerum sapiente delectus corrupti at quas quaerat dolor suscipit modi, ipsa, dolores minima quisquam asperiores accusantium illum! Placeat quam dolore aperiam unde!"""
     }, 
     {
         "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": datetime.datetime(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
     },
     {
         "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": datetime.datetime(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
     }
]



def get_dates(post):
    return post["date"]

sorted_posts = sorted(the_posts, key=get_dates)

# Create your views here.

def homepage(request):
    sorted_posts = sorted(the_posts, key=get_dates)
    latest_posts = sorted_posts[-2:]
    return render(request, "blog/index.html", {
        "my_posts":latest_posts
    })

def posts(request):
    return render(request, "blog/all_posts.html",{
        "all_posts": sorted_posts
    })

def posts_details(request,slug):  #localhost/posts/particularposts
    identified_post = next(post for post in the_posts if post["slug"]== slug) #keep displaying the next one after its chosen 
    return render(request, "blog/post-details.html", {
        "post":identified_post
    })



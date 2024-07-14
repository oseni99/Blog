from django.db import models
from django.utils.text import slugify

# Create your models here.


 
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.caption

 
class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name =  models.CharField(max_length=80)
    email_address = models.EmailField()
    # author_posts = models.ForeignKey(Post, on_delete=models.SET_NULL,null=True, related_name="author")
    
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    
    def __str__(self):
        return self.full_name()
          

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=80)
    image_name = models.ImageField(upload_to='images/')
    date = models.DateField()
    slug = models.SlugField(blank=True,db_index=True, null=False)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True, related_name="author")
    
    def save(self, *args, **kwargs):
        # if not self.slug: MADE SOME CHANGES SO FEELS LIKE THIS ISNT NEEDED AS I WANT TO CHANGE THE SLUGS AS I EDIT THE TITLES 
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=254)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    comments = models.TextField(max_length=400)
    date_ct = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments
    
   
   
    
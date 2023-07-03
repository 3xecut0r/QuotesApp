from django.db import models


class Author(models.Model):
    fullname = models.CharField()
    born_date = models.CharField()
    born_location = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    
    
class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
from django.db import models
from django.conf import settings

class Questions(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    content= models.CharField(max_length=240)
    slug=models.SlugField(max_length=255, unique=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete= models.CASCADE,
                            related_name="questions")


class Answer(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    body=models.TextField()
    question=models.ForeignKey(Questions,
                                on_delete= models.CASCADE,
                            related_name="answers")
    author= models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    voters= models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")                            


from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/img/')
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Form(models.Model):
    firstname = models.CharField( max_length=100)
    lastname = models.CharField( max_length=100)

    def __str__(self):
        return self.firstname
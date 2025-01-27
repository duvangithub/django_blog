from django.db import models

# Create your models here.

# blog/models.py

#Agrega los modelos
class Category(models.Model):
    name = models.CharField(max_length=30)

    #Permite cambiar el nombre de la categoria a plural
    class Meta:
        verbose_name_plural = "categories"

    #Permite ver el nombre de la clase en el backend del admin
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    #Permite ver el nombre de la clase en el backend del admin
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    #Permite ver el nombre de la clase en el backend del admin
    def __str__(self):
        return f"{self.author} on '{self.post}'"

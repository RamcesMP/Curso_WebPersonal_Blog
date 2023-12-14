from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=150, verbose_name="Título")
    description=models.TextField()
    image=models.ImageField(upload_to="projects")
    link=models.URLField(null=True,blank=True,verbose_name="Dirección web")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Proyecto"
        ordering=["-created"]

    def __str__(self):
        return self.title

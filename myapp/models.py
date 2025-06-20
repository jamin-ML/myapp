from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    image = models.ImageField(upload_to='image/')
    demo_url = models.URLField()
    git_hub_url = models.URLField()

    def __str__(self):
       return self.title

from django.db import models

class Myself(models.Model):
    name = models.CharField(max_length=100)
    myImage = models.ImageField(upload_to='images/')
    myResume = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    summary = models.TextField()

    def __str__(self):
        return self.title
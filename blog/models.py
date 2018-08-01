from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(upload_to="imagesblog/")

    def summary(self):
        return self.body[:500]

    def date_pretty(self):
        return self.date.strftime("%b %e %Y")

    def __str__(self):
        return self.title

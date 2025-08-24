from django.db import models

class AffirmationEntry(models.Model):
    quote=models.TextField(max_length=200)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.quote

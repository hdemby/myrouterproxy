from django.db import models

# Create your models here.
class Lists(models.Model):
    name = models.CharField(max_length=64, unique=True)
    descr = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Item(models.Model):
    item = models.CharField(max_length=64)
    detail = models.TextField(max_length=500)
    done = models.BooleanField(default=False)
    tdlst = models.ForeignKey(Lists, on_delete=models.CASCADE)

    def __str__(self):
        return self.item




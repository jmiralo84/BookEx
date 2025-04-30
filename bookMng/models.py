from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class MainMenu(models.Model):
    item = models.CharField(max_length=300, unique=True)
    link = models.CharField(max_length=300, unique=True)

    # New model for icons
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)



class OwnedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    comment = models.TextField(blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

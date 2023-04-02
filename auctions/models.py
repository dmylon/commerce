from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.username + " " + str(self.id)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", default=None)
    date = models.DateTimeField(default=datetime.now())
    message = models.CharField(max_length=200, null=False, default=None)


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    photo = models.ImageField(upload_to="uploads/", default="uploads/default.png", blank=True)
    category = models.CharField(max_length=64, null=False, default=None)
    interested_users = models.ManyToManyField(User, blank=True, related_name="watchlist")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings_created", default=None)
    bid = models.PositiveSmallIntegerField(default=0)
    bid_winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_winning", blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, blank=True, related_name="listings_commented")

    def __str__(self):
        return f"{self.title} (id:{self.id})"
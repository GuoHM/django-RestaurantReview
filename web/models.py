from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Restaurant(models.Model):
    restaurant_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=30)
    price = models.IntegerField(default=0)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,null=True)
    master_comment = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0)
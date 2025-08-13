from django.db import models
from django.contrib.auth.models import User

class Actor(models.Model):
    class GENDER(models.TextChoices):
        MALE = 'male','male'
        FEMALE = 'female', 'female'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER.choices)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.SmallIntegerField(blank=True, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    duration = models.DurationField()

    def __str__(self):
        return self.name

class Review(models.Model):
    comment = models.TextField()
    rate = models.SmallIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.comment[:40]




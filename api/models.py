from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=2_000)

    def num_of_ratings(self) -> int:
        ratings = Rating.objects.all()
        return len(ratings)

    def avg_ratings(self) -> int:
        sum_of_ratings = 0
        ratings = Rating.objects.all()
        for rating in ratings:
            sum_of_ratings += rating.stars

        return round(sum_of_ratings / len(ratings))

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    meal = models.ForeignKey(Meal, models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, models.CASCADE, related_name="ratings")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Value must be at least 1."),
            MaxValueValidator(5, message="Value must be at most 5."),
        ]
    )

    class Meta:
        unique_together = (("meal", "user"),)
        index_together = (("meal", "user"),)

    def __str__(self) -> str:
        return f"{self.meal.name}:{self.user.username}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_token(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_user_token(sender, instance, *args, **kwargs):
    Token.objects.filter(user=instance).delete()

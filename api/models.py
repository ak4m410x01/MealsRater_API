from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=2_000)

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    meal = models.ForeignKey(Meal, models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, models.CASCADE, related_name="ratings")
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (("meal", "user"),)
        index_together = (("meal", "user"),)

    def __str__(self) -> str:
        return f"{self.meal.name}:{self.user.username}"

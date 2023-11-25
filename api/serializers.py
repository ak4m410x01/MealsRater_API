from rest_framework.serializers import ModelSerializer
from api.models import Meal, Rating


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "description", "ratings")
        ordering = ("id",)


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "meal", "user", "stars")
        ordering = ("id",)

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from api.models import Meal, Rating


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = (
            "id",
            "name",
            "description",
            "num_of_ratings",
            "avg_ratings",
            "ratings",
        )
        ordering = ("id",)


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "meal", "user", "stars")
        ordering = ("id",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        ordering = ("id",)
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True,
                "style": {
                    "input_type": "password",
                },
            }
        }

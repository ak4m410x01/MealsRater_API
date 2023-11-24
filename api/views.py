from django.shortcuts import render
from rest_framework import viewsets
from api.models import Meal, Rating
from api.serializers import MealSerializer, RatingSerializer

# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

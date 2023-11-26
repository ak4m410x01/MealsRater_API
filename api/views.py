from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from api.models import Meal, Rating
from api.serializers import MealSerializer, RatingSerializer, UserSerializer

# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=["POST"], detail=True)
    def rate_meal(self, request, pk=None):
        response = {}

        # validate stars has been provided
        if "stars" not in request.data:
            response["stars"] = "This field is required."

        # validate stars in and integer and in range [1, 5]
        elif type(request.data["stars"]) != int or not (
            1 <= request.data["stars"] <= 5
        ):
            response["stars"] = "This field must be an integer value in range [1, 5]."

        if len(response):
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        meal = Meal.objects.get(id=pk)
        stars = request.data["stars"]
        user = request.user

        try:
            # UPDATE
            rating = Rating.objects.get(user=user.id, meal=meal.id)
            rating.stars = stars
            rating.save()
            serializer = RatingSerializer(rating)

            response["message"] = "rating has been updated successfuly :)"
            response["rating"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)

        except Rating.DoesNotExist:
            # CREATE
            # user hasn't rating in this meal
            # create rating for this user
            rating = Rating.objects.create(user=user, meal=meal, stars=stars)
            rating.save()
            serializer = RatingSerializer(rating)

            response["message"] = "rating has been created successfuly :)"
            response["rating"] = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        response = {
            "message": "Invalid Operation",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {
            "message": "Invalid Operation",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token = Token.objects.get(user=user)

        response = {
            "token": token.key,
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = {
            "error": "operation not allowed",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def distroy(self, request, *args, **kwargs):
        response = {
            "error": "operation not allowed",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

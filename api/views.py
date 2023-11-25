from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Meal, Rating
from api.serializers import MealSerializer, RatingSerializer

# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=["POST"], detail=True)
    def rate_meal(self, request, pk=None):
        # validate username has been provided
        is_valid_request_data = True
        if "username" not in request.data:
            response = {
                "error": "username not provided",
            }
            is_valid_request_data = False

        # validate username has been provided
        if "stars" not in request.data:
            response = {
                "error": "stars not provided",
            }
            is_valid_request_data = False

        # validate username has been provided
        if not (1 <= request.data["stars"] <= 5):
            response = {
                "error": "stars must be in range [1, 5]",
            }
            is_valid_request_data = False

        if is_valid_request_data == False:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        meal = Meal.objects.get(id=pk)
        stars = request.data["stars"]
        username = request.data["username"]

        try:
            user = User.objects.get(username=username)
            try:
                # UPDATE
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating)

                response = {
                    "message": "rating has been updated successfuly :)",
                    "rating": serializer.data,
                }
                return Response(response, status=status.HTTP_200_OK)

            except Rating.DoesNotExist:
                # CREATE
                # user hasn't rating in this meal
                # create rating for this user
                rating = Rating.objects.create(user=user, meal=meal, stars=stars)
                rating.save()
                serializer = RatingSerializer(rating)

                response = {
                    "message": "rating has been created successfuly :)",
                    "rating": serializer.data,
                }
                return Response(response, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            response = {
                "error": "Unauthorized User",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

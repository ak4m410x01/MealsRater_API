from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register("meals", views.MealViewSet)
router.register("ratings", views.RatingViewSet)
router.register("users", views.UserViewSet)

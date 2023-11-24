from django.contrib import admin
from api.models import Meal, Rating

# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id",)


class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "meal", "user", "stars")
    list_filter = ("id", "meal", "user", "stars")
    search_fields = ("meal", "user", "stars")
    ordering = ("id",)


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)

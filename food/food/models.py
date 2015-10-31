from django.db import models
import datetime
from django.utils import timezone


class Dining_Hall(models.Model):
    menu_items = ManyToManyField(Menu_Item)
    dining_hall_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dining_hall_name



class Menu_Item(models.Model):
    food_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    #0 is breakfast, 1 is lunch, 2 is dinner
    has_been_rated = False
    def __str__(self):
        return self.food_name

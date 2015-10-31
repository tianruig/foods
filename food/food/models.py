from django.db import models


class MenuItem(models.Model):
    food_name = models.CharField(max_length=255)
    rating = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(default=0)
    #0 is breakfast, 1 is lunch, 2 is dinner

    def __str__(self):
        return self.food_name


class DiningHall(models.Model):
    menu_items = models.ManyToManyField(MenuItem)
    dining_hall_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dining_hall_name



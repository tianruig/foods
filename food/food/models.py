from django.db import models


class MenuItem(models.Model):
    food_name = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(default=0)
    #0 is breakfast, 1 is lunch, 2 is dinner

    def __str__(self):
        return self.food_name


class DiningHall(models.Model):
    dining_halls = (
            ('Crossroads', 'Crossroads'),
            ('Clark Kerr', 'Clark Kerr'),
            ('Cafe 3', 'Cafe 3'),
            ('Foothill', 'Foothill'),
    )

    menu_items = models.ManyToManyField(MenuItem, blank=True)
    name = models.CharField(max_length=100, choices=dining_halls)

    def __str__(self):
        return self.name



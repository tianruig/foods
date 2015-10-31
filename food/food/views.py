from django.http import HttpResponse
from urllib.request import urlopen
import json

from .models import DiningHall, MenuItem


def update(request):
    url = 'http://asuc-mobile.herokuapp.com/api/dining_halls'
    response = urlopen(url)
    data = json.loads(response.read().decode())
    count = 0

    for hall in data['dining_halls']:
        dh_name = hall['name']
        dining_hall, dh_created = DiningHall.objects.get_or_create(name=dh_name)

        for item in hall['breakfast_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 0})

            dining_hall.menu_items.add(itm)
            dining_hall.save()

            itm.save()
            count += 1

        for item in hall['lunch_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 1})

            dining_hall.menu_items.add(itm)
            dining_hall.save()

            itm.save()
            count += 1

        for item in hall['dinner_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 2})

            dining_hall.menu_items.add(itm)
            dining_hall.save()

            itm.save()
            count += 1

    return HttpResponse("{} records updated".format(count))



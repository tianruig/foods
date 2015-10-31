from django.http import HttpResponse
from urllib.request import urlopen
import json

from .models import DiningHall, MenuItem

def suggest(request):
    def get_avg(lst):
        sum = 0
        count = 0
        for i in lst:
            if i.rating is not None:
                sum += i.rating
                count += 1
        return sum / count if count != 0 else 0

    ratings = {}
    for dining_hall in DiningHall.objects.all():
        ratings[dining_hall.name] = get_avg(dining_hall.menu_items.all())
    return HttpResponse("You should go to {} because it has good food."
            .format(max(ratings, key=lambda x: ratings[x])))

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

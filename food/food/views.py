from django.http import HttpResponse
from urllib.request import urlopen
import json

from .models import MenuItem


def update(request):
    url = 'http://asuc-mobile.herokuapp.com/api/dining_halls'
    response = urlopen(url)
    data = json.loads(response.read().decode())
    count = 0

    for hall in data['dining_halls']:
        for item in hall['breakfast_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 0})
            itm.save()
            count += 1

        for item in hall['lunch_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 1})
            itm.save()
            count += 1

        for item in hall['dinner_menu']:
            itm, created = MenuItem.objects.get_or_create(food_name=item['name'], defaults={'time': 2})
            itm.save()
            count += 1

    return HttpResponse("{} records updated".format(count))



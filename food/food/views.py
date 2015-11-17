from django.http import HttpResponse, HttpResponseRedirect
from urllib.request import urlopen
import json
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import DiningHall, MenuItem
from django.views import generic

def index(request):
    response = HttpResponse("<h1>Rate foods!</h1>")
    response.write("<a href='update/'>Update list of foods?</a><br>")
    response.write("<br><a href='suggest/'>Find out which dining hall has the best food for you!</a><br>")
    response.write("<ul>")
    for menu_item in MenuItem.objects.all():
        response.write("<li>")
        w = menu_item.food_name
        response.write("<a href = ")
        response.write("{}".format(menu_item.id))
        response.write(">")
        response.write(w)
        response.write("</a>")
        response.write("</li>")
    response.write("</ul>")
    return response

class DetailView(generic.DetailView):
    model = MenuItem
    template_name = 'food/details.html'
    def get_queryset(self):
        return MenuItem.objects.all()

def update_rating(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    r = request.POST['rating']
    if r == '12':
        menu_item.rating = None
    else:
        menu_item.rating = r
    menu_item.save()
    #return HttpResponse("test")
    return HttpResponseRedirect("../../")

# class DetailView(generic.DetailView):
#     model = MenuItem
#     template_name = 'food/details.html'
#     def get_queryset(self):
#         return MenuItem.objects.all()

# def update_rating(request, menu_item_id):
#     menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
#     menu_item.rating = request.POST['rating']
#     menu_item.save()
#     #return HttpResponse("test")
#     return HttpResponseRedirect("../../")

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
    response =  HttpResponse()
    response.write("You should go to {} because it has good food.".format(max(ratings, key=lambda x: ratings[x])))
    response.write("<br><a href='../'>Return to rating?</a>")
    return response

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
        response =  HttpResponse("{} records updated".format(count))
        response.write("<br><a href = '../'>Return to rating?</a>")
        return response

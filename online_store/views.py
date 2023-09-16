from django.shortcuts import get_object_or_404, render

from .models import Item

from django.http import HttpResponse



def index(request):
    item_list = Item.objects.order_by("name")

    context = {
        "item_list": item_list,
    }
    return render(request, "online_store/index.html", context)


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "online_store/detail.html", {"item": item})


from django.shortcuts import render
from . import models
from django.db.models import Prefetch

def collection(request):
    data = {
        "collections": models.Collection.objects.all()
    }
    return render(request, 'pages/collections.html', data)

def sweets(request, colId):
    col_list = [
        # models.Collection.objects.get(id=colId)
        colId
    ]

    data = {
        "products": models.Product.objects.filter(collection__in=col_list)
    }

    # "products": models.Product.objects.prefetch_related(
    #     Prefetch('collection', queryset=models.Collection.objects.filter(id=colId))
    # )

    # select_related ForeignKey
    # prefetch_related ManyToMany

    return render(request, 'pages/products.html', data)
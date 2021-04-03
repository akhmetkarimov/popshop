from django.shortcuts import render
from django.core.paginator import Paginator
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
    # field, order
    # name, desc

    field = 'name'
    order = '-'

    if order == 'desc':
        order = '-'
    else:
        order = ''

    products = Paginator(
        models.Product.objects.filter(collection__in=col_list).order_by(f'{order}{field}'),
        1
    )

    print(products.num_pages) # Кол страниц

    page = 1
    page_obj = products.get_page(page)
    
    print(page_obj.next_page_number)
    print(page_obj.has_previous())
    print(page_obj.has_next())

    data = {
        "products": page_obj
    }

    # "products": models.Product.objects.prefetch_related(
    #     Prefetch('collection', queryset=models.Collection.objects.filter(id=colId))
    # )

    # select_related ForeignKey
    # prefetch_related ManyToMany

    return render(request, 'pages/products.html', data)

def product_detail(request, pslug):
    # id == pk
    data = {
        "product": models.Product.objects.get(seo_name=pslug)
    }
    return render(request, 'pages/detail.html')

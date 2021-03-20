from django.shortcuts import render
from . import models

def collection(request):
    data = {
        "collections": models.Collection.objects.all()
    }

    return render(request, 'pages/collections.html', data)
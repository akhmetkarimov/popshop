from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.collection),
    path('<int:colId>', views.sweets)
    # re_path(r'(?P<colids>\w+)/$', views.sweets)
]
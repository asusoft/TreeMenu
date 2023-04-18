from django.urls import path
from treeMenuApp.views import home

urlpatterns = [
    path('', home, name='home'),
]
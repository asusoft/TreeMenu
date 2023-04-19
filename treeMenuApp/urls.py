from django.urls import path
from treeMenuApp.views import home

app_name = 'https'
urlpatterns = [
    path('', home, name='home'),
]

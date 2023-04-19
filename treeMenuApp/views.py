from django.shortcuts import render

from .models import MenuItem
from .templatetags.menu_tags import draw_menu

# Create your views here.

def home(request):
   # Get the menu items from the database

    # Call the draw_menu template tag to render the menu HTML
    # Render the HTML page with the menu
    return render(request, 'home.html', {'draw_menu': draw_menu})

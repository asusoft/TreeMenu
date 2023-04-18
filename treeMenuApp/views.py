from django.shortcuts import render

from .models import MenuItem
from .templateTags.menu_tag import draw_menu

# Create your views here.

def home(request):
   # Get the menu items from the database
    menu_items = MenuItem.objects.all()

    # Call the draw_menu template tag to render the menu HTML
    menu_html = draw_menu()

    # Render the HTML page with the menu
    return render(request, 'home.html', {'menu_html': menu_html})

from django.shortcuts import render

# Create your views here.

def home(request):
    # Get the menu items from the database
    # Call the draw_menu template tag to render the menu HTML
    # Render the HTML page with the menu
    return render(request, 'home.html')

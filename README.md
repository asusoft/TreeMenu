# TreeMenu  

TreeMenu is a hierarchical menu display web application, built using Python.

## Installation  

To get started with TreeMenu, follow these steps:  

  1. Clone the repository:  
      `git clone https://github.com/asusoft/TreeMenu.git`  
        
  2. Install the dependencies:  
      `cd TreeMenu`  
      `pip install -r requirements.txt`  
  
  3. Make migrations:  
      `python manage.py migrate`  

## Usage  

To use TreeMenu, follow these steps:  
  
  1. Start the server:  
      `python manage.py runserver`  
  
  2. Create a new menu in the admin panel:  
      The menu title is the name to be displayed on the menu. Eg: Main Menu  
      The menu name is used to call the draw_menu method to draw a specific menu. Eg: main_menu  
  
  3. Add menu items to the created menu.  
  
  4. Draw the menu in your template:  
      Add `{% load draw_menu %}` at the top of your template.  
      Add `{% draw_menu 'main_menu' %}` where you want to display the menu in your template.  
      Replace `main_menu` with your menu's name (not title).  

There is example of drawing a menu named 'main_menu' on the home.html file

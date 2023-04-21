from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    """
    Model for Menu item. 
    Has title and anem fields.
    Name is use in templatetag 'draw_menu' for drawing a specific menu menu
    """
    title = models.CharField(max_length=255)
    name = models.SlugField(max_length=255, verbose_name='Name', null=True,
                            help_text='Use it in templatetag for draw a menu')
    url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Url used in your urls.py file to navigate to the menu page')
    
    def get_absolute_url(self):
        if self.url:
            url = reverse(self.url)
        else:
            url = '/{}/'.format(self.name)
        return url
    
    def __str__(self):
        return self.title
    

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Url used in your urls.py file to navigate to the menu item page')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                                blank=True, null=True, 
                                related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', blank=True, null=True,)
    is_active = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        if self.url:
            url = reverse(self.url)
        else:
            url = '/{}/'.format(self.name)
        
        return url
    
    def set_is_active(self, active):
        self.is_active = active
        self.save()

    def __str__(self):
        return f"MenuItem(name='{self.name}', url='{self.url}', children={self.children}, isActive={self.is_active})"
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

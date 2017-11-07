from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
import atcar.atcarlistinfos as atlist






# Create your models here.
class atcar_cars(models.Model):
    """All the fields regarding cars"""
    id = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=24, choices=atlist.AT_MAKES)
    model = models.CharField(max_length=24)
    year = models.PositiveIntegerField( choices=atlist.AT_YEARS)
    color = models.CharField(max_length=12, blank=True, null=True, choices=atlist.COLORS)
    body = models.CharField(max_length=24, blank=True, null=True, choices=atlist.BODY)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    enginesize = models.IntegerField()
    enginetype = models.CharField(max_length=12)
    mileagekm = models.PositiveIntegerField()
    mileagemiles = models.PositiveIntegerField()
    transmission = models.CharField(max_length=12, blank=True, choices=atlist.TRANSMISSION)
    fuel = models.CharField(max_length=12, choices=atlist.AT_FUEL)
    steer = models.CharField(max_length=4, choices=atlist.SO)
    doors = models.PositiveSmallIntegerField()
    list1 = models.PositiveSmallIntegerField()
    intcolor = models.CharField(max_length=24)
    sellerid = models.IntegerField()
    condition = models.CharField(max_length=24)
    location_parish = models.CharField(max_length=24)
    location_address = models.CharField(max_length=64)
    addinfo = models.CharField(db_column='addinfo', max_length=255, blank=True, null=True)
    image1 = models.ImageField(upload_to='at_private/', max_length=100)
    image2 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    image3 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    image4 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    image5 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    image6 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    image7 = models.ImageField(upload_to='at_private/', max_length=100, blank=True)
    #timeadded = DateTimeField(auto_now_add=True, blank=True)
    

    class Meta:
        managed = False
        app_label = 'atcar'
        db_table = 'atcar_cars'

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("product name", max_length=30)
    price = models.FloatField("price", default=10)
    ptype = models.ForeignKey('Ptype')
    
    def __unicode__(self):
        return "%s --> %d" % (self.name, self.price)
    
class Ptype(models.Model):
    name = models.CharField('type', max_length=10)
    
    def __unicode__(self):
        return "%s" % self.name
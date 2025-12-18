from django.db import models
from django.utils import timezone


# Create your models here.

from django.db import models
from django.utils import timezone


# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('masala', 'Masala Chai'),
        ('ginger', 'Ginger Chai'),
        ('cardamom', 'Cardamom Chai'),
        ('tulsi', 'Tulsi Chai'),
        ('saffron', 'Saffron Chai'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_varieties/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=CHAI_TYPE_CHOICES)
    
    def __str__(self):
        return self.name
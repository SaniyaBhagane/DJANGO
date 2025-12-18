from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description = models.TextField(default='')
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    
# one to many relationship with reviews
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} review for {self.chai.name} ({self.rating}/5)"
    
# many to many relationship with strores
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')
    def __str__(self):
        return self.name
    
# one to one relationship with chai certificate
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_name = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f"{self.certificate_name} for {self.chai.name}"
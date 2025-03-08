from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user_management.models import User
# Create your models here.

class Package(models.Model):
    STATUS_CHOICES = [
        ( 'pending', 'Pending'),
        ( 'shipped', 'Shipped' ),
        ( 'in_transit', 'In Transit'),
        ( 'out_for_delivery', 'Out for Delivery' ),
        ( 'delivered', 'Delivered')
    ]
    sender_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    recipient_name = models.CharField(max_length=255)
    recipient_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
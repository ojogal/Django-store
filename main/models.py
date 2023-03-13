from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import json


class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  characteristics = models.JSONField(null=True, blank=True)

  def update_characteristics(self, data):
    self.characteristics = json.dumps(data)
    self.save()

  def get_characteristics(self):
    return json.loads(self.characteristics) if self.characteristics else {}
  
  def set_characteristics(self, form_data):
    data = {}
    for i in range(1, 6):
        key = form_data.get(f"key_{i}")
        value = form_data.get(f"value_{i}")
        if key and value:
            data[key] = value
    self.characteristics = json.dumps(data)


class Image(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
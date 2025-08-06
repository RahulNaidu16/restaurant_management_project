from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.Charfield(max_length=15)
def _str_(self):
    return self.User.username



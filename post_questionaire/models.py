from django.db import models
from users.models import User

# Create your models here.
class Post_Questionaire(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    q1 = models.CharField(max_length=50, default=None)
    q2 = models.CharField(max_length=50, default=None)
    q3 = models.CharField(max_length=50, default=None)

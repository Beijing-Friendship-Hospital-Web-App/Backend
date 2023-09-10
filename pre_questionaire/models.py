from django.db import models
from users import User

# Create your models here.
class Pre_Questionaire(models.Model):
    user = models.ForeignKey("User", verbose_name=_("user"), on_delete=models.CASCADE)
    

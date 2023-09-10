from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + f" (id: {self.id})"

    class Meta:
        verbose_name = "Userbase"
        verbose_name_plural = "Userbase"

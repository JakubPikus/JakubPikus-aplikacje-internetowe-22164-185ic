from django.db import models
from django.contrib.auth.models import User



class Mecz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team_h = models.CharField(max_length=30)
    team_a = models.CharField(max_length=30)
    referre = models.CharField(max_length=50)
    clock = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    verbose_name_plural = "Moje mecze"    


def __str__(self):
    return self.title







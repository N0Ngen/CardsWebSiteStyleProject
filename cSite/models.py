# Models are classes

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Tutorial(models.Model):
  tut_title = models.CharField(max_length=200)
  tut_content = models.TextField()
  tut_PD = models.DateTimeField('Date published', default=datetime.now())

  def __str__(self):
    return self.tut_title

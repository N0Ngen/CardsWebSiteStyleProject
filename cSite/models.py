from django.db import models

# Create your models here.

class Tutorial(models.Model):
  tut_title = models.CharField(max_length=200)
  tut_content = models.TextField()
  tut_PD = models.DateTimeField()

  def __str__(self):
    return self.tut_title

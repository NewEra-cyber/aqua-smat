from django.db import models

class SuccessStory(models.Model):
  name = models.CharField(max_length=100)
  locality = models.CharField(max_length=100)
  story = models.TextField()
  image = models.ImageField(upload_to='stories/')

  def __str__(self):
    return f"{self.name} from {self.locality}"


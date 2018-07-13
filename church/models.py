from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')
    post = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    #DateField('Career_Date')
    #IntegerField(default=0) 
    #ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
from django.db import models

# Create your models here.
from django.db import models
import datetime
from app.models import *
from django.template.defaultfilters import slugify
from django.urls import reverse


class news(models.Model):
    image = models.ImageField(upload_to='Images')
    tag = models.CharField(max_length=250)
    heading = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField()
    date = models.DateField(default=datetime.date.today)

    impost = models.ImageField(upload_to='Images')
    cat = models.ForeignKey(cato, on_delete=models.CASCADE)
    available = models.BooleanField()

    def __str__(self):
        return self.tag

    def get_url(self):
        return reverse('latest_news', args=[self.cat.slug, self.slug])
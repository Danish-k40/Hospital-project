from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



class cato(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class doctor(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    image = models.ImageField(upload_to='Images')
    dept = models.CharField(max_length=20)
    desc = models.TextField()
    category = models.ForeignKey(cato, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('doctor_details', args=[self.category.slug, self.slug])


class doctors_list(models.Model):
    doct = models.ForeignKey(doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.doct

from django.db import models

# Create your models here.
from django.urls import reverse


class Football(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128, null=True, blank=True)
    description = models.CharField(verbose_name='Описание',max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='football')
    url = models.SlugField(max_length=130, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Футбол'
        verbose_name_plural = 'Футбол'

    def get_absolute_url(self):
        return reverse("footballs", kwargs={"url": self.url})



class MinyFootball(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128, null=True, blank=True)
    description = models.CharField(verbose_name='Описание',max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='miny_football')
    slug = models.SlugField(max_length=130, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини-футбол'
        verbose_name_plural = 'Мини-футбол'

    def get_absolute_url(self):
        return reverse("miny_footballs", kwargs={"slug": self.slug})


from django.db import models
from django.utils.text import slugify


class teachers(models.Model):
    image = models.ImageField(upload_to='medaifiles', blank=True, null=True)
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20, default='Graphic Designer')

    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkdin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name + self.profession


class course(models.Model):
    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='mediafiles', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    info = models.TextField()
    fee = models.FloatField(default=1000)
    duration = models.CharField(
        max_length=10, help_text='like 3 months or 12 months')
    created_date = models.DateField()
    last_date = models.DateField()

    total_seats = models.PositiveIntegerField(default=30)
    seats_reserved = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    seats_remaining = models.PositiveIntegerField(
        null=True, blank=True)

    is_activated = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(course, self).save(*args, **kwargs)


class message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Brand(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class Uav(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uavs/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    uav = models.ForeignKey(Uav, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.uav.name} reserved from {self.start_date} to {self.end_date}"

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    @classmethod
    def is_available(cls, uav, start_date, end_date):
        overlapping_reservations = cls.objects.filter(
            uav=uav,
            start_date__lte=end_date,
            end_date__gte=start_date
        )
        return not overlapping_reservations.exists()

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be less than end date.")
        if not self.is_available(self.uav, self.start_date, self.end_date):
            raise ValueError(f"{self.uav.name} is not available from {self.start_date} to {self.end_date}.")
        super().save(*args, **kwargs)


def create_slug(slug, new_slug=None):
    slug = slugify(slug)
    if new_slug is not None:
        slug = new_slug
    qs = Brand.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(slug, new_slug=new_slug)
    return slug

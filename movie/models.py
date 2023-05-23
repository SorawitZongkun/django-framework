from django.db import models

# Create your models here.

# Step 5 : Make movie model
class Movie(models.Model):
    name_th = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    number = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices
    CHANNEL_CHOICES = [
        ("netflix", "Netflix"),
        ("viu", "VIU"),
        ("youtube", "Youtube"),
    ]
    channel = models.CharField(
        max_length=10,
        choices=CHANNEL_CHOICES,
        default="netflix",
    )

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "ชื่อภาษาไทย: " + self.name_th + ", ราคา: " + str(self.price) + " บาท"
    
# Step 6 : Make migrations
# python manage.py makemigrations
# python manage.py migrate

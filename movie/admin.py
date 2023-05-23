from django.contrib import admin

# Step 7 : Make admin panel
# python manage.py createsuperuser
from movie.models import Movie

# Register your models here.


admin.site.register(Movie)

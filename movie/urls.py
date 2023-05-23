# Step 3 : Make urls.py in anime app and make templates folder

from django.urls import path
from movie import views

urlpatterns = [
    # Step 4 : Make simple route
    path('page_a/', views.page_a),
    path('page_b/', views.page_b),
    path('page_c/', views.page_c),

    # Step 8 : Add data

]

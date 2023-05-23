from django.shortcuts import render, redirect
from django.http import HttpResponse
from movie.models import Movie
from django.contrib import messages

# Create your views here.


def page_a(request):
    # name_movie = 'Dragon Ball'
    # return HttpResponse(name_movie)
    return render(request, 'page_a.html')


def page_b(request):
    return render(request, 'page_b.html')


def page_c(request):
    return render(request, 'page_c.html')


# ----------------------------------------------


def create(request):
    if request.method == "POST":
        # Get reqeust
        name_th = request.POST['name_th']
        name_en = request.POST['name_en']
        number = request.POST['number']
        price = request.POST['price']
        channel = request.POST['channel']
        print(name_th, name_en, number, price, channel)

        # Save data
        movie = Movie.objects.create(
            name_th = name_th,
            name_en = name_en,
            number = number,
            price = price,
            channel = channel
        )
        movie.save()

        # Send message
        messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")

        # Change route
        return redirect("/movie")
    else:
        return render(request, 'create.html')


def index(request):
    return render(request, 'index.html')


def edit(request):
    return render(request, 'page_c.html')


def delete(request):
    return render(request, 'page_c.html')

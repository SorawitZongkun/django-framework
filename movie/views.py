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
    movies = Movie.objects.all()
    # movies = Movie.objects.filter(number=2)
    return render(request, 'index.html', {"movies": movies})


def edit(request, movie_id):
    if request.method == "POST":
        # Get reqeust
        name_th = request.POST['name_th']
        name_en = request.POST['name_en']
        number = request.POST['number']
        price = request.POST['price']
        channel = request.POST['channel']
        print(name_th, name_en, number, price, channel)

        # Validation and Send message
        # messages.error(request, "ข้อมูลไม่ถูกต้อง")

        # Save data
        movie = Movie.objects.get(id=movie_id)
        movie.name_th = name_th
        movie.name_en = name_en
        movie.number = number
        movie.price = price
        movie.channel = channel
        movie.save()

        # Send message
        messages.success(request, "อัพเดทข้อมูลเรียบร้อยแล้ว")

        # Change route
        return redirect("/movie")
    else:
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        movie = Movie.objects.get(id=movie_id)
        return render(request, "edit.html", {"movie": movie})


def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()

    # Send message
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")

    # Change route
    return redirect("/movie")

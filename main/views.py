from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def frontpage(request):

    carousel_images = FrontpageImage.objects.all()[1:]
    first_image = FrontpageImage.objects.first()

    context = {
        "first_image": first_image,
        "carousel_images": carousel_images,
    }

    return render(request, "main/frontpage.html", context)

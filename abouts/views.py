from django.shortcuts import render
from abouts.models import About
# Create your views here.

def about_index(request):
    abouts = About.objects.all()
    context = {"abouts": abouts}
    return render(request, "about_index.html", context)


def about_detail(request, pk):
    about = About.objects.get(pk=pk)
    context = {"about": about}
    return render(request, "about_detail.html", context)

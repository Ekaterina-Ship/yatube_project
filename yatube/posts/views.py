from django.shortcuts import render

# Create your views here.
def group_posts(request, slug):
    return render(request, slug)
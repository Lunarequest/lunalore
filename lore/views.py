from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
async def index(request: HttpRequest):
    return render(request,"index.html")
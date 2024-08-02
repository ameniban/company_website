from os import name
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    context={
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "Django", "JavaScript"],
        "profile": {
            "occupation": "Software Developer",
            "experience": 5
        },
        "current_date": datetime.now()
    }
    return render(request,"index.html" ,context)

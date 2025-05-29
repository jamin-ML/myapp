from django.shortcuts import render
from .models import Project


def home(request):
    projectlist = Project.objects.all()
    return render(request, 'myapp/home.html',{'projectlist':projectlist}) # This function renders the 'home.html' template when the home view is accessed.    

def skills(request):
    return render(request,'myapp/skills.html')
from django.shortcuts import render
from .models import Notes

# Create your views here.

def home(request):
    return render(request,'portal/home.html')
def notes(request):
    notes = Notes.objects.filter(user=request.user)
    context={"notes":notes}
    return render(request,'portal/notes.html',context)

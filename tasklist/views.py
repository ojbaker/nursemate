from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskItem

def tasklistView(request):
    all_task_items = TaskItem.objects.all()
    return render (request, 'tasklist.html',
        {'all_items': all_task_items})

# Create your views here.

from django.shortcuts import render

from .models import Record


def index(request):
    records_list = Record.objects.all()
    context = {'records_list': records_list}
    return render(request, 'coreblog/main.html', context)

def detail(request):
    pass

def edit(request):
    pass


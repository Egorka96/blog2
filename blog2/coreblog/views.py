from django.shortcuts import render

from .models import Record


def index(request):
    records_list = Record.objects.all()
    context = {'records_list': records_list}
    return render(request, 'coreblog/main.html', context)


def detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'coreblog/detail.html', {'record': record})


def edit(request):
    pass


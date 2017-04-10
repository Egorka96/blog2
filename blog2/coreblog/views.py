from django.shortcuts import render, get_object_or_404, redirect

from .models import Record
from .forms import RecordForm
from django.http import HttpResponse
from django.utils import timezone


def index(request):
    records_list = Record.objects.all()
    context = {'records_list': records_list}
    return render(request, 'coreblog/main.html', context)


def detail(request, record_id):
    record = Record.objects.get(id=record_id)
    if 'delete' in request.GET:
        record.delete()
        return render(request, 'coreblog/main.html', {'records_list': Record.objects.all()})
    return render(request, 'coreblog/detail.html', {'record': record})


def edit(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.pub_date = timezone.now()
            rec.save()
            return render(request, 'coreblog/detail.html', {'record': record})
    else:
        form = RecordForm(instance=record)
    return render(request, 'coreblog/edit.html', {'form': form})


def new(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.pub_date = timezone.now()
            record.save()
            return render(request, 'coreblog/detail.html', {'record': record})
    else:
        form = RecordForm()
    return render(request, 'coreblog/edit.html', {'form': form})

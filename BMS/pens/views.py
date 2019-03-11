from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pens.models import Pen

class PenList(ListView):
    model = Pen

class PenView(DetailView):
    model = Pen

class PenCreate(CreateView):
    model = Pen
    fields = ['name', 'price']
    success_url = reverse_lazy('pen_list')

class PenUpdate(UpdateView):
    model = Pen
    fields = ['name', 'price']
    success_url = reverse_lazy('pen_list')

class PenDelete(DeleteView):
    model = Pen
    success_url = reverse_lazy('pen_list')
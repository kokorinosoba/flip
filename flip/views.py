from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import FlipForm
from .models import Flip


def ajax(request):
    flips = list(Flip.objects.values('id', 'team_name', 'text'))
    return JsonResponse({'objects': flips})


def delete_all(request):
    Flip.objects.all().delete()
    return HttpResponse('削除しました')


class FlipCreateView(CreateView):
    model = Flip
    template_name = 'flip/create.html'
    form_class = FlipForm

    def get_success_url(self):
        return reverse_lazy('flip:index')


class FlipUpdateView(UpdateView):
    model = Flip
    template_name = 'flip/update.html'
    form_class = FlipForm

    def get_success_url(self):
        return reverse_lazy('flip:index')


class FlipDeleteView(DeleteView):
    model = Flip
    template_name = 'flip/delete.html'
    form_class = FlipForm
    success_url = reverse_lazy('flip:index')

class FlipListView(ListView):
    model = Flip
    template_name = 'flip/index.html'

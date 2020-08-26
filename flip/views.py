from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import FlipForm
from .models import Flip


def ajax(request):
    flips = list(Flip.objects.values('id', 'team_name', 'text'))
    return JsonResponse({'objects': flips})


class FlipCreateView(CreateView):
    model = Flip
    template_name = 'flip/create.html'
    form_class = FlipForm

    def get_success_url(self):
        return reverse_lazy('flip:index')


class FlipListView(ListView):
    model = Flip
    template_name = 'flip/index.html'

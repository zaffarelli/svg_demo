from django.shortcuts import render
from datetime import datetime
from main.utils.mechanics import FONTSET


def prepare_index(request):
    d = datetime.now()
    context = {'fontset': FONTSET}
    return context


def index(request):
    context = prepare_index(request)
    return render(request, 'main/index.html', context=context)

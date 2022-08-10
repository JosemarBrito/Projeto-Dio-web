from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse('<div class="download">'
                        '<a href="https://www.apple.com/br/app-store/" target="_blank" class="app-download">Teste de Impressao</a>'
                        '<a href="https://play.google.com/store/games" target="_blank" class="app-download"></a>'
                        '</div>')

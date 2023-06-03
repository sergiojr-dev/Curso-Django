from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá django fazendo deploy no dia 3-06')

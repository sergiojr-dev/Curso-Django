from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá django dia 04/06')

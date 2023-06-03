from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá django deploy novo no dia 03/06')

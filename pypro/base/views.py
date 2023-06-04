from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá django data 04-06-23')

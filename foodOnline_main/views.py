from django.http import HttpResponse


def home(request):
    return HttpResponse('Hellow World')
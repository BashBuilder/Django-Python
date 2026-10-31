from django.http import HttpResponse


def index(request):
    return HttpResponse("Asia Tour Agency")

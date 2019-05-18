from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 안녕하세요.")



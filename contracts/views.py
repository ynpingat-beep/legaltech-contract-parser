from django.http import HttpResponse

def home(request):
    return HttpResponse("Contracts App Working!")
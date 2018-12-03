from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello!!!")
def random(request):
    data = request.body
    return HttpResponse(data)

def csrf_failure(request, reason=""):
    '''
    This function is for csrf failure, from django docs! Error, should not be redirected to this function!!!!
    '''
    response = json.dumps("don't forget to put csrf failure in urls.py!") #reminder to put csrf failure in urls.py to avoid this error
    return HttpResponse(response)
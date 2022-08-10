from django.http import HttpResponse

# My views are here.

def homePageView(request):
    return HttpResponse("Hello World!")

"""hello_django_asmnt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import HTTPResponse
from urllib import response
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rectangleAreaRoute(request,length=None,width=None):
    if length == None and width == None:
        queryLength = request.GET.get('length')
        queryWidth = request.GET.get('width')
        if queryLength == None or queryWidth == None:
            return HTTPResponse('<h1>404</h1>')
            # return response.status_code     #find a way to return an HTTP status
        area = int(queryLength)*int(queryWidth)
    else:
        area = length*width
    response = HttpResponse(f'<h1>The Area of a rectangle with {length} and {width} is {area}.</h1>')
    return response   

def circleAreaRoute(request,radius=None):
    if radius == None:
        queryRadius = request.GET.get('radius')
        area = (314*((int(queryRadius**2))))/100
    else:
        area = ((radius**2)*314)/100
    response = HttpResponse(f'<h1>The area of a circle with radius {radius} is {area}.</h1>')
    return response

def rectanglePerimeterRoute(request, length = None, width = None):
    if length == None and width == None:
        queryLength = request.GET.get('length')
        queryWidth = request.GET.get('width')
        perim = (2*(int(queryLength)))+(2*(int(queryWidth)))
    else:
        perim = 2*length + 2*width
    response = HttpResponse(f'<h1>The perimeter of a rectangle with length {length} and width {width} is {perim}</h1>')
    return response

def circlePerimeterRoute(request, radius = None):
    if radius == None:
        queryRadius = request.GET.get('radius')
        #add error log here
        perim = (2*314*int(queryRadius))/100
    else:
        perim = (2*314*radius)/100
    response = HttpResponse(f'<h1>The perimeter of a circle of radius {queryRadius} is {perim}.</h1>')
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/', rectangleAreaRoute),     #format for using the query method
    path('rectangle/perimeter/', rectanglePerimeterRoute),
    path('circle/area/', circleAreaRoute),
    path('circle/perimeter/',circlePerimeterRoute),
    path('rectangle/perimeter/<int:length>/<int:width>', rectanglePerimeterRoute),
    path('rectangle/area/<int:length>/<int:width>', rectangleAreaRoute),
    path('circle/area/<int:radius>', circleAreaRoute),
    path('circle/perimeter/<int:radius>',circlePerimeterRoute)
]

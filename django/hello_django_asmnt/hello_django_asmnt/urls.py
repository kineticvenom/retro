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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rectangleRoute(request):
    response = HttpResponse("<h1>this shows the route to rectangle</h1>")
    return response

def circleRoute(request):
    response = HttpResponse("<h1>this shows the route to circle</h1>")
    return response

def rectangleAreaRoute(request, length, width):
    area = length*width
    response = HttpResponse(f'<h1>The Area of a rectangle is {area}.</h1>')
    return response
    
    
    return response

def circleAreaRoute(request):
    return response

def rectanglePerimeterRoute(request):
    return response

def circlePerimeterRoute(request):
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/', rectangleRoute),
    path('circle/', circleRoute),
    path('rectangle/area/<int:length>/<int:width>', rectangleAreaRoute),
    path('circle/area/', circleAreaRoute),
    path('rectangle/perimeter/', rectanglePerimeterRoute),
    path('circle/perimeter/',circlePerimeterRoute),
]

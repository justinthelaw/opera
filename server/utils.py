from django.urls import path

def register_api_route(route_name, view):
    urlpatterns = [
        path(route_name, view),
    ]
    return urlpatterns
from django.http import JsonResponse

def health_check(request):
    health_status = {
        "status": "healthy",
        "timestamp": "2022-01-01T00:00:00Z"
    }
    return JsonResponse(health_status)
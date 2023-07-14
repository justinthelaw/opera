from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .HealthController import HealthController
from .HealthModels import HealthResponse, PossibleHealthServices, RequestedServiceParams

health_controller = HealthController()

@require_http_methods(["GET"])
def overall_health(request):
    try:
        result = health_controller.get_overall_health()
        return JsonResponse(result, status=200)
    except Exception as error:
        # Log the error
        return JsonResponse({}, status=500)

@require_http_methods(["GET"])
def requested_service_health(request, service):
    try:
        sanitize_input = service  # Apply any necessary sanitization
        result = health_controller.get_requested_service_health(sanitize_input)
        return JsonResponse(result, status=200)
    except Exception as error:
        # Log the error
        return JsonResponse({}, status=400)

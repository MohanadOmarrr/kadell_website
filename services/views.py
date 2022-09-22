from django.shortcuts import render, get_object_or_404
from .models import Service, ServicesProducts


# Create your views here.
def services(request):
    all_services = Service.objects.all
    return render(request, 'services.html', {'all_services': all_services})


def service_details(request, service_id):
    all_services = Service.objects.all
    service = get_object_or_404(Service, pk=service_id)

    return render(request, 'services.html', {'all_services': all_services, 'service': service, 'all_products': [products]})
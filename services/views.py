from django.shortcuts import render, get_object_or_404
from .models import Service, ServicesProduct


# Create your views here.
def services(request):
    all_services = Service.objects.all
    return render(request, 'services.html', {'all_services': all_services})


def service_details(request, service_title, service_id):
    all_services = Service.objects.all
    service = get_object_or_404(Service, pk=service_id)
    service_products = []
    all_products = ServicesProduct.objects.all()
    for product in all_products:
        if str(product.service) == service.title:
            service_products.append(product)

    return render(request, 'services-details.html', {
        'all_services': all_services,
        'service': service,
        'service_products': service_products
    })

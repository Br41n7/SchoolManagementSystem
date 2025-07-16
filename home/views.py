from django.shortcuts import render
from .models import Feature, Testimonial, Client


def landing_page(request):
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()


context = {
    'features': features,
    'testimonials': testimonials,
    'clients': clients,
}
return render(request, 'home/home_page.html', context)

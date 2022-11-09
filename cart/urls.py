from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import cart


urlpatterns = [
    path('', cart.views.cart, name='cart'),
    path('add/<int:product_id>', cart.views.add_to_cart, name='add_to_cart'),
    path('delete/<int:product_id>', cart.views.delete_item, name='delete_item')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

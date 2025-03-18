from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, detail, contact, error_page, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('detail/<int:pk>', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('error_page/', error_page, name='error_page'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
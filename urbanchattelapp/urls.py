from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('',views.property_list,name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
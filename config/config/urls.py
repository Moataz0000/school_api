from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
...
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="School API",
      default_version='v1',
      description="This is the backend API for the school.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)



urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('subject.urls', namespace='subjects')),
   path('api/v1/', include('accounts.urls', namespace='accounts')),
   
   
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
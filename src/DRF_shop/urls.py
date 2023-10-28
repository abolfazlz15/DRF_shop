from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('api/admin/catalog/', include(('apps.product.urls.admin', 'apps.product'), namespace='catalog-admin')),
    path('api/admin/users/', include(('auths.accounts.urls.admin', 'auth.product'), namespace='users-admin'))
]

# front_urls =[
#     path('api/front/catalog/', include(('apps.product.urls.admin', 'apps.product'), namespace='catalog-front'))
# ]

doc_patterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns = [
                  path("admin/", admin.site.urls),
              ] + admin_urls + doc_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'DRF Shop'
admin.site.index_title = 'DRF Shop'
admin.site.index_title = 'DRF Shop'

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

admin_urls = [
    path('api/admin/catalog/', include(('apps.product.urls.admin', 'apps.product'), namespace='catalog-admin'))
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

admin.site.site_title = 'DRF Shop'
admin.site.index_title = 'DRF Shop'
admin.site.index_title = 'DRF Shop'

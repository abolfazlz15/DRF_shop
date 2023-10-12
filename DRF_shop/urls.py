from django.contrib import admin
from django.urls import path, include

admin_urls = [
    path('api/admin/catalog/', include(('apps.product.urls.admin', 'apps.product'), namespace='catalog-admin'))
]

# front_urls =[
#     path('api/front/catalog/', include(('apps.product.urls.admin', 'apps.product'), namespace='catalog-front'))
# ]
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
] + admin_urls

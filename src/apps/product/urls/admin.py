from rest_framework.routers import SimpleRouter

from apps.product.views.admin import CategoryViewSet, ProductClassViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('product-class', ProductClassViewSet, basename='product_class')
urlpatterns = [] + router.urls

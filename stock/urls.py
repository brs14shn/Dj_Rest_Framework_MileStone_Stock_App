from django.urls import path,include
from rest_framework import routers
from .views import (
   CategoryView,
   BrandView,
   ProductView
)

router = routers.DefaultRouter()
router.register("category",CategoryView)
router.register("brand",BrandView)
router.register("product",ProductView)
# router.register("firm",FirmViewSet)
# router.register("stock",StockViewSet)


urlpatterns =[
    
    path("",include(router.urls))
     
]
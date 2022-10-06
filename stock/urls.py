from django.urls import path,include
from rest_framework import routers
from .views import (
   CategoryView,
   BrandView,
   ProductView,
   TransactionView,
   FirmView

)

router = routers.DefaultRouter()
router.register("category",CategoryView)
router.register("brand",BrandView)
router.register("product",ProductView)
router.register("firm",FirmView)
router.register("stock",TransactionView)


urlpatterns =[
    
    path("",include(router.urls))
     
]
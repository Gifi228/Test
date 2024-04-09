
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/media/', include("media.urls")),
    path('api/product/', include("product.urls"))
]


from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('api/', include('temp.urls')),
    # path('api/', include('base.urls')),
    # path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

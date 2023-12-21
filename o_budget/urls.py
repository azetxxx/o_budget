from django.contrib import admin
from django.urls import include, path

from contracts.views import ContractsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contracts/', include('contracts.urls', namespace='contracts')),
]

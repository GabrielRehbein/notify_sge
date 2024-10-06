from django.contrib import admin
from django.urls import path
from webhooks.views import WebhookSaleView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/webhooks/sale/', WebhookSaleView.as_view(), name='webhook-sale'),
]

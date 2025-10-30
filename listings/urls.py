# alx_travel_app/listings/urls.py

from django.urls import path
# from .views import InitiateChapaPayment, VerifyChapaPayment <-- COMMENT OUT THIS LINE

urlpatterns = [
    # Paths are commented out so they don't crash when imports fail
    # path('initiate-payment/', InitiateChapaPayment.as_view(), name='initiate-payment'),
    # path('verify-payment/<str:tx_ref>/', VerifyChapaPayment.as_view(), name='verify-payment'),
]

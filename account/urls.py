from django.urls import path

from account.views import CreateUser,AddressView,DetailAddressView,UpdateAddressView,PaymentView,UpdatePaymentView

urlpatterns = [
    path('user',CreateUser.as_view()),
    path('address',AddressView.as_view()),
    path('address/<int:pk>',DetailAddressView.as_view()),
    path('address/update/<int:pk>',UpdateAddressView.as_view()),
    path('payment',PaymentView.as_view()),
    path('payment/update/<int:pk>',UpdatePaymentView.as_view())
]
from django.urls import path

from hotel.views import HotelStatusApi,HotelAvailabilityApi,HotelCheckRateApi,HotelBookingApi,HotelCancelBookingApi

urlpatterns = [
    path("hotel/status/", HotelStatusApi.as_view(), name="hotel-status"),
    path("hotel/availability/", HotelAvailabilityApi.as_view(), name="hotel-availability"),
    path("hotel/checkrate/", HotelCheckRateApi.as_view(), name="hotel-checkrate"),
    path("hotel/booking/", HotelBookingApi.as_view(), name="hotel-booking"),
    path("hotel/cancel/<str:booking_reference>/", HotelCancelBookingApi.as_view(), name="hotel-cancel"),
]
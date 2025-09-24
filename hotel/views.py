import time
import hashlib
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# 🔹 Credentials



# 🔹 Signature generator
def generate_signature(api_key, secret):
    ts = str(int(time.time()))
    raw = api_key + secret + ts
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


# 🔹 Base function for making requests
def hotelbeds_request(method, endpoint, data=None):
    sig = generate_signature(HOTELS["key"], HOTELS["secret"])
    headers = {
        "Api-key": HOTELS["key"],
        "X-Signature": sig,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = f"{HOTELS['base']}{endpoint}"

    if method == "GET":
        r = requests.get(url, headers=headers)
    elif method == "POST":
        r = requests.post(url, headers=headers, json=data)
    elif method == "DELETE":
        r = requests.delete(url, headers=headers)
    else:
        return None

    return r


# 🔹 1. Status check
@method_decorator(csrf_exempt, name="dispatch")
class HotelStatusApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        r = hotelbeds_request("GET", "/status")
        return Response(r.json(), status=r.status_code)


# 🔹 2. Availability Search
@method_decorator(csrf_exempt, name="dispatch")
class HotelAvailabilityApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # ⚠️ JSON body нужно передавать с фронта / Postman
        body = request.data
        r = hotelbeds_request("POST", "/hotels", body)
        return Response(r.json(), status=r.status_code)


# 🔹 3. Check Rate
@method_decorator(csrf_exempt, name="dispatch")
class HotelCheckRateApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        body = request.data
        r = hotelbeds_request("POST", "/checkrates", body)
        return Response(r.json(), status=r.status_code)


# 🔹 4. Booking
@method_decorator(csrf_exempt, name="dispatch")
class HotelBookingApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        body = request.data
        r = hotelbeds_request("POST", "/bookings", body)
        return Response(r.json(), status=r.status_code)


# 🔹 5. Cancel booking
@method_decorator(csrf_exempt, name="dispatch")
class HotelCancelBookingApi(APIView):
    authentication_classes = []
    permission_classes = []

    def delete(self, request, booking_reference):
        endpoint = f"/bookings/{booking_reference}?cancellationFlag=CANCELLATION"
        r = hotelbeds_request("DELETE", endpoint)
        return Response(r.json(), status=r.status_code)

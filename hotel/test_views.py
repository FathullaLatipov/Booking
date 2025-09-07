import time
import hashlib
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Credentials and endpoints
HOTELS = {
    "key": "9e7d8b5843787356fbd7cdebbf4b7abf",
    "secret": "0baa473b16",
    "base": "https://api.test.hotelbeds.com/hotel-api/1.0"
}
TRANSFERS = {
    "key": "fe7ea7b659b12fdb66c0e05284f87815",
    "secret": "c1c8ce2783",
    "base": "https://api.test.hotelbeds.com/transfer-api/1.0"
}
ACTIVITIES = {
    "key": "ea66f6b771f1675ea92cdf8cb91e2320",
    "secret": "4a1a8b6582",
    "base": "https://api.test.hotelbeds.com/activity-api/3.0"
}

def generate_signature(api_key, secret):
    ts = str(int(time.time()))
    raw = api_key + secret + ts
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()

@method_decorator(csrf_exempt, name='dispatch')
class HotelStatusApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        sig = generate_signature(HOTELS["key"], HOTELS["secret"])
        print(f'This is sig = {sig}')
        headers = {
            "Api-key": HOTELS["key"],
            "X-Signature": sig,
            "Accept": "application/json"
        }
        print(f'This is headers = {headers}')
        r = requests.get(f"{HOTELS['base']}/status", headers=headers)
        print(f'This is r = {r}')
        return Response(r.json(), status=r.status_code)

@method_decorator(csrf_exempt, name='dispatch')
class TransfersStatusApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        sig = generate_signature(TRANSFERS["key"], TRANSFERS["secret"])
        headers = {
            "Api-key": TRANSFERS["key"],
            "X-Signature": sig,
            "Accept": "application/json"
        }
        r = requests.get(f"{TRANSFERS['base']}/status", headers=headers)
        return Response(r.json(), status=r.status_code)

@method_decorator(csrf_exempt, name='dispatch')
class ActivitiesStatusApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        sig = generate_signature(ACTIVITIES["key"], ACTIVITIES["secret"])
        headers = {
            "Api-key": ACTIVITIES["key"],
            "X-Signature": sig,
            "Accept": "application/json"
        }
        r = requests.get(f"{ACTIVITIES['base']}/status", headers=headers)
        return Response(r.json(), status=r.status_code)


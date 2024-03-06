from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account, Destination
from django.http import JsonResponse

class IncomingDataAPI(APIView):
    def post(self, request):
        data = request.data
        secret_token = request.headers.get('CL-X-TOKEN')
        
        if not secret_token:
            return Response({"message": "Un Authenticate"}, status=401)
        
        try:
            account = Account.objects.get(app_secret_token=secret_token)
        except Account.DoesNotExist:
            return Response({"message": "Invalid secret token"}, status=401)
        
        if request.method == 'GET':
            return JsonResponse({"message": "Invalid Data"}, status=400)
        
        destinations = Destination.objects.filter(account=account)
        for destination in destinations:
            if destination.http_method == 'GET':
                # Send data as query parameters
                # Example: requests.get(destination.url, params=data)
                pass
            else:
                # Send data as JSON
                # Example: requests.post(destination.url, json=data, headers=destination.headers)
                pass
        
        return Response({"message": "Data received and sent to destinations successfully"}, status=200)
# Import necessary modules and functions
from django.http import JsonResponse
from .ai.AI import predict_email
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def scam_detection_view(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        print(body)
        x = predict_email(body)
        print(x)
        return( JsonResponse({"x":x}))
    
from django.http import JsonResponse
from .models import Email

def email_addresses(request):
    request.data['emails']
    email_objects = Email.objects.all()
    email_addresses = [email.email_address for email in email_objects]
    res = []
    for i in request.data["emails"]:
        if i in email_addresses:
            res.append(i)
        print(i)
    return JsonResponse(res, safe=False)
def report(request):
    request.data['text']
    return JsonResponse({"success":True})
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
def post_email(request):
     serializer = EmailSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=201)
     return Response(serializer.errors, status=400)

def getPrediction():
    return JsonResponse({"hi":"world"})


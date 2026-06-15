from django.http import HttpResponse

def home(request):
    return HttpResponse("Contracts App Working!")

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Contract
from .serializers import ContractSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_contract(request):

    serializer = ContractSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
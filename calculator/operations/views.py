from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import operationSerializers

# Create your views here.
array =[]

@api_view(["POST"])
def operations(request):
    if(request.method=="POST"):
        serializer = operationSerializers(data=request.data)
        if(serializer.is_valid()):
            array = serializer.validated_data['serializer']
            return Response({'array':array})
@api_view(["GET"])
def operations(request):
    if(request.method=="GET"):
        serializer = operationSerializers(data=request.query_params)
        if(serializer.is_valid()):
            array = serializer.validated_data['serializer']
            return Response(array.data)
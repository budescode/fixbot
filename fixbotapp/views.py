from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import TelemetricSerializer
from .models import TelemetricModel
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


#this class is used to pull all data
class TelemetricDetail(generics.ListAPIView):
    queryset = TelemetricModel.objects.all()
    serializer_class = TelemetricSerializer


#this class is used to retrieve, update and delete a single data.
class TelemetricModelDetail(APIView):
    """
    Retrieve, update or delete a TelemetricModel instance.
    """
    def get_object(self, pk):
        try:
            return TelemetricModel.objects.get(pk=pk)
        except TelemetricModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        TelemetricModel = self.get_object(pk)
        serializer = TelemetricSerializer(TelemetricModel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        TelemetricModel = self.get_object(pk)
        serializer = TelemetricSerializer(TelemetricModel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        TelemetricModel = self.get_object(pk)
        TelemetricModel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#this class is used to post data
class TelemetricPost(APIView):
    """
    post a TelemetricModel instance.
    """
    def post(self, request, format=None):
        serializer = TelemetricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
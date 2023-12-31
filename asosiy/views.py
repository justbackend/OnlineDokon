from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.conf import settings



class MahsulotQidiruvApi(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        qidiruv_soz = request.query_params.get("brend")
        if qidiruv_soz:
            mahsulotlar = Mahsulot.objects.filter(brend__contains=qidiruv_soz)
        serializer = MaxsulotSerializers(mahsulotlar, many=True)
        return Response(serializer.data)

class MahsulotGetApi(APIView):
    def get(self, request, pk):
        model = Mahsulot.objects.filter(nom__contains=pk)
        serializer = MaxsulotSerializers(model, many=True)
        return Response(serializer.data)


from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import *
from .serializers import *

class MahsulotModelViewSet(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MaxsulotSerializers

class MediaAPIView(APIView):
    def get(self, pk, request):
        product = Mahsulot.objects.get(id=pk)
        media = Media.objects.filter(mahsulot=product)
        serializer = MediaSerializers(media, many=True)
        return Response(serializer.data)


class IzohAPIView(APIView):
    def get(self, pk, request):
        product = Mahsulot.objects.get(id=pk)
        izoh = Izoh.objects.filter(mahsulot=product)
        serializer = IzohSerializer(izoh, many=True)
        return Response(serializer.data)

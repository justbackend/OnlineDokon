from  rest_framework import serializers

from .models import *

class MaxsulotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"



class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"

class BolimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = "__all__"


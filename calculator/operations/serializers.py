from rest_framework import serializers

class operationSerializers(serializers.ModelSerializer):
    array = serializers.ListField(child=serializers.IntegerField())
from rest_framework import serializers

class TwoNumberSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()

class NumberSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=0)

class PowerSerializer(serializers.Serializer):
    base = serializers.FloatField()
    exp = serializers.FloatField()

class MatrixMultiplySerializer(serializers.Serializer):
    A = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    B = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import TwoNumberSerializer, NumberSerializer, PowerSerializer, MatrixMultiplySerializer
from math import factorial
from typing import List
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AddView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={200: openapi.Response('Toplama sonucu', TwoNumberSerializer)}
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.validated_data['a']
            b = serializer.validated_data['b']
            return Response({"result": a + b})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubtractView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={200: openapi.Response('Çıkarma sonucu', TwoNumberSerializer)}
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.validated_data['a']
            b = serializer.validated_data['b']
            return Response({"result": a - b})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MultiplyView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={200: openapi.Response('Çarpma sonucu', TwoNumberSerializer)}
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.validated_data['a']
            b = serializer.validated_data['b']
            return Response({"result": a * b})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DivideView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={
            200: openapi.Response('Bölme sonucu', TwoNumberSerializer),
            400: "Sıfıra bölünemez"
        }
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.validated_data['a']
            b = serializer.validated_data['b']
            if b == 0:
                return Response({"error": "Sıfıra bölünemez"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"result": a / b})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FactorialView(APIView):
    @swagger_auto_schema(
        request_body=NumberSerializer,
        responses={200: openapi.Response('Faktöriyel sonucu', NumberSerializer)}
    )
    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            n = serializer.validated_data['n']
            return Response({"result": factorial(n)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsPrimeView(APIView):
    @swagger_auto_schema(
        request_body=NumberSerializer,
        responses={200: openapi.Response('Asal kontrol sonucu', NumberSerializer)}
    )
    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            n = serializer.validated_data['n']
            if n < 2:
                return Response({"is_prime": False})
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return Response({"is_prime": False})
            return Response({"is_prime": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GcdView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={200: openapi.Response('EBOB sonucu', TwoNumberSerializer)}
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a, b = int(serializer.validated_data['a']), int(serializer.validated_data['b'])
            while b != 0:
                a, b = b, a % b
            return Response({"result": a})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LcmView(APIView):
    @swagger_auto_schema(
        request_body=TwoNumberSerializer,
        responses={200: openapi.Response('EKOK sonucu', TwoNumberSerializer)}
    )
    def post(self, request):
        serializer = TwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            a, b = int(serializer.validated_data['a']), int(serializer.validated_data['b'])
            def gcd(x, y):
                while y:
                    x, y = y, x % y
                return x
            lcm = abs(a*b)//gcd(a,b)
            return Response({"result": lcm})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PowerView(APIView):
    @swagger_auto_schema(
        request_body=PowerSerializer,
        responses={200: openapi.Response('Üs alma sonucu', PowerSerializer)}
    )
    def post(self, request):
        serializer = PowerSerializer(data=request.data)
        if serializer.is_valid():
            base = serializer.validated_data['base']
            exp = serializer.validated_data['exp']
            return Response({"result": base ** exp})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatrixMultiplyView(APIView):
    @swagger_auto_schema(
        request_body=MatrixMultiplySerializer,
        responses={200: openapi.Response('Matris çarpma sonucu', MatrixMultiplySerializer)}
    )
    def post(self, request):
        serializer = MatrixMultiplySerializer(data=request.data)
        if serializer.is_valid():
            A = serializer.validated_data['A']
            B = serializer.validated_data['B']
            if len(A[0]) != len(B):
                return Response({"error": "Matris boyutları uyumsuz"}, status=status.HTTP_400_BAD_REQUEST)
            result: List[List[float]] = [[0]*len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k]*B[k][j]
            return Response({"result": result})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

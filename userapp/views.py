from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class AccountApi(APIView):
    def get(self, request):
        model = Account.objects.all()
        serializer = AccountSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:": "Account created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountApiOne(APIView):
    def get(self, request, pk):
        try:
            model = Account.objects.get(id=pk)
        except:
            return Response({"message": "Account doesnt exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            model = Account.objects.get(id=pk)
        except:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account updated successfully"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Account.objects.get(id=pk).delete()
            return Response({"message": "Account deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"message": "Something went wrong"}, status=status.HTTP_204_NO_CONTENT)





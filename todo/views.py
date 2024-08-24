from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TodoSerializer, RegistationSerializer
from .models import TodoModels


class TodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Assign the todo to the logged-in user
        request.data['user'] = request.user.id
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Fetch todos for the logged-in user
        todos = TodoModels.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            # Fetch todo for the logged-in user
            todo = TodoModels.objects.get(id=pk, user=request.user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TodoModels.DoesNotExist:
            return Response({"Item does not exist"}, status=status.HTTP_404_NOT_FOUND)


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            # Use the username for authentication
            user = authenticate(username=user.username, password=password)
            if user:
                token = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(token),
                    "access": str(token.access_token),
                }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pass  # fall through to the invalid credentials response
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

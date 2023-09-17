from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

class UserView(ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    # /user/is_user_staff/
    @action(detail=False, methods=['GET'])
    def is_user_staff(self, request):
        user=request.user
        is_staff= user.is_staff
        return Response(is_staff)
    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'user created'})
        return Response(data=ser.errors)
    def retrieve(self, request, pk=None):
        try:
            if(pk=='0'):
                user = self.request.user
            else:
                user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found'})
        serializer = UserSerializer(user)
        return Response(serializer.data)

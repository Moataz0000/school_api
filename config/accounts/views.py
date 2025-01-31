from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeacherSerializer, StudentSerializer
from .common.exceptions import UserRegisterException
from rest_framework_simplejwt.tokens import RefreshToken

class TeacherRegisterView(APIView):
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        
        if serializer.is_valid():
            teacher = serializer.save()
            refresh = RefreshToken.for_user(teacher)
            return Response({
                'message': 'Teacher registered successfully.',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            },status=status.HTTP_201_CREATED)
        raise UserRegisterException()
        








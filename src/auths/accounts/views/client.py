from django.core.cache import cache
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.accounts.models import User

from auths.accounts.otp_service import OTP
from auths.accounts.serializers.client import CreateUserSerializer, VerifyOTPCodeSerializer


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            clean_data = serializer.validated_data
            otp_service = OTP()
            otp_code = otp_service.generate_otp(clean_data['email'])
            cache.set(key=otp_code, value={'email': clean_data['email'], 'password': clean_data['password'],
                                           'full_name': clean_data['full_name'], 'phone': clean_data['phone']}, timeout=300)

            return Response({'email': clean_data['email'], 'result': 'email sent', 'success': True},
                            status=status.HTTP_202_ACCEPTED)
        return Response({'errors': serializer.errors, 'success': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
class VerifyOTPCodeView(APIView):
    serializer_class = VerifyOTPCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        otp = OTP()
        if serializer.is_valid():
            clean_data = serializer.validated_data
            user_data = cache.get(clean_data['code'])
            if user_data is None:
                return Response({'error': 'this code not exist or invalid', 'success': False}, status=status.HTTP_404_NOT_FOUND)
            
            if otp.verify_otp(otp=clean_data['code'], email=user_data['email']):
                user = User.objects.create_user(email=user_data['email'], full_name=user_data['full_name'], password=user_data['password'], phone=user_data)
                result = serializer.save(validated_data=user)
                return Response(result, status=status.HTTP_201_CREATED)

            return Response({'error': 'this code not exist or invalid', 'success': False}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

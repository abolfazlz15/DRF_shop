from django.core.cache import cache
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from auths.accounts.otp_service import OTP
from auths.accounts.serializers.client import CreateUserSerializer


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
                                           'full_name': clean_data['full_name']}, timeout=300)

            return Response({'email': clean_data['email'], 'result': 'email sent', 'success': True},
                            status=status.HTTP_202_ACCEPTED)
        return Response({'errors': serializer.errors, 'success': False}, status=status.HTTP_406_NOT_ACCEPTABLE)

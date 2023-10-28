from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auths.accounts.serializers.admin import AdminLoginSerializer


class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save(validated_data=serializer.validated_data)
        return Response(result, status=status.HTTP_200_OK)

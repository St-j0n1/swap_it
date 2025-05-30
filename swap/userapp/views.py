from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegistrationSerializer, ProfileSerializer, PasswordResetSerializer, EmailVerificationSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .utils import send_verification_code


class RegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = []
    authentication_classes = []

class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

#TODO: add a view for password reset
class PasswordResetWithRecoveryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendVerificationCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        send_verification_code(request.user.email)
        return Response({"detail": "Verification code resent."})


class EmailVerificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.user.email.lower()  # normalize
        code = serializer.validated_data['code']

        redis_key = f'verify:{email}'
        stored_code = cache.get(redis_key)

        if not stored_code:
            return Response({"error": "Verification code expired or not found."}, status=status.HTTP_400_BAD_REQUEST)

        if code != stored_code:
            return Response({"error": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.confirm_email =  True
        request.user.save()
        cache.delete(redis_key)
        return Response({"detail": "Email verified successfully."}, status=status.HTTP_200_OK)

class DeleteOwnAccountView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "Account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


#TODO: add a view for email change

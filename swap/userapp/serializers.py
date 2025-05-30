from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser
from .utils import send_verification_code

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    recovery_question_answer = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'birth_date',
            'username', 'password', 'confirm_password', 'email',
            'recovery_question', 'recovery_question_answer', 'location'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['recovery_question_answer'] = make_password(validated_data['recovery_question_answer'])
        email = validated_data.get('email')
        user = CustomUser.objects.create(**validated_data)
        send_verification_code(email)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'username', 'email', 'location']
        read_only_fields = ['username', 'email']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    recovery_question_answer = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.context['request'].user

        # Check old password
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})

        # Check recovery question answer
        if not check_password(attrs['recovery_question_answer'], user.recovery_question_answer):
            raise serializers.ValidationError({"recovery_question_answer": "Recovery answer is incorrect."})

        # Confirm a new password match
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user

from rest_framework import serializers

class EmailVerificationSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=6, max_length=6)

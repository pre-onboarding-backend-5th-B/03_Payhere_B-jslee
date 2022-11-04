from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework import serializers

User = get_user_model()
password_regx = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
password_caution = '최소 8글자 이상, 하나 이상의 문자, 숫자, 특수문자가 포함되어야 합니다.'


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        validators=[RegexValidator(password_regx, message=password_caution)],
        write_only=True,
        help_text=password_caution,
    )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'password']

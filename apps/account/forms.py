from django import forms
from django.contrib.auth import authenticate

from .models import Account


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=6, max_length=68)
    password2 = forms.CharField(min_length=6, max_length=68)

    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise forms.ValidationError(
                {'success': False, 'message': 'Password did not match, please try again', })
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=101, required=True)
    password = forms.CharField(max_length=68, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise

        data = {
            'success': True,
            'email': user.email,
        }
        return data

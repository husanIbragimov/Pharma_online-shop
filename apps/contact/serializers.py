from rest_framework import serializers
from .models import GetInTouch, Subscribe


class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = ['id',
                  'full_name',
                  'phone',
                  'email',
                  'message',
                  'user_data',
                  ]


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']

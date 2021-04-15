from rest_framework import serializers

# from chat.models import Message
from .models import Message


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'author', 'text')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

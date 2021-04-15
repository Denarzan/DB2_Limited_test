from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Message
from .serializers import MessageListSerializer, MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer


class MessageListView(generics.ListAPIView):
    pagination_class = PageNumberPagination
    PageNumberPagination.page_query_param = ''
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()


class MessageDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

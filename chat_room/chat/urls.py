from django.contrib import admin
from django.urls import path, include
# from chat.views import *

from .views import *

app_name = 'chat'
urlpatterns = [
    path('chat/create/', MessageCreateView.as_view()),
    path('messages/list/', MessageListView.as_view()),
    path('messages/single/<int:pk>', MessageDetailView.as_view()),
]

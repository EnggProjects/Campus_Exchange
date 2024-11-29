from django.urls import path
from . import views

urlpatterns = [
    # Initiates a conversation with a specific user by their user_id
    path('start/<int:user_id>/', views.start_conversation, name='start_conversation'),

    # View the details of a specific conversation using its primary key (conversation_id)
    path('chat/conversation/<int:pk>/', views.conversation_detail, name='conversation_detail'),

    # Sends a message in a specific conversation
    path('<int:pk>/send/', views.send_message, name='send_message'),

    # Lists all the conversations for the current user
    path('my-chats/', views.my_chats, name='my_chats'),

    #delete convos
    path('conversation/<int:pk>/delete/', views.delete_conversation, name='delete_conversation'),
]

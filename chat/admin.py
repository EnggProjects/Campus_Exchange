from django.contrib import admin
from .models import Conversation, Message

# Register the Conversation model
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_participants')  # Show conversation ID and participants
    search_fields = ('participants__username',)  # Assuming User has a 'username' field

    def get_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    get_participants.short_description = 'Participants'

# Register the Message model
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'content', 'timestamp', 'read')
    search_fields = ('conversation__participants__username', 'sender__username', 'content')
    list_filter = ('timestamp', 'read')
    readonly_fields = ('timestamp',)  # Make 'timestamp' field read-only

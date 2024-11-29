# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseForbidden

User = get_user_model()

@login_required
def start_conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)  # Use get_object_or_404 for safety

    if other_user == request.user:
        return redirect('product_list')  # Prevent user from starting a chat with themselves.

    # Check if a conversation already exists
    conversation = Conversation.objects.filter(
        Q(participants=request.user) & Q(participants=other_user)
    ).first()

    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)

    return redirect('conversation_detail', pk=conversation.id)


@login_required
def conversation_detail(request, pk):  # Changed conversation_id to pk
    # Get the conversation or return a 404 if it doesn't exist
    conversation = get_object_or_404(Conversation, id=pk, participants=request.user)

    # Mark messages as read for the logged-in user
    Message.objects.filter(conversation=conversation, read=False).exclude(sender=request.user).update(read=True)

    # Fetch all messages in the conversation
    messages = conversation.message_set.all()

    return render(request, 'chat/conversation_detail.html', {
        'conversation': conversation,
        'messages': messages,
        'unread_message_count': Message.objects.filter(conversation__participants=request.user, read=False).exclude(sender=request.user).count()
    })

@login_required
def delete_conversation(request, pk):
    conversation = get_object_or_404(Conversation, id=pk, participants=request.user)
    
    if request.method == 'POST':
        # Ensure the user is part of the conversation
        if request.user in conversation.participants.all():
            conversation.delete()  # Delete the conversation and its associated messages
            return redirect('my_chats')  # Redirect to the chats list
        else:
            return HttpResponseForbidden("You are not allowed to delete this conversation.")
    
    return render(request, 'chat/delete_confirmation.html', {'conversation': conversation})


@login_required
def send_message(request, pk):  # Changed conversation_id to pk
    if request.method == 'POST':
        conversation = get_object_or_404(Conversation, id=pk)  # Use get_object_or_404 for safety
        content = request.POST.get('content')
        Message.objects.create(conversation=conversation, sender=request.user, content=content, read=False)
        return redirect('conversation_detail', pk=pk)  # Use pk here


@login_required

def my_chats(request):
    conversations = Conversation.objects.filter(participants=request.user)
    
    conversation_data = []
    for conversation in conversations:
        other_participant = conversation.participants.exclude(id=request.user.id).first()
        latest_message = conversation.message_set.last()
        
        # Get unread message count for this specific conversation
        unread_count = Message.objects.filter(
            conversation=conversation,
            read=False
        ).exclude(sender=request.user).count()
        
        conversation_data.append({
            'conversation': conversation,
            'other_participant_username': other_participant.username if other_participant else 'Unknown',
            'latest_message': latest_message,
            'unread_count': unread_count  # Add unread count for this conversation
        })

    return render(request, 'chat/my_chats.html', {
        'conversations': conversation_data,
    })


@login_required  
def some_view(request):
    unread_message_count = Message.objects.filter(conversation__participants=request.user, read=False).exclude(sender=request.user).count()
    return render(request, 'base.html', {'unread_message_count': unread_message_count})

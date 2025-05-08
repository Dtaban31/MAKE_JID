from django.contrib import admin
from .models import Post, RSVP, Account

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created_by')
    list_filter = ('event_date', 'created_by')

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('post', 'created_at')

# Also register the Account model so you can manage users in the admin
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')

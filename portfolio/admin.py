from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "title", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "title", "message")
    list_editable = ("is_read",)

admin.site.register(ContactMessage, ContactMessageAdmin)

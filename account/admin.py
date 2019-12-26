from __future__ import unicode_literals

from django.contrib import admin

from pinax.documents.models import Folder, Document, UserStorage

from .models import (
    Account,
    AccountDeletion,
    EmailAddress,
    PasswordExpiry,
    PasswordHistory,
    SignupCode,
)

class FolderAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "author", "created", "modified", "modified_by"]
    search_fields = ["name", "author", "created"]
    list_filter = ["author", "created"]

class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "folder", "author", "created", "modified", "modified_by", "file", "original_filename"]
    search_fields = ["name", "folder", "author", "created", "file"]
    list_filter = ["created", "file", "modified_by"]

class UserStorageAdmin(admin.ModelAdmin):
    list_display = ["user", "bytes_used", "bytes_total"]

class SignupCodeAdmin(admin.ModelAdmin):

    list_display = ["code", "max_uses", "use_count", "expiry", "created"]
    search_fields = ["code", "email"]
    list_filter = ["created"]
    raw_id_fields = ["inviter"]


class AccountAdmin(admin.ModelAdmin):

    raw_id_fields = ["user"]


class AccountDeletionAdmin(AccountAdmin):

    list_display = ["email", "date_requested", "date_expunged"]


class EmailAddressAdmin(AccountAdmin):

    list_display = ["user", "email", "verified", "primary"]
    search_fields = ["email", "user__username"]


class PasswordExpiryAdmin(admin.ModelAdmin):

    raw_id_fields = ["user"]


class PasswordHistoryAdmin(admin.ModelAdmin):

    raw_id_fields = ["user"]
    list_display = ["user", "timestamp"]
    list_filter = ["user"]
    ordering = ["user__username", "-timestamp"]


admin.site.register(Folder, FolderAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(UserStorage, UserStorageAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(SignupCode, SignupCodeAdmin)
admin.site.register(AccountDeletion, AccountDeletionAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(PasswordExpiry, PasswordExpiryAdmin)
admin.site.register(PasswordHistory, PasswordHistoryAdmin)

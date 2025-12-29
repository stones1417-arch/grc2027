from django.contrib import admin
from .models import (
    OrganizationUnit,
    Site,
    Role,
    UserProfile,
    Attachment
)


@admin.register(OrganizationUnit)
class OrganizationUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at')
    search_fields = ('name',)
    list_filter = ('parent',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization_unit', 'role', 'site')
    list_filter = ('organization_unit', 'role', 'site')
    search_fields = ('user__username',)


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_at')
    search_fields = ('title',)

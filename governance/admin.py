from django.contrib import admin
from .models import (
    Framework,
    Policy,
    Procedure,
    Control
)


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'approved', 'owner')
    list_filter = ('approved',)
    search_fields = ('title',)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('title', 'policy')
    search_fields = ('title',)


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ('name', 'control_type', 'framework', 'owner')
    list_filter = ('control_type', 'framework')
    search_fields = ('name',)

from django.contrib import admin
from .models import (
    Role,
    Status,
    Permission,
    RolePermission,
    EscalationRule,
    TicketField,
    Ticket,
    TicketFieldValue,
    TicketHistory,
    UserRole
)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'description', 'created_at')
    search_fields = ('role_name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'description', 'status_order', 'created_at')
    search_fields = ('status_name',)
    ordering = ('status_order',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_name', 'description')
    search_fields = ('permission_name',)


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission', 'created_at')
    search_fields = ('role__role_name', 'permission__permission_name')
    autocomplete_fields = ('role', 'permission')


@admin.register(EscalationRule)
class EscalationRuleAdmin(admin.ModelAdmin):
    list_display = ('role', 'escalation_time', 'description', 'created_at')
    search_fields = ('role__role_name',)
    list_filter = ('role',)


@admin.register(TicketField)
class TicketFieldAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'field_type', 'is_required', 'created_at')
    search_fields = ('field_name',)
    list_filter = ('field_type', 'is_required')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'escalation_deadline', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('status', 'priority', 'created_at')
    autocomplete_fields = ('user', 'status')


@admin.register(TicketFieldValue)
class TicketFieldValueAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'field', 'value')
    search_fields = ('ticket__title', 'field__field_name', 'value')
    autocomplete_fields = ('ticket', 'field')


@admin.register(TicketHistory)
class TicketHistoryAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'action_by', 'action', 'status', 'role', 'timestamp')
    search_fields = ('ticket__title', 'action_by__username', 'action')
    list_filter = ('action', 'status', 'role')
    autocomplete_fields = ('ticket', 'action_by', 'status', 'role')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at')
    search_fields = ('user__username', 'role__role_name')
    autocomplete_fields = ('user', 'role')

from django.db import models
from django.contrib.auth.models import User

# Role Model
class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name


# Status Model
class Status(models.Model):
    status_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    status_order = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_name


# Permission Model
class Permission(models.Model):
    permission_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.permission_name


# RolePermissions Model
class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('role', 'permission')


# Escalation Rules Model
class EscalationRule(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="escalation_rules")
    escalation_time = models.PositiveIntegerField(help_text="Time in minutes")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role.role_name} - {self.escalation_time} mins"


# TicketFields Model
class TicketField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('dropdown', 'Dropdown'),
    ]

    field_name = models.CharField(max_length=100, unique=True)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPES)
    field_options = models.JSONField(null=True, blank=True, help_text="Options for dropdown fields")
    is_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field_name


# Ticket Model
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name="tickets")
    priority = models.CharField(max_length=20, default="Medium", choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ])
    escalation_deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# TicketFieldValues Model
class TicketFieldValue(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="field_values")
    field = models.ForeignKey(TicketField, on_delete=models.CASCADE, related_name="field_values")
    value = models.TextField()

    def __str__(self):
        return f"{self.ticket.title} - {self.field.field_name}: {self.value}"


# TicketHistory Model
class TicketHistory(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="history")
    action_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="ticket_actions")
    action = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name="ticket_histories")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="ticket_histories")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket.title} - {self.action} by {self.action_by}"


# UserRole Assignment (Optional if User-Role mapping is needed)
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="role_assignment")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"

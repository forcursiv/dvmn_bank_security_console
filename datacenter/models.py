from django.db import models
from django.utils import timezone
from .utils import format_duration


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_formatted_duration(self):
        seconds = self.get_duration_seconds()
        return format_duration(seconds)

    def get_duration_seconds(self):
        delta = (self.leaved_at or timezone.now()) - self.entered_at
        return delta.total_seconds()

    def is_strange(self, minutes = 60):
        duration = int(self.get_duration_seconds() // 60)
        return duration > minutes

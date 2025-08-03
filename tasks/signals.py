from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def notify_owner_on_status_change(sender, instance, created, **kwargs):
    if created:
        return  # Не отправляем при создании

    if instance.status != instance.last_notified_status:
        print(f"📧 Email to {instance.owner.email}: Task '{instance.title}' changed status to {instance.status.upper()}!")

        # Сохраняем последний уведомлённый статус
        instance.last_notified_status = instance.status
        instance.save(update_fields=['last_notified_status'])

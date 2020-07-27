from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


# through это ссылка на таблицу, так как users_like это всего лишь m2m менеджер
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()

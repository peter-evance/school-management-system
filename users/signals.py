from io import BytesIO
from os.path import basename

from PIL import Image
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import ProfileImage


@receiver(post_save, sender=ProfileImage)
def generate_thumbnail(sender, instance, created, **kwargs):
    if created:
        image = Image.open(instance.image)
        image.thumbnail((100, 100))
        thumb_io = BytesIO()
        image.save(thumb_io, format="png")

        instance.thumbnail.save(
            basename(instance.image.name), ContentFile(thumb_io.getvalue())
        )
        instance.save()

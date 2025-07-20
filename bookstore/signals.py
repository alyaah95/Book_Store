from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book,ISBN
import uuid

@receiver(post_save, sender=Book)
def book_save_handler(sender, instance, created, **kwargs):
    if created:
        try:
            if not hasattr(instance, 'ISBN'):

                unique_id = str(uuid.uuid4().int)[:13] 
                generated_isbn = unique_id

                ISBN.objects.create(
                    ISBN_number=generated_isbn,
                    book=instance 
                )
            

        except Exception as e:
            print(f"an error occured with'{instance.title}': {e}")




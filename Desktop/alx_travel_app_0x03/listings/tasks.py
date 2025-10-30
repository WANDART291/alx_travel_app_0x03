# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, listing_title, recipient_email):
    """Sends a booking confirmation email asynchronously."""
    subject = f'Booking Confirmation for {listing_title}'
    message = (
        f"Dear User,\n\nYour booking (ID: {booking_id}) for the listing '{listing_title}' "
        f"has been successfully confirmed.\n\nThank you for using the ALX Travel App!"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email], fail_silently=False)
    print(f"Celery Worker Log: Confirmation email 'sent' for booking {booking_id}")
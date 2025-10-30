# listings/views.py (Modify your existing BookingViewSet)

from rest_framework import viewsets
# ... other imports ...

from .tasks import send_booking_confirmation_email
# from .models import Booking, Listing, etc.
# from .serializers import BookingSerializer, ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    # ... existing queryset, serializer_class, etc.

    def perform_create(self, serializer):
        # 1. Save the new Booking object
        booking = serializer.save()

        # 2. Gather necessary data (assuming these fields exist on your models)
        booking_id = booking.id
        listing_title = booking.listing.title 
        recipient_email = booking.user.email 

        # 3. Trigger the Celery Task (Offload to background)
        send_booking_confirmation_email.delay(
            booking_id,
            listing_title,
            recipient_email
        )
        
        print(f"Django Server Log: Task for booking {booking_id} queued successfully via Redis.")
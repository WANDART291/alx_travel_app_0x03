from django.db import models
import uuid

# =========================================================
# 1. Existing Models (Listing and Booking)
# =========================================================

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    guest_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        # fstring from your screenshot: f"Booking for {self.guest_name} at {self.listing.title}"
        return f"Booking for {self.guest_name} at {self.listing.title}"


# =========================================================
# 2. New Payment Integration Models/Logic
# =========================================================

# Define the choices for payment status
class PaymentStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class Payment(models.Model):
    # Field to link the Payment back to a single, unique Booking record
    booking = models.OneToOneField(
        'Booking', 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # tx_ref (Transaction Reference): Unique ID sent to Chapa
    tx_ref = models.CharField(
        max_length=100,
        unique=True,
        default=uuid.uuid4,  # Auto-generated unique ID
        verbose_name="Transaction Reference"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='ETB') 
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Chapa's unique identifier for the transaction (stored after verification)
    chapa_transaction_id = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.tx_ref} - {self.status}"
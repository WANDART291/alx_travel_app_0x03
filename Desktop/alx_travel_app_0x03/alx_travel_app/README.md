# alx_travel_app_0x02: Milestone 4 - Chapa Payment Integration

## 📝 Project Overview

This project completes **Milestone 4** of the Django-based travel booking application by integrating the **Chapa Payment Gateway** for secure transaction processing. The core focus was to establish a reliable payment workflow, from initiation to verification, ensuring bookings are only confirmed upon successful payment.

---

## ✨ Learning Outcomes

By completing this task, the following technical skills were demonstrated:

* **API Integration:** Successfully connected the Django backend to the external Chapa REST API using the `requests` library.
* **Secure Credential Management:** Implemented the `python-dotenv` library to securely load and utilize the `CHAPA_SECRET_KEY` from environment variables.
* **Data Modeling:** Created the `Payment` model to persist and track transaction data (`tx_ref`, `amount`, `status`, etc.).
* **Payment Workflow:** Built API endpoints for:
    1.  **Initiation:** Sending booking details to Chapa and receiving a secure checkout URL.
    2.  **Verification:** Handling the callback/redirect from Chapa to confirm the transaction status and update the local database record.
* **Security Handling:** Used the `@csrf_exempt` decorator on the payment initiation endpoint to allow external POST requests while maintaining Django's general security.
* **Asynchronous Tasks (Conceptual):** Integrated a placeholder function to simulate the asynchronous sending of confirmation emails using a Celery task upon successful payment.

---

## 📂 Project Structure

The primary file modifications were made within the `listings` application and the main project configuration:

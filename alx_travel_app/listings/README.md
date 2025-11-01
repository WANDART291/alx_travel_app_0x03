# alx_travel_app_0x03: Milestone 5 - Setting Up Background Jobs for Email Notifications

This project implements asynchronous background processing using Celery with Redis as the message broker to handle email notifications, ensuring the main application remains responsive.

---

## Project Requirements
The following files were updated/created to meet the requirements of Milestone 5:

* **`alx_travel_app/settings.py`**: Configured Celery broker (`redis://`), result backend, and `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`.
* **`alx_travel_app/celery.py`**: Created the Celery application instance (`app`) and configured it using Django settings.
* **`alx_travel_app/__init__.py`**: Imported the Celery app instance to ensure it loads with Django.
* **`listings/tasks.py`**: Created the `@shared_task` function `send_booking_confirmation_email`.
* **`listings/views.py`**: Modified `BookingViewSet.perform_create` to trigger the task using `.delay()`.
* **`manage.py`**: (Implicitly fixed/reverted to standard template to resolve environment issues).

---

## 🚀 Execution & Manual QA Verification Guide

The application requires three separate processes to be running simultaneously to verify the asynchronous workflow.

### 1. Start the Message Broker (Redis)

The Redis server must be running on the default port.

```bash
# Must be executed from your Redis installation directory

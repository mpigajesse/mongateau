"""Regenerate order tickets with updated QR payload."""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongateau.settings')
django.setup()

from orders.models import Order
from orders.ticket_generator import generate_order_ticket


def main():
    orders = Order.objects.filter(is_deleted=False).order_by('created_at')
    total = orders.count()
    regenerated = 0

    for order in orders:
        try:
            ticket_path = generate_order_ticket(order)
            order.ticket_path = ticket_path
            order.save(update_fields=['ticket_path'])
            regenerated += 1
            print(f"OK: {order.order_number} -> {ticket_path}")
        except Exception as exc:
            print(f"ERROR: {order.order_number}: {exc}")

    print(f"Regenerated {regenerated}/{total} tickets")


if __name__ == '__main__':
    main()

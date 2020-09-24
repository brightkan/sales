from salesapp.models import Order


def get_all_orders(limit=None):
    orders = Order.objects.all()
    if orders:
        return orders[:limit]


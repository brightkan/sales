from django.db.models import Sum


def get_total_profit(orders):
    sum = 0
    for order in orders:
        sum = sum + order.total_profit

    return sum
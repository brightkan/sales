import csv
import datetime

from django.db import IntegrityError, transaction

from salesapp.models import Location, Item, Order


def get_or_create_location(country: str, region: str):
    try:
        location = Location.objects.get_or_create(
            country=country,
            region=region
        )
    except IntegrityError:
        location = Location.objects.get(country=country, region=region)

    return location


def get_or_create_item(type: str):
    item, created = Item.objects.get_or_create(
        type=type
    )
    return item


def get_or_create_order(location: Location,
                        item: Item,
                        order_id: int,
                        priority: str,
                        date,
                        ship_date,
                        units_sold: int,
                        unit_cost: float,
                        unit_price: float,
                        sales_channel: float,
                        ):
    order, created = Order.objects.get_or_create(
        location=location,
        item=item,
        sales_channel=sales_channel,
        order_id=order_id,
        priority=priority,
        date=date,
        ship_date=ship_date,
        units_sold=units_sold,
        unit_cost=unit_cost,
        unit_price=unit_price
    )
    return order


def create_item_and_location_objects(csv_obj):
    with open(csv_obj.file_name.path, 'r') as f:
        reader = csv.reader(f)
        locations = []
        items = []
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                region = row[0]
                country = row[1]
                item_type = row[2]
                location = Location(country=country, region=region)
                locations.append(location)
                item = Item(type=item_type)
                items.append(item)

        Location.objects.bulk_create(locations, ignore_conflicts=True)
        Item.objects.bulk_create(items, ignore_conflicts=True)


def create_order_objects(csv_obj):
    with open(csv_obj.file_name.path, 'r') as f:
        reader = csv.reader(f)
        orders = []
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                print("Program reaches here")
                region = row[0]
                country = row[1]
                item_type = row[2]
                sales_channel = row[3]
                order_priority = row[4]
                order_date = row[5]
                order_id = row[6]
                ship_date = row[7]
                units_sold = row[8]
                unit_price = row[9]
                unit_cost = row[10]
                format_str = '%m/%d/%Y'
                order_datetime_obj = datetime.datetime.strptime(order_date, format_str)
                order_date = order_datetime_obj.date()
                ship_datetime_obj = datetime.datetime.strptime(ship_date, format_str)
                ship_date = ship_datetime_obj.date()

                location = Location.objects.get(region=region, country=country)
                item = Item.objects.get(type=item_type)
                order = Order(
                    location=location,
                    item=item,
                    sales_channel=sales_channel,
                    order_id=order_id,
                    priority=order_priority,
                    date=order_date,
                    ship_date=ship_date,
                    units_sold=units_sold,
                    unit_cost=unit_cost,
                    unit_price=unit_price
                )
                orders.append(order)
        Order.objects.bulk_create(orders, ignore_conflicts=True)



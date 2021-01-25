from salesapp.models import Stock


def get_item(id):
    return Stock.objects.get(pk=id)




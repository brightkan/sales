from salesapp.models import Receipt


def get_receipt(id):
    return Receipt.objects.get(pk=id)

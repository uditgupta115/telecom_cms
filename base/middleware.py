from django.middleware.common import CommonMiddleware
from customers.models import Customer


class SetUserMiddleware(CommonMiddleware):
    def process_request(self, request):
        request.customer = Customer.objects.filter(id=1).last()
        return super().process_request(request)

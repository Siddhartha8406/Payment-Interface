from django.http import JsonResponse
from .models import CardDetails

class View:
    def __init__(self) -> None:
        self.card_id = ""

    def set_card_id(self, request, id):
        self.card_id = id
        return JsonResponse({'card_id': self.card_id})
    
    def get_card_id(self, request):
        return JsonResponse({'card_id': self.card_id})

    def index(self, request):
        content = CardDetails.objects.all().values()
        return JsonResponse({'status':'successful', 'content': list(content)})
    
    def pay(self, request, amount):
        if (self.card_id != ""):
            customer = CardDetails.objects.get(card_id=self.card_id)
            if (customer.balance >= amount):
                customer.balance -= amount
                customer.save()
                return JsonResponse({'status': 'successful', 'amount': customer.balance})
            else:
                return JsonResponse({'status': 'unsuccessful', 'amount': customer.balance})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def add_money(self, request, amount):
        if (self.card_id != ""):
            customer = CardDetails.objects.get(card_id=self.card_id)
            customer.balance += amount
            customer.save()
            return JsonResponse({'status':'successful','amount': customer.balance})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def add_card(self, request, name):
        if (self.card_id != ""):
            if not (CardDetails.objects.filter(card_id = self.card_id).exists()):
                customer = CardDetails(card_id=self.card_id, card_holder_name=name)
                customer.save()
                return JsonResponse({'details':list(CardDetails.objects.all().filter(card_id=self.card_id).values())})
            else:
                return JsonResponse({'status': 'unsuccessful', 'content': 'card_id already exists'})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def delete_card(self, request):
        if (self.card_id != ""):
            if (CardDetails.objects.filter(card_id = self.card_id).exists()):
                customer = CardDetails.objects.get(card_id=self.card_id)
                customer.delete()
                return JsonResponse({'status': 'successful'})
            else:
                return JsonResponse({'status': 'exists'})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
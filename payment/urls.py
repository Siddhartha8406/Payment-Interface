from django.urls import path
from . import views

view = views.View()

urlpatterns = [
    path('', view.index, name='index'),
    path('pay/<int:amount>', view.pay, name='pay'),
    path('add_money/<int:amount>', view.add_money, name='add_money'),
    path('send_card_id/<str:id>', view.set_card_id, name='send_card_id'),

    path('add_card/<str:name>', view.add_card, name='add_card'),
    path('delete_card', view.delete_card, name='delete_card'),
    path('get_card_id/', view.get_card_id, name='get_card_id'),
]

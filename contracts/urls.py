from django.urls import path
from . import views
from .views import*

urlpatterns = [
    path('api/upload/', views.upload_contract, name='upload-contract'),
]


from .views import (
    home,
    upload_page,
    contract_list,
    contract_detail
)


urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'upload/',
        upload_page,
        name='upload_page'
    ),

    path(
        'contracts/',
        contract_list,
        name='contract_list'
    ),

    path(
        'contracts/<int:contract_id>/',
        contract_detail,
        name='contract_detail'
    ),

    path(
        'delete/<int:pk>/',
        delete_contract,
        name='delete_contract'
    ),

]



path(
    'delete/<int:pk>/',
    delete_contract,
    name='delete_contract'
)

path(
    'contracts/<int:pk>/',
    views.contract_detail,
    name='contract_detail'
),
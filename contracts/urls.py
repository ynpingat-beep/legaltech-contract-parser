from django.urls import path
from . import views

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

    path('', home),

    path(
        'upload/',
        upload_page
    ),

    path(
        'contracts/',
        contract_list
    ),

    path(
        'contracts/<int:contract_id>/',
        contract_detail
    ),

]
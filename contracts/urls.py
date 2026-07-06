from django.urls import path
from . import views

urlpatterns = [

    # Home Page
    path(
        '',
        views.home,
        name='home'
    ),

    # Upload Contract (HTML)
    path(
        'upload/',
        views.upload_page,
        name='upload_page'
    ),

    # Upload Contract (API)
    path(
        'api/upload/',
        views.upload_contract,
        name='upload_contract'
    ),

    # Contract List
    path(
        'contracts/',
        views.contract_list,
        name='contract_list'
    ),

    # Contract Details
    path(
        'contracts/<int:contract_id>/',
        views.contract_detail,
        name='contract_detail'
    ),

    # Delete Contract
    path(
        'delete/<int:pk>/',
        views.delete_contract,
        name='delete_contract'
    ),

    # -----------------------
    # NEW WEEK 4 API
    # -----------------------

    # List all contracts
    path(
        'api/contracts/',
        views.contract_list_api,
        name='contract_list_api'
    ),

    # Get one analyzed contract
    path(
        'api/contracts/<int:pk>/',
        views.contract_detail_api,
        name='contract_detail_api'
    ),

]
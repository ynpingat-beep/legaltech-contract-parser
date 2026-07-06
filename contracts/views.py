from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Contract, ExtractedClause
from .serializers import ContractSerializer


def home(request):

    total_contracts = Contract.objects.count()

    latest_contract = Contract.objects.order_by(
        '-uploaded_at'
    ).first()

    return render(
        request,
        'contracts/home.html',
        {
            'total_contracts': total_contracts,
            'latest_contract': latest_contract
        }
    )


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_contract(request):

    serializer = ContractSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def upload_page(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        uploaded_file = request.FILES.get(
            'uploaded_file'
        )

        Contract.objects.create(
            title=title,
            uploaded_file=uploaded_file
        )

        return redirect('/contracts/')

    return render(
        request,
        'contracts/upload.html'
    )


def contract_list(request):

    contracts = Contract.objects.all()

    return render(
        request,
        'contracts/contract_list.html',
        {
            'contracts': contracts
        }
    )


def contract_detail(request, contract_id):

    contract = get_object_or_404(
        Contract,
        id=contract_id
    )

    organizations = ExtractedClause.objects.filter(
        contract=contract,
        clause_type="Organization"
    )

    dates = ExtractedClause.objects.filter(
        contract=contract,
        clause_type="Date"
    )

    governing_law = ExtractedClause.objects.filter(
        contract=contract,
        clause_type="Governing Law"
    )

    # Risk Flags
    risks = contract.risks.all()

    # Categorized Clauses
    categorized_clauses = ExtractedClause.objects.exclude(
        clause_type__in=[
            "Organization",
            "Date",
            "Governing Law"
        ]
    ).filter(
        contract=contract
    )

    return render(
        request,
        'contracts/contract_detail.html',
        {
            'contract': contract,
            'organizations': organizations,
            'dates': dates,
            'governing_law': governing_law,
            'risks': risks,
            'categorized_clauses': categorized_clauses,
        }
    )


def delete_contract(request, pk):

    contract = get_object_or_404(
        Contract,
        pk=pk
    )

    contract.delete()

    return redirect('contract_list')


# ===================================================
# WEEK 4 REST API
# ===================================================

@api_view(['GET'])
def contract_list_api(request):

    contracts = Contract.objects.all()

    serializer = ContractSerializer(
        contracts,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def contract_detail_api(request, pk):

    contract = get_object_or_404(
        Contract,
        pk=pk
    )

    serializer = ContractSerializer(contract)

    return Response(serializer.data)
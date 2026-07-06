from rest_framework import serializers
from .models import (
    Contract,
    ExtractedClause,
    RiskFlag
)


class ExtractedClauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtractedClause
        fields = [
            "clause_type",
            "clause_text"
        ]


class RiskFlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskFlag
        fields = [
            "risk_level",
            "description"
        ]


class ContractSerializer(serializers.ModelSerializer):

    clauses = ExtractedClauseSerializer(
        many=True,
        read_only=True
    )

    risks = RiskFlagSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Contract
        fields = [
            "id",
            "title",
            "uploaded_file",
            "uploaded_at",
            "extracted_text",
            "clauses",
            "risks"
        ]
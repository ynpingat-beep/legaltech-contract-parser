from django.db import models
from .utils import (
    extract_text_from_pdf,
    extract_entities,
    extract_governing_law,
    detect_risks
)


class Contract(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='contracts/')
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # Save contract first
        super().save(*args, **kwargs)

        # Process only once
        if self.uploaded_file and not self.extracted_text:

            try:

                # --------------------------------
                # Extract Text
                # --------------------------------
                self.extracted_text = extract_text_from_pdf(
                    self.uploaded_file.path
                )

                super().save(update_fields=["extracted_text"])

                # --------------------------------
                # Remove old extracted data
                # --------------------------------
                self.clauses.all().delete()
                self.risks.all().delete()

                # --------------------------------
                # Extract Organizations & Dates
                # --------------------------------
                entities = extract_entities(self.extracted_text)

                # Save Organizations
                for organization in entities["organizations"]:

                    ExtractedClause.objects.create(
                        contract=self,
                        clause_type="Organization",
                        clause_text=organization
                    )

                # Save Dates
                for date in entities["dates"]:

                    ExtractedClause.objects.create(
                        contract=self,
                        clause_type="Date",
                        clause_text=date
                    )

                # --------------------------------
                # Extract Governing Law
                # --------------------------------
                governing_law = extract_governing_law(
                    self.extracted_text
                )

                if governing_law:

                    ExtractedClause.objects.create(
                        contract=self,
                        clause_type="Governing Law",
                        clause_text=governing_law
                    )

                # --------------------------------
                # Detect High Risk Keywords
                # --------------------------------
                risks = detect_risks(self.extracted_text)

                for risk in risks:

                    RiskFlag.objects.create(
                        contract=self,
                        risk_level="High",
                        description=risk
                    )

            except Exception as e:
                print("Extraction Error:", e)

    def __str__(self):
        return self.title


class ExtractedClause(models.Model):

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="clauses"
    )

    clause_type = models.CharField(max_length=100)

    clause_text = models.TextField()

    def __str__(self):
        return f"{self.clause_type} - {self.contract.title}"


class RiskFlag(models.Model):

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="risks"
    )

    risk_level = models.CharField(max_length=20)

    description = models.TextField()

    def __str__(self):
        return f"{self.risk_level} - {self.contract.title}"
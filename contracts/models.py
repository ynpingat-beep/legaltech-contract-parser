from django.db import models
from .utils import extract_text_from_pdf, extract_entities


class Contract(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='contracts/')
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # Save contract first to generate file path
        super().save(*args, **kwargs)

        # Process only if text hasn't been extracted yet
        if self.uploaded_file and not self.extracted_text:

            try:
                # -----------------------------
                # Extract text from PDF
                # -----------------------------
                self.extracted_text = extract_text_from_pdf(
                    self.uploaded_file.path
                )

                super().save(update_fields=["extracted_text"])

                # -----------------------------
                # Extract Organizations & Dates
                # -----------------------------
                entities = extract_entities(self.extracted_text)
                print("=" * 50)
                print("Extracted Entities:", entities)
                print("=" * 50)

                # Remove previous extracted clauses (safety)
                self.clauses.all().delete()

                # Save Organizations
                for organization in entities["organizations"]:
                    print("Saving Organization:", organization)

                    ExtractedClause.objects.create(
                        contract=self,
                        clause_type="Organization",
                        clause_text=organization
                    )

                # Save Dates
                for date in entities["dates"]:
                    print("Saving Date:", date)

                    ExtractedClause.objects.create(
                        contract=self,
                        clause_type="Date",
                        clause_text=date
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
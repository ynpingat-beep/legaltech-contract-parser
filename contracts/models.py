from django.db import models
from .utils import extract_text_from_pdf

class Contract(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='contracts/')
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.uploaded_file and not self.extracted_text:
            try:
                self.extracted_text = extract_text_from_pdf(
                    self.uploaded_file.path
                )
                super().save(update_fields=['extracted_text'])
            except Exception as e:
                print("Extraction Error:", e)
    
    
    def __str__(self):
        return self.title


class ExtractedClause(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='clauses'
    )

    clause_type = models.CharField(max_length=100)
    clause_text = models.TextField()

    def __str__(self):
        return self.clause_type


class RiskFlag(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='risks'
    )

    risk_level = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.risk_level
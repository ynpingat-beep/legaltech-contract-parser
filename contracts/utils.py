import fitz
import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    text = ""

    pdf_document = fitz.open(pdf_path)

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    # Text Cleaning
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text


def extract_entities(text):
    """
    Extract organizations and dates using spaCy NER.
    Filters common false positives.
    """

    doc = nlp(text)

    organizations = set()
    dates = set()

    ignored_organizations = {
        "NDA",
        "Agreement",
        "Contract",
        "The Effective Date",
        "Effective Date",
        "Party",
        "Receiving Party",
        "Disclosing Party"
    }

    for ent in doc.ents:

        value = ent.text.strip()

        if ent.label_ == "ORG":

            if value in ignored_organizations:
                continue

            # Ignore very short names
            if len(value) < 4:
                continue

            organizations.add(value)

        elif ent.label_ == "DATE":

            # Ignore relative durations
            if "days" in value.lower():
                continue

            dates.add(value)

    return {
        "organizations": sorted(organizations),
        "dates": sorted(dates)
    }


def extract_governing_law(text):
    """
    Extract the governing law from contract text.
    """

    pattern = r"governed by the laws of ([A-Za-z ]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None


def detect_risks(text):
    """
    Detect risky clauses and return the full sentence
    containing the risky keyword.
    """

    risk_keywords = [
        "indemnify",
        "unlimited liability",
        "exclusive",
        "confidential",
        "terminate",
        "breach"
    ]

    risk_sentences = []

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:

        lower_sentence = sentence.lower()

        for keyword in risk_keywords:

            if keyword in lower_sentence:

                risk_sentences.append({
                    "level": "High",
                    "description": sentence.strip()
                })

                break

    return risk_sentences


# --------------------------------
# Clause Categorization
# --------------------------------

def categorize_clauses(text):

    clause_keywords = {
        "Confidentiality": ["confidential", "non-disclosure"],
        "Termination": ["terminate", "termination"],
        "Liability": ["liability", "liable"],
        "Payment": ["payment", "invoice", "fee"],
        "Governing Law": ["governing law", "jurisdiction"]
    }

    clauses = []

    sentences = text.split(".")

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        lower_sentence = sentence.lower()

        for clause_type, keywords in clause_keywords.items():

            if any(keyword in lower_sentence for keyword in keywords):

                clauses.append({
                    "type": clause_type,
                    "text": sentence
                })

                break

    return clauses
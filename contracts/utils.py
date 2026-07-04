import fitz, spacy, re 


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
    """

    doc = nlp(text)

    organizations = set()
    dates = set()

    for ent in doc.ents:

        if ent.label_ == "ORG":
            organizations.add(ent.text.strip())

        elif ent.label_ == "DATE":
            dates.add(ent.text.strip())

    return {
        "organizations": sorted(list(organizations)),
        "dates": sorted(list(dates))
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

    risk_keywords = [
        "indemnify",
        "unlimited liability",
        "exclusive",
        "confidential",
        "terminate",
        "breach"
    ]

    found_risks = []

    lower_text = text.lower()

    for keyword in risk_keywords:

        if keyword in lower_text:

            found_risks.append(keyword)

    return found_risks


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

    # Split text into sentences
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
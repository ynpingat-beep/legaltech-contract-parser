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
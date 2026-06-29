import fitz, spacy


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
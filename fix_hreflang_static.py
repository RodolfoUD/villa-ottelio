from bs4 import BeautifulSoup
import os

BASE_URL = "https://www.villaottelio.it"

PAGES = [
    {"it": "it/index.html",        "en": "index.html",                    "fr": "fr/index.html",             "de": "de/index.html",       "nl": "nl/index.html",         "zh": "zh/index.html"},
    {"it": "it/dimora.html",        "en": "the-manor.html",                "fr": "fr/le-manoir.html",         "de": "de/anwesen.html",     "nl": "nl/landhuis.html",      "zh": "zh/the-estate.html"},
    {"it": "it/parco.html",         "en": "the-park.html",                 "fr": "fr/le-parc.html",           "de": "de/park.html",        "nl": "nl/park.html",          "zh": "zh/the-garden.html"},
    {"it": "it/vegetazione.html",   "en": "nature.html",                   "fr": "fr/nature.html",            "de": "de/botanik.html",     "nl": "nl/botanica.html",      "zh": "zh/nature.html"},
    {"it": "it/investimento.html",  "en": "investment.html",               "fr": "fr/investissement.html",    "de": "de/investition.html", "nl": "nl/investering.html",   "zh": "zh/investment.html"},
    {"it": "it/contatti.html",      "en": "contact.html",                  "fr": "fr/contact.html",           "de": "de/kontakt.html",     "nl": "nl/contact.html",       "zh": "zh/contact.html"},
    {"it": "it/privacy.html",       "en": "privacy-policy.html",           "fr": "fr/politique-confidentialite.html", "de": "de/datenschutz.html", "nl": "nl/privacybeleid.html", "zh": "zh/privacy-policy.html"},
    {"it": "it/blog.html",          "en": "blog.html",                     "fr": "fr/blog.html",              "de": "de/blog.html",        "nl": "nl/blog.html",          "zh": "zh/blog.html"},
]

ROOT = r"C:\Users\rdeca\villa-ottelio"

def build_hreflang_tags(soup, page_map):
    tags = []
    for lang, path in page_map.items():
        tag = soup.new_tag("link", rel="alternate")
        tag["hreflang"] = lang
        tag["href"] = f"{BASE_URL}/{path}"
        tags.append(tag)
    # x-default punta a EN
    xd = soup.new_tag("link", rel="alternate")
    xd["hreflang"] = "x-default"
    xd["href"] = f"{BASE_URL}/{page_map['en']}"
    tags.append(xd)
    return tags

def fix_file(filepath, page_map):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    head = soup.find("head")
    if not head:
        print(f"  SKIP (no <head>): {filepath}")
        return

    # Rimuovi tutti gli hreflang esistenti
    for tag in head.find_all("link", rel="alternate"):
        tag.decompose()

    # Inserisci i nuovi
    new_tags = build_hreflang_tags(soup, page_map)
    for tag in new_tags:
        head.append(tag)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"  OK: {filepath}")

print("=== FIX HREFLANG PAGINE STATICHE ===\n")
for page_map in PAGES:
    for lang, path in page_map.items():
        filepath = os.path.join(ROOT, path.replace("/", os.sep))
        if os.path.exists(filepath):
            fix_file(filepath, page_map)
        else:
            print(f"  FILE NON TROVATO: {filepath}")

print("\nDone.")

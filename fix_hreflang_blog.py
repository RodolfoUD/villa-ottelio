from bs4 import BeautifulSoup
import os

BASE_URL = "https://www.villaottelio.it"
ROOT = r"C:\Users\rdeca\villa-ottelio"

# Mappa slug blog: chiave = slug IT, valori = slug per lingua
# None = articolo non esistente in quella lingua
BLOG_MAP = [
    {"it": "affreschi-travi-storia-soffitti", "en": "frescoes-beams-reading-history", "fr": "fresques-poutres-histoire", "de": "fresken-balken-geschichte", "nl": "fresco-balken-geschiedenis", "zh": "bihua-liang-lishi"},
    {"it": "analisi-mercato-immobiliare", "en": "real-estate-analysis", "fr": "analyse-marche-immobilier", "de": "immobilienmarkt-analyse", "nl": "vastgoedmarkt-analyse", "zh": "fangdichan-shichang-fenxi"},
    {"it": "architettura-ibrida-veneto-friulana", "en": "hybrid-architecture-venetian-friulian", "fr": "architecture-hybride-venitienne-frioulane", "de": "hybride-architektur-veneto-friaul", "nl": "hybride-architectuur-venetiaans-friuliaans", "zh": "hunhe-jianzhu-fenni-weini"},
    {"it": "artisti-scrittori-dimore-storiche", "en": "artists-writers-historic-villas", "fr": "artistes-ecrivains-demeures-historiques", "de": "kunstler-schriftsteller-historische-anwesen", "nl": "kunstenaars-schrijvers-historische-landgoederen", "zh": "yishujia-zuojia-lishi-zhuangyuan"},
    {"it": "asset-anti-inflazione-beni-culturali", "en": "anti-inflation-asset-cultural-heritage", "fr": "actif-anti-inflation-patrimoine-culturel", "de": "inflationsschutz-kulturgueter", "nl": "anti-inflatie-asset-cultureel-erfgoed", "zh": "fangtonghuo-zichan-wenhua-yichan"},
    {"it": "atelier-artista-luce-ispirazione", "en": None, "fr": "atelier-artiste-lumiere-inspiration", "de": "kuenstleratelier-licht-inspiration", "nl": "atelier-kunstenaar-licht-inspiratie", "zh": "yishujia-gongzuoshi-guangxian"},
    {"it": "autunno-primavera-colori-giardino", "en": "autumn-spring-colour-garden", "fr": "automne-printemps-couleurs-jardin", "de": "herbst-fruehling-farben-garten", "nl": "herfst-lente-kleuren-tuin", "zh": "qiuji-chunjie-huayuan-secai"},
    {"it": "bene-vincolato-vantaggi-fiscali", "en": "listed-property-tax-advantages", "fr": "bien-classe-avantages-fiscaux", "de": "denkmalimmobilie-steuervorteile", "nl": "beschermd-monument-belastingvoordelen", "zh": "baohu-jianzhu-shuishou-youhui"},
    {"it": "bonus-restauro-ville-storiche", "en": "restoration-bonus-historic-villas", "fr": "prime-restauration-villas-historiques", "de": "restaurierungsbonus-historische-villen", "nl": "restauratiebonus-historische-villa", "zh": "xiufu-jiangjin-lishi-bieshu"},
    {"it": "botole-pietra-vino-salone", "en": "stone-trapdoors-wine-salon", "fr": "trappes-pierre-vin-salon", "de": "steinlueken-wein-salon", "nl": "stenen-luiken-wijn-salon", "zh": "shitou-dicang-putao-jiu"},
    {"it": "cantinone-monumentale-quattro-metri", "en": "monumental-wine-cellar", "fr": "cave-monumentale", "de": "monumentaler-weinkeller", "nl": "monumentale-wijnkelder", "zh": "juda-jiu-jiao"},
    {"it": "cappella-san-gaetano-storia", "en": "chapel-san-gaetano-history", "fr": "chapelle-san-gaetano-histoire", "de": "kapelle-san-gaetano-geschichte", "nl": "kapel-san-gaetano-geschiedenis", "zh": "sheng-gaetano-jiaotang-lishi"},
    {"it": "cappelle-private-spazio-sacro", "en": "private-chapels-sacred-space", "fr": "chapelles-privees-espace-sacre", "de": "private-kapellen-sakraler-raum", "nl": "prive-kapellen-heilige-ruimte", "zh": "siren-jiaotang-shensheng"},
    {"it": "colli-orientali-friuli-terroir", "en": "colli-orientali-friuli-terroir", "fr": "colli-orientali-frioul-terroir", "de": "colli-orientali-friaul-terroir", "nl": "colli-orientali-friuli-terroir", "zh": "colli-orientali-terroir"},
    {"it": "corporate-hq-sedi-aziendali", "en": "corporate-hq-business-headquarters", "fr": "siege-social-entreprise-prestige", "de": "corporate-hq-firmensitz", "nl": "hoofdkantoor-prestigieuze-locatie", "zh": "qiye-zongbu-mingwang-dizhi"},
    {"it": "deducibilita-manutenzione-beni-vincolati", "en": "maintenance-deductibility-listed-properties", "fr": "deductibilite-maintenance-biens-classes", "de": "steuerabzug-instandhaltung", "nl": "aftrekbaarheid-onderhoud-monumenten", "zh": "baohu-jianzhu-weihu-koushui"},
    {"it": "dieci-ville-storiche-opere-arte", "en": "ten-historic-villas-art-inspiration", "fr": "dix-villas-historiques-oeuvres-art", "de": "zehn-historische-villen-kunstwerke", "nl": "tien-historische-villa-kunstwerken", "zh": "shi-ge-lishi-bieshu-yishu"},
    {"it": "ecobonus-dimore-storiche", "en": "ecobonus-historic-homes", "fr": "ecobonus-demeures-historiques", "de": "ecobonus-historische-anwesen", "nl": "ecobonus-historische-landgoederen", "zh": "lüse-jiangjin-lishi-zhuangyuan"},
    {"it": "facciata-principale-villa", "en": "main-facade-villa", "fr": "facade-principale-villa", "de": "hauptfassade-villa", "nl": "hoofdgevel-villa", "zh": "zhuyao-liguan-bieshu"},
    {"it": "famiglia-ottelio-notai-conti-friulani", "en": "ottelio-family-notaries-counts", "fr": "famille-ottelio-notaires-comtes", "de": "familie-ottelio-notare-grafen", "nl": "familie-ottelio-notarissen-graven", "zh": "ottelio-jiazu-gongjue"},
    {"it": "mare-montagna-posizione-centrale", "en": "sea-mountains-central-location", "fr": "mer-montagne-position-centrale", "de": "meer-berge-zentrale-lage", "nl": "zee-bergen-centrale-ligging", "zh": "hai-shan-zhongxin-weizhi"},
    {"it": "olio-extravergine-single-estate", "en": "extra-virgin-olive-oil-single-estate", "fr": "huile-olive-single-estate", "de": "natives-olivenoel-single-estate", "nl": "extra-vergine-olijfolie-single-estate", "zh": "teji-chuzhen-olive-you"},
    {"it": "possedere-pezzo-di-storia", "en": "owning-piece-of-history", "fr": "posseder-morceau-histoire", "de": "stuck-geschichte-besitzen", "nl": "bezitten-stuk-geschiedenis", "zh": "yongyou-lishi-pian"},
    {"it": "restauro-conservativo-cosa-mantenuto", "en": "conservative-restoration-preserved", "fr": "restauration-conservative", "de": "konservative-restaurierung", "nl": "conservatieve-restauratie", "zh": "baohu-xiu-fu"},
    {"it": "roi-villa-storica-relais", "en": "roi-historic-villa-relais", "fr": "roi-villa-historique-relais", "de": "roi-historische-villa-relais", "nl": "roi-historische-villa-relais", "zh": "lishi-bieshu-touzi-huibao"},
    {"it": "sicurezza-qualita-vita-friuli", "en": "safety-quality-life-friuli", "fr": "securite-qualite-vie-frioul", "de": "sicherheit-lebensqualitat-friaul", "nl": "veiligheid-levenskwaliteit-friuli", "zh": "anquan-shenghuo-zhiliang-friuli"},
    {"it": "silenzio-giardino-murato-lusso", "en": "silence-walled-garden-luxury", "fr": "silence-jardin-clos-luxe", "de": "stille-ummauterter-garten-luxus", "nl": "stilte-ommuurde-tuin-luxe", "zh": "jinbi-huayuan-luxe"},
    {"it": "silenzio-nuovo-lusso-vita-lenta", "en": "silence-new-luxury-slow-living", "fr": "silence-nouveau-luxe-vie-lente", "de": "stille-neuer-luxus-langsames-leben", "nl": "stilte-nieuwe-luxe-langzaam-leven", "zh": "jijing-xin-shehuo-man-shenghuo"},
    {"it": "soffitta-travi-vista-volumi-nascosti", "en": None, "fr": "grenier-poutres-apparentes", "de": "dachboden-sichtbalken", "nl": "zolder-zichtbare-balken", "zh": "gefei-louge-cang-kongjian"},
    {"it": "spazi-rappresentanza-privati-villa", "en": "reception-private-spaces-villa", "fr": "espaces-representation-prives-villa", "de": "repraesentations-private-raeume-villa", "nl": "representatieve-prive-ruimtes-villa", "zh": "daibiao-siren-kongjian-bieshu"},
    {"it": "vicini-famosi-collio-vini", "en": "famous-neighbours-collio-wines", "fr": "voisins-celebres-collio-vins", "de": "beruhmte-nachbarn-collio-weine", "nl": "beroemde-buren-collio-wijnen", "zh": "zhuming-linju-collio-putaojiu"},
    {"it": "villa-privata-residenza-artistica", "en": "private-villa-artist-residence", "fr": "villa-privee-residence-artistique", "de": "private-villa-kunstlerresidenz", "nl": "prive-villa-artistieke-residentie", "zh": "siren-bieshu-yishu-juzhu"},
    {"it": "wedding-venue-location-prestigio", "en": "wedding-venue-prestigious-location", "fr": "lieu-mariage-prestige", "de": "hochzeitslocation-prestige", "nl": "hunli-changsuo-mingwang", "zh": "hunli-changsuo-mingwang"},
]

LANG_PATHS = {
    "it": "it/blog",
    "en": "blog",
    "fr": "fr/blog",
    "de": "de/blog",
    "nl": "nl/blog",
    "zh": "zh/blog",
}

def get_url(lang, slug):
    if lang == "en":
        return f"{BASE_URL}/blog/{slug}.html"
    return f"{BASE_URL}/{lang}/blog/{slug}.html"

def fix_file(filepath, slugs):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    head = soup.find("head")
    if not head:
        print(f"  SKIP (no <head>): {filepath}")
        return

    # Rimuovi hreflang esistenti
    for tag in head.find_all("link", rel="alternate"):
        tag.decompose()

    # Inserisci solo le lingue con slug esistente
    en_slug = slugs.get("en")
    for lang, slug in slugs.items():
        if slug is None:
            continue
        tag = soup.new_tag("link", rel="alternate")
        tag["hreflang"] = lang
        tag["href"] = get_url(lang, slug)
        head.append(tag)

    # x-default: EN se esiste, altrimenti IT
    xd_slug = en_slug if en_slug else slugs.get("it")
    xd_lang = "en" if en_slug else "it"
    xd = soup.new_tag("link", rel="alternate")
    xd["hreflang"] = "x-default"
    xd["href"] = get_url(xd_lang, xd_slug)
    head.append(xd)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"  OK: {filepath}")

print("=== FIX HREFLANG BLOG ===\n")
skipped = []
for slugs in BLOG_MAP:
    for lang, slug in slugs.items():
        if slug is None:
            continue
        folder = LANG_PATHS[lang]
        filepath = os.path.join(ROOT, folder.replace("/", os.sep), f"{slug}.html")
        if os.path.exists(filepath):
            fix_file(filepath, slugs)
        else:
            msg = f"  FILE NON TROVATO: {filepath}"
            print(msg)
            skipped.append(msg)

print(f"\nDone. File saltati: {len(skipped)}")

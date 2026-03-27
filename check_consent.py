import os
from bs4 import BeautifulSoup

def check_consent():
    file_path = "index.html"
    if not os.path.exists(file_path):
        print(f"File {file_path} non trovato.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    
    if soup.head:
        first_script = soup.head.find("script")
        if first_script:
            content = first_script.string or first_script.text or ""
            print(content.strip()[:200])
        else:
            print("Nessun tag <script> trovato nel <head>.")
    else:
        print("Tag <head> non trovato.")

if __name__ == "__main__":
    check_consent()

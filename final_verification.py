
import os
from bs4 import BeautifulSoup

def count_noindex_tags(root_dir):
    count = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                soup = BeautifulSoup(content, "html.parser")
                if soup.find("meta", attrs={"name": "robots", "content": "noindex"}):
                    count += 1
    return count

def count_fi_es_text(root_dir):
    count = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "fi-es" in content:
                    count += 1
    return count

def count_relative_hrefs(root_dir):
    count = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                soup = BeautifulSoup(content, "html.parser")
                for a_tag in soup.find_all("a", href=True):
                    if "../" in a_tag["href"]:
                        count += 1
    return count

def check_robots_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return "Allow: /" in content

def count_html_files_in_dir(directory):
    count = 0
    if os.path.exists(directory) and os.path.isdir(directory):
        for _, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".html"):
                    count += 1
    return count


# Esegui i controlli

# 1. File HTML con "noindex"
noindex_count = count_noindex_tags(".")

# 2. File HTML con "fi-es"
fi_es_count = count_fi_es_text(".")

# 3. File HTML con href="../"
relative_href_count = count_relative_hrefs(".")

# 4. robots.txt contiene "Allow: /"
robots_txt_ok = check_robots_txt("public/robots.txt")

# 5. nl/blog/ contiene file HTML
nl_blog_html_count = count_html_files_in_dir("nl/blog")

# 6. zh/blog/ contiene file HTML
zh_blog_html_count = count_html_files_in_dir("zh/blog")

print(f"1. File HTML con \"noindex\": {noindex_count}")
print(f"2. File HTML con \"fi-es\": {fi_es_count}")
print(f"3. File HTML con href=\"../\": {relative_href_count}")
print(f"4. robots.txt contiene \"Allow: /\": {robots_txt_ok}")
print(f"5. nl/blog/ contiene file HTML: {nl_blog_html_count}")
print(f"6. zh/blog/ contiene file HTML: {zh_blog_html_count}")

import csv
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"
GIRL_GROUPS_CATEGORY_URL = f"{BASE_URL}/wiki/Category:South_Korean_girl_groups"
BOY_BANDS_CATEGORY_URL = f"{BASE_URL}/wiki/Category:South_Korean_boy_bands"
HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; cicizhu2@illinois.edu)"
}
REQUEST_DELAY = 1.0
PAGES_PER_CATEGORY = 40
RESULTS_OUTPUT = "wikipedia_kpop_groups.csv"


def fetch_soup(url):
    if not url:
        print("No URL was found for this page.")
        return None

    response = requests.get(url, headers=HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)

    if response.status_code != 200:
        print(f"Could not download {url}: HTTP {response.status_code}")
        return None

    return BeautifulSoup(response.text, "html.parser")


def scrape_groups(category_page, source_url):
    groups = []
    if category_page is None:
        return groups

    groups_section = category_page.find(id="mw-pages")
    if groups_section is None:
        return groups

    if source_url == GIRL_GROUPS_CATEGORY_URL:
        group_type = "girl group"
    else:
        group_type = "boy band"

    group_items = groups_section.find_all("li")
    for item in group_items:
        link = item.find("a", href=True)
        if link is None:
            continue

        group_name = link.get_text(" ", strip=True)
        if group_name.startswith("List of"):
            continue

        groups.append({
            "group": group_name,
            "group_type": group_type,
            "source_url": source_url,
            "group_url": f"{BASE_URL}{link['href']}",
        })

    return groups[:PAGES_PER_CATEGORY]


def get_internal_links(content):
    if content is None:
        return []

    links = []
    for link in content.find_all("a", href=True):
        href = link["href"]
        is_wiki_link = (
            href.startswith("/wiki/")
            or href.startswith("./")
            or href.startswith(f"{BASE_URL}/wiki/")
        )
        if is_wiki_link and "#" not in href:
            links.append(href)

    return links


def analyze_group(group):
    soup = fetch_soup(group["group_url"])
    record = group.copy()
    record["word_count"] = 0
    record["character_count"] = 0
    record["internal_link_count"] = 0
    record["unique_internal_link_count"] = 0

    if soup is None:
        return record

    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        return record

    article_text = content.get_text(" ", strip=True)
    word_count = len(article_text.split())
    character_count = len(article_text)
    internal_links = get_internal_links(content)
    unique_internal_links = []
    for href in internal_links:
        if href not in unique_internal_links:
            unique_internal_links.append(href)

    record["word_count"] = word_count
    record["character_count"] = character_count
    record["internal_link_count"] = len(internal_links)
    record["unique_internal_link_count"] = len(unique_internal_links)
    return record


def save_csv(records, output_path):
    if not records:
        print(f"No records to save to {output_path}")
        return

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def main():
    print("Finding South Korean girl groups...")
    girl_groups_page = fetch_soup(GIRL_GROUPS_CATEGORY_URL)
    girl_groups = scrape_groups(girl_groups_page, GIRL_GROUPS_CATEGORY_URL)

    print("Finding South Korean boy bands...")
    boy_bands_page = fetch_soup(BOY_BANDS_CATEGORY_URL)
    boy_bands = scrape_groups(boy_bands_page, BOY_BANDS_CATEGORY_URL)

    all_groups = girl_groups + boy_bands
    print(f"Found {len(all_groups)} group pages.")

    results = []
    for number, group in enumerate(all_groups, start=1):
        print(f"Processing {number}/{len(all_groups)}: {group['group']}")
        results.append(analyze_group(group))

    save_csv(results, RESULTS_OUTPUT)
    print(f"Saved {len(results)} group pages to {RESULTS_OUTPUT}")


if __name__ == "__main__":
    main()
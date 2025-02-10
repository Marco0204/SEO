import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Shared Utility Functions
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower().strip())

def get_phrases(text, n):
    words = re.findall(r'\b\w+\b', text)
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)] if words else []

def calculate_density(counter, total):
    return [(phrase, count, (count/total)*100 if total > 0 else 0) 
            for phrase, count in counter.most_common(5)]

# Analysis Modules
def analyze_headings(soup):
    headings = [h.get_text() for h in soup.find_all(re.compile('^h[1-6]$'))]
    results = {'1-word': [], '2-word': [], '3-word': []}
    
    for h_text in headings:
        cleaned = clean_text(h_text)
        for n in [1, 2, 3]:
            results[f'{n}-word'].extend(get_phrases(cleaned, n))
    
    total = len(headings)
    return {k: calculate_density(Counter(v), total) for k, v in results.items()}

def analyze_links(soup):
    links = [a.get_text(strip=True) for a in soup.find_all('a', href=True)]
    results = {'1-word': [], '2-word': [], '3-word': []}
    
    for l_text in links:
        cleaned = clean_text(l_text)
        for n in [1, 2, 3]:
            results[f'{n}-word'].extend(get_phrases(cleaned, n))
    
    total = len(links)
    return {k: calculate_density(Counter(v), total) for k, v in results.items()}

def analyze_images(soup):
    images = [img.get('alt', '') for img in soup.find_all('img')]
    images = [alt.strip() for alt in images if alt.strip()]
    results = {'1-word': [], '2-word': [], '3-word': []}
    
    for i_text in images:
        cleaned = clean_text(i_text)
        for n in [1, 2, 3]:
            results[f'{n}-word'].extend(get_phrases(cleaned, n))
    
    total = len(images)
    return {k: calculate_density(Counter(v), total) for k, v in results.items()}

def analyze_body(soup):
    body = soup.find('body')
    if not body: return {}
    
    text = clean_text(body.get_text())
    words = re.findall(r'\b\w+\b', text)
    results = {
        '1-word': words,
        '2-word': get_phrases(text, 2),
        '3-word': get_phrases(text, 3)
    }
    
    totals = {
        '1-word': len(words),
        '2-word': len(results['2-word']),
        '3-word': len(results['3-word'])
    }
    
    return {k: calculate_density(Counter(results[k]), totals[k]) for k in results}

# Main Analysis Function
def full_seo_analysis(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return {
            'headings': analyze_headings(soup),
            'links': analyze_links(soup),
            'images': analyze_images(soup),
            'body': analyze_body(soup)
        }
    except Exception as e:
        return f"Error: {str(e)}"

# Reporting Functions
def print_section(name, data):
    print(f"\n{'='*40}")
    print(f" {name.upper()} DENSITY ANALYSIS")
    print(f"{'='*40}")
    
    for n in ['1-word', '2-word', '3-word']:
        print(f"\n** {n.replace('-', ' ').title()} **")
        print(f"{'Phrase':<25} | {'Count':<6} | {'Density (%)':<10}")
        print("-" * 45)
        for phrase, count, density in data.get(n, []):
            print(f"{phrase[:25]:<25} | {count:<6} | {round(density, 2):<10}")

def print_full_report(results):
    for section in ['headings', 'links', 'images', 'body']:
        print_section(section, results.get(section, {}))

# Execution
if __name__ == "__main__":
    url = input("Enter URL to analyze: ")
    analysis = full_seo_analysis(url)
    
    if isinstance(analysis, dict):
        print(f"\nSEO DENSITY REPORT FOR: {url}")
        print_full_report(analysis)
    else:
        print(analysis)
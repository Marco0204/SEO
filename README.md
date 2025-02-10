# SEO Keyword Density Analyzer

## Overview
This is a Python-based SEO Keyword Density Analyzer that extracts and analyzes keyword frequency from different sections of a webpage. It calculates keyword density for headings, links, images (alt text), and body content, providing insights into the most commonly used terms on a webpage.

## Features
- Extracts and analyzes text from:
  - Headings (H1-H6)
  - Links (Anchor text)
  - Image Alt attributes
  - Body content
- Calculates keyword density for:
  - Single-word phrases
  - Two-word phrases
  - Three-word phrases
- Outputs a structured keyword density report

## Requirements
Ensure you have Python installed along with the required libraries:
```sh
pip install requests beautifulsoup4
```

## Usage
Run the script and enter the URL to analyze:
```sh
python seo_analyzer.py
```
Follow the on-screen instructions and receive a full keyword density report.

## Code Structure
- **Utility Functions**: Text cleaning, phrase extraction, and density calculation
- **Analysis Modules**: Separate functions for headings, links, images, and body content
- **Main Function**: `full_seo_analysis(url)` performs the full analysis
- **Report Functions**: Print detailed reports with density calculations

## Example Output
```
========================================
 HEADINGS DENSITY ANALYSIS
========================================

** 1 Word **
Phrase                    | Count  | Density (%)
---------------------------------------------
seo                       | 5      | 10.0      
keyword                   | 3      | 6.0       
...
```

## Future Improvements
- Support for more languages
- Stop-word filtering
- Graphical visualization of keyword density
- Export results to CSV or JSON

## License
This project is open-source 


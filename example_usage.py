"""
example_usage.py -- Demonstrates WebsiteStyleAnalyzerClient
"""
from client import WebsiteStyleAnalyzerClient

def main():
    client = WebsiteStyleAnalyzerClient()
    result = client.analyze_palette(["#FF0000", "#00FF00"])
    print("[Website Design Palette Result]")
    print(f"Branding Theme: {result['branding_theme'].upper()}")
    print(f"HSL Mapped: {result['hsl_tokens']}")

if __name__ == "__main__":
    main()

"""
website-style-analyzer-skill: Client SDK
Transforms hex colors into theme styles and HSL declarations.
"""
from __future__ import annotations
from typing import Optional


class WebsiteStyleAnalyzerClient:
    """
    SDK for design token compiling.
    """

    def analyze_palette(self, hex_colors: list[str]) -> dict:
        hsl_list = []
        for hc in hex_colors:
            clean = hc.replace("#", "")
            if len(clean) == 6:
                r = int(clean[0:2], 16) / 255.0
                g = int(clean[2:4], 16) / 255.0
                b = int(clean[4:6], 16) / 255.0
                
                mx = max(r, g, b)
                mn = min(r, g, b)
                df = mx - mn
                
                # Hue calculation
                if df == 0:
                    h = 0
                elif mx == r:
                    h = (60 * ((g - b) / df) + 360) % 360
                elif mx == g:
                    h = (60 * ((b - r) / df) + 120) % 360
                else:
                    h = (60 * ((r - g) / df) + 240) % 360
                    
                # Lightness
                l = (mx + mn) / 2.0
                
                # Saturation
                if df == 0:
                    s = 0
                else:
                    s = df / (1 - abs(2 * l - 1))
                    
                hsl_list.append(f"hsl({int(h)}, {int(s*100)}%, {int(l*100)}%)")

        # Basic theme categorization logic
        theme = "vibrant" if len(hsl_list) > 2 else "minimalistic"

        return {
            "branding_theme": theme,
            "hsl_tokens": hsl_list
        }

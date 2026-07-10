# website-style-analyzer-skill

> **GenPark AI Agent Skill** -- HEX color-to-HSL design token compiler.

## Quick Start

```python
from client import WebsiteStyleAnalyzerClient
client = WebsiteStyleAnalyzerClient()
res = client.analyze_palette(["#000000"])
print(res["hsl_tokens"])
```

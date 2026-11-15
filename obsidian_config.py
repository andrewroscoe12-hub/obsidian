import requests
import os
import json
from pathlib import Path

def main():

    filepath = r""          # Insert where you want vault creating

    ksbs = json.loads(Path("data/ksbs.json").read_text(encoding="utf-8"))
    topics = json.loads(Path("data/topics.json").read_text(encoding="utf-8"))
    themes = json.loads(Path("data/themes.json").read_text(encoding="utf-8"))

    for category in ksbs:
        for code, description in ksbs.get(category).items():
            ksbs_folder = os.path.join(filepath, category)
            os.makedirs(ksbs_folder, exist_ok=True)

            ksbs_path = os.path.join(ksbs_folder, f"{code}.md")
            with open(ksbs_path, "w", encoding="utf-8") as f:
                f.write(f"{code}\n{description}")
                
    for year in topics:
        for module in topics.get(year):
            topics_folder = os.path.join(filepath, year)
            os.makedirs(topics_folder, exist_ok=True)

            topics_path = os.path.join(topics_folder, f"{module}.md")    
            with open(topics_path, "w", encoding="utf-8") as f:            
                f.write(f"# {module}\n\n")
                for ksb in topics.get(year).get(module):
                    f.write(f"- [[{ksb}]]\n")

    themes_folder = os.path.join(filepath, "Themes")
    os.makedirs(themes_folder, exist_ok=True)
    for theme in themes:
        theme_path = os.path.join(themes_folder, f"{theme}.md")
        with open(theme_path, "w", encoding="utf-8") as f:
            f.write(f"# {theme}\n")
            for ksb in themes.get(theme):
                f.write(f"- [[{ksb}]]\n")

if __name__ == "__main__":
    main()
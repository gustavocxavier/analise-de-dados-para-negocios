
import json
import os
from pathlib import Path

BASE_REPO_URL = "https://colab.research.google.com/github/gustavocxavier/analise-de-dados-para-negocios/blob/main"
ROOT_DIR = r"c:\code\curso-python-com-colab\analise-de-dados-para-negocios-com-python-e-colab"

def add_colab_button_to_notebook(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb_data = json.load(f)

    # Get relative path for the GitHub link
    rel_path = Path(nb_path).relative_to(ROOT_DIR).as_posix()
    colab_link = f"{BASE_REPO_URL}/{rel_path}"
    
    colab_badge_md = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})"
    
    # Create the new cell
    new_cell = {
        "cell_type": "markdown",
        "id": "colab_button_cell",
        "metadata": {},
        "source": [colab_badge_md + "\n"]
    }
    
    # Check if a colab cell already exists to avoid duplicates
    first_cell_src = "".join(nb_data['cells'][0]['source']) if nb_data['cells'] else ""
    if "colab-badge.svg" in first_cell_src:
        print(f"Skipping {nb_path}, already has colab button.")
        return

    # Add the cell at the beginning
    nb_data['cells'].insert(0, new_cell)
    
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb_data, f, ensure_ascii=False, indent=2)
    print(f"Added Colab button to {nb_path}")

# Notebooks to process
notebooks = [
    os.path.join(ROOT_DIR, "01_intro", "modulo_1.ipynb"),
    os.path.join(ROOT_DIR, "02_carregar_limpar", "modulo_2.ipynb"),
    os.path.join(ROOT_DIR, "03_visualizacao", "modulo_3.ipynb"),
    os.path.join(ROOT_DIR, "04_teste_de_hipotese", "modulo_4.ipynb"),
    os.path.join(ROOT_DIR, "analise-de-dados-para-negocios-com-python-e-colab1.ipynb")
]

for nb in notebooks:
    if os.path.exists(nb):
        add_colab_button_to_notebook(nb)
    else:
        print(f"File not found: {nb}")

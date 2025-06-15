import os
import requests

# Define directories
directories = {
    "cours": [
        "http://mletournel.free.fr/suites_normes_chapitre_intro.pdf",
        "http://mletournel.free.fr/cours_series.pdf",
        "http://mletournel.free.fr/suites_series_fonctions.pdf",
        "http://mletournel.free.fr/Integration_derivation_suites_et_series_de_fonctions.pdf",
        "http://mletournel.free.fr/derivation_fts_vectorielles.pdf",
        "http://mletournel.free.fr/Approximation.pdf",
        "http://mletournel.free.fr/series_entieres.pdf",
        "http://mletournel.free.fr/topo2014.pdf",
        "http://mletournel.free.fr/proba.pdf",
        "http://mletournel.free.fr/proba_partie2.pdf",
        "http://mletournel.free.fr/matrices.pdf",
        "http://mletournel.free.fr/reduction.pdf",
        "http://mletournel.free.fr/intgene.pdf",
        "http://mletournel.free.fr/prehilbertien_reel.pdf",
        "http://mletournel.free.fr/prehilbertien_reel.pdf",
        "http://mletournel.free.fr/equa_diff.pdf",
        "http://mletournel.free.fr/Courbes_parametrees.pdf",
        "http://mletournel.free.fr/calcul_differentiel.pdf"
    ],
    "exos": [
        "http://mletournel.free.fr/suites_normes_exe.pdf",
        "http://mletournel.free.fr/series_exe.pdf"
        "http://mletournel.free.fr/series_complement_exe.pdf",
        "http://mletournel.free.fr/familles_sommables_exe.pdf",
        "https://www.xif.fr/public/pr%C3%A9pas-dupuy-de-l%C3%B4me-maths/exos.zip"
    ]
}
# Create directories and download files if not already present
for folder, urls in directories.items():
    os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist

    for url in urls:
        try:
            filename = os.path.basename(url)
            path = os.path.join(folder, filename)

            if os.path.exists(path):
                print(f"Skipping {filename}: already exists.")
                continue  # Skip download

            print(f"Downloading {filename} to {path}...")
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            with open(path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Failed to download {url}: {e}")

import zipfile

# Path to the ZIP file
zip_path = 'exos/exos.zip'

# Destination directory to extract to
extract_to = 'exos'

# Make sure the destination directory exists
os.makedirs(extract_to, exist_ok=True)

# Extract the ZIP file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")


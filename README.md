# ⭐ spaCy Project Extention: latincy_ext

Code designed to add functionality to the [LatinCy](https://huggingface.co/latincy) models, e.g. custom components, etc. that are not (or at least not yet) part of the main project.

## Contents

- **liner**: Retrieve lines (e.g. lines of verse) as a custom, named span.
- **trf_vectors**: Retrieve contextual vector as a token attribute; compatible only with la_core_web_trf.

## Install

- To install the current version...
    - `pip install git+https://github.com/diyclassics/latincy_ext.git#egg=latincy_ext`

- Sample usage...

```
import spacy
from latincy_ext.liner import liner

nlp = spacy.load("la_core_web_lg")

text = """bella per Emathios plus quam ciuilia campos
iusque datum sceleri canimus, populumque potentem
in sua uictrici conuersum uiscera dextra
cognatasque acies, et rupto foedere regni
certatum totis concussi uiribus orbis
in commune nefas, infestisque obuia signis
signa, pares aquilas et pila minantia pilis."""

nlp.add_pipe("liner", name="liner", last=True)

doc = nlp(text)
lines = doc._.lines

for line in lines:
    print line
    break
```

## Current version

| Feature | Description |
| --- | --- |
| **Name** | `latincy_ext` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.5.3,<3.6.0` |
| **License** | `MIT` |
| **Author** | [Patrick J. Burns](https://diyclassics.github.io/) |

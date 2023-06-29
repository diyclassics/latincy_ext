# Pipeline component for efficiently getting spaCy spans per line of text

import spacy
from spacy.language import Language
from spacy.tokens import Doc, Span

@Language.component("liner")
def liner(doc):
    doc.spans["lines"] = []

    linebreaks = [token.i for token in doc if token.text == '\n']
    linebreaks_spans = []
    j = 0
    for i, linebreak in enumerate(linebreaks):
        linebreaks_spans.append((j, linebreak))
        j = linebreak + 1
    linebreaks_spans.append((j, len(doc))) # Catch last line if no linebreak at end of text

    for span in linebreaks_spans:
        line =  Span(doc, span[0], span[1])
        doc.spans["lines"].append(line)
    
    Doc.set_extension("lines", default=None, force=True)
    doc._.lines = doc.spans["lines"]
    return doc

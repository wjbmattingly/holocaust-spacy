import srsly
import spacy
from spacy.util import filter_spans
from spacy.tokens import Span
from spacy.language import Language
import re
import pandas as pd
from tqdm import tqdm


ghetto_pattern1 = r"[A-Z]\w+((-| )*[A-Z]\w+) (g|G)hetto"
ghetto_pattern2 = r"((g|G)hetto) (in|at) ([A-Z]\w+((-| )*[A-Z]\w+)*)"
# ghetto_pattern = r"([A-Z]\w+((-| )*[A-Z]\w+)* (g|G)hetto)|(ghetto in [A-Z][^\s]+)|(ghetto at [A-Z][^\s]+)"
@Language.component("find_ghettos")
def find_ghettos(doc):
    fps = ["That", "The"]
    text = doc.text
    ent_matches = []
    original_ents = list(doc.spans["sc"])
    for match in re.finditer(ghetto_pattern1, text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")


        # if span is not None and span.text not in fps:
        # if "The " in span.text:
        #     if span.text.split()[-1].lower() == "ghetto":
        #         ent_matches.append((span.start+1, span.end, span.text))
        # else:
        ent_matches.append((span.start, span.end, span.text))

    for match in re.finditer(ghetto_pattern2, text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        if span.text.split()[-1].lower() == "ghetto":
            print("found")
            ent_matches.append((span.start, span.end-1, span.text))
        else:
            ent_matches.append((span.start, span.end, span.text))
    for start, end, _ in ent_matches:  # Unpack start and end from ent_matches
        original_ents.append(Span(doc, start, end, label="GHETTO"))
    # filtered = filter_spans(original_ents)
    doc.spans["sc"] = original_ents

    return (doc)
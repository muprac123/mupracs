import spacy 
import pandas as pd 
from spacy import displacy 

NER = spacy.load("en_core_web_sm") 
text = "Apple acquired zoom-in-China-on-wednesday-6th May 2020. This news made Apple and Google stock jump by 5% on Dow Jones Index in the United States of America."

doc = NER(text)
entities = []
labels = []
position_start = []
position_end = []

for ent in doc.ents:
    entities.append(ent.text)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)

df = pd.DataFrame({
    'Entities': entities, 
    'Labels': labels, 
    'Position_Start': position_start, 
    'Position_End': position_end
})

print(df)
displacy.serve(doc, style='dep', options={'distance': 120})
displacy.render(doc, style="ent")

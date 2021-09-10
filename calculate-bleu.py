import datasets
sacrebleu = datasets.load_metric("sacrebleu")
import json

lang = 'german'
many  = True
prose = False
zeroshot = False
langpair = False
multiopus = False
f = './testdatawithtranslations/'+lang+'/gold'+lang+'.txt'
if many:
    g = './testdatawithtranslations/'+lang+'/'+lang+'poetrymanybeam5.txt'
else:
    if multiopus:
        g = './testdatawithtranslations/'+lang+'/'+lang+'multiopus.txt'
    if zeroshot:
        g = './testdatawithtranslations/'+lang+'/'+lang+'zeroshot.txt'
    elif prose:
        g = './testdatawithtranslations/'+lang+'/'+lang+'prosebeam5.txt'
    elif langpair:
        g = './testdatawithtranslations/'+lang+'/'+lang+'langpair.txt'
    else:
        g = './testdatawithtranslations/'+lang+'/'+lang+'poetrybeam5.txt'
  
for x,y in zip(open(f),open(g)):
    if x.strip()=='--------------------------------------------------------------------------------':
        continue
    sys.append(y.strip())
    refs.append([x.strip()])
    result = sacrebleu.compute(predictions=sys, references=refs)
    print(result['score'])

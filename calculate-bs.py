from bert_score import score
import json
cands = []
refs =  []
import os
os.environ["CUDA_VISIBLE_DEVICES"]='2'


lang = 'german'
langpair = False
many  = False
prose = True
zeroshot = False
f = './testdatawithtranslations/'+lang+'/gold'+lang+'.txt'
if many:
    g = './testdatawithtranslations/'+lang+'/'+lang+'poetrymanybeam5.txt'
else:
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
    cands.append(y)
    refs.append(x)
    P, R, F1 = score(cands, refs, lang="en", model_type='microsoft/deberta-large-mnli')
    result = F1.mean()
    print(result)
from transformers import MBart50Tokenizer, MBartForConditionalGeneration

modelname = "TuhinColumbia/russianpoetrymany"
tokenizer = MBart50Tokenizer.from_pretrained(modelname)
model = MBartForConditionalGeneration.from_pretrained(modelname)
model.eval()
model.to('cuda')

def translateSourceToTarget(inp,source_lang):
	line = inp
	tokenizer.src_lang = source_lang
	inputs = tokenizer(line, return_tensors="pt")
	inputs = inputs.to('cuda')
	generated_tokens = model.generate(**inputs, no_repeat_ngram_size=2, num_beams=5,num_return_sequences=5,forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
	res = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
	res = [(r,len(r.split())) for r in res]
	return res[0][0]

result = translateSourceToTarget("В их сенях ветра шум и свежее дыханье,","ru_RU")
print(result)
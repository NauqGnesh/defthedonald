from transformers import pipeline, AutoTokenizer

pipe = None

def get_generations(model_folder, num_samples):
    global pipe
    if pipe is None:
        tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
        pipe = pipeline('text-generation',model=model_folder, framework="pt", tokenizer=tokenizer)
        # pipe = pipeline('text-generation', model='./model_files/distilgpt2', tokenizer='distilgpt2',
        #                 config={'max_length': 800})
    start_token = '<|startoftext|>'
    end_token = '<|endoftext|>'
    results = pipe([start_token]*num_samples)
    # print(results)
    return [result[0]['generated_text'].replace(start_token, '').replace(end_token, '') for result in results]
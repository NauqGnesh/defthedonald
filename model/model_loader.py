from transformers import pipeline
# import gpt_2_simple as gpt2
# import tensorflow as tf

# sess = None
pipe = None

def initialize_model():
    # global sess
    # sess = gpt2.start_tf_sess()
    # gpt2.load_gpt2(sess, run_name='run1', checkpoint_dir='model_files')
    pass

def get_generations():
    global pipe
    if pipe is None:
        pipe = pipeline('text-generation', model='./model_files/distilgpt2', tokenizer='distilgpt2',
                        config={'max_length': 800})
    return pipe('I want')
    # global sess
    # return gpt2.generate(sess,
    #          run_name='run1',
    #          checkpoint_dir='model_files', # default 'checkpoint',
    #          model_name=None,
    #          model_dir='models',
    #          sample_dir='samples',
    #          return_as_list=True, # default False,
    #          truncate='<|endoftext|>', # default None,
    #          destination_path=None,
    #          sample_delim='=' * 20 + '\n',
    #          prefix='<|startoftext|>', # default None,
    #          seed=None,
    #          nsamples=20, # default 1,
    #          batch_size=20, # default 1,
    #          length=200, # default 1023,
    #          temperature=0.7,
    #          top_k=0,
    #          top_p=0.0,
    #          include_prefix=False) # default True)
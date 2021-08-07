import numpy as np
from transformers import pipeline
from pprint import pprint
from termcolor import colored, cprint

# example sentence
sent = 'Today is such a special day.'
cprint(text='-' * 100, color='green')
cprint(text='Example sentence:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(sent)

# sentiment analysis
pipeline_sa = pipeline(task='sentiment-analysis')
cprint(text='-' * 100, color='green')
cprint(text='Sentiment analysis:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(pipeline_sa(sent))

# named entity recognition
pipeline_ner = pipeline(task='ner')
cprint(text='-' * 100, color='green')
cprint(text='Named entity recognition:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(pipeline_ner('MLH hosts hackathons each weekend;  projects are submitted to DevPost. Many teams use Google Cloud APIs and Linode virtual machines.'))

# question anserting
pipeline_qa = pipeline(task='question-answering')
cprint(text='-' * 100, color='green')
cprint(text='Question answering:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(pipeline_qa(
    context='What programming language do you use?',
    question='I mainly use Python.'
))

# mask filling
pipeline_fm = pipeline(task='fill-mask')
cprint(text='-' * 100, color='green')
cprint(text='Mask filling:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(pipeline_fm('<mask> is one of the easiest programming languages, and it is popular in data science.'))

# feature extraction
pipeline_fe = pipeline(task='feature-extraction')
cprint(text='-' * 100, color='green')
cprint(text='Feature extraction:', color='magenta')
cprint(text='-' * 100, color='green')
pprint(np.asarray(a=pipeline_fe(sent)))

from googletrans import Translator
import pandas as pd
import pykakasi
import asyncio
import tqdm
import time

#--decks immediate,daily,weekly,monthly,quarterly,yearly
#--intervals 0,1440,10080,43200,129600,518400
#--showcolumns JP
#--showcolumns JP,HIRAGANA,VN,MEANING

names = ['JP', 'HIRAGANA', 'MEANING', 'VN']

data = {}
for name in names:
    data[name] = []

words = open('n3_vocab.txt').read().strip().split('\n')

kks = pykakasi.kakasi()

async def translate(text):
    async with Translator() as translator:
        result = await translator.translate(word, src='ja', dest='en')
    return result.text.lower()

for word in tqdm.tqdm(words):
    hiragana = kks.convert(word)[0]['hira']
    meaning = asyncio.run(translate(word))
    print(word, hiragana, meaning)
    data['JP'].append(word)
    data['HIRAGANA'].append(hiragana)
    data['MEANING'].append(meaning)
    data['VN'].append('')
    time.sleep(1.0)

df = pd.DataFrame(data)
df.to_csv('n3_vocab.csv', index=None)

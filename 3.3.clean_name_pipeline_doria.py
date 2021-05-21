import stanza
import gensim
from gensim import interfaces, utils
import pandas as pd
import texthero as hero
from texthero import preprocessing
import nltk
from nltk.corpus import stopwords
import re
import numpy as np
from pprint import pprint
import logging
import texthero as hero
from texthero import preprocessing
import pandas as pd
from IPython.display import Audio, display
def allDone():
    display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))
import warnings
warnings.filterwarnings("ignore")
import csv
csv.field_size_limit()
131072
csv.field_size_limit(256 << 10)
131072
csv.field_size_limit()
262144
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Make your stopwords
stopwords_portuguese = re.split('\s+', 'a, agora, ainda, alguém, algum, alguma, algumas, alguns, ampla, amplas, amplo, amplos, ante, antes, ao, aos, após, aquela, aquelas, aquele, aqueles, aquilo, as, até, através, cada, coisa, coisas, com, como, contra, contudo, da, daquele, daqueles, das, de, dela, delas, dele, deles, depois, dessa, dessas, desse, desses, desta, destas, deste, deste, destes, deve, devem, devendo, dever, deverá, deverão, deveria, deveriam, devia, deviam, disse, disso, disto, dito, diz, dizem, do, dos, e, é, ela, elas, ele, eles, em, enquanto, entre, era, essa, essas, esse, esses, esta, está, estamos, estão, estas, estava, estavam, estávamos, este, estes, estou, eu, fazendo, fazer, feita, feitas, feito, feitos, foi, for, foram, fosse, fossem, grande, grandes, há, isso, isto, já, la, lá, lhe, lhes, lo, mas, me, mesma, mesmas, mesmo, mesmos, meu, meus, minha, minhas, muita, muitas, muito, muitos, na, não, nas, nem, nenhum, nessa, nessas, nesta, nestas, ninguém, no, nos, nós, nossa, nossas, nosso, nossos, num, numa, nunca, o, os, ou, outra, outras, outro, outros, para, pela, pelas, pelo, pelos, pequena, pequenas, pequeno, pequenos, per, perante, pode, pude, podendo, poder, poderia, poderiam, podia, podiam, pois, por, porém, porque, posso, pouca, poucas, pouco, poucos, primeiro, primeiros, própria, próprias, próprio, próprios, quais, qual, quando, quanto, quantos, que, quem, são, se, seja, sejam, sem, sempre, sendo, será, serão, seu, seus, si, sido, só, sob, sobre, sua, suas, talvez, também, tampouco, te, tem, tendo, tenha, ter, teu, teus, ti, tido, tinha, tinham, toda, todas, todavia, todo, todos, tu, tua, tuas, tudo, última, últimas, último, últimos, um, uma, umas, uns, vendo, ver, vez, vindo, vir, vos, vós, *, -, sp, av, r, ii')

newlist = []
for n in stopwords_portuguese:
    newlist.append(n.replace(",", ''))
stopwords_portuguese = newlist

filename = 'C:/Users/user/1.IRONHACK/stopwords.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1,
                  encoding='utf-8', dtype=str)
new_stop = data.tolist()
joined_stop = new_stop + stopwords_portuguese
joined_stop = [x.strip(' ') for x in joined_stop]
#nltk.download('stopwords')
stop_words = stopwords.words('portuguese')
stop_words.extend([joined_stop, 'segunda', 'terça', 'quarta','quinta', 'internos',
                   'sexta', 'sabado', 'domingo', 'feira','sao', 'paulo', 'eu','elas',
                   'secretaria', 'municipio', 'prefeitura', 'sr', 'sra', 'nos',
                   'no', 'na', 'local', 'despacho', 'despachos', 'gabinete', 'nós',
                   'cidade', 'reuniao', 'agenda', 'gabinete', 'ele', 'ela', 'eles'])

# %% Define your function
def doria(x):
    # Load file
    df = pd.read_csv('C:/Users/user/2. GIT_PROJECTS/Desafios/Projeto 5 - NLP Secretarias/tables/doria/'+str(x)+'_doria_covas.csv', sep=r'Γ')
    #Preprocess: Remove urls
    df['text'] = df['text'].str.replace('http\S+|www.\S+', '', case=False)

    # Preprocess automate Hero with no Lem
    # create a custom cleaning pipeline
    custom_pipeline = [preprocessing.fillna
                    , preprocessing.lowercase
                    , preprocessing.remove_punctuation
                    , preprocessing.remove_digits
                    , preprocessing.remove_diacritics
                    #, preprocessing.remove_stopwords
                    , preprocessing.remove_whitespace
                    #, preprocessing.stem]
                    ]
    # Clean numbers and dates
    df['clean_title'] = df['text'].apply(lambda x: re.sub('\d{1,2}h\d\d', '', x))
    df['clean_title']= df['clean_title'].str.replace(r'\d+','')
    # pass the custom_pipeline to the pipeline argument
    df['clean_title'] = hero.clean(df['clean_title'], pipeline=custom_pipeline)
    # Erase stopwords with Python's list comprehension and pandas.DataFrame.apply.
    df['clean_title'] = df['clean_title'].apply(lambda x: ' '.join(
    [word for word in x.split() if word not in (stop_words)]))
    df.head()

    # Extract your train variable from table
    train_text = df['clean_title']
    train_text.head()

    # Clean NaNs
    df = df.dropna()
    # Save table
    df.to_csv('C:/Users/user/2. GIT_PROJECTS/Desafios/Projeto 5 - NLP Secretarias/tables_clean/doria/'+str(x)+'_doria_covas.csv', sep=r'Γ', index=False)
    return allDone()

#%%create your graphs!
doria('assistencia_social')
doria('capitalsp')
doria('controladoria_geral')
doria('cultura')
doria('desenvolvimento')
doria('direitos_humanos')
doria('direitos_humanos-poprua')
doria('esportes')
doria('fazenda')
doria('gestao')
doria('governo')
doria('habitacao')
doria('justica')
doria('meio_ambiente')
doria('obras')
doria('pessoa_com_deficiencia')
doria('procuradoria_geral')
doria('relacoes_internacionais')
doria('relacoes_sociais')
doria('saude')
doria('seguranca_urbana-defesa_civil')
doria('seguranca_urbana-guarda_civil')
doria('subprefeituras')
doria('transportes')
doria('urbanismo')
doria('seguranca_urbana')
#%% Big Table
doria('big_table')

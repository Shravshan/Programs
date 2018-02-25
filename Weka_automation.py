import pandas as pd
import glob, os
import csv
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile, join
import time
import datetime
import sys
from datetime import datetime
import glob 
import fnmatch
import shutil
import collections
import re
import pymsgbox

    
stop_words = nltk.corpus.stopwords.words('english')
newStopWords = ['a',
'able',
'about',
'above',
'according',
'accordingly',
'across',
'actually',
'after',
'afterwards',
'again',
'against',
'all',
'allow',
'allows',
'almost',
'alone',
'along',
'already',
'also',
'although',
'always',
'am',
'among',
'amongst',
'an',
'and',
'another',
'any',
'anybody',
'anyhow',
'anyone',
'anything',
'anyway',
'anyways',
'anywhere',
'apart',
'appear',
'appreciate',
'appropriate',
'are',
'around',
'as',
'aside',
'ask',
'asking',
'associated',
'at',
'available',
'away',
'awfully',
'b',
'be',
'became',
'because',
'become',
'becomes',
'becoming',
'been',
'before',
'beforehand',
'behind',
'being',
'believe',
'below',
'beside',
'besides',
'best',
'better',
'between',
'beyond',
'both',
'brief',
'but',
'by',
'c',
'came',
'can',
'cannot',
'cant',
'cause',
'causes',
'certain',
'certainly',
'changes',
'clearly',
'co',
'com',
'come',
'comes',
'concerning',
'consequently',
'consider',
'considering',
'contain',
'containing',
'contains',
'corresponding',
'could',
'course',
'currently',
'd',
'definitely',
'described',
'despite',
'did',
'different',
'do',
'does',
'doing',
'done',
'down',
'downwards',
'during',
'e',
'each',
'edu',
'eg',
'eight',
'either',
'else',
'elsewhere',
'enough',
'entirely',
'especially',
'et',
'etc',
'even',
'ever',
'every',
'everybody',
'everyone',
'everything',
'everywhere',
'ex',
'exactly',
'example',
'except',
'f',
'far',
'few',
'fifth',
'first',
'five',
'followed',
'following',
'follows',
'for',
'former',
'formerly',
'forth',
'four',
'from',
'further',
'furthermore',
'g',
'get',
'gets',
'getting',
'given',
'gives',
'go',
'goes',
'going',
'gone',
'got',
'gotten',
'greetings',
'h',
'had',
'happens',
'hardly',
'has',
'have',
'having',
'he',
'hello',
'help',
'hence',
'her',
'here',
'hereafter',
'hereby',
'herein',
'hereupon',
'hers',
'herself',
'hi',
'him',
'himself',
'his',
'hither',
'hopefully',
'how',
'howbeit',
'however',
'i',
'ie',
'if',
'ignored',
'immediate',
'in',
'inasmuch',
'inc',
'indeed',
'indicate',
'indicated',
'indicates',
'inner',
'insofar',
'instead',
'into',
'inward',
'is',
'it',
'its',
'itself',
'j',
'just',
'k',
'keep',
'keeps',
'kept',
'know',
'knows',
'known',
'l',
'last',
'lately',
'later',
'latter',
'latterly',
'least',
'less',
'lest',
'let',
'like',
'liked',
'likely',
'little',
'll', #// added to avoid words like you'll,I'll etc.
'look',
'looking',
'looks',
'ltd',
'm',
'mainly',
'many',
'may',
'maybe',
'me',
'mean',
'meanwhile',
'merely',
'might',
'more',
'moreover',
'most',
'mostly',
'much',
'must',
'my',
'myself',
'n',
'name',
'namely',
'nd',
'near',
'nearly',
'necessary',
'need',
'needs',
'neither',
'never',
'nevertheless',
'new',
'next',
'nine',
'no',
'nobody',
'non',
'none',
'noone',
'nor',
'normally',
'not',
'nothing',
'novel',
'now',
'nowhere',
'o',
'obviously',
'of',
'off',
'often',
'oh',
'ok',
'okay',
'old',
'on',
'once',
'one',
'ones',
'only',
'onto',
'or',
'other',
'others',
'otherwise',
'ought',
'our',
'ours',
'ourselves',
'out',
'outside',
'over',
'overall',
'own',
'p',
'particular',
'particularly',
'per',
'perhaps',
'placed',
'please',
'plus',
'possible',
'presumably',
'probably',
'provides',
'q',
'que',
'quite',
'qv',
'r',
'rather',
'rd',
're',
'really',
'reasonably',
'regarding',
'regardless',
'regards',
'relatively',
'respectively',
'right',
's',
'said',
'same',
'saw',
'say',
'saying',
'says',
'second',
'secondly',
'see',
'seeing',
'seem',
'seemed',
'seeming',
'seems',
'seen',
'self',
'selves',
'sensible',
'sent',
'serious',
'seriously',
'seven',
'several',
'shall',
'she',
'should',
'since',
'six',
'so',
'some',
'somebody',
'somehow',
'someone',
'something',
'sometime',
'sometimes',
'somewhat',
'somewhere',
'soon',
'sorry',
'specified',
'specify',
'specifying',
'still',
'sub',
'such',
'sup',
'sure',
't',
'take',
'taken',
'tell',
'tends',
'th',
'than',
'thank',
'thanks',
'thanx',
'that',
'thats',
'the',
'their',
'theirs',
'them',
'themselves',
'then',
'thence',
'there',
'thereafter',
'thereby',
'therefore',
'therein',
'theres',
'thereupon',
'these',
'they',
'think',
'third',
'this',
'thorough',
'thoroughly',
'those',
'though',
'three',
'through',
'throughout',
'thru',
'thus',
'to',
'together',
'too',
'took',
'toward',
'towards',
'tried',
'tries',
'truly',
'try',
'trying',
'twice',
'two',
'u',
'un',
'under',
'unfortunately',
'unless',
'unlikely',
'until',
'unto',
'up',
'upon',
'us',
'use',
'used',
'useful',
'uses',
'using',
'usually',
'uucp',
'v',
'value',
'various',
've', #added to avoid words like I've,you've etc.
'very',
'via',
'viz',
'vs',
'w',
'want',
'wants',
'was',
'way',
'we',
'welcome',
'well',
'went',
'were',
'what',
'whatever',
'when',
'whence',
'whenever',
'where',
'whereafter',
'whereas',
'whereby',
'wherein',
'whereupon',
'wherever',
'whether',
'which',
'while',
'whither',
'who',
'whoever',
'whole',
'whom',
'whose',
'why',
'will',
'willing',
'wish',
'with',
'within',
'without',
'wonder',
'would',
'would',
'x',
'y',
'yes',
'yet',
'you',
'your',
'yours',
'yourself',
'yourselves',
'z',
'zero',
'i'
]
stop_words.extend(newStopWords)

results = pd.DataFrame([])
results_contents = pd.DataFrame([])
empty = False

path=r'C:\Users\Public\PythonFiles\Input\\'

#try:
#    os.listdir(path)
#    empty = True
#except OSError:
#    empty = False

#print(empty)
#if (empty == True):
#    pymsgbox.native.alert('Input folder empty. Please try again!','Error')
#    exit()
    

os.chdir(r'C:\Users\Public\PythonFiles\Input\\' )
results = pd.DataFrame([])
for counter, file in enumerate(glob.glob(os.path.join('',"*.csv"))):
    namedf = pd.read_csv(file, skiprows=0, encoding='iso-8859-1')
    results = results.append(namedf)

results_contents=results['Contents']
        #results_contents.head(5)

datestring_clean = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
clean_file_output = open(r'C:\Users\Public\PythonFiles\Clean\Clean_out' + datestring_clean + '.csv', 'a+',newline='')

regex=r'[^A-Za-z0-9\\ ]'

for row in results_contents:
    out=re.sub(regex,'',str(row))
    words = out.split()
    word = [w for w in words if not w in newStopWords]
    clean_file_output.write(' '.join(word) + '\n')


def move_files():
    
    dir_src = (r'C:\Users\Public\PythonFiles\Input\\')
    dir_dst = (r'C:\Users\Public\PythonFiles\Archive\\') 
    for file in os.listdir(dir_src):
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(dir_dst, file)
        shutil.move(src_file, dst_file)
    
############################################ MOVE TO ARCHIVE ############################################



def tokenize(string):
    """Convert string to lowercase and split into words (ignoring
    punctuation), returning list of words.
    """
    return re.findall(r'\w+', string.lower())


def count_ngrams(lines, min_length=3, max_length=5):
    """Iterate through given lines iterator (file object or list of
    lines) and return n-gram frequencies. The return value is a dict
    mapping the length of the n-gram to a collections.Counter
    object of n-gram tuple and number of times that n-gram occurred.
    Returned dict includes n-grams of length min_length to max_length.
    """
    lengths = range(min_length, max_length + 1)
    ngrams = {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen=max_length)

    # Helper function to add n-grams at start of current queue to dict
    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1

    # Loop through all lines and words and add n-grams to dict
    for line in lines:
        for word in tokenize(line):
            queue.append(word)
            if len(queue) >= max_length:
                add_queue()

    # Make sure we get the n-grams at the tail end of the queue
    while len(queue) > min_length:
        queue.popleft()
        add_queue()

    return ngrams


def print_most_frequent(ngrams, num=200):
    """"Print num most common n-grams of each length in n-grams dict."""
    #ch=open(final, 'w',newline='')
    datestring = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    final = open(r'C:\Users\Public\PythonFiles\Output\Final_out' + datestring + '.csv', 'w',newline='')
    for n in sorted(ngrams):
        #print('----- {} most common {}-grams -----'.format(num,n))
        for gram, count in ngrams[n].most_common(num):
            final.write(' '.join(gram)+'\n')
            #print('{0}: {1}'.format(' '.join(gram), count))
        #print('')


if __name__ == '__main__':
    start_time = time.time()
    move_files()
    clean_file_output.seek(0, 0)
    with clean_file_output as f:
        m= pymsgbox.prompt('Enter minimum number of words', 'Input')
        min_length= int(m)
#int(input('Enter minimum number of words:'))
        n=pymsgbox.prompt('Enter maximum number of words', 'Input')
        max_length=int(n)
    #int(input('Enter maximum number of words:'))
        u=pymsgbox.prompt('Enter the frequency of phrases', 'Input')
        num=int(u)
#int(input('Enter the limit for phrases:'))
        ngrams = count_ngrams(f,min_length,max_length)
    print_most_frequent(ngrams,num)
    pymsgbox.native.alert('Output file ready to view','Completed!')
    elapsed_time = time.time() - start_time
    #print('Took {:.03f} seconds'.format(elapsed_time))


clean_file_output.close()




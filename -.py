from bs4 import BeautifulSoup #required to parse html
import requests #required to make request
import re
import datetime
from newspaper import Article
import os # To dynamically get filepaths

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

csv_file = '2016_Verizon_DigitalNews_or_Blog_Mentions_Final.csv'

urls_list = open(csv_file).read().splitlines()

i = 0

for url in urls_list:

    try: # Make URL request; block redirects; ensure verification
        response = session.get(url,allow_redirects=False,verify=True)
        response.close()

    # May happen with bad SSL certificates 
    except requests.exceptions.ConnectionError:
        print("Connection Error with URL:",url)
        pass

    # Happens with =HYPERLINK("http://...") Excel formulas
    except requests.exceptions.InvalidSchema:
        print("Invalid schema with URL:",url)
        pass

    if response.ok: # Check if ok (e.g. not "404")   
    
        article = Article(url)
        article.download()
        
        # See https://github.com/codelucas/newspaper/issues/357#issuecomment-359545682
        # ArticleDownloadState.NOT_STARTED is 0
        # ArticleDownloadState.FAILED_RESPONSE is 1
        # ArticleDownloadState.SUCCESS is 2
        if article.download_state == 2:
            article.parse() 
            date=str(article.publish_date)
            regex=r'[^A-Za-z0-9\\ ]'  # I appended str(i) to the end of the file name, since some dates might be the sample 
            out = open(os.getcwd() + '\\text_files\\articles_' + date[:10] + '_' + str(i) + '.txt', 'w',encoding='iso-8859-1')
            out.write(re.sub(regex,' ',article.text))
            out.close()
            i+=1
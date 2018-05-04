with open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Watson\Watson\Weber Shandwick - Tone Analyzer Script\Weber Shandwick\toneAnalyzer\input\Flu_tweets.csv','r') as f:
    csv_raw_cont=f.read()

split_csv=csv_raw_cont.split('\n')

split_csv.remove('')

separator=","

i=1

for each in split_csv:
    url_row_index=0 #in our csv file the url is the first row so we set 0
    url = each.split(separator)[url_row_index]
    out = open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Watson\Watson\Weber Shandwick - Tone Analyzer Script\Weber Shandwick\toneAnalyzer\input\Link' + str(i) + '.txt', 'w',encoding='iso-8859-1')
    out.write(url)
    out.close()
    i+=1
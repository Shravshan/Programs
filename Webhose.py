import webhoseio

# Mention the path of the output file. 
f=open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Webhose\Output4.csv','w',encoding='utf-8')

# Use your token to access Webhose API
webhoseio.config(token="1e13db35-ed2b-4f04-a1f4-a6264829d264")

# Mention the query parameters. It is currently crawling for '1' previous day
query_params = {  "q": "(((\"finance\" OR \"bank\" OR \"financial\" OR \"wealth\" OR \"business\" OR \"economic\" OR \"economy\"  )",
"ts": "1517756775835","sort": "crawled" }

#Filtering the web content accoridng to the query parameters mentioned
output = webhoseio.query("filterWebContent", query_params)

# Iterating through every post that the query returned
for post in output['posts']:
    #Removing commas to save the output as a CSV file. Accessing only 'text' in the post
    post['text'] = post['text'].replace(',',' ')
    print(post['text'])
    # Write evry post to the CSV file
    for row in post['text']:
        f.write(row)
        
# Get the next batch of posts
output = webhoseio.get_next()

#Close the file
f.close()       
    

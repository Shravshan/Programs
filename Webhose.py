import webhoseio

# Mention the path of the output file. 
f=open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Webhose\Output4.csv','w',encoding='utf-8')

# Use your token to access Webhose API
webhoseio.config(token="1e13db35-ed2b-4f04-a1f4-a6264829d264")

# Mention the query parameters. It is currently crawling for '1' previous day
query_params = {  "q": "(((\"finance\" OR \"bank\" OR \"financial\" OR \"wealth\" OR \"business\" OR \"economic\" OR \"economy\" OR \"biz owner\" OR \"invest\") AND ((\"diversity\" OR \"equity\" OR \"inclusion\" OR \"women\" OR \"military\" OR \"LGBTQ\" OR \"disability\" OR \"veteran\" OR \"disabled\" OR \"disabilities\" OR \"inclusive\") AND (\"work place\" OR \"corporate\" OR \"company\" OR \"employ\" OR \"job\" OR \"policy\" OR \"workplace\"))) OR (\"community development\" OR \"workforce development\" OR \"philanthropic partner\" OR \"youth employment\" OR \"education\" OR \"workplace re-entry\" OR \"social responsibility\" OR \"CSR\" OR \"social impact\" OR \"employment\" OR \"women leaders\" OR \"female leaders\" OR \"women leadership\" OR \"female leadership\" OR \"women empowerment\" OR \"donation\" OR \"donate\" OR \"diverse leaders\" OR \"#PowerWomen\" OR \"gendergap\" OR \"gender gap\" OR \"mentor\" OR \"women biz owner\" OR \"inclusive workplace\" OR \"financial resources\" OR \"women owned businesses\" OR \"#WomenLead\" OR \"diversity\" OR \"racial equity\" OR \"inclusive\")) AND NOT (\"bank of america stadium\" OR \"bofa stadium\" OR \"b of a stadium\" OR \"bankofamerica stadium\" OR \"#hiring\" OR \"to apply\" OR \"#careerarc\" OR \"latest opening\" OR \"jobscharlote\" OR \"jobschicago\" OR \"job post\" OR \"bourseettrading\" OR \"Makeyourownlane\" OR \"mpgvip\" OR Author:jobscharlotte1 OR author:tmj_clit_itjava OR Author:tmj_clt_mgmt OR Author:joegibbsracing OR Author:tmj_clit_it OR Author:watchem_foldup OR Author:switfcoentinc OR Author:ednamartinal OR Author:johsontrey OR Author:SharpPointBooks OR Author:knunez82 OR Author:prepzilla OR Author:DI_Knox OR Author:CompleteScrub )",
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
    
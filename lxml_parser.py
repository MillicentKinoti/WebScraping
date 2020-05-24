from bs4 import  BeautifulSoup
import  requests

url='https://www.codechef.com/problems/easy'
res = requests.get(url)

page = BeautifulSoup(res.text, 'lxml')

datatable_tags = page.select('table.dataTable')#table is the tag and dataTable is the class of the table


datatable = datatable_tags[0] #just the first row

prob_tags = datatable.select('a > b')#going inside the a tag and getting the content (b)

prob_names= [tag.getText().strip() for tag in prob_tags]#get the text in the tags

for i in prob_names:
    print(i)


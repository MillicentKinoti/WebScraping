from bs4 import BeautifulSoup

raw_html = open('demo.html').read()
html= BeautifulSoup(raw_html,'html.parser') #parser selects only what is needed
#BeautifulSoup class takes two arguments, raw_html or the url and the parser

for p in html.select('p'): #to display the paragraphs only
    print(p.text)#p.text removes the p tags



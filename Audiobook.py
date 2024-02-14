# pip install requests-html
from Googlekey import *
import requests 
import os
from requests_html import HTMLSession
from bs4 import BeautifulSoup
#Pla
#Download pdf from pdfdrive.com
#print("Current working directory:", os.getcwd())

#PART 1 - Get the list of books
#*------------*
page = 'https://www.goodreads.com/list/show/97681.The_Guardian_100_Best_Nonfiction_Books_'
page_response = requests.get(page) 
soup = BeautifulSoup(page_response.content, "html.parser") 

#<a title- for book title
#<spam> for book author
#Extract Book Titles and Authors from the HTML Web inspection file

title_tags = soup.find_all("a", {"title": True})
author_tags = soup.find_all("a", class_ = "authorName")
#Remove comments and other strings under the same HTML tags
remove= ["Goodreads Home", "Flag this list as inappropriate.", "it was ok", "liked it", "really liked it", "did not like it", "it was amazing", "did not like it"]

#Get Book Titles and Authors in a list 
#Remove white spaces with strip
titles = [title.get("title").strip() for title in title_tags if title.get("title").strip() not in remove]
#For authors, now find the exact author from the <spam> tag within the <a> tag
authors = [author.find("span").get_text(strip=True) for author in author_tags]

new_title= []
#Iterate simultaneously using zip
for (bookname, aut) in zip(titles, authors):
    new_title.append(bookname + " by " +aut) 

#print(new_title)
#print(len(new_title))

#Step 2####
    
# Downloading the book

#Warned
#Overcoming the AV https://youtu.be/JesHXRoJbzw?si=uIKNI8sqAFAaj4fT 
#web= ["https://www.gutenberg.org/", ]
#Ok
#webdownload = ["https://manybooks.net/", "https://www.pdfdrive.com/" ]

#for book in new_title:

#with open('Googlekey.py', 'r') as file:
#    API_KEY = file.readline().strip()
 #   SEARCH_ENGINE_ID = file.readline().strip()    

    
# Initialize search_query as a global variable
search_query = ""

def booktitle(lst):
    global search_query

    if lst == []:
        return "Finished"
    else:
        search_query += lst[0]
        search_net()
        return booktitle(lst[1:])
booktitle(new_title)

def search_net():

#Call glabal twice so that python doesn't assume we a creating a new local variable with same name
    global search_query
    #sending the request to this
    url= 'https://www.googleapis.com/customsearch/v1'

#########Google Custom Search API supports
#q (query), key, cx (custom search engine), searchType, num (number of results)
# start (start index), 'siteSearch': 'example.com', 'fileType': 'pdf', 'alt': 'json' 
#'language': 'en', 'safe': 'high, 'dateRestrict': '2022-01-01:2024-01-01', 'globe': 'US'##########
    
    params= {

    'q': search_query, 
    'key': API_KEY, 
    'cx': SEARCH_ENGINE_ID,
    'fileType': 'pdf',
    'language': 'en'

    }

    response = requests.get(url, params=params)
#json is used to transfer data as text that can be sent over a network.
    results= response.json()['items']

    for item in results:
        print(item['link'])
    search_query = search_query[1:]







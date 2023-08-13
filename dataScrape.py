import requests
from bs4 import BeautifulSoup

#create a loop for month names
for month in range(12):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october', 'november', 'december']

    # URL of the website you want to scrape
    url = "http://lottoresults.co.nz/lotto/" + months[month] +"-2023"
    print(url)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article titles on the page
    article_titles = soup.find_all('li', class_="draw-result__ball" )

    # Loop through the article titles and print them
    list = []
    for title in article_titles:
        # create list and seperate the list into tuples of 6
        list.append(title.text.strip())

    list = [list[i:i+6] for i in range(0, len(list), 6)]


    #put this into a text file
    with open('lotto.txt', 'a') as f:
        for item in list:
            #write additional lines, don't overwrite
            f.write("%s\n" % item)



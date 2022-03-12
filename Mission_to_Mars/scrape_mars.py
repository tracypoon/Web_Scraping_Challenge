from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scape_info()
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit the website we want to scape
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    # NASA Mars News
    #scape for article news titles
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all('div', class_='content_title')
    title

    #identify the latest news article title
    news_title = title[0].text
    news_title

    #scape for article news paragraph text
    text = soup.find_all('div', class_='article_teaser_body')
    text

    #identify the latest news paragraph text
    news_p = text[0].text
    news_p

    #JPL Mars Space Images - Featured Image
    #get featured image from url
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #search for source image by indexing list
    relative_image_path = soup.find_all('img')[1]["src"]

    #add to the url to get the full path
    featured_img = url + relative_image_path
    featured_img

    print(f"Featured_image_url = {featured_img}")

    # Mars Facts
    #scape table information per the request
    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    tables

    #index the list to select one of the tables
    table = tables[1]
    table

    #turn the table into html
    html_table = table.to_html()
    html_table

    #Mars Hemispheres
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #search by tag and class
    results = soup.find_all("div", class_="description")
    results

    #create list to append
    hemisphere_img_urls = []

    #create loop to get the requested information
    for result in results:

    hemisphere = {}

    #searches for the titles
    title=result.find('h3').text
    browser.click_link_by_partial_text(title)

    #searches for the image source url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    output = soup.find("img", class_="wide-image")['src']
    img_url = f'https://marshemispheres.com/' + output

    #append the results into the empty list and create dictionary
    hemisphere = {"title" : title, "img_url" : img_url}
    hemisphere_img_urls.append(hemisphere)

    #tells the browser to go back to the original page to search for title again
    browser.back()

    #print out dictionary
    hemisphere_img_urls

    # Store data in a dictionary
    mars_data = {
    "news_title": news_title,
    "news_p": news_p,
    "featured_img": featured_img,
    "html_table" : html_table,
    "hemisphere_img_urls" : hemisphere_img_urls
    }

    mars_data

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


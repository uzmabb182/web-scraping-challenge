from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    #-------------------------------------------------------------------------
    # Visit JPL Mars Space Images - Featured Image
    #-------------------------------------------------------------------------
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Scrape page into Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get the featured page
    # @TODO: YOUR CODE HERE!

    image_url = soup.find_all('a', class_='showimg')[0]['href']
    featured_image_url = url + image_url
    
    #--------------------------------------------------------------------------
    # NASA Mars News
    #--------------------------------------------------------------------------

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrape page into Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the NASA Mars News title
    # @TODO: YOUR CODE HERE!

    news_title = soup.find_all('div', class_='content_title')[0].text

    # Get the NASA Mars News paragraph
    # @TODO: YOUR CODE HERE!

    news_para = soup.find_all('div', class_='article_teaser_body')[0].text

    #--------------------------------------------------------------------------
    # NASA Mars Facts
    #--------------------------------------------------------------------------

    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Scrape page into Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the NASA Mars facts
    # @TODO: YOUR CODE HERE!

    Mars_table = pd.read_html(url)
    df = Mars_table[0]
    df.reset_index(inplace = True) 
    df.columns = ['Id', 'Specifications', 'Mars', 'Earth']
    html_table = df.to_html()
    html_table = html_table.replace('\n', '') 

    #--------------------------------------------------------------------------
    # NASA Mars Hemispheres
    #--------------------------------------------------------------------------

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Scrape page into Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the NASA Mars hemispheres data
    # @TODO: YOUR CODE HERE!

    results1 = soup.find_all('div', class_='description')
    title = []  
    img_url = []
    

    for result in results1:
        # Identify and return href (eg:cerberus.html, schiaparelli.html, syrtis.html, valles.html)
        relative_image_path = result.find('a')['href']
        print(relative_image_path)
        browser.visit(url + relative_image_path)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image_title = soup.find('h2', class_="title").text
        print(image_title)
        results2 = soup.find('div', class_="wide-image-wrapper" )
        image_link = results2.find('a')['href']
        full_image_link = url + image_link 
        #full_image_link = browser.click_link_by_href(full_image_link)
        print(full_image_link)
        title.append(image_title)
        img_url.append(full_image_link)
        # Store data in a dictionary
    hemisphere_data = {
        "image_title": image_title,
        "full_image_link": full_image_link
        }


    # Store data in a dictionary
    mars_data = {
        "featured_image_url": featured_image_url,
        "news_title": news_title,
        "news_para": news_para,
        "html_table": html_table,
        "title": title,
        "img_url": img_url 
    }

    # Quite the browser after scraping
    browser.quit()

    # Return results
    return mars_data

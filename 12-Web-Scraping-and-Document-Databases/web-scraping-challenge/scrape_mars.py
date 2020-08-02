from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd


scraped_dict = {}

def init_browser():
  executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
  return Browser('chrome', **executable_path, headless=False)

def marsNews():
  try:
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    news_soup = BeautifulSoup(html, 'lxml')
    
    titles = news_soup.find_all('div', class_="content_title")
    p = news_soup.find_all('div', class_="article_teaser_body")
    first_title = ""
    for title in titles:
      if title.a:
        first_title = title
        break
    news_title = first_title.a.text.strip()
    news_p = p[0].text.strip()
    
    scraped_dict['news_title'] = news_title
    scraped_dict['news_p'] = news_p

    return scraped_dict

  finally:
    browser.quit()

def marsSpaceImages():
  try: 
    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    image_soup = BeautifulSoup(html, "lxml")
    image = image_soup.find_all(class_="carousel_item")
    featured_image_url = 'https://www.jpl.nasa.gov' + image[0]["style"].split(" ")[1].split("'")[1]
    
    scraped_dict['featured_image_url'] = featured_image_url

    return scraped_dict

  finally:
    browser.quit()




def marsWeather():
  try:
    browser = init_browser()

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    weather_soup = BeautifulSoup(html, 'lxml')
    mars_weather = weather_soup.find_all("span")
    mars_weather_tweet = ""
    for tweet in mars_weather:
      if tweet.text:
        if "InSight sol" in tweet.text:
          mars_weather_tweet = tweet.text
          break
    scraped_dict['mars_weather_tweet'] = mars_weather_tweet

    return scraped_dict

  finally:
    browser.quit()




def marsFacts():
  try: 
    browser = init_browser()

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html
    fact_soup = BeautifulSoup(html, 'lxml')
    table = pd.read_html(url)
    df = table[0]
    df.columns = ['Attribute', 'Value']
    scraped_dict["mars_facts"] = df.to_html()

    return scraped_dict
    

  finally:
    browser.quit()





def marsHemispheres():
  try:
    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'lxml')
    items = hemisphere_soup.find_all('div', class_='item')
    hemisphere_image_urls = []

    for item in items:
      title = item.find('h3').text
      link = item.find('a', class_="itemLink")['href']
      hemisphere_link = "https://astrogeology.usgs.gov" + link
      browser.visit(hemisphere_link)
      hemisphere_html = browser.html
      new_soup = BeautifulSoup(hemisphere_html, 'lxml')
      image = new_soup.find('img', class_="wide-image")['src']
      img_url = "https://astrogeology.usgs.gov"+ image
      hemisphere_image_urls.append({"title": title, "image_url":img_url})

      scraped_dict["hemisphere_image_urls"] = hemisphere_image_urls

    return scraped_dict

  finally:
    browser.quit()
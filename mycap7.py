import requests
from bs4 import Beautifulsoup
import pandas
url="https://www.oyorooms.com/hotels-in-bangalore/"
max_page_num=3
scraped_list=[]
for page_num in range(1,max_page_num):
    req=requests.get(url,str(page_num))
    content=req.content
    soup=Beautifulsoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class": "hotelcardlisting"})
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class" :"listinghoteldescription_hotelname"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop": "streetaddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"hotelrating_ratingsummary"}).text
        try:
            hotel_dict["rating"]=hotel.find("span", {"class":"hotelrating_ratingsummary"}).text
        except AttributeError:
            pass
            parent_amentities_element=hotel.find("div", {"class": "amenitywrapper"})
            amentities_list=[]
            for amenity in parent_amenities_elements.find_all("div", {"class": "amenitywrapper_amenity"}):
                amenities_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())
                hotel_dict["amenities"]=', '.join(amenities_list[:-1])
                scraped_info_list.append(hotel_dict)
dataFrame=pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv("oyo.csv")

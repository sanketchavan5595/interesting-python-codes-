from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from tqdm import tqdm
# import lxml

def TripAdvisorScrape(pages, fileName):
    numpages = pages * 50

    # lists
    titles = []
    reviews = []
    bedrooms = []
    bathrooms = []
    sleeps = []
    location = []


    for i in tqdm(range(0, numpages, 50)):

        url = 'https://www.tripadvisor.in/VacationRentals-g186338-Reviews-oa{}-London_England-Vacation_Rentals.html'.format(i)
        page = requests.get(url)
        time.sleep(5)
        soup = BeautifulSoup(page.text, 'lxml')

        homes = soup.find_all('div', attrs={'class': '_1L5PA1gU'})
        for home in homes:
            title = home.find('a', class_='_2K0y-IXo').text
            titles.append(title)

            try:
                reviews.append(home.find('span', attrs={'class': '_16Nxw4iy'}).text)
            except:
                reviews.append('not reviewed')

            try:
                location.append(home.find('div', class_='_3bBwqjUk').text)
            except:
                location.append('not available')

            for h in home.find_all('div', class_='M1tanZPN'):
                try:
                    if 'bathroom' in h.text:
                        bathrooms.append(h.text)
                except:
                    bathrooms.append('no bathrooms')

                try:
                    if 'bedroom' in h.text:
                        bedrooms.append(h.text)
                except:
                    bedrooms.append('no bedrooms')

                try:
                    if 'Sleep' in h.text:
                        sleeps.append(h.text)
                except:
                    sleeps.append('no sleeps')


        # print(f'page number: {int(i/50) + 1} done....')


    d = {
        'titles': titles,
        'reviews': reviews,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sleeps': sleeps,
        'location': location
    }
    print('COMPLETED!!!')
    final_name = fileName + '.csv'
    return pd.DataFrame(d).to_csv(final_name)


number_of_pages = int(input("Enter the number of pages you want to scrape: "))
filename = input("Enter the name of final output file: ")
if __name__ == '__main__':
    TripAdvisorScrape(number_of_pages, filename)
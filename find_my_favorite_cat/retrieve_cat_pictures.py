import os
import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


class BOULDER_HUMANE_SOCIETY:

    def __init__(self, website):

        self.downloadDirectory = 'data/BHS_{date}'.format(date=datetime.datetime.today().strftime('%Y%m%d'))
        if not os.path.exists(self.downloadDirectory):
            os.system('mkdir -p {directory}'.format(directory=self.downloadDirectory))
        else:
            os.system('rm -rf {directory}/*'.format(directory=self.downloadDirectory))

        html = urlopen(website)
        bs   = BeautifulSoup(html.read(), 'html.parser')

        website = 'https://www.boulderhumane.org'
        catUrlItems = bs.findAll('a', {'title':'Adopt Me!'})
        catUrls = []
        for item in catUrlItems:
            catUrls.append(website+item['href'])

        html0 = urlopen(catUrls[0])
        bs0   = BeautifulSoup(html0.read(), 'html.parser')
        item  = bs0.findAll('div', {'id':'petinfo'})[0]
        catName   = item.find('h2', {'class':'petname'}).get_text().replace('About', '').strip()
        catGender = item.find('h2', {'class':'petname'}).get_text().replace('About', '').strip()
        catImages = item.find('div', {'id':'petpics'}).findAll(src=True)
        print(catImages)
        # print(bs0)



        # catNameItems = bs.findAll('div', {'class':'views-field views-field-field-pp-animalname'})
        # catNames = []
        # for item in catNameItems:
        #     catNames.append(item.get_text().strip())

        # catAgeItems = bs.findAll('div', {'class':'views-field views-field-field-pp-age'})
        # catAges = []
        # for item in catAgeItems:
        #     catAges.append(item.get_text().replace('Age:', '').strip())

        # catPrimaryBreedItems = bs.findAll('div', {'class':'views-field views-field-field-pp-primarybreed'})
        # catPrimaryBreeds = []
        # for item in catPrimaryBreedItems:
        #     catPrimaryBreeds.append(item.get_text().strip())

        # catSecondaryBreedItems = bs.findAll('div', {'class':'views-field views-field-field-pp-secondarybreed'})
        # catSecondaryBreeds = []
        # for item in catSecondaryBreedItems:
        #     catSecondaryBreeds.append(item.get_text().strip())

        # catGenderItems = bs.findAll('div', {'class':'views-field views-field-field-pp-gender'})
        # catGenders = []
        # for item in catGenderItems:
        #     catGenders.append(item.get_text().replace('Sex:', '').strip())

        # catImageUrlItems = bs.findAll('img', {'title':'Adopt Me'})
        # catImageUrls = []
        # for item in catImageUrlItems:
        #     catImageUrls.append(item['src'])



        # print(catNames)
        # print(catAges)
        # print(catPrimaryBreeds)
        # print(catSecondaryBreeds)
        # print(catGenders)
        # print(catImageUrls)


        # downloadList = self.CREATE_DOWNLOAD_LIST()
        # for key in downloadList.keys():
        #     print(key, downloadList[key])


    def CREATE_DOWNLOAD_LIST(self, keyWord='https://g.petango.com'):
        downloadList = {}
        i = 1
        for item in self.bs.findAll(src=True):
            catDict = {}
            if keyWord in item['src']:
                catDict['image_url'] = item['src']
                downloadList['cat_{index}'.format(index=str(i).zfill(4))] = catDict
                i += 1
        return downloadList





def getAbsoluteURL(baseUrl, source):

    pass






if __name__ == '__main__':
    website = 'https://www.boulderhumane.org/animals/adoption/cats'
    cat_web1 = BOULDER_HUMANE_SOCIETY(website)

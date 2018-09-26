import os
import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


class BOULDER_HUMANE_SOCIETY:

    def __init__(self):

        self.downloadDirectory = 'data/BHS_{date}'.format(date=datetime.datetime.today().strftime('%Y%m%d'))
        if not os.path.exists(self.downloadDirectory):
            os.system('mkdir -p {directory}'.format(directory=self.downloadDirectory))

        website = 'https://www.boulderhumane.org'
        websiteCat = website + '/animals/adoption/cats'
        html = urlopen(websiteCat)
        bs   = BeautifulSoup(html.read(), 'html.parser')

        catUrlItems = bs.findAll('a', {'title':'Adopt Me!'})
        catUrls = []
        for item in catUrlItems:
            catUrls.append(website+item['href'])

        catNameItems = bs.findAll('div', {'class':'views-field views-field-field-pp-animalname'})
        catNames = []
        for item in catNameItems:
            catNames.append(item.get_text().strip())

        catAgeItems = bs.findAll('div', {'class':'views-field views-field-field-pp-age'})
        catAges = []
        for item in catAgeItems:
            catAges.append(item.get_text().replace('Age:', '').strip())

        catPrimaryBreedItems = bs.findAll('div', {'class':'views-field views-field-field-pp-primarybreed'})
        catPrimaryBreeds = []
        for item in catPrimaryBreedItems:
            catPrimaryBreeds.append(item.get_text().strip())

        catSecondaryBreedItems = bs.findAll('div', {'class':'views-field views-field-field-pp-secondarybreed'})
        catSecondaryBreeds = []
        for item in catSecondaryBreedItems:
            catSecondaryBreeds.append(item.get_text().strip())

        catGenderItems = bs.findAll('div', {'class':'views-field views-field-field-pp-gender'})
        catGenders = []
        for item in catGenderItems:
            catGenders.append(item.get_text().replace('Sex:', '').strip())

        catStatusItems = bs.findAll('div', {'class':'views-field-field-pp-splashtitle'})
        catStatus = []
        for item in catStatusItems:
            catStatus.append(item.get_text().strip())

        catImageUrlItems = bs.findAll('div', {'class':'views-field-field-pp-photo'})
        catImageUrls   = []
        catImageLocals = []
        for i, item in enumerate(catImageUrlItems):
            imageUrl   = item.find(src=True)['src']
            catImageUrls.append(imageUrl)
            imageLocal = '{fdir}/cat_{index}_{name}.png'.format(fdir=self.downloadDirectory, index=catUrls[i].split('/')[-1], name='-'.join(catNames[i].split()))
            catImageLocals.append(imageLocal)
            urlretrieve(imageUrl, imageLocal)

        catAll = {}
        for i, catName in enumerate(catNames):

            cat0 = {}
            cat0['name']        = catName
            cat0['sex']         = catGenders[i]
            cat0['age']         = catAges[i]
            cat0['breed']       = '\n'.join([catPrimaryBreeds[i], catSecondaryBreeds[i]]).strip()
            cat0['status']      = catStatus[i]
            cat0['image_url']   = catImageUrls[i]
            cat0['image_local'] = catImageLocals[i]
            cat0['url']         = catUrls[i]

            catAll['cat_{index}'.format(index=str(i).zfill(2))] = cat0

        self.cats = catAll





if __name__ == '__main__':

    cat_web = BOULDER_HUMANE_SOCIETY()

from bs4 import BeautifulSoup
import requests
import unittest

# Task 2: Look at the Get the URL that links to webpage of universities with Olympic medal wins
# search for the url in the University of Michgian wikipedia page (in the third pargraph of the intro)
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def getLink(soup):
    links = soup.find('a', title = 'List of American universities with Olympic medals')
    info = links.get('href')
    link_start = "https://en.wikipedia.org"
    #print(links)
    print(link_start + info)
    return link_start + info


# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.
def getAdmissionsInfo2019(soup):
    table = soup.find('table', class_ = "toccolours")
    trs = table.find_all('tr')
    
    for tr in trs[3:]:
        data = tr.find('td')
    
    

    school_dict = {}

        
    #print(table)
    



def main():
    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this

    #### YOUR CODE HERE####
    r = requests.get("https://en.wikipedia.org/wiki/University_of_Michigan")
    soup = BeautifulSoup(r.text, 'html.parser')

    #Call the functions getLink(soup) and getAdmissionsInfo2019(soup) on your soup object.
    getLink(soup)
    getAdmissionsInfo2019(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_link_nobel_laureates(self):
        self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')

    def test_admissions_info(self):
        self.assertEqual(getAdmissionsInfo2019(self.soup), {'Engineering': '1854', 
                                                            'Law': '1859',
                                                            'Dentistry': '1875', 
                                                            'Pharmacy': '1876', 
                                                            'Music, Theatre &Dance': '1880', 
                                                            'Nursing': '1893', 
                                                            'Architecture &Urban Planning': '1906', 
                                                            'Graduate Studies': '1912', 
                                                            'Government': '1914', 'Education': 
                                                            '1921', 'Business': '1924', 
                                                            'Environment andSustainability': '1927', 
                                                            'Public Health': '1941', 
                                                            'Social Work': '1951', 
                                                            'Information': '1969', 
                                                            'Art & Design': '1974', 
                                                            'Kinesiology': '1984'})

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
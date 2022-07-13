import requests

API_ENDPOINT = "https://www.wikidata.org/w/api.php"





def Search(query):
    try:
        params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': query
        }

        r = requests.get(API_ENDPOINT, params = params)

        return r.json()['search'][0]["description"]
    except:
        return "Not Found"

if __name__ == "__main__":
    query = "Python"

    print(Search(query))
    

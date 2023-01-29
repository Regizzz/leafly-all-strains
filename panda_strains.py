import requests
import pandas as pd
import time

url = "https://consumer-api.leafly.com/api/strain_playlists/v2"

strain_list = []

for x in range(0, 6360, 60):
    querystring = {"skip":str(x), "take":"60","sort[0][review_count]":"desc"}

    payload = ""
    headers = {
        # put your request headers here
    }

    # saving response from api to json object
    response_info = requests.request("GET", url, data=payload, headers=headers, params=querystring).json()

    # creating empty array and filling it with data from stored in response_info
    for strain_name in response_info['hits']['strain']:
        strain_list.append([strain_name['name'], str([strain_name['phenotype']])[2:-2], str([strain_name['reviewCount']])[1:-1], strain_name['topEffect'], strain_name['thc'], str(strain_name['subtitle'])[4:]])
    time.sleep(3)


# creating a pandas DataFrame
strain_df = pd.DataFrame(data=strain_list, columns=['Name', 'phenotype', 'reviewCount', 'topEffect', 'thc', 'subtitle'])

# printing out result
#print(strain_df)

# saving to csv with specific separator
strain_df.to_csv('top-most-reviewed-strains.csv', sep=' ')

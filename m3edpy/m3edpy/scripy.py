
import requests
import pdb
dataset_list_url = ("https://raw.githubusercontent.com/"
                    "daniilidis-group/m3ed/main/dataset_list.yaml")

dataset_list = requests.get(dataset_list_url).text
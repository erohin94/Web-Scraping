import requests
import pandas as pd

headers = {
"User-Agent" :	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
}
page = 1
params = {
    'page': page,
    'view': '90',
    'sort': '4',
    'q': 'hoodie',
    'pagetype': 'Shopping',
    'rootCategory': 'Men',
    'pricetype': 'FullPrice',
    'c-category': '136398',
}

response = requests.get(
    'https://www.farfetch.com/uk/plpslice/listing-api/products-facets',
    params = params,
    headers = headers,
)
items = response.json()["listingItems"]["items"]

brand_name = []
product_name = []
price_final = []
price_old = []

for i in items:
    brand_name.append(i['brand']['name'])
    product_name.append(i['shortDescription'])
    price_final.append(i['priceInfo']['finalPrice'])
    price_old.append(i['priceInfo']['initialPrice'])



df = pd.DataFrame({
    'brand_name' : brand_name,
    'product_name' : product_name,
    'price_final' : price_final,
    'price_old': price_old
})
df.to_excel('farfetch_men.xlsx')

    #print(f'--{i}--')
    #print(f"{x['shortDescription']} ({x['brand']['name']})")
    #print(x['priceInfo']['finalPrice'])
    #print(x['priceInfo']['initialPrice'])
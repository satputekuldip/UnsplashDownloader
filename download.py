import urllib
import requests
key = 'YOUR_UNSPLASH_API_KEY'
query = input("Enter Your Query: ")
orientations = ['landscape', 'portrait', 'squarish']
orientation_id = input("Enter Orientation number :\n0: landscape\n1: portrait\n2: squarish\nEnter number: ")
# print(orientations[int(orientation_id)])
url_query = urllib.parse.quote(query)
url = "https://api.unsplash.com/search/photos/?query={}&orientation={}&client_id={}".format(url_query,orientations[int(orientation_id)],key)
# print(url)
res = requests.get(url)

init_res_json = res.json()
# print(init_res_json)
print('Total Pages ' + str(init_res_json['total_pages']))
pages = input("How much pages You Want to download(1 page = 10 imgs): ")
check_android = input('is this Android Device :\n0: NO\n1: YES\nEnter Number(0 or 1): ')
download_path = "./"
if check_android == '1':
    download_path = '/storage/emulated/0/Download/'
else:
    download_path = input('Enter Full Download Path: ')

print('Downloading Images Please wait')
count = 0
for i in range(int(pages)):
    response = requests.get("https://api.unsplash.com/search/photos/?query={}&orientation={}&client_id={}&page={}".format(url_query,orientations[int(orientation_id)],key,str(i)))
    res_json = response.json()
    
    for img in res_json['results']:
        print( "Downloading image " + img['id'] + '.jpg')
        urllib.request.urlretrieve(img['urls']['regular'],download_path + img['id'] + '.jpg')
        count += 1

print('....')  
print(str(count) + " Images Downloaded...\nDownload Complete...")
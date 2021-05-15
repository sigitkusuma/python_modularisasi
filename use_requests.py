import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! {response.status_code}')
        print(f'Hasil {response.text}')
    else:
        print(f'Terdapat Kesalahan {response.status_code}')

except Exception as s:
    print('There is Error', s)
print('Program Ended')

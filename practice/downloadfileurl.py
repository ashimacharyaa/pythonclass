import requests
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path,'wb') as f:
        for chunk in response.iter_content(8192):
            f.write(chunk)

    print(f'Saved to {save_path}')

download_file('https://picsum.photos/200/300','my-image')




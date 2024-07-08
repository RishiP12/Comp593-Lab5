import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/doc_api'
API_DEV_KEY = '5lvd8TGcVgF4h1hLJkHSk3DKS3mD3a5D'

def post_new_paste(title, body_text, expiration='N', listed=True):
   

    params = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }
    
    
    print("Sending request to pastebin_api")
    response = requests.post(PASTEBIN_API_POST_URL, data=params)
    
    
    if response.status_code == 200 and response.text.startswith('https://'):
        print("Paste created successfully!")
        return response.text
    else:
        print("Failed to paste. Response status code:", response.status_code)
        print("Response text:", response.text)
        return None


if __name__ == "__main__":
    
    api_key = '5lvd8TGcVgF4h1hLJkHSk3DKS3mD3a5D'
    paste_url = post_new_paste("Test Paste", "This is a test paste.", "10M", True)
    if paste_url:
        print("Paste URL:", paste_url)
    else:
        print("Failed")

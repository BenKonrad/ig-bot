import os
import requests

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")

def post_to_instagram(image_url, caption):
    create_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    create_resp = requests.post(create_url, data=create_payload)
    creation_id = create_resp.json().get("id")

    if not creation_id:
        print("❌ Error creating media object:", create_resp.json())
        return

    print(f"✅ Media object created: {creation_id}")

    publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN
    }
    publish_resp = requests.post(publish_url, data=publish_payload)

    if publish_resp.status_code == 200:
        print("✅ Successfully posted to Instagram!")
    else:
        print("❌ Error publishing:", publish_resp.json())

if __name__ == "__main__":
    image_url = "https://i.imgur.com/0KFBHTB.jpeg"
    caption = "Posted from Railway ☁️ #RomanFiction"
    post_to_instagram(image_url, caption)

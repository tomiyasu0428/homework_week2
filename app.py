import requests
import time


def top_stories():

    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    if response.status_code != 200:
        print("Failed to top stories.")
        return []

    story_ids = response.json()
    return story_ids[:30]


def top_story_details(story_id):
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(story_url)
    if response.status_code != 200:
        print(f"Failed to top story details for ID: {story_id}")
        return None

    return response.json()


def main():
    story_ids = top_stories()

    for story_id in story_ids:
        story_details = top_story_details(story_id)
        if story_details:
            title = story_details.get("title", "No Title")
            link = story_details.get("url", "No URL")
            news_info = {"title": title, "link": link}
            print(news_info)

    for i in range(10):
        time.sleep(1)  #
        print(i)


if __name__ == "__main__":
    main()

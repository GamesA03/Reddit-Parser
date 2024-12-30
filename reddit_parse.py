import os

import praw
from praw.models import MoreComments
from typing import Optional
from llama_index.core.schema import Document
from dotenv import load_dotenv





# Load environment variables from .env file
load_dotenv()



def load_data(
    
    subreddits: list[str],
    search_keys: list[str],
    post_limit: Optional[int] = 10,
    #list changed from Document type to list type to ensure subscriptability when parsing for different elements 
    #such as titles, comments, etc, as well as to ensure a more visually appealing format when displaying each post
) -> (list[dict]):
    """
    Load text from relevant posts and top-level comments in subreddit(s), given keyword(s) for search.

    Args:
        subreddits (List[str]): List of subreddits you'd like to read from
        search_keys (List[str]): List of keywords you'd like to use to search from subreddit(s)
        post_limit (Optional[int]): Maximum number of posts per subreddit you'd like to read from, defaults to 10

    Returns:
        List[dict]: A list of dictionaries containing post titles, text, links, and top-level comments.

    """

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )


    posts = []

    for sr in subreddits:
        ml_subreddit = reddit.subreddit(sr)

        for kw in search_keys:
            relevant_posts = ml_subreddit.search(kw, limit=post_limit)

            for post in relevant_posts:
                #sub-list implemented to return better formatted details
                post_data = {
                    "title" : post.title,
                    "text" : post.selftext or "No text available",
                    "link": f"https://www.reddit.com{post.permalink}",
                    "comments": []
                }
                #posts.append(Document(text=post.selftext))
                #changed from posting full selftext of document to iterating through a list of each comment
                for top_level_comment in post.comments:
                    if isinstance(top_level_comment, MoreComments):
                        continue
                    post_data["comments"].append(top_level_comment.body or "No comment text available")

                posts.append(post_data)


    return posts
    

if __name__ == "__main__":
    #topicInput = input("Enter subreddit topics you would like to select: ")
    #topics = topicInput.split(",")
    #keyInput = input("Enter keywords you would like to search: ")
    #keys = keyInput.split(",")
    #postNumInput = input("Enter the number of posts you would like to limit to:")

    #Need to work on more user-friendly way of allowing people to input keywords and subreddits, will bookmark for later
    subreddits = ["cryptocurrency", "Bitcoin"]
    #subreddits = [topics]
    search_keys = ["Bitcoin", "NFTs","Crypto News" ]
    #search_keys = [keys ]
    post_limit = 3

    posts = load_data(subreddits=subreddits, search_keys=search_keys, post_limit=post_limit)
    #print(f"Fetched {len(documents)} documents:")
    #for i, doc in enumerate(documents):
        #print(f"Document {i + 1}: {doc.text[:200]}")  # Print first 200 characters of each document
    print(f"\nFetched {len(posts)} posts:")
    print("=" * 80)

    for i, post in enumerate(posts):
        #For loop for iterating through posts list, print values below print out a basic-formatted approximation of a reddit post
        print(f"Post {i + 1}")
        print("-" * 80)
        print(f"Title: {post['title']}")
        print(f"Link: {post['link']}")
        print(f"Text: {post['text'][:500]}")  # Limit post text to 500 characters
        print("\nTop-Level Comments:")
        if post["comments"]:
            for j, comment in enumerate(post["comments"], start=1):
                print(f"  {j}. {comment[:300]}")  # Limit comment text to 300 characters, may be worth changing to allow user to choose how much they want to limit comment text
        else:
            print("  No top-level comments available.")
        print("=" * 80)

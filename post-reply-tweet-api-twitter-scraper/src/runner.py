thonimport json
import os
from extractors.tweet_parser import parse_tweet
from extractors.utils import load_cookie
from outputs.exporters import export_to_file

def main():
    # Load the Twitter cookie (authentication)
    cookie = load_cookie("cookie.txt")
    
    # Load tweet content from an example file or predefined list
    tweet_data = parse_tweet("data/inputs.sample.txt")
    
    # Export the tweet content (for example, save to a JSON file)
    export_to_file(tweet_data, "output.json")
    
if __name__ == "__main__":
    main()
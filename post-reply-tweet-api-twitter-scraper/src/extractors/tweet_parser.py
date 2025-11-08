thonimport re

def parse_tweet(file_path):
    """
    Parse the tweet content from the given file and return as a structured list.
    """
    tweet_data = []
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            # Example of extracting tweet content and media URL
            if "tweetContent" in line:
                tweet_content = line.strip()
                media_url = extract_media_url(line)
                tweet_data.append({
                    "tweetContent": tweet_content,
                    "mediaUrl": media_url
                })
    
    return tweet_data

def extract_media_url(line):
    """
    Extract the media URL from the tweet line.
    """
    match = re.search(r'(https?://[^\s]+)', line)
    return match.group(0) if match else ""
import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    # 1. Fetch the HTML content
    # We add a 'User-Agent' header so the website doesn't block us as a bot
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check for errors
        
        # 2. Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. Find headlines (most news sites use h2 or h3 for top stories)
        headlines = soup.find_all(['h2', 'h3'])
        
        # Clean and store unique headlines
        unique_headlines = set()
        for h in headlines:
            text = h.get_text().strip()
            if len(text) > 10: # Filter out short menu items or navigation
                unique_headlines.add(text)
        
        # 4. Save to a .txt file
        with open("headlines.txt", "w", encoding="utf-8") as f:
            for i, title in enumerate(unique_headlines, 1):
                f.write(f"{i}. {title}\n")
        
        print(f"Successfully saved {len(unique_headlines)} headlines to headlines.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (You can change this to a specific news URL)
if __name__ == "__main__":
    target_url = "https://www.bbc.com/news"
    scrape_news(target_url)

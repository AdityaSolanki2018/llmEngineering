import requests

from bs4 import BeautifulSoup
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    """
    A utility class to represent a Website that we have scraped, now with links
    """

    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)   #to download the HTML content of a webpage.
        self.body = response.content                    # .content gives you the raw HTML (in bytes), like the source code of the page.
        soup = BeautifulSoup(self.body, 'html.parser')  # This turns the raw HTML into a soup object so you can easily search for tags like <title>, <a>, <body>

        # This gets the content inside the <title> tag of the webpage. If there's no title, it gives "No title found" instead.
        self.title = soup.title.string if soup.title else "No title found"   
        
        # If there's a <body> tag, this loop removes unnecessary parts like: <script>: JavaScript code, <style>: CSS, <img>: Images, <input>: Form inputs.
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)        # This extracts all readable text from the cleaned-up <body>, with each block of text on a new line.
        else:
            self.text = ""
            
        # Finds all <a> tags (which define links). Grabs their href attribute (which holds the actual URL). Filters out any None values or empty links.    
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"
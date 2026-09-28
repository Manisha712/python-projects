import pandas as pd
import requests # pip install requests
import io
url = "https://chandoo.org/wp/wp-content/uploads/2022/09/hotel-booking-data.txt"
# 1. Pretend to be a real web browser (Chrome)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# 2. Fetch the text from the web page
response = requests.get(url, headers=headers)
# 3. Pass the fetched raw text into Pandas
df = pd.read_csv(io.StringIO(response.text), sep="\t")
# sep="\t" tells Pandas that columns are separated by tabs
print(df.head())
#headers: Tricking the web server into thinking a human opened the link in Google Chrome.
#io.StringIO(): Converts the raw web text into a virtual file stream so pd.read_csv can
# process it as if it were a local .txt or .csv file on your hard drive.
print("\nShape:", df.sh)
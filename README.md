# Medium articles scrapper (``medium_scrapper`` library)

Library for scrapping articles with the medium using Selenium and BeautifulSoup

## Motivation
* limit on the number of articles per day without a subscription
* inability to pay for a subscription from some regions
* lack of data for analysis
---

* [Setup](#step1)
* [Usage](#step2)
* [Methods](#step3)
* [ToDo List](#step4)


<a name = "step1"></a>
# Setup
1. Open cmd (Win+R)
2. Write the command below:
```
pip install medium_scrapper
```
3. Run the code (like in [Usage](#step2))

<a name = "step2"></a>
# Usage

```python
from medium_scrapper import scrap_articles_async_list, get_desired_options, get_colunmns
import pandas as pd

links = ['https://medium.com/swlh/handling-exceptions-in-python-a-cleaner-way-using-decorators-fae22aa0abec',
         'https://medium.com/codex/say-goodbye-to-loops-in-python-and-welcome-vectorization-e4df66615a52',
         'https://medium.com/geekculture/hey-chatgpt-solve-these-coding-tasks-using-python-b2e7482f2c18',
         'https://medium.com/@markwschaefer/20-entertaining-uses-of-chatgpt-you-never-knew-were-possible-3bc2644d4507',
         'https://medium.com/bitsrc/i-asked-chat-gpt-to-build-a-to-do-app-have-we-finally-met-our-replacement-ad347ad74c51'            
]

options = get_desired_options()
scrap_articles_async_list(links, options, path="./table.csv")
pd.read_csv("table.csv", names=get_columns())

```
<a name = "step3"></a>
# Arguments
| Method | Type | Arguments |Description |
| :---         |     :---:      |     :---:      |          :--- |
| `scrape` | Public | soup: `BeautifulSoup`, link: `str` | The function that calls all other private methods to scrape several fields |
| `get_pure_text_` | Public | link: `str`, options: `webdriver.edge.options` | The separate function to scrape only the full text of the article. |
| `scrape_page` | Public | link: str, options: webdriver.edge.options, csv_writer, compare: bool, idle_row: pd.Series | The function that creates a webdriver, sends a request and scrapes per one link. |
| `scrap_articles_csv` | Public | df: pd.DataFrame, options: webdriver.edge.options, rows: int, path: str | The function that takes links from an existing dataframe and scrapes everything into a separate dataframe |
| `scrap_articles_async` | Public | df:`pd.DataFrame`, options, columns:`list`, pools:`int`, path:`str` | The function that asynchronously takes links from an existing dataframe and scrapes everything into a separate dataframe |
| `scrap_articles_async_list` | Public | links: `list`, options, columns:`list`, pools:`int`, path:`str` | The function that asynchronously takes links from an given lists and scrapes everything into a separate dataframe |
| `__get_title` | Private | soup: `BeautifulSoup` | The function that collects the title of an article from its ``lxml`` parse |
| `__get_subtitle` | Private | soup: `BeautifulSoup` | The function that collects the subtitle of an article from its ``lxml`` parse |
| `__get_publication` | Private | soup: `BeautifulSoup` | The function that collects the publication type of an article from its ``lxml`` parse |
| `__get_author` | Private | soup: `BeautifulSoup` | The function that collects the author of an article from its ``lxml`` parse |
| `__get_reading_time` | Private | soup: `BeautifulSoup` | The function that collects the reading time required for an article from its ``lxml`` parse |
| `__get_claps` | Private | soup: `BeautifulSoup` | The first function that collects the claps count of an article from its ``lxml`` parse |
| `__get_claps2` | Private | link: `str` | The second type of function that collects the claps count of an article by simple request. |
| `__get_responses` | Private | soup: `BeautifulSoup` | The function that collects the responses count of an article from its ``lxml`` parse |
| `__get_date` | Private | soup: `BeautifulSoup` | The first function that collects the date an article was published from its ``lxml`` parse |
| `__get_followers` | Private | soup: `BeautifulSoup` | The function that collects the number of subscribers per article author from its ``lxml`` parse |
| `__get_mean_size` | Private | soup: `BeautifulSoup` | The function that calculates the average size of photos of an article html page its ``lxml`` parse. |
| `__count_figures` | Private | soup: `BeautifulSoup` | The function that counts the number of images on an article page from its ``lxml`` parse |
| `__get_pure_text` | Private | soup: `BeautifulSoup` | The function that collects the full text of an article from its ``lxml`` parse |
| `__count_words` | Private | soup: `BeautifulSoup` | The function that counts the words and syntax of an article from its ``lxml`` parse |
| `__count_lists` | Private | soup: `BeautifulSoup` | The function that counts the markered lists (bullet lists) of an article from its ``lxml`` parse |
| `__bold_text_count` | Private | soup: `BeautifulSoup` | The function that counts the number of blocks of bold text of an article from its ``lxml`` parse |
| `__italic_text_count` | Private | soup: `BeautifulSoup` | The function that counts the number of blocks of italic text of an article from its ``lxml`` parse |
| `__count_vids` | Private | soup: `BeautifulSoup` | The function that counts the number of videos on an article page from its ``lxml`` parse |
| `__count_links` | Private | soup: `BeautifulSoup` | The function that collects the number of references in an article from its ``lxml`` parse |
| `__count_code_chunks` | Private | soup: `BeautifulSoup` | The function that collects the number of code chunks in an article from its ``lxml`` parse |


<a name = "step4"></a>

# ToDo List

- [ ] Extrapolate for different webdrivers (Chrome, Explorer)
- [ ] Make the writer ster more mobile

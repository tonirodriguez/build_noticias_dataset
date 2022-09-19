# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['keywords', 'r', 'results', 'ddg_news', 'ddg']

# %% ../00_core.ipynb 4
from duckduckgo_search import ddg
from duckduckgo_search import ddg_news

# %% ../00_core.ipynb 5
def ddg_news(keywords, region='wt-wt', safesearch='Moderate', time=None, max_results=25, output=None):
    """DuckDuckGo news search

    Args:
        keywords: keywords for query.
        region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2). Defaults to "Moderate".
        time: 'd' (day), 'w' (week), 'm' (month). Defaults to None.
        max_results: maximum DDG_news gives out 240 results. Defaults to 25.
        output: csv, json, print. Defaults to None.

    Returns:
        DuckDuckGo news search results.
    """

# %% ../00_core.ipynb 6
keywords = "russia invasion ukraine"
r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='d', max_results=100)
print(r)

# %% ../00_core.ipynb 7
def ddg(keywords, region='wt-wt', safesearch='Moderate', time=None, max_results=25, output=None):
    """DuckDuckGo text search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str, optional): country - wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str, optional): On(kp=1), Moderate(kp=-1), Off(kp=-2). Defaults to "Moderate".
        time (str, optional): 'd' (day), 'w' (week), 'm' (month), 'y' (year). Defaults to None.
        max_results (int, optional): return not less than max_results, max=200. Defaults to 25.
        output (str, optional): csv, json, print. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo text search results.
    """

# %% ../00_core.ipynb 8
keywords = 'Bella Ciao'
results = ddg(keywords, region='wt-wt', safesearch='Moderate', time='y', max_results=25)
print(results)

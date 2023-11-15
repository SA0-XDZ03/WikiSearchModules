""" pip install wikipedia """
""" To build a Python program that uses the Wikipedia API to search for a specific topic, you will need to do the following:
Install the wikipedia library, which is a Python wrapper for the Wikipedia API. You can do this by running the following command: 
Import the wikipedia library and use it to search for articles on Wikipedia that match a specific search term.
"""
import wikipedia

searchInput = input("Enter Search: ")

def search_wikipedia(search_term):
    search_results = wikipedia.search(search_term)
    for result in search_results:
        print(result)

search_wikipedia(searchInput)

""" This code will print a list of Wikipedia articles that match the search term "python".
To get more information about a specific Wikipedia article, you can use the wikipedia.page() function to retrieve the content of the article. """
import wikipedia

def get_wikipedia_article(article_title):
    article = wikipedia.page(article_title)
    print(article.title)
    print(article.summary)

get_wikipedia_article(searchInput)

""" This code will print the title and summary of the Wikipedia article with the title "Python (programming language)".
This is a basic example of how you can use the Wikipedia API with Python to search for and retrieve information from Wikipedia articles. You can customize the search by specifying additional parameters, such as the language of the articles to search in or the number of results to return. For more information on the available options, you can refer to the wikipedia documentation. """
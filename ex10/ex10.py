##################################################
#  FILE: ex10.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex10 2015-2016
#  DESCRIPTION : 
#
##################################################


def read_article_links(file_name='links_demo.txt'):
    """
    Reads a list of articles from a file and returns a tuple
    :param file_name: file path as string
    :return: list of tuples of articles
    """
    with open(file_name, 'r') as file:
        return [tuple(article.strip() for article in articles.split('\t'))
                for articles in file.readlines()]

class Article:
    """
    Article object definition
    """
    def __init__(self, name):
        self.name = name
        self.article_collection = []

    def get_name(self):
        return self.name

    def add_neighbor(self, neighbor):
        pass

    def get_neighbors(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def __contains__(self, article):
        pass

class WikiNetwork:
    """
    WikiNetwork object definition
    """
    def __init__(self, link_list=[]):
        self.link_lst = link_list

    def update_network(self, link_list):
        pass

    def get_articles(self):
        pass

    def get_titles(self):
        pass

    def __contains__(self, article_name):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def __getitem__(self, article_name):
        pass
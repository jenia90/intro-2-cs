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
        self.__name = name
        self.__neighbors = set()

    def get_name(self):
        return self.__name

    def add_neighbor(self, neighbor):
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        return self.__neighbors

    def __repr__(self):
        return str(self.__name) + str([neighbor for neighbor in self.__neighbors])

    def __len__(self):
        return len(self.__neighbors)

    def __contains__(self, article):
        return True if article in self.__neighbors else False


class WikiNetwork:
    """
    WikiNetwork object definition
    """
    def __init__(self, link_list=[]):
        self.__article_dict = self.__create_network(link_list)
        print(self.__article_dict)
        # set(self.__add_article(article, neighbor)
        #                         for article, neighbor in link_list)

    def __create_network(self, links_list=[]):
        article_dict = {Article(article): neighbor
                               for article, neighbor in links_list}
        print({article.add_neighbor(neighbor): neighbor
                for article, neighbor in article_dict.items()})

        for article, neighbor in article_dict.items():
            del article_dict[article]
            article = article.add_neighbor(neighbor)
            article_dict[article] = neighbor
            #TODO: Finish implementation

        return {article.add_neighbor(neighbor): neighbor
                for article, neighbor in article_dict.items()}



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

WikiNetwork(read_article_links())
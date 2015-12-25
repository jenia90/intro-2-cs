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
        """
        Initializes the WikiNetwork object
        :param link_list: a linked list of articles as tuple
        """
        self.__article_dict = self.__create_network(link_list)

    def __create_network(self, links_list=[]):
        article_dict = {}
        article_obj_list_temp = [(Article(article), neighbor)
                               for article, neighbor in links_list]

        for article, neighbor in article_obj_list_temp:
            article.add_neighbor(neighbor)
            article_dict[article] = neighbor

        return article_dict

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

    def page_rank(self, iters, d=0.9):
        pass

    def jaccard_index( self , article_name):
        pass

    def travel_path_iterator(self, article_name):
        pass

    def friends_by_depth(self, article_name, depth):
        pass


WikiNetwork(read_article_links())
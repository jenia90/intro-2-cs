##################################################
#  FILE: ex10.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex10 2015-2016
#  DESCRIPTION : 
#
##################################################


def read_article_links(file_name='links.txt'):
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
        """

        :param name:
        """
        self.__name = str(name)
        self.__neighbors = set()

    def get_name(self):
        """

        :return:
        """
        return self.__name

    def add_neighbor(self, neighbor):
        """

        :param neighbor:
        """
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        """

        :return:
        """
        return self.__neighbors

    def __repr__(self):
        """

        :return:
        """
        return self.__name, str([n for n in self.__neighbors])

    def __len__(self):
        """

        :return:
        """
        return len(self.__neighbors)

    def __contains__(self, article):
        """

        :param article:
        :return:
        """
        return  article in self.__neighbors


class WikiNetwork:
    """
    WikiNetwork object definition
    """
    def __init__(self, link_list=[]):
        """
        Initializes the WikiNetwork object
        :param link_list: a linked list of articles as tuple
        """
        self.__article_dict = {}
        self.update_network(link_list)

    def update_network(self, link_list):
        """
        Updates the WikiNetwork database according to the passed in list of
        links
        :param link_list: list of links as tuple
        :type tuple(article_name, neighbor)
        """
        for article, neighbor in link_list:
            if article not in self.__article_dict:
                self.__article_dict[article] = Article(article)
            self.__article_dict[article].add_neighbor(neighbor)

    def get_articles(self):
        """

        :return:
        """
        return [article.get_neighbors() for article in self.__article_dict.values()]

    def get_titles(self):
        """

        :return:
        """
        return self.__article_dict.keys()

    def __contains__(self, article_name):
        """

        :param article_name:
        :return:
        """
        return article_name in self.get_titles()

    def __len__(self):
        """

        :return:
        """
        return len(self.__article_dict)

    def __repr__(self):
        """

        :return:
        """
        return str({key: value.__repr__()
                for key, value in self.__article_dict.items()})

    def __getitem__(self, article_name):
        """

        :param article_name:
        :return:
        """
        if self.__contains__(article_name):
            return self.__article_dict[article_name]
        else:
            raise KeyError(article_name)


    def page_rank(self, iters, d=0.9):
        return self.__page_rank_helper(iters, d)

    def __page_rank_helper(self, iters, d, ranked_dict={}):
        if iters == 0:
            return ranked_dict

        else:
            pass
            # ranked_dict =

    def jaccard_index( self , article_name):
        pass

    def travel_path_iterator(self, article_name):
        pass

    def friends_by_depth(self, article_name, depth):
        pass

print(WikiNetwork(read_article_links()))
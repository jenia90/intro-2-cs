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
        return self.__name, [n for n in self.__neighbors]

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
        for article, neighbor in link_list:
            pass # TODO: Finish implementation!

        '''
        for article, neighbor in link_list:
            if article in self.__article_dict.keys():
                self.__article_dict[article].append(neighbor)
            else:
                self.__article_dict[article] = []

        for article in self.__article_dict.keys():
            art = Article(article)
            for neighbor in self.__article_dict[article]:
                if not art.__contains__(neighbor):
                    art.add_neighbor(neighbor)

            self.__article_dict[art] = self.__article_dict.pop(article)
        '''

    def get_articles(self):
        return [article.get_neighbors() for article in self.__article_dict.keys()]

    def get_titles(self):
        return [article.get_name() for article in self.__article_dict.keys()]

    def __contains__(self, article_name):
        return article_name in self.get_titles()

    def __len__(self):
        return len(self.__article_dict)

    def __repr__(self):
        return str({article.get_name(): article.__repr__()
                for article in self.__article_dict.keys()})

    def __getitem__(self, article_name):
        if self.__contains__(article_name):
            return self.__article_dict.fromkeys()

    def page_rank(self, iters, d=0.9):
        pass

    def jaccard_index( self , article_name):
        pass

    def travel_path_iterator(self, article_name):
        pass

    def friends_by_depth(self, article_name, depth):
        pass


print(WikiNetwork(read_article_links()))
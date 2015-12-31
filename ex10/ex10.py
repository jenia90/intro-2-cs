##################################################
#  FILE: ex10.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex10 2015-2016
#  DESCRIPTION : WikiNetwork basic implementation exercise
#
##################################################


def read_article_links(file_name='links.txt'):
    """
    Reads a list of articles from a file and returns a tuple
    :param file_name: file path as string
    :return: list of tuples of articles and their neighbors
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
        Initializes the Article class
        :param name:
        """
        self.__name = str(name)
        self.__neighbors = set()

    def get_name(self):
        """
        Gets the name of the article object
        :return:
        """
        return self.__name

    def add_neighbor(self, neighbor):
        """
        Adds neighbor of type Article to the article object
        :param neighbor: neighbor Article object
        :type Article:
        """
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        """
        Gets list of all neighbors
        :return: returns a list of all neighboring Article objects
        """
        return list(self.__neighbors)
       
    def get_neighbors_names(self):
        """
        Gets the names of all neighbor Article objects
        :return: returns set of article names as strings
        """
        return set(neighbor.get_name() for neighbor in self.__neighbors)

    def __repr__(self):
        """
        Override of the __repr__ method
        :return: string representing the article name and it's article neighbors
        """
        return str((self.__name, list(self.get_neighbors_names())))

    def __len__(self):
        """
        Override of the len method
        :return: returns number of neighboring articles
        """
        return len(self.__neighbors)

    def __contains__(self, article):
        """
        Override of the __contains__ method
        :param article: article in question
        :type Article:
        :return: True if Article in neighbors else False
        """
        return article in self.get_neighbors()


class WikiNetwork:
    """
    WikiNetwork object definition
    """
    def __init__(self, link_list=[]):
        """
        Initializes the WikiNetwork object
        :param link_list: a linked list of articles as tuple
        :type tuple():
        """
        # creates a dictionary to hold the article network
        self.__article_dict = {}

        # updates the networkd according to the link_list
        self.update_network(link_list)

    def update_network(self, link_list):
        """
        Updates the WikiNetwork database according to the passed in list of
        links
        :param link_list: list of links as tuples
        :type list():
        """
        for article, neighbor in link_list:
            # if the article already in dictionary gets the object else
            # creates a new Article object
            article_obj = self.__article_dict.get(article, Article(article))

            # adds the object to the dictionary if it's not there
            if article not in self:
                self.__article_dict[article] = article_obj

            # same as with article but about the neighbor object
            neighbor_obj = self.__article_dict.get(neighbor, Article(neighbor))
            if neighbor not in self:
                self.__article_dict[neighbor] = neighbor_obj

            # adds the neighbor to the article object
            self.__article_dict[article].add_neighbor(neighbor_obj)

    def get_articles(self):
        """
        Gets a list of all Article objects in the dictionry
        :return: list of Article objects
        """
        return list(self.__article_dict.values())

    def get_titles(self):
        """
        Gets a list of names of Articles
        :return: list of strings representing the names of articles in dictionary
        """
        return list(self.__article_dict.keys())

    def __contains__(self, article_name):
        """
        Overrides the __contains__ method
        :param article_name: article in question
        :return: True if article in network else False
        """
        return article_name in self.__article_dict

    def __len__(self):
        """
        Overrides the __len__ method
        :return: Number of articles in the network
        """
        return len(self.__article_dict)

    def __repr__(self):
        """
        Overrides the __repr__ method
        :return: string of all article names and representations of their
        corresponding objects
        """
        return str(self.__article_dict)

    def __getitem__(self, article_name):
        """
        Gets a specific article by it's name
        :param article_name: Article's name
        :type str:
        :return: corresponding Article object else raises KeyError
        """
        if article_name in self:
            return self.__article_dict[article_name]
        else:
            raise KeyError(article_name)

    def page_rank(self, iters, d=0.9):
        """
        Implementation of the Page Rank algorithm for ranking articles by
        amount of references to them from other articles over a set number of
        iterations.
        :param iters: number of iterations to calculate the rank
        :type int:
        :param d: damping factor
        :return: returns descending list of articles by their rank
        """
        # create a dictionary holding the rank for each article.
        # Initial value = 1
        rnkd_dict = {article: 1
                       for article in self.__article_dict}

        # dictionary which holds the transfers made for each article.
        # Initial value = 0
        iter_transfers = {article: 0 for article in rnkd_dict}

        # performs given number of iterations to calculate the rank
        for i in range(iters):
            # iterates over the articles in the ranked dictionary
            for article_name in rnkd_dict:
                # gets the article object
                article = self.__article_dict[article_name]

                # calculates the out rank of the article
                out_rank = d * (rnkd_dict[article_name] / article.__len__())

                # sets the remainder for each rank
                rnkd_dict[article_name] = 1 - d

                # iterates over the article's neighbors and adds the out rank
                for neighbor in article.get_neighbors():
                    if neighbor.get_name() in rnkd_dict.keys():
                        iter_transfers[neighbor.get_name()] += out_rank

            # iterates over ranked dictionary and adds the sum of ranks
            for article_name in rnkd_dict:
                rnkd_dict[article_name] += iter_transfers[article_name]
                iter_transfers[article_name] = 0

        return [article[0] for article in sorted(rnkd_dict.items(),
                                                 key=lambda x: (-x[1], x[0]))]

    def jaccard_index(self , article_name):
        """
        Calculates the Jaccard coefficient of articles compared to the given article
        :param article_name: article to compare to
        :type str:
        :return: sorted list of article names by their jaccard index
        """
        # checks if article not in the network
        if article_name not in self:
            return None

        # checks if article doesn't have any neighbors
        if len(self[article_name]) == 0:
            return None

        # this dictionary will hold the jaccard indexes
        index_dict = {}

        # gets the article's object from the dictionary
        art = self.__article_dict[article_name]

        # gets the article's neighbors names
        art_neighbors = art.get_neighbors_names()

        # iterates over a list of article objects and calculates the
        # jaccard index between each of the articles and the original article
        for article in self.__article_dict.values():
            # if original article and article from the list are the same
            # assign index of 1
            if art == article:
                index_dict[article_name] = 1

            else:
                # gets the neighbors of the article from the list
                article_neighbors = article.get_neighbors_names()

                # calculates the index and assigns it to the indexes dictionary
                index_dict[article.get_name()] = \
                    len(set.intersection(article_neighbors, art_neighbors)) / \
                    len(set.union(article_neighbors, art_neighbors))

        return [item[0]
                for item in sorted(index_dict.items(),
                                   key=lambda item: (-item[1], item[0]))]

    def travel_path_iterator(self, article_name):
        """
        Iterator of articles in a graph object which connections are neighboring
        articles. Each iteration it returns the next article in graph based on
        the number of its outgoing and incomming connections
        :param article_name: starting point in the graph
        :yield: next article in graph
        """
        # in case articl is not in the dictionary the iterator is stopped
        if article_name not in self:
            raise StopIteration

        # if article exists, return it and get the next one in line (if exists)
        while article_name:
            yield article_name
            article_name = self.__next_article__(article_name)

    def __next_article__(self, article_name):
        """
        Gets the next article with highest number of incoming connections
        :param article_name: article's name
        :return: sorted list of articles by their incoming connections number (level)
        """
        # gets the neighbors of the article (outgoing connections)
        out_neighbors = self[article_name].get_neighbors_names()

        # creates a new dictionary containing all neighbros and their level set to 0
        level_dict = {neighbor: 0 for neighbor in out_neighbors}

        # bool variable for checking if the current article was ranked before
        is_ranked = False

        # iterates over the list of outgoing neighbors
        for neighbor in out_neighbors:
            # iterates over the list of Article objects
            for article in self.get_articles():
                # checks if current neighbor is in Article's neighbor list
                if neighbor in article.get_neighbors_names():
                    # if yes, increments its level
                    level_dict[neighbor] += 1

                    # sets the current article as ranked
                    if not is_ranked:
                        is_ranked = True

        # if article was ranked before returns None
        if not is_ranked:
            return None

        return [item[0]
                for item in sorted(level_dict.items(),
                                   key=lambda item: (-item[1], item[0]))][0]

    def friends_by_depth(self, article_name, depth):
        """
        Gets a list of articles of a given number of steps from the given article
        :param article_name: Name of the article to get its friends
        :type str:
        :param depth: distance from the original article
        :type int:
        :return: list of friends of given distance from the original article
        """
        # if article doesn't exist returns None
        if article_name not in self:
            return None

        # creates the Set which will hold the friends list
        friends = {article_name}

        # 'depth' number of iterations
        for i in range(depth):
            # iterates over the current list of articles in friends Set
            for friend in list(friends):
                # gets the article object from the dictionary else assigns None
                neighbor_article = self.__article_dict.get(friend)

                # if neighboring article exists adds all it's neighbors to the Set
                if neighbor_article:
                    for neighbor in neighbor_article.get_neighbors_names():
                        friends.add(neighbor)

        return list(friends)

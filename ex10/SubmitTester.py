from ex10 import *

network = WikiNetwork(read_article_links('links.txt'))
s = len(network)
print('Size of network: %d' % s)

print('Page rank:')
print(network.page_rank(50)[:3])

print('Jaccard:')
print(network.jaccard_index('United_Kingdom')[:2])
print(network.jaccard_index('Israel')[:2])
print(network.jaccard_index('United_States')[:2])
print(network.jaccard_index('Algebra')[:2])
print(network.jaccard_index('World_War_II')[:2])


def percent(nominator, denominator):
    return str(nominator / denominator * 100) + '%'


print('Friends percentage:')
print(percent(len((network.friends_by_depth('Christopher_Columbus', 1))), s))
print(percent(len((network.friends_by_depth('DNA', 2))), s))
print(percent(len((network.friends_by_depth('History', 3))), s))
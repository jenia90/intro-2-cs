#######################################################################
#  FILE: hangman.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex5 2015-2016
#  DESCRIPTION : A simple program to compare prices from different stores
#
#######################################################################

import xml.etree.ElementTree as ET
import re

MAX_VALUE_FINE = 1.25
ITEM_CODE_TAG = 'ItemCode'
ITEM_PRICE_TAG = 'ItemPrice'
ITEM_NAME_TAG = 'ItemName'


def get_attribute(store_db, ItemCode, tag):
    '''
    Returns the attribute (tag) 
    of an Item with code: Itemcode in the given store

    '''
    return store_db[ItemCode][tag]


def string_item(item):
    '''
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'

    '''
    return '[' + item[ITEM_CODE_TAG] + ']\t{' + item[ITEM_NAME_TAG] + '}'


def string_store_items(store_db):
    '''
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    '''
    if not store_db:
        return ''

    return ''.join(string_item(store_db[item]) + '\n' for item in store_db)


def read_prices_file(filename):
    '''
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    Returns a tuple: store_id and a store_db, 
    where the first variable is the store name
    and the second is a dictionary describing the store. 
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    :param filename: XML database file of a store
    :return: returns a tuple of StoreId and the database dictionary
    '''
    tree = ET.parse(filename)
    root = tree.getroot()
    store_db = {}

    # iterates through all XML nodes and finds the relevant ones and then adds them to the store_db dictionary
    for items in root.findall('Items'):
        store_db = {item.find(ITEM_CODE_TAG).text:
                    {attrib.tag: attrib.text for attrib in item}
                    for item in items.findall('Item')}

    return root.find('StoreId').text, store_db


def filter_store(store_db, filter_txt):
    """
    Create a new dictionary that includes only the items
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName.
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    :param filter_txt:
    :param store_db:
    :return:
    """
    return {item[ITEM_CODE_TAG]: item
            for item in store_db.values() if filter_txt in item[ITEM_NAME_TAG]}


def create_basket_from_txt(basket_txt): 
    '''
    Receives text representation of few items (and maybe some garbage 
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt

    '''

    return [item_code.strip('[]')
            for item_code in re.findall(re.compile(r"\[\d*\]"), basket_txt)]


def get_basket_prices(store_db, basket):
    '''
    Arguments: a store - dictionary of dictionaries and a basket - 
       a list of ItemCodes
    Go over all the items in the basket and create a new list 
      that describes the prices of store items
    In case one of the items is not part of the store, 
      its price will be None.

    '''
    basket_prices = []

    for item_index in range(len(basket)):
        if basket[item_index] not in store_db:
            basket_prices.append(None)
        else:
            basket_prices.append(float(get_attribute(store_db, basket[item_index], ITEM_PRICE_TAG)))

    return basket_prices

def sum_basket(price_list):
    '''
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones) 
      and the number of missing items (Number of Nones)

    '''
    sum_price_list = 0
    missing_items = 0

    for price in price_list:
        if not price:
            missing_items += 1
        else:
            sum_price_list += price

    return sum_price_list, missing_items

 
def basket_item_name(stores_db_list, ItemCode): 
    ''' 
    stores_db_list is a list of stores (list of dictionaries of 
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not available in any of the stores return only [ItemCode]

    '''
    for store_db in stores_db_list:
        if ItemCode in store_db:
            return string_item(store_db[ItemCode])

    return '[' + ItemCode + ']'


def save_basket(basket, filename):
    ''' 
    Save the basket into a file
    The basket representation in the file will be in the following format:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    '''
    f = open(filename, 'w')

    for item in basket:
        f.writelines('[' + item + ']' + '\n')

    f.close()


def load_basket(filename):
    ''' 
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    '''
    with open(filename) as file:
        basket = [line.rstrip().strip('[]') for line in file]

    return basket


def check_if_other_value_is_none(frst_lst_value, scnd_lst_value):
    if not frst_lst_value:
        return scnd_lst_value * MAX_VALUE_FINE
    elif not scnd_lst_value:
        return frst_lst_value * MAX_VALUE_FINE
    else:
        return max(frst_lst_value, scnd_lst_value) * MAX_VALUE_FINE

def best_basket(list_of_price_list):
    '''
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a 
    missing item has a price of its maximal price in the other stores *1.25

    '''
    basket_prices = []
    for lst in range(len(list_of_price_list)):
        current_basket_price = 0
        for index in range(len(list_of_price_list[lst])):
            if list_of_price_list[lst][index]:
                current_basket_price += list_of_price_list[lst][index]
            else:
                current_basket_price += check_if_other_value_is_none(list_of_price_list[(lst+1)%3][index],
                                                                     list_of_price_list[(lst+2)%3][index])
        basket_prices.append(current_basket_price)

    return basket_prices.index(min(basket_prices))

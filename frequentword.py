# from collections import Counter
# def advanced_count(text):
#     maxword=
#     list1=text.split()
#     words= Counter(list1)
#     return words

# print(advanced_count("Это пробный текст текст текст"))

from collections import Counter, OrderedDict
def advanced_count(text):
    listString= OrderedCounter(text)
    return  list(c.keys())[0]
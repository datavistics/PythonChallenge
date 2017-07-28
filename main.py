import zipfile
import pickle
import re
import texts
from collections import defaultdict
from pprint import pprint
import operator
import requests


def p1():
    return str(2 ** 38)


def p2():
    to_ignore = ",()'."
    result = []
    for letter in texts.p2_other_string:
        if letter in "yz":
            d = {'y': 'a', 'z': 'b'}
            result.append(d[letter])
        elif letter in to_ignore:
            pass
        else:
            result.append(chr(ord(letter)+2))

    return ''.join(result)


def p3():
    d = defaultdict(lambda: 0)
    for i in texts.p3_txt:
        d[i] += 1

    return ''.join(sorted(d, key=d.get, reverse=False)[:8])


def p4():
    regex_findall = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', texts.p4_text)
    return ''.join([middle[4] for middle in regex_findall])


def p5():
    num = str(66831)
    url_start = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    while True:
        r = requests.get(url_start+num)
        result = str(r.content)
        num = result[result.rfind(' '):-1]
        if not result.startswith('and the next nothing is'):
            return str(result[2:-6])


def p6():
    r = requests.get(r'http://www.pythonchallenge.com/pc/def/banner.p')
    p = pickle.loads(r.content)

    string_out = ''
    for outer_list in p:
        for tup in outer_list:
            string_out += tup[0] * tup[1]
        string_out += "\n"
    print(string_out)
    return 'channel'


def p7():
    r = requests.get(r'http://www.pythonchallenge.com/pc/def/channel.zip')
    zip_file = r.content
    zipfile.

def main():
    url_prefix = 'http://www.pythonchallenge.com/pc/def/'
    funs = [p1, p2, p3, p4, p6]
    for i, f in enumerate(funs):
        result = f()
        print(f"The solution to problem {i+1} is:\n\t {url_prefix}{result}.html")

if __name__ == '__main__':
    main()


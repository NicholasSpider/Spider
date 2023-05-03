from random import choice
from config import func_main


def func_pages(site):
    if not site:
        func_file(site)
    func_history(site)

def func_file(site):
    try:
        with open('sites.txt', 'r') as f:
            site = f.readlines()
            func_history(site)
            #print(site)
    except:
        input('File sites.txt is unavailable. Press key Enter...')
        print(site)

def func_history(site):
    try:
        with open('history_site.txt', 'r') as f:
            history = f.readlines()
    except:
        input('File history_site.txt is unavailable. Press key Enter')
    finally:
        func_main(site, history)


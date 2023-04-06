from random import choice


def func_pages(site):
    if not site:
        func_file()
    print(site)

def func_file():
    try:
        if not site:
            with open('sites.txt', 'r') as f:
        if site:
            with open('sites.txt', 'r') as f:
                sites = f.readlines()
        print(sites)
    except:
        print('File unavailable. The program will automatically select the necessary previous page.')
        input('Press key Enter...')
        print(site)
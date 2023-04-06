import pages


def start():
    site = input('Enter a website or simply press Enter to load websites from sites.txt: ')
    print(site)
    pages.func_pages(site)


if __name__ == '__main__':
    start()


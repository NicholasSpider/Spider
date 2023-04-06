try:
    with open('history_site.txt', 'r') as f:
        sites = f.readlines()
    print(sites)
    h_site = choice(sites).strip()
except:
    print('File unavailable. The program will automatically select the necessary previous page.')
    input('Press key Enter...')
te()
print('Hello!!!!')
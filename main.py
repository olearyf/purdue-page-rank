import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import numpy as np
from scipy.linalg import solve

U = []
def getLinks(url):
    http = httplib2.Http()
    try:
        status, response = http.request(url)
    except:
        print('Error')
        return []
    links = []
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if 'https' in link['href']:
                links.append(link['href'])

    return links

def getHash(url):
    sum = 0;
    for i in range(len(url)):
        sum += ord(url[i])
    return len(url) + 1024*sum

def getLinksNum(url, n):
    #print('test')
    # create U, nx1 column vector of URLs
    global U
    U = [0]*n
    # create hash, nx1 column vector of zeros
    hash_list = [0]*n
    # create G, an nxn matrix where G(i,j) = 1 if node j is linked to node i
    G = [[0 for x in range(n)] for y in range(n)]
    # set U[0][0] = url
    m = 0
    U[m] = url
    # hash[0] = getHash(url)
    hash_list[m] = getHash(url)
    # for j = 0 to n
    for j in range(n):
        print('J: ', end='');
        print(j, end=' ')
        print(' ', end='')
        print(U[j])
        links = getLinks(U[j])
        print(len(links))
        if links != []:

    # try to open the page at U[j]
    # for link on page U[j]
            loc = 0
            for link in links:
                loc = 0
                for i in range(m):
                    if hash_list[i] == getHash(link):
                        if (U[i] == link):
                            loc = i
                if (loc == 0 and m < n-1):
                    m = m+1
                    U[m] = link
                    hash_list[m] = getHash(link)
                    loc = m
                if (loc > 0):
                    #print(link)
                    G[loc][j] = 1

        else:
            j = j-2
    for m in range(n):
        print(m, end='')
        print(' ', end='')
        print(U[m])
    for i in range(n):
        for j in range(n):
            print(G[i][j], end='')
            print(' ', end='')
        print('')
    # check if page is already in url list
    # iterate thorugh hash and if hash = gethash(current url), check is url and
    # U[hashnum] = current url
    # add new url to graph if fewer than n
    # add a new link
    return G

def page_rank(G, n):
    # remove self links from G
    for i in range(n):
        if G[i][i] == 1:
            G[i][i] == 0
    # create dc of size n xn
    Dc = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + G[j][i]
        if sum == 0:
           Dc[i][i] = 0
        else:
            Dc[i][i] = 1/sum
    # create I
    I = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        I[i][i] = 1
    p = 0.85
    # create e
    e = [1] * n
    A = [[0 for x in range(n)] for y in range(n)]
    A = np.subtract(I, np.multiply(np.multiply(p, G), Dc))
    x = [1] * n
    x = solve(A, e)
    y = [1] * n
    y = solve(A, e)
    y = y.sort()
    print(solve(A, e))
    indices =np.argsort(x)
    print(indices)
    print(x[indices[99]])
    print(U)
    for i in range(n-1,n-10,-1):
        print(x[indices[i]])
        print(U[indices[i]])


    # solve the matrix equation x = (I-p*G*Dc)\e

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #getLinks('https://www.purdue.edu/')
    G = getLinksNum('https://www.purdue.edu/', 100)
    page_rank(G, 100)
    #getLinksNum('https://www.harvard.edu/', 85)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import numpy as np
from scipy.linalg import solve

# returns a list of all the links that
# are listed on an input URL
def getLinks(url):
    http = httplib2.Http()
    try:
        status, response = http.request(url)
    except:
        print('Error getting page. Moving on.')
        return []
    links = []
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if not('tel' in link['href']):
                if 'https' in link['href']:
                    links.append(link['href'])
                # elif to handle weird Purdue network anomaly
                elif ('//' in link['href'] and not ('http' in link['href'])):
                    links.append('https:' + link['href'])
    return links

# hash function for URL indexing
def getHash(url):
    sum = 0;
    for i in range(len(url)):
        sum += ord(url[i])
    return len(url) + 1024*sum

# creates and returns an nxn adjacency matrix of the connections
# between the pages linked on the input URL. Recursively
# finds links until n are found
def createGraph(url, n):
    global U
    U = [0]*n # to store the URLs
    hash_list = [0]*n
    G = [[0 for x in range(n)] for y in range(n)] # adjacency matrix
    m = 0
    U[m] = url
    hash_list[m] = getHash(url)
    # recursively walk lists of linked links and add them to G
    for j in range(n):
        print('Accessing Link Number ', end='');
        print(j, end=' ')
        print(': ', end='')
        print(U[j])
        links = getLinks(U[j])
        if links != []:
            for link in links:
                loc = -1
                # determine is URL is already logged
                for i in range(m):
                    if hash_list[i] == getHash(link):
                        if (link in U[i] and len(link) == len(U[i])):
                            loc = i
                            break
                # if URL is not already logged, add it
                if (loc == -1 and m < n-1):
                    m = m + 1
                    U[m] = link
                    hash_list[m] = getHash(link)
                    loc = m
                # update G
                if (loc >= 0):
                    G[loc][j] = 1
    return G

# takes an input of an nxn adjacency matrix G
# that represents the page connections and
# runs PageRank on them; prints out links in order
def page_rank(G, n):
    G = np.array(G)
    D = np.zeros((n, n))
    colSums = np.sum(G, 0)
    for i in range(n):
        D[i, i] = colSums[i]
    # create column stochastic matrix Dc
    Dc = np.zeros((n, n))
    for i in range(n):
        if D[i, i] == 0:
            Dc[i, i] = 0.0
        else:
            Dc[i, i] = 1.0 / D[i, i]
    I = np.identity(n)
    e = np.ones((n, 1))
    pGDc = G.dot(Dc)
    pGDc = pGDc * 0.85
    result = I - pGDc
    # compute order, sort
    x = solve(result, e)
    indices = x.argsort(0)
    # print out results
    print('\n')
    print('Results Printed Below: ')
    print('\n')
    count = 1
    for i in range(n-1,0,-1):
        print('#', end='');
        print(count, end='');
        print(' Rank Value: ', end='');
        print(str(x[indices[i]]), end='')
        print(' URL: ', end='')
        print(str(np.array(U)[indices[i]]), end='')
        print('\n')
        count = count + 1

if __name__ == '__main__':
    G = createGraph('https://www.purdue.edu', 100)
    page_rank(G, 100)

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import numpy as np
from scipy.linalg import solve

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
            if not('tel' in link['href']):
                if 'https' in link['href']:
                    links.append(link['href'])
                elif ('//' in link['href'] and not ('http' in link['href'])):
                    links.append('https:' + link['href'])

    return links

def getHash(url):
    sum = 0;
    for i in range(len(url)):
        sum += ord(url[i])
    return len(url) + 1024*sum

def getLinksNum(url, n):
    U = [0]*n
    hash_list = [0]*n
    G = [[0 for x in range(n)] for y in range(n)]
    m = 0
    U[m] = url
    hash_list[m] = getHash(url)
    for j in range(n):
        print('J: ', end='');
        print(j, end=' ')
        print(' ', end='')
        print(U[j])
        links = getLinks(U[j])
        print(len(links))
        if links != []:
            for link in links:
                loc = -1
                for i in range(m):
                    if hash_list[i] == getHash(link):
                        if (link in U[i] and len(link) == len(U[i])):
                            loc = i
                            break
                if (loc == -1 and m < n-1):
                    m = m + 1
                    U[m] = link
                    hash_list[m] = getHash(link)
                    loc = m
                if (loc >= 0):
                    G[loc][j] = 1

    for m in range(n):
        print(m, end='')
        print(' ', end='')
        print(U[m])
    Dc = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + G[j][i]
        if sum == 0:
            Dc[i][i] = 0
        else:
            for k in range(n):
                Dc[j][i] = float(float(1) / float(sum))
    I = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        I[i][int(i)] = float(1)
    p = [[float(0.85) for x in range(1)] for y in range(n)]
    e = [[float(1) for x in range(1)] for y in range(n)]
    A = [[0 for x in range(n)] for y in range(n)]
    A = np.multiply(np.multiply(np.array(G), p), np.array(Dc))
    A = np.subtract(I, A)
    x = solve(A, e)
    y = [1] * n
    for i in range(n):
        y[i] = x[i][0] * 10.0
    print(solve(A, e))

    indices = np.argsort(y)
    print(indices)
    w = 0
    for i in range(n - 1, 0, -1):
        print(y[indices[i]])
        print(U[indices[w]])
        w = w+1
    return G

def page_rank(G, n):
    # remove self links from G
    #for i in range(n):
        #if G[i][i] == 1:
            #G[i][i] == 0
    #G = np.matrix(G).transpose()
    #G = np.array(G).transpose()
    # create dc of size n xn
    Dc = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + G[j][i]
        if sum == 0:
           Dc[i][i] = 0
        else:
            #print('I: ')
            #print(i)
            #print(sum)
            Dc[i][i] = float(float(1)/float(sum))
            if (i == 0):
                print('I is equal to zero!')
                print(sum)
    # create I
    I = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        I[i][i] = float(1)
    p = float(0.85)
    # create e




    # make e and x into column vectors!!!


    #e = [float(1)] * n
    e = [[float(1) for x in range(1)] for y in range(n)]
    A = [[0 for x in range(n)] for y in range(n)]
    #A = np.multiply(p, np.multiply(G, Dc))
    A = np.subtract(I,np.multiply(p, Dc))
    print("HEREG")
    print(G[0][0])
    #for i in range(n):
            #Dc[i][i] = p*Dc[i][i]
    print("HERE")
    print(Dc[0][0])
    #A = np.subtract(I, np.multiply(p, np.multiply(G, Dc)))
    #for i in range(n):
        #I[i][i] = float(1)-Dc[i][i]
    #A = np.subtract(I, Dc)
    print("HERE")
    print(I[0][0])
    print(A[0][0])
    #for i in range(n):
       # Dc[i][i] = Dc[i][i]*0.85
    #for i in range(n):
        #for j in range(n):
            #for k in range(n):
               # A[i][j] += G[i][k] * Dc[k][j]
    #print("HERE")
    #print(A[0][0])
   # for i in range(n):
        #A[i][i] = float(1) - A[i][i]
    #x = [1] * n
    x = [[float(1) for x in range(1)] for y in range(n)]
    x = solve(A, e)
    #x = np.linsolve(A, e)
    y = [1] * n
    #y = solve(A, e)
    #y = np.linsolve(A,e)
    #y = y.sort()
    for i in range(n):
        y[i] = x[i][0]
    print(solve(A, e))
    #indices =np.argsort(x)
    indices = np.argsort(y)
    print(indices)
    #print(y[indices[99]])
    #print(U[indices[99]])
    for i in range(n-1,0,-1):
        print(y[indices[i]])
        #print(U[indices[i]])
    sum1 = 0
    for i in range(n):
        if G[61][i] == 1:
            sum1 = sum1 + 1
    sum2 = 0
    for i in range(n):
        if G[0][i] == 1:
            sum2 = sum2+1
    print(sum1)
    print(sum2)
    for j in range(100):
        print(A[j][0])
    print(indices)


    # solve the matrix equation x = (I-p*G*Dc)\e

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #getLinks('https://www.purdue.edu/')
    G = getLinksNum('https://www.purdue.edu', 5)
    #print(U[0])
    #np.matrix(G).view()
    #G = np.transpose(G)
    #page_rank(G, 100)
    #for j in range(100):
        #print(G[j][75])
    #getLinksNum('https://www.harvard.edu/', 85)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

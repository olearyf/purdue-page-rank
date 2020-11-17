import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import numpy as np
from scipy.linalg import solve

if __name__ == '__main__':
    G = np.array([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0]])
    D = np.zeros((5, 5))
    colSums = np.sum(G, 0)
    for i in range(5):
        D[i, i] = colSums[i]
    print(D)
    Dc = np.zeros((5, 5))
    for i in range(5):
        Dc[i, i] = 1.0 / D[i, i]
    print(Dc)
    e = np.ones((5, 1))
    print(e)
    p = np.array([[0.85], [0.85], [0.85], [0.85], [0.85]])
    print(p)
    I = np.identity(5)
    print(I)
    pGDc = G.dot(Dc)
    print(pGDc)
    pGDc = pGDc * 0.85
    print(pGDc)
    result = I - pGDc
    print(result)
    x = solve(result, e)
    print(x)


# purdue-page-rank
A simple script that takes the first 100 links it finds by walking down the listed links of https://www.purdue.edu/, and ranks them using some linear algebra and Google's PageRank algorithm. For more information, visit https://olearyfrances.com/projects-1#/page-ranking-purdue/.
## Results:
 - #1 Rank Value: [[9.21338764]] URL: ['https://www.purdue.edu']
 - #2 Rank Value: [[6.77607646]] URL: ['https://www.purdue.edu/disabilityresources/']
 - #3 Rank Value: [[5.84282071]] URL: ['https://www.purdue.edu/directory/']
 - #4 Rank Value: [[5.28089884]] URL: ['https://www.purdue.edu/purdue/giveNow.html']
 - #5 Rank Value: [[5.21939596]] URL: ['https://www.purdue.edu/purdue/commercialization/index.php']
 - #6 Rank Value: [[4.93934603]] URL: ['https://www.purdue.edu/securepurdue/security-programs/copyright-policies/reporting-alleged-copyright-infringement.php']
 - #7 Rank Value: [[4.87223517]] URL: ['https://www.purdue.edu/marketing/']
 - #8 Rank Value: [[4.84837967]] URL: ['https://www.purdue.edu/purdue/ea_eou_statement.php']
 - #9 Rank Value: [[4.71570977]] URL: ['https://one.purdue.edu']
 - #10 Rank Value: [[4.31497709]] URL: ['https://www.purdue.edu/boilerconnect/']
 ### Highlight
 Below is an image of a visualization I generated in Matlab of the digraph adjacency matrix for the 100 sites I analyzed:
 ![](https://github.com/olearyf/purdue-page-rank/blob/master/sparse.jpg)

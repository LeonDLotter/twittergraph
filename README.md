# A network visualization generated from the Science Twitter Graph

As of Elmos takeover of Twitter, John Beatty ([Twitter](https://twitter.com/john_d_beatty), [Mastodon](https://social.coop/@beatty)) started to collect the ORCID handles and followings of researchers on Twitter to preserve the "Science Twitter Graph".  

I spontaneously wrote some Python code that creates an interactive network visualization from the OpenCheck data. You can search for your own ORCID ID in the top menu and when you hover over nodes, a link to the respective ORCID page pops up. The network might take some time to load. Especially when you recreate it, there might be a lot more nodes and edges. 

First commit: 641 nodes with 4995 edges.
2 hours later: 859 nodes with 7922 edges.

### *[TO THE NETWORK](http://leonlotter.de/twittergraph/graph.html)*

Data source: [OpenCheck](https://opencheck.is/scitwitter)   
Code Package: [pyvis](https://pyvis.readthedocs.io/) based on [visjs](https://visjs.org/)  
License: [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/)  

You can find me on [Twitter](https://twitter.com/LeonDLotter) and [Mastodon](https://fediscience.org/@LeonDLotter).

### The network

<img src="graph.png" style="background-color:white">

### The edge-contest winner
<img src="graph_selected.png" style="background-color:white">


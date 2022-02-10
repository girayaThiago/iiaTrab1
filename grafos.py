# Create dictionary with straight line distance
straight_distance = {
    "arad" : 366,
    "bucharest" : 0,
    "craiova" : 160,
    "dobreta" : 242,
    "eforie" : 161,
    "fagaras" : 178,
    "giurgiu" : 77,
    "hirsova" : 151,
    "iasi" : 226,
    "lugoj" : 244,
    "mehadia" : 241,
    "neamt" : 234,
    "oradea" : 380,
    "pitesti" : 98,
    "rimnicu vilcea" : 193,
    "sibiu" : 253,
    "timisoara" : 329,
    "urziceni" : 80,
    "vaslui" : 199,
    "zerind" : 374
}

# Create the dictionary with graph elements
graph = { 
   "arad" : {
       "zerind" : 75,
       "sibiu" : 140,
       "timisoara": 118
   },
   "bucharest" : {
       "urziceni" : 85,
       "pitesti" : 101,
       "fagaras" : 211,
       "giurgiu" : 90
   },
   "craiova" : {
       "pitesti" : 138,
       "rimnicu vilcea" : 146,
       "dobreta" : 120
   },
   "dobreta " : {
       "craiova" : 120,
       "mehadia" : 75
   },
   "eforie" : {
       "hirsova" : 86
   },
   "fagaras" : {
       "sibiu" : 99,
       "bucharest" : 211
   },
   "giurgiu" : {
       "bucharest" : 90
   },
   "hirsova" : {
       "eforie" : 86,
       "urziceni" : 98
   },
   "iasi" : {
       "vaslui" : 92,
       "neamt" : 87
    },
   "lugoj" : {
       "timisoara" : 111,
       "mhadia" : 70
   },
   "mehadia" : {
       "lugoj" : 70,
       "dobreta" : 75
   },
   "neamt" : {
       "iasi" : 87
   },
   "oradea" : {
       "oradea" : 71,
       "sibiu" : 151
   },
   "pitesti" : {
       "rimnicu vilcea" : 97,
       "bucharest" : 101,
       "craiova" : 138
   },
   "rimnicu vilcea" : {
       "sibiu" : 80,
       "pitesti" : 97,
       "craiova" : 146
   },
   "sibiu" : {
       "fagaras" : 99,
       "arad" : 140,
       "oradea" : 151,
       "rimnicu vilcea" : 80
   },
   "timisoara" : {
       "arad" : 118,
       "lugoj" : 70
   },
   "urziceni" : {
       "bucharest" : 85,
       "hirsova" : 98,
       "vaslui" : 142
   },
   "vaslui" : {
       "iasi" : 92,
       "urziceni" : 142
   },
   "zerind" : {
       "arad" : 71,
       "oradea" : 75
   }

}

print(graph.keys())
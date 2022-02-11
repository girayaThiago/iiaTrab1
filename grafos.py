# Create dictionary with straight line distance to bucharest
from audioop import reverse


straight_distance_arad_bucharest = {
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
       "timisoara": 118,
       "sibiu" : 140},
   "bucharest" : {
       "urziceni" : 85,
       "giurgiu" : 90,
       "pitesti" : 101,
       "fagaras" : 211},
   "craiova" : {
       "dobreta" : 120,
       "pitesti" : 138,
       "rimnicu vilcea" : 146},
   "dobreta " : {
       "mehadia" : 75,
       "craiova" : 120},
   "eforie" : {
       "hirsova" : 86},
   "fagaras" : {
       "sibiu" : 99,
       "bucharest" : 211},
   "giurgiu" : {
       "bucharest" : 90},
   "hirsova" : {
       "eforie" : 86,
       "urziceni" : 98},
   "iasi" : {
       "neamt" : 87,
       "vaslui" : 92},
   "lugoj" : {
       "mhadia" : 70,
       "timisoara" : 111},
   "mehadia" : {
       "lugoj" : 70,
       "dobreta" : 75},
   "neamt" : {
       "iasi" : 87},
   "oradea" : {
       "oradea" : 71,
       "sibiu" : 151},
   "pitesti" : {
       "rimnicu vilcea" : 97,
       "bucharest" : 101,
       "craiova" : 138},
   "rimnicu vilcea" : {
       "sibiu" : 80,
       "pitesti" : 97,
       "craiova" : 146},
   "sibiu" : {
       "rimnicu vilcea" : 80,
       "fagaras" : 99,
       "arad" : 140,
       "oradea" : 151},
   "timisoara" : {
       "lugoj" : 70,
       "arad" : 118},
   "urziceni" : {
       "bucharest" : 85,
       "hirsova" : 98,
       "vaslui" : 142},
   "vaslui" : {
       "iasi" : 92,
       "urziceni" : 142},
   "zerind" : {
       "arad" : 71,
       "oradea" : 75}

}

visited = []
solution = []
### Goals - find routes from arad to bucharest using 3 different means: 
# 1.Uniform Cost traversal; 
# 2.Greedy Approach; 
# 3.A*
#
def UCS(graph, origin = "arad", destination = "bucharest"):
    if graph == None:
        return None
    if origin in graph and destination in graph:
        return None

def Greedy(graph, straight_distance, origin = "arad", destination = "bucharest"):
    if (origin not in visited):
        visited.append(origin)
    if origin in graph and destination in graph:
        origin_cost = straight_distance[origin]
        if origin_cost == 0:
            solution.append(origin)
            return 1
        #reorder node from closest to farthest
        neighbours = list(graph[origin].keys())
        distance_list = []
        for n in neighbours:
            distance_list.append((n, straight_distance[n]))
        distance_list.sort(key=lambda y: y[1])
        for (n,_) in distance_list:
            if (n not in visited):
                if Greedy(graph, straight_distance, n, destination) == 1:
                    # if return 1 -> destination found -> add self as path to solution ->  signal to retroactively add caller
                    solution.append(origin)
                    return 1
    return None

def Astar(graph, origin = "arad", destination = "bucharest"):
    if graph == None:
        return None
    if origin in graph and destination in graph:
        return None
        #do your thing :)
            

Greedy(graph, straight_distance_arad_bucharest)
solution.reverse()
cost = 0
current = None
for city in solution:
    if current != None:
        cost += graph[current][city]
        print(f"added cost from {current} to {city} = {graph[current][city]}")
    current = city

print(f"greedy solution pathway = {solution}, total cost: {cost}")

#print(visited)

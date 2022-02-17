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
   "dobreta" : {
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
       "mehadia" : 70,
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

class Path_ucs:
    def __init__(self,cost = 9999, path = []):
        self.cost = cost
        self.path = path

    def __str__(self):
        return f"cost to reach: {self.cost} path = {self.path}"


#(custo, [caminho])
path_from_origin = {
    "arad" :            Path_ucs(),
    "bucharest" :       Path_ucs(),
    "craiova" :         Path_ucs(),
    "dobreta" :         Path_ucs(),
    "eforie" :          Path_ucs(),
    "fagaras" :         Path_ucs(),
    "giurgiu" :         Path_ucs(),
    "hirsova" :         Path_ucs(),
    "iasi" :            Path_ucs(),
    "lugoj" :           Path_ucs(),
    "mehadia" :         Path_ucs(),
    "neamt" :           Path_ucs(),
    "oradea" :          Path_ucs(),
    "pitesti" :         Path_ucs(),
    "rimnicu vilcea" :  Path_ucs(),
    "sibiu" :           Path_ucs(),
    "timisoara" :       Path_ucs(),
    "urziceni" :        Path_ucs(),
    "vaslui" :          Path_ucs(),
    "zerind" :          Path_ucs()
}


#guardar caminho em listas, quando trocar caminho expurgar lista antiga, guardar nova
def UCS(graph, origin = "arad", current = "arad", current_path = []):
    path_from_origin[origin].cost = 0
    destination = "bucharest"
    print(f"Visiting {current}")
    neighbours = list(graph[current].keys())
    current_path.append(current)
    for n in neighbours:
        current_cost = path_from_origin[current].cost
        traverse_cost = graph[current][n]
        if current_cost + traverse_cost < path_from_origin[n].cost:
            path_from_origin[n].cost = current_cost + traverse_cost
            path_from_origin[n].path = current_path.copy()
        if n not in current_path:
            # print(n)
            UCS(graph,"arad", n, current_path.copy())
    return

UCS(graph, "arad", "arad", [])
print(path_from_origin["bucharest"])


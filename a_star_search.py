import heapq

def a_star_search(graph, heuristic, start, goal):
    visited = set()
    priorityQ = []
    
    # g(n) 
    g = {start: 0}
    
    # f(n) = g(n) + h(n)
    f = {start: heuristic[start]}
    
    heapq.heappush(priorityQ, (f[start], start))

    while priorityQ:
        _, current = heapq.heappop(priorityQ)
        
        if current == goal:
            print(f"Goal Reached: {goal}")
            return
        
        if current not in visited:
            print(f"{current} -> ", end='')
            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    tentative_g = g[current] + weight
                    
                    if neighbor not in g or tentative_g < g[neighbor]:
                        g[neighbor] = tentative_g
                        f[neighbor] = tentative_g + heuristic[neighbor]
                        heapq.heappush(priorityQ, (f[neighbor], neighbor))

    print("Goal not reachable.")

graph = {
    'Arad': [('Timisoara', 1), ('Zerind', 1), ('Sibiu', 1)],
    'Zerind': [('Arad', 1), ('Oradea', 1)],
    'Oradea': [('Zerind', 1), ('Sibiu', 1)],
    'Timisoara': [('Arad', 1), ('Lugoj', 1)],
    'Lugoj': [('Timisoara', 1), ('Mehadia', 1)],
    'Mehadia': [('Lugoj', 1), ('Dobreta', 1)],
    'Dobreta': [('Mehadia', 1), ('Craiova', 1)],
    'Sibiu': [('Arad', 1), ('Oradea', 1), ('Fagaras', 1), ('Rimnicu_Vilcea', 1)],
    'Fagaras': [('Sibiu', 1), ('Bucharest', 1)],
    'Rimnicu_Vilcea': [('Sibiu', 1), ('Pitesti', 1), ('Craiova', 1)],
    'Pitesti': [('Rimnicu_Vilcea', 1), ('Bucharest', 1), ('Craiova', 1)],
    'Craiova': [('Dobreta', 1), ('Rimnicu_Vilcea', 1), ('Pitesti', 1)],
    'Bucharest': [('Fagaras', 1), ('Pitesti', 1), ('Giurgiu', 1), ('Urziceni', 1)],
    'Giurgiu': [('Bucharest', 1)],
    'Urziceni': [('Bucharest', 1), ('Hirsova', 1)],
    'Hirsova': [('Urziceni', 1), ('Eforie', 1), ('Vaslui', 1)],
    'Eforie': [('Hirsova', 1)],
    'Vaslui': [('Hirsova', 1), ('Iasi', 1)],
    'Iasi': [('Vaslui', 1), ('Neamt', 1)],
    'Neamt': [('Iasi', 1)]
}

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu_Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

a_star_search(graph, heuristic, 'Arad', 'Bucharest')

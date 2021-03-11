
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        # 如果节点没有被处理
        if node not in processed:
            if costs[node] < lowest_cost:  # 当前值更小，更新lowest
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node

def find_shortest_path():
    # 从终点开始
    node = end
    shortest_path = [end]
    while parents[node] != start:
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append(start)
    return shortest_path

# 计算图中从start到end的最短路径
def dijkstra(graph):
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost    # 更新cost
                parents[neighbor] = node    # 更新parent，parent里全是最短邻居
        # 标记当前节点为已处理
        processed.append(node)
        node = find_lowest_cost_node(costs)
    shortest_path = find_shortest_path()
    shortest_path.reverse() 
    print('从{}到{}的最短路径：\n{}'.format(start, end, shortest_path))


graph = {1:{2:100}, 2:{3:50, 4:90}, 3:{2:50, 4:100, 5:60}, 4:{2:90, 3:100, 5:100}, 5:{3:60, 4:100}}

start, end = 2, 5
costs = {}    # 所有节点的cost，cost指从起点到该节点的距离
costs[start] = 0    # 初始节点cost为0
parents = {}    # 存储父节点
processed = []
dijkstra(graph) 
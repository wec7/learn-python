import argparse

def read_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', action="store", default="0/0")
	parser.add_argument('-m', action="store", default="2")
	return parser.parse_args()

def construct_graph(size):
	graph = {}
	keys = [str(a)+'/'+str(b) for a in range(size) for b in range(size)]
	for key in keys:
		graph[key] = set([key[-1]+'/'+str(a) for a in range(size)]) - set([key])
	return graph

def dfs(start, visited, tmp_path):
	global graph, success, path
	if set(graph[start]) - set(visited+[start, start[::-1]]) == set([]):
		if len(visited+list(set([start, start[::-1]]))) == len(graph):
			success = True
			path = tmp_path+[start]
	for next in set(graph[start]) - set(visited+[start, start[::-1]]):
		dfs(next, visited+list(set([start, start[::-1]])), tmp_path+[start])
		if success:
			break
	return path

if int(read_arg().m) > 2 and int(read_arg().m)%2 == 1:
	print "NO SOLUTION"
	exit()
graph, success, path = construct_graph(int(read_arg().m)+1), False, list()
dfs(read_arg().s, list(), list())
if path == list():
	print "NO SOLUTION"
	exit()
print ' - '.join(path)
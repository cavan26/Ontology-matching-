
class OntologyTree():
    def __init__(self, Table):
        self.table = Table
        self.tree = self.createTree()

    def createTree(self):
        tree = {}
        for line in self.table:
            if line[0] in tree.keys():
                tree[line[0]].append(line[1])
            else:
                tree[line[0]] = [line[1]]
        return tree

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.tree.has_key(start):
            return None
        for node in self.tree[start]:
            if node not in path:
                newpath = self.find_path(self.tree, node, end, path)
                if newpath: return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not self.tree.has_key(start):
            return []
        paths = []
        for node in self.tree[start]:
            if node not in path:
                newpaths = self.find_all_paths(self.tree, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.tree.has_key(start):
            return None
        shortest = None
        for node in self.tree[start]:
            if node not in path:
                newpath = self.find_shortest_path(self.tree, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
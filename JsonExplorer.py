from Node import *
from Strategy import *

class JsonExplorer:
    def __init__(self, style, icons):
        self.style = style
        self.icons = icons
        self.root = Node('root', None, 0, self.icons[0])  # 创建根节点

    def _load(self, data):
        self._parse(data, self.root, 0)  # 解析数据并构建树结构
        return self.root  # 返回根节点

    def _parse(self, data, parent, level):
        for key, value in data.items():
            if isinstance(value, dict):  # 如果值是字典类型，递归处理
                node = Node(key, None, level + 1, self.icons[0], parent)
                parent.add(node)
                self._parse(value, node, level + 1)
            else:
                node = Node(key, value, level + 1, self.icons[1], parent)
                parent.add(node)

    def show(self, line_length):
        if self.style == 'tree':
            strategy = TreeStyleStrategy(self.root)  # 创建树形风格策略
        elif self.style == "rectangle":
            strategy = RectangleStyleStrategy(self.root)  # 创建矩形风格策略
        strategy.draw(line_length)  # 可视化
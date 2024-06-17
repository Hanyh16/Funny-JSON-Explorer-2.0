from abc import ABC, abstractmethod
from Iterator import *

# 策略接口
class Strategy(ABC):
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def draw(self, line_length):
        pass

# 树形风格具体策略
class TreeStyleStrategy(Strategy):
    def draw(self, line_length):
        iterator = Iterator(self.root)  # 使用迭代器遍历节点
        parent_is_last = []  # 记录父节点是否为最后一个子节点的列表

        while iterator.has_more():
            node = iterator.get_next()
            is_first = (node == node.parent.children[0] if node.parent else False)
            is_last = (node == node.parent.children[-1] if node.parent else False)
            if node.level >= 1:
                self.draw_node(node, is_first, is_last, parent_is_last, line_length)  # 绘制当前节点

    def draw_node(self, node, is_first, is_last, parent_is_last, line_length):
        while len(parent_is_last) < node.level - 1:
            parent_is_last.append(False)  # 确保 parent_is_last 列表长度正确

        # 构建前缀
        prefix = "".join("    " if parent_is_last[i] else "│   " for i in range(node.level - 1))
        prefix += "└─" if is_last else "├─"  # 根据是否为最后一个子节点确定前缀

        # 打印节点信息
        if node.value is not None:
            print(f"{prefix}{node.icon} {node.name}: {node.value}")
        else:
            print(f"{prefix}{node.icon} {node.name}")

        # 更新 parent_is_last 列表
        if len(parent_is_last) > node.level:
            parent_is_last[node.level - 1] = is_last
        else:
            parent_is_last.append(is_last)

# 矩形风格具体策略
class RectangleStyleStrategy(Strategy):
    def draw(self, line_length):
        iterator = Iterator(self.root)  # 使用迭代器遍历节点
        parent_is_last = []  # 记录父节点是否为最后一个子节点的列表

        while iterator.has_more():
            node = iterator.get_next()
            is_first = (node == node.parent.children[0] if node.parent else False)
            is_last = (node == node.parent.children[-1] if node.parent else False)
            if node.level >= 1:
                self.draw_node(node, is_first, is_last, parent_is_last, line_length)  # 绘制当前节点

    def draw_node(self, node, is_first, is_last, parent_is_last, line_length):
        # 确保 parent_is_last 列表长度正确
        while len(parent_is_last) < node.level:
            parent_is_last.append(False)

        # 构建前缀
        prefix = "".join("    " if parent_is_last[i] else "│   " for i in range(node.level - 1))

        # 根据层次和是否为第一个节点确定前缀和后缀
        if node.children:
            if node.level == 1 and is_first:
                prefix += "┌─"
                subfix = '─┐'
            else:
                prefix += "├─"
                subfix = '─┤'
        else:
            flag = all(parent_is_last[1:node.level - 1])

            if flag and is_last:
                prefix = '└───' + '───' * (node.level - 2)
                prefix += "┴─"
            else:
                prefix += "├─"

            subfix = '─┘' if flag and is_last else '─┤'

        # 计算填充长度
        content_length = len(node.icon) + len(node.name) + (len(str(node.value)) + 2 if node.value else 0)
        padding = line_length - len(prefix) - content_length

        # 打印节点信息
        if node.value is not None:
            print(f"{prefix}{node.icon} {node.name}: {node.value} " + '─' * padding + subfix)
        else:
            print(f"{prefix}{node.icon} {node.name} " + '─' * padding + subfix)

        # 更新 parent_is_last 列表
        if len(parent_is_last) > node.level:
            parent_is_last[node.level - 1] = is_last
        else:
            parent_is_last.append(is_last)

        # 确保恢复 parent_is_last 列表状态
        if len(parent_is_last) > node.level:
            parent_is_last[node.level - 1] = False
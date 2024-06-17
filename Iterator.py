class Iterator:
    def __init__(self, root):
        self.stack = [(root, 0)]  # 初始化栈，栈中存储元组 (节点, 层级)

    def has_more(self):
        return len(self.stack) > 0  # 判断栈中是否还有元素

    def get_next(self):
        if self.has_more():  # 如果栈中有元素
            current, level = self.stack.pop()  # 弹出栈顶元素
            if current.children:  # 如果当前节点有子节点
                for child in reversed(current.children):  # 将子节点逆序压入栈中
                    self.stack.append((child, level + 1))
            return current
        return None
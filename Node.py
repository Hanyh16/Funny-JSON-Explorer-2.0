class Node:
    def __init__(self, name, value, level, icon, parent=None):
        self.name = name
        self.value = value
        self.level = level
        self.icon = icon
        self.parent = parent
        self.children = []

    def add(self, child):
        self.children.append(child)
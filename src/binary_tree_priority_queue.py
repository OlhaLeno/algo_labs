class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_el = Node(value, priority)
        if self.root is None:
            self.root = new_el
        else:
            self.insert_recursive(self.root, new_el)

    def insert_recursive(self, current_el, new_el):
        if new_el.priority <= current_el.priority:
            if current_el.left is None:
                current_el.left = new_el
            else:
                self.insert_recursive(current_el.left, new_el)
        else:
            if current_el == self.root:
                parent = None
                while current_el:
                    parent = current_el
                    if new_el.priority <= current_el.priority:
                        current_el = current_el.left
                    else:
                        current_el = current_el.right
                if new_el.priority <= parent.priority:
                    parent.left = new_el
                else:
                    new_el.left = parent
                    new_el.right = parent.right
                    if self.root == parent:
                        self.root = new_el

    def find_highest_priority(self):
        if self.root:
            return self.root.value
        return None

    def delete_highest_priority(self, current_el=None):
        if not current_el:
            current_el = self.root

        if not current_el.right:
            if current_el == self.root:
                self.root = current_el.left
            else:
                current_el = current_el.left
            return current_el
        else:
            return self.delete_highest_priority(current_el.right)

    def display_priority_queue(self):
        self.display_priority_queue_recursive(self.root)

    def display_priority_queue_recursive(self, current_el):
        if current_el:
            self.display_priority_queue_recursive(current_el.left)
            print(f"Value: {current_el.value}, Priority: {current_el.priority}")
            self.display_priority_queue_recursive(current_el.right)

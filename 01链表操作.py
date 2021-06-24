# 定义节点
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList(object):
    # 初始化
    def __init__(self):
        self._head = None

    # 判断链表是否为空
    def is_empty(self):
        return self._head is None

    # 链表长度
    def length(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count

    # 遍历链表
    def item(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    # 向链表头部添加元素
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    # 尾部添加元素
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current is not None:
                current = current.next
            current.next = new_node

    # 指定位置插入元素
    def insert_index(self, index, value):
        if index <= 0:
            self.insert_head(value)
        elif index > (self.length() - 1):
            self.append(value)
        else:
            new_node = Node(value)
            current = self._head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # 删除节点
    def remove(self, value):
        current = self._head
        pre = None
        while current is not None:
            if current.value == value:
                if not pre:
                    self._head = current.next
                else:
                    pre.next = current.next
                return True
            else:
                pre = current
                current = current.next

    def find(self, value):
        return value in self.item()

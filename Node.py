# Узел двусвязного списка
class Node:
    # 1ТП4Т Конструктор
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
 
# Вспомогательная функция для помещения узла в начало двусвязного списка
def push(head, data):
 
    node = Node(data, None, head)
 
    # изменяет `prev` существующего головного узла, чтобы он указывал на новый узел.
    if head:
        head.prev = node
 
    # обновить указатель заголовка и возврат
    head = node
    return head
 
 
# Вспомогательная функция # для печати узлов двусвязного списка
def printDDL(msg, head):
 
    print(msg, end='')
    while head:
        print(head.data, end=' —> ')
        head = head.next
 
    print('None')
 
 
# Функция для замены указателей `next` и `prev` данного узла
def swap(node):
 
    prev = node.prev
    node.prev = node.next
    node.next = prev
 
 
# Функция для обращения двусвязного списка
def reverseDDL(head):
 
    prev = None
    curr = head
 
    # пройтись по списку
    while curr:
        # поменять местами указатели `next` и `prev` для текущего узла
        swap(curr)
 
        # обновляет предыдущий узел перед переходом к следующему узлу
        prev = curr
 
        # перейти к следующему узлу в двусвязном списке
        # (переход с использованием указателя `prev`, так как указатели `next` и `prev` поменялись местами)
        curr = curr.prev
 
    # обновляет указатель заголовка на последний узел
    if prev:
        head = prev
 
    return head
 
 
if __name__ == '__main__':
 
    head = None
    for key in range(1, 6):
        head = push(head, key)
 
    printDDL('Original A: ', head)
    head = reverseDDL(head)
    printDDL('Reversed A: ', head)
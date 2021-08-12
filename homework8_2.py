'''
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''

from collections import Counter, deque

def walk_tree(node: 'Node', track: list):
    # нашли лист
    if node.value:
        track = track if track else [ 0]
        return {node.value: track}
    print(sorted(freq.items(), key=lambda x: x[1]))
    result = {}
    if node.left:
        result.update(walk_tree(node.left, [*track, 0]))
    if node.right:
        result.update(walk_tree(node.right, [*track, 1]))
    return result

def build_tree(string):
    freq = Counter(string)
    deq = deque([(i, Node(value=c)) for c, i in sorted(freq.items(), key=lambda x: x[1])])
    while len(deq) > 1:
        a, b = deq.popleft(), deq.popleft()
        weight = a[0] + b[0]
        idx = 0
        try:
            while deq[idx][0] < weight:
                idx += 1
        except IndexError:
            pass
        deq.insert(idx, (weight, Node(left=a[1], right=b[1])))
    return deq[0][1]

class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

s = input("Введите произвольную строку: ")
print(f"Длина исходной строки составляет {len(s) * 8} бит")

string = 'Beep bop beer'
freq = Counter(string)
root = build_tree(s)
codes = walk_tree(root, [])
print(codes)

encoded_len = 0

print(f"Закодированная строка '{s}' представляется как:")

for el in s:
    representation = codes[el]
    encoded_len += len(representation)
    print(f"{''.join(map(str, representation))}", end=" ")

print(f"И занимает теперь {encoded_len} бит")

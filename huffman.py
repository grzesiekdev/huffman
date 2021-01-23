import heapq
from heapq import heappop, heappush


class Node:
    def __init__(self, ch, frequency, left=None, right=None):
        self.ch = ch
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


def isLeaf(root):
    return root.left is None and root.right is None


def encode(root, encoded_str, code):

    if root is None:
        return

    if isLeaf(root):
        code[root.ch] = encoded_str if len(encoded_str) > 0 else '1'

    encode(root.left, encoded_str + '0', code)
    encode(root.right, encoded_str + '1', code)


output_decoded = ""


def decode(root, index, encoded_str):
    global output_decoded
    if root is None:
        return index

    if isLeaf(root):
        output_decoded += root.ch
        return index

    index = index + 1
    root = root.left if encoded_str[index] == '0' else root.right
    return decode(root, index, encoded_str)


def buildHuffmanTree(text, is_decoding):
    global output_decoded

    if len(text) == 0:
        return

    frequency = {i: text.count(i) for i in set(text)}

    primary_queue = [Node(k, v) for k, v in frequency.items()]
    heapq.heapify(primary_queue)

    while len(primary_queue) != 1:
        left = heappop(primary_queue)
        right = heappop(primary_queue)
        total = left.frequency + right.frequency
        heappush(primary_queue, Node(None, total, left, right))

    root = primary_queue[0]

    huffmanCode = {}
    encode(root, "", huffmanCode)

    encoded_str = ""
    for c in text:
        encoded_str += huffmanCode.get(c)

    with open('converted_to_bin.txt', 'w') as binary:
        binary.write(encoded_str)

    byte_array = bytearray()
    for i in range(0, len(encoded_str), 8):
        byte_array.append(int(encoded_str[i:i + 8], 2))
    with open('encoded.bin', 'wb') as output:
        output.write(byte_array)

    if is_decoding:
        if isLeaf(root):
            while root.frequency > 0:
                output_decoded += root.ch
                root.frequency = root.frequency - 1
        else:
            index = -1
            while index < len(encoded_str) - 1:
                index = decode(root, index, encoded_str)
        with open("decoded.txt", 'w') as decoded_file:
            decoded_file.write(output_decoded)

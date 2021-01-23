import huffman
import time
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="Encode specified file from .txt to .bin")
    parser.add_argument("-d", action='store_true', help="Decode encoded file back to .txt")
    args = parser.parse_args()

    start_time = time.time()
    if args.e:
        with open(args.e, 'r') as file:
            text = file.read()
        huffman.buildHuffmanTree(text, args.d)
    else:
        print("You have to pass an argument! use python3 main.py -h for help")
    print(f"Elapsed time: {time.time() - start_time} seconds")

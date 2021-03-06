# Huffman algorithm
My own implementation of Huffman algorithm created as the task for my programming exercises. You can take a look at what Huffman coding is at wiki https://en.wikipedia.org/wiki/Huffman_coding

![representation of huffman coding](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Huffman_%28To_be_or_not_to_be%29.svg/250px-Huffman_%28To_be_or_not_to_be%29.svg.png)

## How to run
Clone repository, then run following command: ` python3 main.py -e <name_of_file>.txt `.
You have to pass an -e argument, otherwise program won't work. For more specific informations run `python main.py -h`

You can find some dummy data in `data/` folder. 

If you are on UNIX based system and want to create some big random .txt files, just for the purpose of testing, you can run following command:
`base64 /dev/urandom | head -c 1000000000 > file.txt`
This will create 1GB random base64 .txt file.

## Optimization
This implementation stores output into .bin file. **Clean base64 file are always downsized for ~25%**, but other files can be reduced approx. even 50%. 
Running this algorithm for big files takes some time, for example:

10MB base64 file -> ~19sec

100MB base64 file -> ~50sec

1GB base64 file -> 1360sec

42.8MB polish vocabulary .txt file(contains about 2.7 million words) -> 11.36sec and gets reduced to 21.6MB

## Output
After running program you can find following files in the root folder:

`encoded.bin` -> encoded file saved into .bin

`converted_to_bin.txt` -> Binary representation of the file(usually much bigger than original file)

`decoded.txt` -> created only if you pass `-d` boolean flag, made for educational purpose - you can see, that original file can be also decoded

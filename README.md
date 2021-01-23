# Huffman algorithm
My own implementation of Huffman algorithm for my programming class. You can take a look at what Huffman coding is at wiki https://en.wikipedia.org/wiki/Huffman_coding

## How to run
Clone repository, run following command: ` python3 main.py -e file_to_encode.txt `
You have to pass an -e argument, otherwise program won't work. For more specific informations run `python main.py -h`

You can find some dummy data in `data/` folder. 

If you are on UNIX system and want to create some big random .txt files just for the purpose of testing, you can run following command:
`base64 /dev/urandom | head -c 1000000000 > file.txt`
This will create 1GB random base64 .txt file.

## Optimization
This implementation stores output into .bin file. Clean base64 file are always downsized for ~25%, but other files can be reduced approx. even 50%. 
Running this algorithm for big files takes some time, for example:

10MB base64 file -> ~19sec

100MB base64 file -> ~50sec

1GB base64 file -> 1360sec

As you can see, this algorithm doesn't do well with big .txt files, but it's best i could do. 

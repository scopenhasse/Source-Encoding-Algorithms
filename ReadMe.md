# Encoding Programs

This repository contains four Python programs that perform different encoding algorithms.

## Program 1: Run Length Encoding

The `RLE.py` program implements the run-length encoding algorithm for compressing strings. It takes a string as input and outputs a compressed string using the following format:

<pre class=""><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-php-template"><span class="xml"><count><character>
</span></code></div></div></pre>

For example, the input string "aaabbbbcc" would be compressed to "3a4b2c". The program is based on the following algorithm:

1. Initialize a count variable to 1 and start iterating through the input string from the second character.
2. If the current character is the same as the previous character, increment the count variable.
3. If the current character is different from the previous character, output the count and the previous character, and reset the count variable to 1.
4. When the end of the string is reached, output the count and the last character.

To run the program, execute the following command:

<pre class=""><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python RLE.py
</code></div></div></pre>

## Program 2: Huffman Code

The `Huffman.py` program implements the Huffman coding algorithm for compressing strings. It takes a string as input and outputs the Huffman code for each character in the string. The program is based on the following algorithm:

1. Compute the frequency of each character in the string.
2. Sort the characters in descending order of frequency.
3. Assign a binary code to each character using the Huffman coding algorithm.
4. Output the binary code for each character.

To run the program, execute the following command:

<pre class=""><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python Huffman.py
</code></div></div></pre>

## Program 3: Shannon Fennon Compression Code

This code defines two classes `compress` and `shannon_fennon_compression`. The `compress` class is used to store different parameters of a string. The `shannon_fennon_compression` class is used to compress data using Shannon-Fano encoding.

### `compress` class

The `compress` class has four attributes:

* `original`: stores the original character
* `count`: stores the count of the character in the input string
* `code`: stores the compressed version of the character
* `probability`: stores the probability of the character in the input string

### `shannon_fennon_compression` class

The `shannon_fennon_compression` class has three methods:

#### `__getProbability()`

This is a private method that returns the probability of a character in the input string.

#### `compress_data()`

This method takes a string as input and returns a list of compressed characters. The method first processes the input string and finds the probability of all the unique occurrences of characters in the string. It then sorts the probability in descending order and splits the probabilities in the order used in Shannon-Fano encoding. Finally, it encodes the string to its compressed version of string data in binary.

#### `__splitter()`

This is a private method that splits the probabilities in the order used in Shannon-Fano encoding.

#### `__encoder()`

This is a private method that encodes the string to its compressed version of string data in binary.

### Main function

The main function takes user input of a string and compresses it using the `shannon_fennon_compression` class. The compressed data is then printed to the console.

## Program 4: LZW compression

The LZW algorithm works by building a dictionary of substrings from the input string, where each substring is mapped to a unique code. The dictionary is initially populated with all possible single-character substrings. Then, the algorithm reads through the input string one character at a time, building up substrings until it encounters a substring that is not in the dictionary. When this happens, the algorithm outputs the code for the previous substring, adds the new substring to the dictionary with a new code, and resets the current substring to the last character it read. This process continues until the end of the input string is reached.

The `compress` function implements this algorithm by initializing the dictionary with all possible single-character substrings (ASCII characters 0-255), and then iterating through the input string one character at a time. It builds up substrings by appending each new character to the previous substring, checking if the resulting substring is in the dictionary, and if so, appending the new character to the current substring. If the resulting substring is not in the dictionary, the code for the current substring is output, the new substring is added to the dictionary with a new code, and the current substring is reset to the last character read. The function returns the list of output codes.

The `decompress` function takes a list of output codes and reverses the compression process. It initializes the dictionary with all possible single-character substrings (ASCII characters 0-255), and then reads through the list of output codes one code at a time. It uses each code to look up the corresponding substring in the dictionary, outputting the substring and updating the dictionary with a new code for the current substring concatenated with the first character of the next substring (if there is one). The function returns the decompressed string.

In the main block of the code, the user is prompted to enter a string to compress. The input string is then compressed using the `compress` function, and the compressed data is printed to the console. The compressed data is then passed to the `decompress` function, and the decompressed data is printed to the console.

## Written by

@ ILYAS "Sc0Pe" NHASSE supervised by @ Malika ALAMI MARKTANI

@ ENSA FES 2022 - 2023

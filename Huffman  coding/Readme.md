# Huffman Coding Algorithm

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies. The assigned codes are prefix codes, ensuring there is no ambiguity when decoding the generated bitstream.

## Prefix Codes

Prefix codes are codes (bit sequences) assigned in such a way that the code assigned to one character is not the prefix of the code assigned to any other character. This eliminates ambiguity in decoding the compressed bitstream.

### Counter Example

Let's consider characters a, b, c, and d with their corresponding variable-length codes as 00, 01, 0, and 1, respectively. This coding leads to ambiguity because the code assigned to c is the prefix of codes assigned to a and b. For example, the compressed bitstream 0001 could be de-compressed as “cccd”, “ccb”, “acd”, or “ab”.

## Huffman Coding Algorithm

The Huffman coding algorithm has two main parts:

1. Build a Huffman Tree from input characters.
2. Traverse the Huffman Tree and assign codes to characters.

### Algorithm

```pseudo
Algorithm Huffman(c)
{
   n = |c|
   Q = c
   for i <- 1 to n-1
   do
   {
       temp <- get node()
       left[temp] = Get_min(Q)
       right[temp] = Get_min(Q)
       a = left[temp]
       b = right[temp]
       f[temp] = f[a] + f[b]
       insert(Q, temp)
   }
   return Get_min(0)
}
```

### Steps to Build Huffman Tree

1. Input is an array of unique characters along with their frequency of occurrences.
2. Create a leaf node for each unique character and build a min heap of all leaf nodes.
3. Extract two nodes with the minimum frequency from the min heap.
4. Create a new internal node with a frequency equal to the sum of the two nodes' frequencies. Make the first extracted node its left child and the other extracted node its right child. Add this node to the min heap.
5. Repeat steps 2 and 3 until the heap contains only one node. The remaining node is the root node, and the tree is complete.

#### Example

| Character | Frequency |
|-----------|-----------|
| a         | 5         |
| b         | 9         |
| c         | 12        |
| d         | 13        |
| e         | 16        |
| f         | 45        |

**Step 1:** Build a min heap with 6 nodes, each representing a single character.

**Step 2:** Extract two minimum frequency nodes, create a new internal node with frequency 5 + 9 = 14.

**Step 3:** Extract two minimum frequency nodes, create a new internal node with frequency 12 + 13 = 25.

**Step 4:** Extract two minimum frequency nodes, create a new internal node with frequency 14 + 16 = 30.

**Step 5:** Extract two minimum frequency nodes, create a new internal node with frequency 25 + 30 = 55.

**Step 6:** Extract two minimum frequency nodes, create a new internal node with frequency 45 + 55 = 100.

The min heap now contains only one node with a frequency of 100, which is the root of the Huffman Tree.

### Steps to Print Codes from Huffman Tree

1. Traverse the tree starting from the root.
2. Maintain an auxiliary array.
3. While moving to the left child, write 0 to the array. While moving to the right child, write 1 to the array.
4. Print the array when a leaf node is encountered.

#### Example

The codes for the characters are:

| Character | Code-word |
|-----------|-----------|
| f         | 0         |
| c         | 100       |
| d         | 101       |
| a         | 1100      |
| b         | 1101      |
| e         | 111       |

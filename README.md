# Binary search Tree and Image Editor
Implemented Binary search Tree and build an Image editor
[Problem Statement](https://github.com/amangupt01/Binary-search-Tree-and-Image-Editor-/blob/master/COL100%20Assignment.pdf)

## Part 1 : Binary Search Tree (Magiclist.py)
Implemented a Binary search tree having the following in built function :
* finfMin : Returns the minimun element of the tree 
* insert : Inserts an element into the tree
* deletemin : Deletes the minimum element of the Tree 
* k-sum : Takes a list an input and returns the sum of the smallest k elements of the list . This is done using a binary search tree  

## Part 2 : Image Editor(Pgm.py)
The image editor can perform the following function on a pgm(Grey Scale) image :
* Averaging Filter : This function is used to blur the image by replacing each pixel by average of pixels surrounding that cell. 
* Edge Detection : This function detects the sudden change of pixel in an image so as to detect the Boundary of an object in the image . This is done by wrapping the image and the normalizing the gradient image .
* Path of least energy: In this function we find the path of least energy in the image so that we can crop the unnecessary parts of photo and focusing on main parts(Seam Carving) . This is done by Dynamic programming algorithm , following the top-bottom and bottom-up approach .  

Sample pgm images have been provided on this repository to test the Image Editor .

## Motivation
This small script was made so that I can:
1. Practice using PyCParser
2. Have some more hands-on work with abstract syntax trees


## Limitations
I really haven't looked into analyzying recursive functions, and I'm not super confident on whether or not this tool would be useful for it.
The script is mainly looking at the AST, ignoring anything that isn't some looping node, and then finding the weight of every looping block.

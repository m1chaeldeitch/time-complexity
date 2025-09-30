## Motivation
This small script was made so that I can:
1. Practice using PyCParser
2. Have some more hands-on work with abstract syntax trees


## Limitations
I really haven't looked into analyzying recursive functions, and I'm not super confident on whether or not this tool would be useful for it.
The script is mainly looking at the AST, ignoring anything that isn't some looping node, and then finding the weight of every looping block.
It's also worth noting as an extension to the lack recursive analysis, the deeper rooted issue likely lies with the fact that the script fails
to look into method calls. So if main contains no base looping structures, but calls some function "loop()" which has a single while-loop, the
script will present loop() has being "O(n^1)" and main() as "O(n^0)".

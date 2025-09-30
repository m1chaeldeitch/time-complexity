import sys
import pycparser
from numpy.f2py.crackfortran import endifs
from pycparser.c_ast import Return as return_node
from pycparser.c_ast import For as for_node
from pycparser.c_ast import While as while_node
from pycparser.c_ast import DoWhile as do_while_node



def ast_from_file(filename):
    return pycparser.parse_file(filename)

def find_all_func(ast):
    funcs = []
    for node in ast.children():
        if node[1].decl.name is not None:
            print(node[1].decl.name)
            funcs.append(node[1])

    return funcs


def create_nodes(function_list):
    nodes = []
    for funct in function_list:
        nodes.append(NodeAnalysis(funct))

    return nodes


# noinspection SpellCheckingInspection
def analyze_node(node):

    ## ATTEMPT 1
    # itern = node.node
    #
    # while itern is not None:
    #     if itern.children() is not None:
    #         for child in itern.children():
    #             if child[0] == 'for' or child[0] == 'while':
    #                 print("Found a loop")
    #                 analyze_further(child, 1)
    #             elif child[0] == 'body':
    #                 itern = child
    #                 break
    #             elif child[0] == 'block_items':
    #                 itern = child
    #                 break
    #         stop = '0'


    #ATTEMPT 2
    iter_n = node.node.body.block_items
    secondaryCount = 0

    while iter_n is not None:
        found = False
        for item in iter_n:
            if (isinstance(item, for_node) or
                    isinstance(item, while_node) or isinstance(item, do_while_node)):
                node.increment_complexity()
                iter_n = item.stmt.block_items
                found = True
                break
        if not found:
            break
    return node.get_complexity()


def analyze_further(node, count):
    x = 'balls'


class NodeAnalysis:
    def __init__(self, node):
        self.big_oh = 0
        self.node = node

    def increment_complexity(self):
        self.big_oh += 1

    def get_complexity(self):
        return self.big_oh


if __name__ == '__main__':
    #Create AST from source file...
    ast = ast_from_file('colors.c')

    #Identify and store all function nodes
    functions = find_all_func(ast)
    # for func in functions:
    #     if func.decl.name == "alvin":
    #         print('success')

    #Create analysis objects from all the function nodes
    analyses = create_nodes(functions)
    #analyze_node(analyses[0])
    x = analyze_node(analyses[0])
print('end')
ast.show()


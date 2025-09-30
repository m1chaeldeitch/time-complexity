import pycparser
from pycparser.c_ast import For as for_node
from pycparser.c_ast import While as while_node
from pycparser.c_ast import DoWhile as do_while_node



def ast_from_file(filename):
    return pycparser.parse_file(filename)

def find_all_func(ast):
    funcs = []
    for node in ast.children():
        if node[1].decl.name is not None:
            #print(node[1].decl.name)
            funcs.append(node[1])

    return funcs


def analyze_function(function):
    #Traverse through the function body and see its different components
    body = function.body.block_items

    #For each looping node within this function, call a recursive inspection method
    #to total the weight for all looping nodes
    node_weights = []
    for item in body:
        if isinstance(item, for_node or while_node or do_while_node):
            node_weights.append(analyze_further(item, 1))

    #Analyze results to see which node was the heaviest, and the weight of that node
    if not node_weights:
        return 0
    return max(node_weights)


def analyze_further(looping_node, count):
    #Base case is that the looping_node has no loop within it
    body = looping_node.stmt.block_items

    if not any(isinstance(item, for_node or while_node or do_while_node) for item in body):
        return count

    #Reursive case
    # 1) Get the weights of all of its children looping_nodes
    children_weights = []
    for item in body:
        if isinstance(item, for_node or while_node or do_while_node):
            children_weights.append(analyze_further(item, count + 1))

    # 2) Compare to see what the max weight of all the children are
    return max(children_weights)

if __name__ == '__main__':
    #Create AST from source file...
    ast = ast_from_file('colors.c')

    #Identify and store all function nodes
    functions = find_all_func(ast)

    #Analyze each function
    function_complexities = {}

    for funct in functions:
        function_complexities[funct] = analyze_function(funct)

    #Output
    print('FUNCTION NAME\tCOMPLEXITY')
    for item in function_complexities:
        print(f'{item.decl.name}\t\t\tO(n^{function_complexities[item]})')
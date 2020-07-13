#Pass by value or reference??

#---------------- Mutable datatype -------------------------------------
print("\n------------Experiment with List---------------------")
global_scope_list = ['Welcome','to','boot','camp']

def modify_list(incoming_list):
    incoming_list.append("2020")
    print("List inside modify_list:", incoming_list)

modify_list(global_scope_list)
print("List at global scope:", global_scope_list)

#---------------- Immutable datatype -------------------------------------
print("\n------------Experiment with Tuple---------------------")
global_scope_tuple = ('Welcome','to','boot','camp')

def modify_tuple(incoming_tuple):
    incoming_tuple = ("Virtual","bootcamp")
    print("Tuple inside modify_tuple:", incoming_tuple)

modify_tuple(global_scope_list)
print("Tuple at global scope:", global_scope_tuple)

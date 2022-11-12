
# def favorite_food(*args):
#     #print(args, type(args))
#     add=0
#     for i in args:
#          add+=i
#     return add
# print(favorite_food( 9, 9, 9, 9) )



# payload = {
#      'title': 'Calladita',
#      'artist': 'Bad bunny',
#      'album': 'quien sabe',
#      'genre' : 'arte',
#     }
# def favorite_song(**songs)->str:
#     return f'the song is {songs} for type {type( songs)}'

# print(favorite_song(**payload))


# try:
#      print(1/1)
# except ZeroDivisionError:
#     print('No se puede dividir entre cero.')
# else:
#     print('No se genero exception!!')
# finally:
#     print ("siempre se ejecuta")


# class AcademloStudentSleepingError(Exception):
#     def _init_(self) -> None:
#         super(). init_("Se ejecuta cuando un estudiante de academlo se esta durmiendo")
# if 5 > 8:
#     print('wow')
# else:
#      raise AcademloStudentSleepingError


# from collections. abc import Sequence
# def decimal_to_binary(no_of_variable: int, minterms: Sequence [float]) -> list[str]:
#   """
#   >>>decimal_to_binary(3, [1.5])
#   ['0.00.01.5']
#   """
#   temp = []                               #constante O(1)
#   for minterm in minterms:                #lineal O(n)
#     string = ""
#     for i in range(no_of_variable):       #lineal O(n^2)
#       string = str(minterm & 2) + string  #lineal O(n^2)
#       minterm //= 2                       #lineal O(n^2)
#       temp.append(string)                 #lineal O(n^2)
#   return temp                             #lineal O(n)

# # algoritmo De complejidad O(n^4)

# def bin_exp_mod(a, n, b):
#   """
#   >>> bin_exp_mod(3, 4, 5)
#   1
#   >>> bin_exp_mod(7, 13, 10)
#   7
#   """
#   # mod b
#   assert not (b == 0), " This cannot accept modulo that is == 0" #constante O(1)
#   if n == 0:                                                     #constante O(1)
#     return 1                                                     #constante O(1)
#   if n % 2 == 1:                                                 #constante O(1)
#     return (bin_exp_mod(a, n - 1, b) * a) % b                    #lineal O(n)
#   r = bin_exp_mod(a, n / 2, b)                                   #lineal O(n)
#   return (r * r) % b                                             #constante O(1)

# # algoritmo De complejidad O(n^2) cuadrática


# def imprimir(*caracter):
#   return print(*caracter)

# data = [4,6,7,8,45,2,4,4,1,4,5,68,89,2,433,21,4,3,2,13.45,3,11]
# for x in data:
#     for y in data:
#        imprimir(x, y)


# from dataclasses import dataclass

# @dataclass
# class Queue:

#     items = []
#     limit = 10

#     def add(self, e):

#         if len(self.items)<self.limit:
#             self.items.insert(len(self.items), e)
#             return True
#         return False

#     def element(self):
#         return self.items[0]

#     def offer1(self, e):
#         self.items.insert(len(self.items), e)
#         return True

#     def offer2(self, e):
#         if len(self.items)>=self.limit:
#             del self.items[-1]
#             self.items.insert(len(self.items), e)
#             return True
#         return False

#     def peek(self):

#         if len(self.items)==0:
#             return None
#         return self.items[0]

#     def poll(self):
#         if len(self.items)==0:
#             return None
#         aux = self.items[0]
#         del self.items[0]
#         return aux

#     def remove(self):
#         aux = self.items[0]
#         del self.items[0]
#         return aux

#     def size(self):
#         return len(self.items)

#     def is_empty(self):
#         return len(self.items)==0

# queue = Queue()

# # print(queue.peek())
# print(queue.is_empty())
# #print(queue.add(9))
# queue.add(10)
# queue.add(11)
# queue.add(12)
# queue.add(13)
# queue.add(14)
# queue.add(15)
# queue.add(16)
# queue.add(17)
# queue.add(18)
# queue.add(19)
# queue.add(20)

# print(queue.add(21))
# print(queue.offer1(22))
# print(queue.offer2(23))

# print(queue.items)
# print(queue.peek())

# print(queue.poll())
# print(queue.items)

# print(queue.remove())
# print(queue.items)

# print(queue.size())
# print(queue.is_empty())




# class Tree:

#     def __init__(self, key) -> None:
        
#         self.val = key
#         self.left = None
#         self.right = None


# def insert(root, key):

#     if root is None:
#         return Tree(key)
    
#     else:
#         if root.val == key:
#             return root
#         elif root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
    
#     return root

# def preorder(root):
#     if root:
#         print(root.val)
#         preorder(root.left)
#         preorder(root.right)


# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)


# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val)

# def search(root, key):
#     if root is None or root.val==key:
#         return root

#     if root.val < key:
#         return search(root.right, key)
    
#     return search(root.left, key)

# root = Tree(15)

# root = insert(root, 6)
# root = insert(root, 20)
# root = insert(root, 3)
# root = insert(root, 9)
# root = insert(root, 18)
# root = insert(root, 24)
# root = insert(root, 1)
# root = insert(root, 4)
# root = insert(root, 7)
# root = insert(root, 12)
# root = insert(root, 17)





# # print(f'search')
# print(f'inorder')
# inorder(root)

# print(f'preorder')
# preorder(root)

# print(f'postder')
# postorder(root)

# # print(search(root, 81) is not None)


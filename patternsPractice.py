# for x in range(0, 5):
#     print("\n")
#     for y in range(0, 5):
#         print ("*", end=" ")
# * * * * * 

# * * * * * 

# * * * * * 

# * * * * * 

# * * * * * 

# for x in range(1, 6):
#     print("\n")
#     for y in range(x):
#         print("*", end=" ")

# * 

# * * 

# * * * 

# * * * * 

# * * * * * 


# for x in range(1, 6):
#     print("\n")
#     for y in range(1, x+1):
#         print(y, end=" ")

# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 

# 1 2 3 4 5 

# for x in range(1, 6):
#     print("\n")
#     for y in range(1, x+1):
#         print(x, end=" ")

# 1 

# 2 2 

# 3 3 3 

# 4 4 4 4 

# 5 5 5 5 5 

# for x in range(0, 5):
#     print("\n")
#     for y in range(x, 5):
#         print("*", end=" ")

# * * * * * 

# * * * * 

# * * * 

# * * 

# * 

# for x in range(6, 1, -1):
#     print("\n")
#     for y in range(1, x):
#         print(y, end=" ")

# 1 2 3 4 5 

# 1 2 3 4 

# 1 2 3 

# 1 2 

# 1 

# for x in range(0, 5):
#     print("\n")
#     for y in range(4-x):
#         print(" ", end=" ")
#     for y in range(x*2+1):
#         print("*", end=" ")
#     for y in range(4-x):
#             print(" ", end=" ")

#         *         

#       * * *       

#     * * * * *     

#   * * * * * * *   

# * * * * * * * * * 

# for x in range(0, 5):
#     print("\n")
#     for y in range(4-x):
#         print(" ", end=" ")
#     for y in range(x*2+1):
#         print("*", end=" ")
#     for y in range(4-x):
#         print(" ", end=" ")
# for x in range(0, 5):
#     print("\n")
#     for y in range(x):
#         print(" ", end=" ")
#     for y in range(9-x*2):
#          print("*", end=" ")
#     for y in range(x):
#             print(" ", end=" ")

#         *         

#       * * *       

#     * * * * *     

#   * * * * * * *   

# * * * * * * * * * 

# * * * * * * * * * 

#   * * * * * * *   

#     * * * * *     

#       * * *       

#         *       

# for x in range(1, 6):
#     print("\n")
#     for y in range(x):
#         print("*", end=" ")
# for x in range(0, 5):
#     print("\n")
#     for y in range(4-x):
#         print("*", end=" ")

# * 

# * * 

# * * * 

# * * * * 

# * * * * * 

# * * * * 

# * * * 

# * * 

# * 

# for x in range(1, 6):
#     print("\n")
#     for y in range(x):
#         if(y % 2 == 0):
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
# 1 

# 1 0 

# 1 0 1 

# 1 0 1 0 

# 1 0 1 0 1 

# for x in range(1, 5):
#     print("\n")
#     for y in range(x):
#         print(y+1, end=" ")
#     for y in range(8-2*x):
#         print(" ", end=" ")
#     for y in range(x, 0, -1):
#         print(y, end=" ")
# 1             1 

# 1 2         2 1 

# 1 2 3     3 2 1 

# 1 2 3 4 4 3 2 1 

# num = 1
# for x in range(0, 5):
#     print("\n")
#     for y in range(x+1):
#         print(num, end=" ")
#         num+= 1
# 1 

# 2 3 

# 4 5 6 

# 7 8 9 10 

# 11 12 13 14 15 

# for x in range(5, 0, -1):
#     print("\n")
#     for y in range(ord('A'), ord('A')+x):
#         print(chr(y), end=" ")
# A B C D E 

# A B C D 

# A B C 

# A B 

# A 

# for x in range(ord("A"), ord("E")+1):
#     print("\n")
#     for y in range((x-(ord("A")-1))):
#         print(chr(x), end=" ")
# A 

# B B 

# C C C 

# D D D D 

# E E E E E 

# for x in range(0, 4):
#     print("\n")
#     for y in range(4-x):
#         print(" ", end=" ")
#     for y in range(ord('A'), ord('A')+x+1):
#         print(chr(y), end=" ")
#     for y in range(ord('A')+x, ord('A'), -1):
#         print(chr(y-1), end=" ")

#         A 

#       A B A 

#     A B C B A 

#   A B C D C B A 


# for x in range(5):
#     print("\n")
#     for y in range(ord('E')-x, ord('F')):
#         print(chr(y), end=" ")

# E 

# D E 

# C D E 

# B C D E 

# A B C D E 

# for x in range(0, 5):
#     print("\n")
#     for y in range(5-x):
#         print("*", end=" ")
#     for y in range(2*x):
#         print(" ", end=" ")
#     for y in range(5-x):
#         print("*", end=" ")
# for x in range(1, 6):
#     print("\n")
#     for y in range(x):
#         print("*", end=" ")
#     for y in range(2*(5-x)):
#         print(" ", end=" ")
#     for y in range(x):
#         print("*", end=" ")

# * * * * * * * * * * 

# * * * *     * * * * 

# * * *         * * * 

# * *             * * 

# *                 * 

# *                 * 

# * *             * * 

# * * *         * * * 

# * * * *     * * * * 

# * * * * * * * * * * 
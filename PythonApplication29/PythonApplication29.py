import random
from debugprint import Debug
import time
loop = True
global dim3
def func1():
    i = 0
    array = []
    attempt2 = 0
    j = 0
    attempt = 0
    temp = 0
    x0 = []
    x1 =[]
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    y1 = []
    y2 = []
    y3=[]
    dim3 = 0
    drake = 0
    topaz = 0
    store1 = []
    store2 = []
    store3 = []
    ez =0
    store4 =[]
    store5 = []
    store6 = []
    store7 = []
    store8 = []
    holder = 0
    dim = []
    code1= True
    n =0
    idk = 0
    lol2 = 0
    array3 =[]
    global y
    array2 = []
    placeholder = 0
    brrr= 0
    loopy =True
    code = True
    k =0
    x = str("arr")
    z = str("arr")
    print("\nThis is a matrix generator")
    menu = input("1. Choose matrices' dimensions \n2. Random dimensions\n3. Can you multiply these matrices?\n4. Multiplication with matrices practice\n5. Find the determinant of this random matrix\n6.Find the Inverse of a matrix\n\n")
    if menu.isdigit() and 1<= int(menu) <=7:
        menu = int(menu)
    else:
        print("\nError, Please enter a number from 1 to 6")
        time.sleep(1)
        func1()
    if menu == 1:
        dim = input("Please enter the dimensions you want for the matrix with a space between each character\n")
        dim = dim.split(" ")
        while True:
            if dim[0].isdigit() and dim[2].isdigit and dim[1]=="x":
                break
            else:
                print("Please enter a valid input such as 3 x 2 with a space between each character")
        for i in range (0,int(dim[0])):
            y = str(i)
            x += y
            x = []
            for j in range (0,int(dim[2])):
                (x).append(random.randint(0,9))
                if len(x) == int(dim[2]):
                    print(x)
    elif menu == 2:
        while True:
            l = input("What do you want the max number of rows or columns to be? ")
            if l.isdigit():
                l = int(l)
                break
            else:
                print("\nPlease enter a valid number")
                func1()


        dim1 = random.randint(2,l)
        dim2 = random.randint(2,l)#
        while True:
            maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
            if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                maxsize = int(maxsize)
                break
            else:
                print("Please enter a valid number")
        if maxsize == 1:
            digit = 10
        elif maxsize == 2:
            digit = 100
        for i in range (0,int(dim1)):
            y = str(i)
            x += y
            x = []
            for j in range (0,int(dim2)):
                (x).append(random.randint(0,digit))
                if len(x) == int(dim2):
                    print(x)        

    elif menu == 3:
        que = input("Would you like to choose the dimensions?\n\n")
        if que == "Yes":
            while True:
                dim = input("Please enter the dimensions you want for the matrix with a space between each character\n")
                dim = dim.split(" ")
                if dim[0].isdigit() and dim[1]=="x"and dim[2].isdigit():
                    l = int(l)
                    break
                else:
                    print("\nPlease enter in the correct form such as 3 x 4 ")
            while True:
                maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
                if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                    maxsize = int(maxsize)
                    break
                else:
                    print("Please enter a valid number")
            if maxsize == 1:
                digit = 10
            elif maxsize == 2:
                digit = 100

            for i in range (0,int(dim[0])):
                y = str(i)
                x += y
                x = []
                for j in range (0,int(dim[2])):
                    (x).append(random.randint(0,digit))
                    if len(x) == int(dim[2]):
                        array.append(x)
            while True:
                dim1 = input("Please enter the dimensions you want for the matrix with a space between each character\n")
                dim1 = dim1.split(" ")
                if dim[0].isdigit() and dim[1]=="x"and dim[2].isdigit():
                    l = int(l)
                    break
                else:
                    print("\nPlease enter in the correct form such as 3 x 4 ")

 
            for i in range (0,int(dim1[0])):
                y = str(i)
                x += y
                x = []
                for j in range (0,int(dim1[2])):
                    (x).append(random.randint(0,digit))
                    if len(x) == int(dim1[2]):
                        store4.append(x)
            #dim[0] == dims
            #dim[2] == dim3
            #dim1[0] == dim1
            #dim1[2] == dim2 
            i=0
            for i in range (0,len(array)):
                if len(array[i]) > int(dim[2]):
                    array[i].pop()
                print(array[i])
            i=0
            print("\n\n")
            for i in range (0,len(store4)):
                if len(store4[i]) > int(dim1[2]):
                    store4[i].pop()
                print(store4[i])
                


            ques = input("Can these two arrays be multiplied?")
            if ques == "No":
                if int(dim1[0]) == int(dim[2]):
                    if int(dim[0]) == int(dim1[2]):
                        print("You are incorrect, they can be multiplied")
                else:
                    print("You're correct, they cannot be multiplied")
            elif ques == "Yes":
                if int(dim1[0]) == int(dim[2]):
                    if int(dim[0]) == int(dim1[2]):
                        print("You are correct, they can be multiplied")
                else:
                    print("You're incorrect, they cant be multiplied")
            time.sleep(1.5)
            code = False


        
        elif que == "No":
            w = 0
            while code == True:
                while True:
                    l = input("What do you want the max number of rows or columns to be? ")
                if l.isdigit():
                    l = int(l)
                    break
                else:
                    print("\nPlease enter a valid number")
                while True:
                    maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
                    if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                        maxsize = int(maxsize)
                        break
                    else:
                        print("Please enter a valid number")
                if maxsize == 1:
                    digit = 10
                elif maxsize == 2:
                    digit = 100
                #makes num of rows
                for brrr in range (0,2):
                    if brrr == 0:
                        dims = random.randint(2,l)
                        dim3 = random.randint(2,l)

                        for i in range (0,int(dims)):
                            #dim1 = num of rows
                            #dim2 = size of row
                            y = str(i)
                            x += y
                            x = []
                            for j in range (0,int(dim3)):
                                #adds nums to arrays/ rows
                                (x).append(random.randint(0,digit))
                                if len(x) == int(dim3):
                                    array.append(x) 
                    elif brrr == 1:
                        dim1 = random.randint(2,l)
                        dim2 = random.randint(2,l)
                        for i in range (0,int(dim1)):
                            #dim1 = num of rows
                            #dim2 = size of row

                            drake = int(y)+int(i)
                            x += y
                            x = []
                            for j in range (0,int(dim2)):
                                #adds nums to arrays/ rows
                                (x).append(random.randint(0,digit))
                                if len(x) == int(dim2):
                                    store4.append(x) 


                
                for i in range (0,len(array)):
                    if len(array[i]) > dim3:
                        array[i].pop()
                    print(array[i])

                print("\n\n")
                for i in range (0,len(store4)):
                    if len(store4[i]) > dim2:
                        store4[i].pop()
                    print(store4[i])
                


                ques = input("Can these two arrays be multiplied?")
                if ques == "No":
                    if dim1 == dim3:
                        if dims == dim2:
                            print("You are incorrect, they can be multiplied")
                    else:
                        print("You're correct, they cannot be multiplied")
                elif ques == "Yes":
                    if dim1 == dim3:
                        if dims == dim2:
                            print("You are correct, they can be multiplied")
                    else:
                        print("You're incorrect, they cant be multiplied")
                time.sleep(1.5)
                code = False
                            
      
    elif menu == 4:
        que = input("Would you like to choose the dimensions?\n\n")
        if que == "Yes":
            dim = input("Please enter the dimensions you want for the matrix with a space between each character\n")
            dim = dim.split(" ")
            while True:
                if dim[0].isdigit() and dim[2].isdigit and dim[1]=="x":
                    break
                else:
                    print("Please enter a valid input such as 3 x 2 with a space between each character")

            for i in range (0,int(dim[0])):
                y = str(i)
                x += y
                x = []
                for j in range (0,int(dim[2])):
                    (x).append(random.randint(0,9))
                    if len(x) == int(dim[2]):
                        array.append(x)
            dim1 = input("Please enter the dimensions you want for the 2nd matrix with a space between each character\n")
            dim1 = dim1.split(" ")
            while True:
                if dim1[0].isdigit() and dim1[2].isdigit and dim1[1]=="x":
                    break
                else:
                    print("Please enter a valid input such as 3 x 2 with a space between each character")
            while True:
                maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
                if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                    maxsize = int(maxsize)
                    break
                else:
                    print("Please enter a valid number")
            if maxsize == 1:
                digit = 10
            elif maxsize == 2:
                digit = 100
            if dim1[0] == dim[2] and dim[0] == dim1[2] :
                for i in range (0,int(dim1[0])):
                    y = str(i)
                    x += y
                    x = []
                    for j in range (0,int(dim1[2])):
                        (x).append(random.randint(0,digit))
                        if len(x) == int(dim1[2]):
                            store4.append(x)
            else:
                print("These arrays with these dimensions cannot be multiplied")
            #dim[0] == dims
            #dim[2] == dim3
            #dim1[0] == dim1
            #dim1[2] == dim2 
            i=0
            for i in range (0,len(array)):
                if len(array[i]) > int(dim[2]):
                    array[i].pop()
                print(array[i])
            i=0
            print("\n\n")
            for i in range (0,len(store4)):
                if len(store4[i]) > int(dim1[2]):
                    store4[i].pop()
                print(store4[i])
            #print(store1)
            #print(store2)
            i = 0
            j=0
            #print(str(dim1))
            #print(str(dim2))
            #print(str(dims))
            #dim[0](num of rows)[2] (size of rows) is original matrix dim1 is 2nd matrix
            #dims(num of rows) and dim3(size of row) is original, dim1(num of rows) and 2(size of row) is 2nd matrix
            #print(dim[0])
          #  print(dim[2])
            if dim1[0] < dim[0]:
                dim[0] = dim1[0]
                #print(str(dim3))
            if dim1[2] < dim[2]:
                back = int(dim1[2])
            #print(dim[0])
           # print(dim[2])
            dim2 = int(dim[0])
            dim3 = int(dim[2])
            x = x
            for k in range (0,back):
                #print("hi")
                for j in range(0,dim2):
                    for i in range(0, dim3):                               
                            add = array[j][i]*store4[i][k]
                            #print(str(array[j][i])+" x "+str(store4[i][k])+ " = " +str(add))
                            holder += add
                    store3.append(holder)
                    holder = 0
                #print(store3)
              #  print(store3)
                for t in range(0,back):
                    if t == 0:
                        x0.append(store3[t])
                    elif t ==1:
                        x1.append(store3[t])
                    elif t ==2:
                        x2.append(store3[t])
                    elif t ==3:
                        x3.append(store3[t])
                    elif t ==4:
                        x4.append(store3[t])
                    elif t == 5:
                        x5.append(store3[t])
                    elif t == 6:
                        x6.append(store3[t])
                store3.clear()

            code = False
            print("\n\n")
            if len(x0)>0:
                print(x0)
            if len(x1)>0:
                print(x1)
            if len(x2)>0:
                print(x2)
            if len(x3)>0:
                print(x3)
            if len(x4)>0:
                print(x4)
            if len(x5)>0:
                print(x5)
            if len(x6)>0:
                print(x6)




        elif que == "No":
            w = 0
            while code == True:

                l = int(input("What do you want the max number of rows or columns to be? "))
                while code1 == True:
                    dims = random.randint(2,l)
                    dim3 = random.randint(2,l)
                    dim1 = random.randint(2,l)
                    dim2 = random.randint(2,l)
                    if dim3 <= dim2:
                        if dim1 == dim3:
                            if dim2 == dims:
                                code1 = False

                while True:
                    maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
                    if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                        maxsize = int(maxsize)
                        break
                    else:
                        print("Please enter a valid number")
                if maxsize == 1:
                    digit = 10
                elif maxsize == 2:
                    digit = 100
                #makes num of rows
                for brrr in range (0,2):
                    if brrr == 0:
                        for i in range (0,int(dims)):
                            #dims = num of rows
                            #dim3 = size of row
                            y = str(i)
                            x += y
                            x = []
                            for j in range (0,int(dim3)):
                                #adds nums to arrays/ rows
                                (x).append(random.randint(0,digit))
                                if len(x) == int(dim3):
                                    array.append(x)
                    elif brrr == 1:
                        for i in range (0,int(dim1)):
                            #dim1 = num of rows
                            #dim2 = size of row

                            drake = int(y)+int(i)
                            x += y
                            x = []
                            for j in range (0,int(dim2)):
                                #adds nums to arrays/ rows
                                (x).append(random.randint(0,digit))
                                if len(x) == int(dim2):
                                    store4.append(x)


                

                i=0
                for i in range (0,len(array)):
                    if len(array[i]) > dim3:
                        array[i].pop()
                    print(array[i])
                i=0
                print("\n\n")
                for i in range (0,len(store4)):
                    if len(store4[i]) > dim2:
                        store4[i].pop()
                    print(store4[i])
                #print(store1)
                #print(store2)
                i = 0
                j=0
                #print(str(dim1))
               # print("hi")
                #print(str(dim3))
               # print(str(dim2))
                #print(str(dims))
                if dim1 < dims:
                    dims = dim1
                if dim2 < dim3:
                    dim3 = dim2
                print(str(dim3))
                print(str(dim2))
                #dim2 is number of rows
                #dim3 is size of rows
                for k in range (0,dim3):
                    for j in range(0,dim2):
                        for i in range(0, dim3):                               
                                add = array[j][i]*store4[i][k]
                                print(str(array[j][i])+" x "+str(store4[i][k])+ " = " +str(add))
                                holder += add
                        store3.append(holder)
                        holder = 0
                    #print(store3)
                    for t in range(0,dim3):
                        if t == 0:
                            x0.append(store3[t])
                        elif t ==1:
                            x1.append(store3[t])
                        elif t ==2:
                            x2.append(store3[t])
                        elif t ==3:
                            x3.append(store3[t])
                        elif t ==4:
                            x4.append(store3[t])
                        elif t == 5:
                            x5.append(store3[t])
                        elif t == 6:
                            x6.append(store3[t])
                    store3.clear()


                code = False
                print("\n\n")
                if len(x0)>0:
                    print(x0)
                if len(x1)>0:
                    print(x1)
                if len(x2)>0:
                    print(x2)
                if len(x3)>0:
                    print(x3)
                if len(x4)>0:
                    print(x4)
                if len(x5)>0:
                    print(x5)
                if len(x6)>0:
                    print(x6)

    if menu == 5:
        dim = input("\nPlease enter the dimensions you want for the matrix with a space between each character (either 2 x 2 or 3 x 3)\n")
        dim = dim.split(" ")
        while True:
            if dim[0].isdigit() and dim[1]=="x"and dim[2].isdigit():
                l = int(l)
                break
            else:
                print("\nPlease enter in the correct form such as 3 x 4 ")
            while True:
                maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
                if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                    maxsize = int(maxsize)
                    break
                else:
                    print("Please enter a valid number")
            if maxsize == 1:
                digit = 10
            elif maxsize == 2:
                digit = 100
            for i in range (0,int(dim[0])):
                y = str(i)
                x += y
                x = []
                for j in range (0,int(dim[2])):
                    (x).append(random.randint(0,digit))
                    if len(x) == int(dim[2]):
                        print(x)
                        store1.append(x)


        else:
            print("You can only find the determinant of a square matrix ")
        if int(dim[0]) ==2:
            multiplied = (store1[0][0]*store1[1][1])-(store1[0][1]*store1[1][0])
            print(str(multiplied))
        if int(dim[0]) == 3:
            for i in range(0,len(x)):
                pack = [1,2]
                pack2 = [0,1,2]
                pack2.pop(int(i))
                n1 = pack2[0]
                n2 = pack2[1]
                if i ==1:
                   # print(str(store1[0][i]) + " * (" +str(store1[1][int(n1)])+ " * "+str(store1[2][int(n2)])+" -( "+str(store1[2][int(n1)])+" * "+str(store1[1][int(n1)+2])+ ")")
                    sumdet = int(store1[0][i])*((((store1[1][int(n1)])))*(store1[2][int(n2)])-((store1[2][int(n1)])*(store1[1][int(n1)+2])))
                else:
                    #print(str(store1[0][i]) + " * (" +str(store1[1][int(n1)])+ " * "+str(store1[2][int(n2)])+" -( "+str(store1[2][int(n1)])+" * "+str(store1[1][int(n1)+1])+")")
                    sumdet = int(store1[0][i])*((((store1[1][int(n1)])))*(store1[2][int(n2)])-((store1[2][int(n1)])*(store1[1][int(n1)+1])))
                print(" = "+str(sumdet))
                x1.append(sumdet)
        determin = int(x1[0])-int(x1[1])+int(x1[2])
        det = int(input("Find the determinant of this matrix"))
        if det == determin:
            print("You are right, the determinant is "+ str(determin))
        else:
            print("You are incorrect, the determinant is "+ str(determin))

    if menu == 6:
        dim = input("\nPlease enter the dimensions you want for the matrix with a space between each character (either 2 x 2 or 3 x 3)\n")
        dim = dim.split(" ")
        while True:
            if dim[0].isdigit() and dim[1]=="x"and dim[2].isdigit():
                l = int(l)
                break
            else:
                print("\nPlease enter in the correct form such as 3 x 4 ")
        while True:
            maxsize = input("What do you want the maximum number of digits per number to be?(2 or 1)")
            if maxsize.isdigit() and 1 <= int(maxsize) <=2:
                maxsize = int(maxsize)
                break
            else:
                print("Please enter a valid number")
        if maxsize == 1:
            digit = 10
        elif maxsize == 2:
            digit = 100
        print("\n")
        Debug("Hello")
        if int(dim[0])>3 or int(dim[0])<2:
            print("Please enter either 2 x 2 or 3 x 3 in that form")
            func1()
        if int(dim[0]) == int(dim[2]):
            if isinstance(dim[0], int):
                print("Please enter in the form such as 3 x 3 ")

            for i in range (0,int(dim[0])):
                y = str(i)
                x += y
                x = []
                for j in range (0,int(dim[2])):
                    (x).append(random.randint(0,digit))
                    if len(x) == int(dim[2]):
                        print(x)
                        store1.append(x)


        else:
            print("You can only find the Inverse of a square matrix ")
        if int(dim[0]) ==2:
            determin = (store1[0][0]*store1[1][1])-(store1[0][1]*store1[1][0])
        elif int(dim[0]) == 3:
            for i in range(0,len(x)):
                #pack = [1,2]
                #pack2 = [0,1,2]
               # pack2.pop(int(i))
                #n1 = pack2[0]
                #n2 = pack2[1]
                if i ==0:
                    print(str(store1[1][1])+ " * "+str(store1[2][2])+" -( "+str(store1[2][2])+" * "+str(store1[1][2])+ ")")
                    sumdet = ((((store1[1][1])))*(store1[2][2])-((store1[2][1])*(store1[1][2])))

                elif i ==1:
                    print(str(store1[1][0])+ " * "+str(store1[2][2])+" -( "+str(store1[2][0])+" * "+str(store1[1][2])+ ")")
                    sumdet = ((((store1[1][0])))*(store1[2][2])-((store1[2][0])*(store1[1][2])))
                else:
                    print(str(store1[1][0])+ " * "+str(store1[2][1])+" -( "+str(store1[2][0])+" * "+str(store1[1][1])+")")
                    sumdet = ((((store1[1][0])))*(store1[2][1])-((store1[2][0])*(store1[1][1])))
                print(" = "+str(sumdet))
                x1.append(sumdet)
            for i in range(0,len(x)):
              #  pack = [0,2]
              #  pack2 = [0,1,2]
              #  pack2.pop(int(i))
              #  n1 = pack2[0]
              #  n2 = pack2[1]
                if i == 0:
                    print(str(store1[0][1])+ " * "+str(store1[2][2])+" -( "+str(store1[0][2])+" * "+str(store1[2][1])+")")
                    sumdet = ((((store1[0][1])))*(store1[2][2])-((store1[0][2])*(store1[2][1])))
                elif i ==1:
                    print(str(store1[0][0])+ " * "+str(store1[2][2])+" -( "+str(store1[2][0])+" * "+str(store1[0][2])+ ")")
                    sumdet = ((((store1[0][0])))*(store1[2][2])-((store1[2][0])*(store1[0][2])))
                else:
                    print(str(store1[0][0])+ " * "+str(store1[2][1])+" -( "+str(store1[2][0])+" * "+str(store1[0][1])+")")
                    sumdet = ((((store1[0][0])))*(store1[2][1])-((store1[2][0])*(store1[0][1])))
                print(" = "+str(sumdet))
                x2.append(sumdet)
            for i in range(0,len(x)):
                #pack = [0,1]
               # pack2 = [0,1,2]
               # pack2.pop(int(i))
              #  n1 = pack2[0]
              #  n2 = pack2[1]
                if i ==0:
                    print(str(store1[0][1])+ " * "+str(store1[1][2])+" -( "+str(store1[0][2])+" * "+str(store1[1][1])+")")
                    sumdet = ((((store1[0][1])))*(store1[1][2])-((store1[0][2])*(store1[1][1])))
                elif i ==1:
                    print(str(store1[0][0])+ " * "+str(store1[1][2])+" -( "+str(store1[1][0])+" * "+str(store1[0][2])+ ")")
                    sumdet = ((((store1[0][0])))*(store1[1][2])-((store1[1][0])*(store1[0][2])))
                else:
                    print(str(store1[0][0])+ " * "+str(store1[1][1])+" -( "+str(store1[0][1])+" * "+str(store1[1][0])+")")
                    sumdet = (((store1[0][0])*(store1[1][1]))-((store1[0][1])*(store1[1][0])))
                print(" = "+str(sumdet))
                x3.append(sumdet)
            x1[1]=-1*x1[1]
            x2[0]=-1*x2[0]
            x2[2]=-1*x2[2]
            x3[1]=-1*x3[1]
            y1.append(x1[0])
            y1.append(x2[0])
            y1.append(x3[0])
            y2.append(x1[1])
            y2.append(x2[1])
            y2.append(x3[1])
            y3.append(x1[2])
            y3.append(x2[2])
            y3.append(x3[2])
               # print("x3 is "+str(x3))

        for i in range(0,len(x)):
            pack = [1,2]
            pack2 = [0,1,2]
            pack2.pop(int(i))
            n1 = pack2[0]
            n2 = pack2[1]
            if i ==1:
                print(str(store1[0][i]) + " * (" +str(store1[1][int(n1)])+ " * "+str(store1[2][int(n2)])+" -( "+str(store1[2][int(n1)])+" * "+str(store1[1][int(n1)+2])+ ")")
                sumdet = int(store1[0][i])*((((store1[1][int(n1)])))*(store1[2][int(n2)])-((store1[2][int(n1)])*(store1[1][int(n1)+2])))
            else:
                print(str(store1[0][i]) + " * (" +str(store1[1][int(n1)])+ " * "+str(store1[2][int(n2)])+" -( "+str(store1[2][int(n1)])+" * "+str(store1[1][int(n1)+1])+")")
                sumdet = int(store1[0][i])*((((store1[1][int(n1)])))*(store1[2][int(n2)])-((store1[2][int(n1)])*(store1[1][int(n1)+1])))
            print(" = "+str(sumdet))
            x4.append(sumdet)
        determin = int(x4[0])-int(x4[1])+int(x4[2])
        det = int(input("What is the determinant for this matrix? "))
        if det == determin:
            print("correct")
        else:
            print("incorrect, it is "+str(determin))
        for i in range(0,len(y1)):
            attempt = int(input("What is the num "+str(i+1)+" element of the matrix? "))
            if attempt == y1[i]:
                print("correct")
            else:
                print("Incorrect, it should be "+str(y2[i]))
        for i in range(0,len(y2)):
            attempt = int(input("What is the num "+str(i+1)+" element of the matrix? "))
            if attempt == y2[i]:
                print("correct")
            else:
                print("Incorrect, it should be "+str(y2[i]))
        for i in range(0,len(y3)):
            attempt = int(input("What is the num "+str(i+1)+" element of the matrix? "))
            if attempt == y3[i]:
                print("correct")
            else:
                print("Incorrect, it should be "+str(y3[i]))
            
        print("\n\nThe inverse is ")
        if 100 >determin > 10:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"     "+str(y3))
        elif determin > 100:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"   "+str(y3))
        elif 0 <determin < 10:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"      "+str(y3))
        elif determin == 0:
            print("There is no inverse")
        elif 0> determin >-10:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"   "+str(y3))
        elif -10>determin>-100:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"    "+str(y3))
        elif -100 > determin:
            print("1      " + str(y1) + "\n---"+ " X  "+ str(y2)+ "\n"+str(determin)+"   "+str(y3))


        if int(dim[0]) == 2:

            temp = int(store1[0][0])
            temp2 = -1*int(store1[0][1])
            temp3 = -1*int(store1[1][0])
            temp4 = int(store1[1][1])
            store1.clear()
            store2.clear()
            store1.append(temp4)
            store1.append(temp2)

            store2.append(temp3)
            store2.append(temp)
            attempt2= int(input("What is the determinant?"))
            if attempt2 == determin:
                print("You are correct\n")
            else:
                print("Not quite right, the answer is:")
                print(str(determin))
            for i in range(0,4):
                attempt = int(input("What is the num "+str(i+1)+" element of the matrix? "))
                if i < 2:                    
                    if attempt == store1[i]:
                        print("correct")
                        print("\n")
                        time.sleep(1)
                    else:
                        print("Not quite right, it should be:")
                        print(store1[i])
                        print("\n")
                        time.sleep(1)
                elif i >= 2:
                    i = i-2
                    if attempt == store2[i]:
                        print("correct")
                        print("\n")
                        time.sleep(1)
                    else:
                        print("Not quite right, it should be:")
                        print(store2[i])
                        print("\n")
                        time.sleep(1)                 


            time.sleep(1.5)
            print("\n\nThe inverse is ")
            if 100 >determin > 10:
                print("1      " + str(store1) + "\n---"+ " X  "+ str(store2)+ "\n"+str(determin))
            elif determin > 100:
                print("1      " + str(store1) + "\n---"+ " X  "+ str(store2)+ "\n"+str(determin))
            elif determin < 10:
                print("1      " + str(store1) + "\n---"+ " X  "+ str(store2)+ "\n"+str(determin))

      

while True:
    func1()
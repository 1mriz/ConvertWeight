import time
while True:
    print("""
     _____________________________________________________________
    |                                                             |
    |                     Weight Converter                        |
    |_____________________________________________________________|
    """)
    print("""
    Options:
    1) Kilogram to gram
    2) Gram to kilogram
    3) Pound to kilogram
    4) Kilogram to pound
    5) Gram to pound
    6) Pound to Gram
    7) Exit
    """)
    try:
        convert = int(input("Enter an option: "))
        if convert not in [1, 2, 3, 4, 5, 6, 7]:
            print("Invalid option selected. Please try again")
            continue
        else:
           break
    except ValueError:
      print("Invalid option")


while True:
 try:
    if convert == 1:
        k2g = float(input("Enter weight: "))
        if k2g < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{k2g} kilogram(s) in gram(s) is: {k2g * 1000}")
           exit()
    elif convert == 2:
        g2k = float(input("Enter weight: "))
        if g2k < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{g2k} gram(s) in kilogram(s) is: {g2k / 1000}")
           exit()        
    elif convert == 3:
        p2k = float(input("Enter weight: "))
        if p2k < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{p2k} pound(s) in kilogram(s) is: {p2k * 0.45359237}")
           exit()
    if convert == 4:
        k2p = float(input("Enter weight: "))
        if k2p < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{k2p} kilogram(s) in pound(s) is: {k2p / 2.204623}")
           exit()
    elif convert == 5:
        g2p = float(input("Enter weight: "))
        if g2p < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{g2p} gram(s) in pound(s) is: {g2p * 0.00220462}")
           exit()
    elif convert == 6:
        p2g = float(input("Enter weight: "))
        if p2g < 0:
         print("please enter a positive number")
         continue
        else:
           print(f"{p2g} pound(s) in gram(s) is: {p2g * 453.59237}")
           exit()
    elif convert == 7:
       print("Exiting the program...")
       time.sleep(1)
       exit()
 except ValueError:
    print("Please enter a valid number") 


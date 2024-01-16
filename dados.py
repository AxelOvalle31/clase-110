import random

resp = "y"

while resp == "y": 
    no = random.randint(1,6)
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")   
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]") 
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")    
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[    0]")
        print("[     ]")
        print("[0    ]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

    resp = input("Presiona y para rodar de nuevo, presiona n para salir")
    print("\n")
    


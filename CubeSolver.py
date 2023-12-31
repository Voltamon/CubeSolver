import time
import kociemba

class ARCS():
    cube = {"U" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "R" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "F" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "D" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "L" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "B" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]}
    
    def __init__(self):
        pass
    
    def U(self, i):
        for k in range(0, i):
            ctr = "U"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], 
            self.cube[ctr][0][2]], self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["L"][0][j], self.cube["F"][0][j], 
                self.cube["R"][0][j], self.cube["B"][0][j]) = (
                self.cube["F"][0][j], self.cube["R"][0][j], 
                self.cube["B"][0][j], self.cube["L"][0][j])
    
    def D(self, i):
        for k in range(0, i):
            ctr = "D"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], self.cube[ctr][0][2]], 
            self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["L"][2][j], self.cube["F"][2][j], 
                self.cube["R"][2][j], self.cube["B"][2][j]) = (
                self.cube["B"][2][j], self.cube["L"][2][j], 
                self.cube["F"][2][j], self.cube["R"][2][j])

    def L(self, i):
        for k in range(0, i):
            ctr = "L"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], self.cube[ctr][0][2]], 
            self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["U"][j][0], self.cube["F"][j][0], 
                self.cube["D"][j][0], self.cube["B"][2-j][2]) = (
                self.cube["B"][2-j][2], self.cube["U"][j][0], 
                self.cube["F"][j][0], self.cube["D"][j][0])
    
    def R(self, i):
        for k in range(0, i):
            ctr = "R"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], self.cube[ctr][0][2]], 
            self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["U"][j][2], self.cube["F"][j][2], 
                self.cube["D"][j][2], self.cube["B"][2-j][0]) = (
                self.cube["F"][j][2], self.cube["D"][j][2], 
                self.cube["B"][2-j][0], self.cube["U"][j][2])
    
    def F(self, i):
        for k in range(0, i):
            ctr = "F"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], self.cube[ctr][0][2]], 
            self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["U"][2][j], self.cube["R"][j][0], 
                self.cube["D"][0][2-j], self.cube["L"][2-j][2]) = (
                self.cube["L"][2-j][2], self.cube["U"][2][j], 
                self.cube["R"][j][0], self.cube["D"][0][2-j])
    
    def B(self, i):
        for k in range( 0, i):
            ctr = "B"
            block = self.cube[ctr][2][2]
            (self.cube[ctr][0], 
            [self.cube[ctr][0][2], self.cube[ctr][1][2], self.cube[ctr][2][2]], 
            self.cube[ctr][2], 
            [self.cube[ctr][0][0], self.cube[ctr][1][0], self.cube[ctr][2][0]]) = (
            [self.cube[ctr][2][0], self.cube[ctr][1][0], self.cube[ctr][0][0]], 
            self.cube[ctr][0], 
            [self.cube[ctr][2][2], self.cube[ctr][1][2], self.cube[ctr][0][2]], 
            self.cube[ctr][2])
            self.cube[ctr][2][0] = block
            
            for j in range(0, 3):
                (self.cube["U"][0][j], self.cube["R"][j][2], 
                self.cube["D"][2][2-j], self.cube["L"][2-j][0]) = (
                self.cube["R"][j][2], self.cube["D"][2][2-j], 
                self.cube["L"][2-j][0], self.cube["U"][0][j])
    
    def move_cube(self, moves):
        move = moves
        move_no = int(move[1])
        
        if move[0] == "U":
            self.U(move_no)
        elif move[0] == "R":
            self.R(move_no)
        elif move[0] == "F":
            self.F(move_no)
        elif move[0] == "D":
            self.D(move_no)
        elif move[0] == "L":
            self.L(move_no)
        elif move[0] == "B":
            self.B(move_no)
        else:
            pass
    
    def scramble(self):
        self.display()
        print()
        
        try:
            print("1> Solve")
            print("2> Return")
            print()
            
            mv = input("Enter move : ")
            print()
            
            if len(mv) < 3:
                if len(mv) == 1:
                    if mv == "1":
                        self.solve()
                    elif mv == "2":
                        self.main()
                    else:
                        mv += "1"
                else:
                    mv = mv.replace("\'", "3")
                
                l = []
                for i in range(1, 4):
                    for j in ["L", "R", "U", "D", "F", "B"]:
                        l.append(str(j + str(i)))
                
                if mv in l:
                    self.move_cube(mv)
                    print()
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input, Try Again")
            
        self.scramble()
    
    def solve(self):
        cube = self.set_clear_state()
        cube_scramble = self.get_cube_state()
        
        try:
            solve_formula = kociemba.solve(cube_scramble)
        except ValueError:
            print("Invalid Input, Re-enter scramble")
            print()
            
            self.cube = cube
            self.get_cube_scramble()
            
        formula = solve_formula.split()
        cube = self.set_solved_state(cube)
        
        if self.cube == cube:
            print("Cube Already Solved !!!")
            print()
            self.main()
        else:
            for i in range(0, len(formula)):
                j = formula[i].replace("\'", "3")
                if len(j) == 1:
                    j += "1"
                
                print()
                print(formula[i])
                print()
                
                self.move_cube(j)
                self.display()
                time.sleep(3)
            
            print("Formula used :", end=" ")
            for j in formula:
                print(j, end=" ")
            print()
            print()
            self.main()
    
    def menu(self):
        print("         ~~~ARCS~~~         ")
        print("Advanced Rubik's Cube Solver")
        print()
        print("1> Scramble a Cube")
        print("2> Solve a Cube")
        print("3> Controls")
        print("4> Exit")
        print()
    
    def set_cube_state(self, cube_str):
        x = 0
        if type(cube_str) == type(list()):
            cube_l = cube_str
            cube_str = ""
            for i in cube_l:
                cube_str += i
        
        l = ["U", "R", "F", "D", "L", "B"]
        for i in l:
            for j in range(0, 3):
                for k in range(0, 3):
                    self.cube[i][j][k] = cube_str[x]
                    x += 1 
    
    def get_cube_state(self):
        cube_str = ""
        l = ["U", "R", "F", "D", "L", "B"]
        for i in l:
            for j in range(0, 3):
                for k in range(0, 3):
                    cube_str += self.cube[i][j][k]
        
        l = [("Y", "U"), ("R", "R"), ("B", "F"), ("W", "D"), ("O", "L"), ("G", "B")]
        for i in l:
            cube_str = cube_str.replace(i[0], i[1])
        
        return cube_str
    
    def get_cube_scramble(self):
        cube_str = self.get_cube_state()
        
        cube_l = cube_str
        cube_str = []
        for i in cube_l:
            cube_str.append(i)
        
        i = 0
        while i < 54:
            while True:
                cube_str[i] = "_"
                self.set_cube_state(cube_str)
                self.display()
                
                print("1> Back")
                print("2> Return")
                print()
                
                ch = input("Enter color : ")
                ch = ch.upper()
                
                print()
                try:
                    if ch in ["Y", "R", "B", "W", "O", "G", "1", "2"]:
                        if ch == "1":
                            cube_str[i] = " "
                            if i == 0:
                                i -= 1
                            else:
                                i -= 2
                        elif ch == "2":
                            self.main()
                        else:
                            cube_str[i] = ch
                        break
                    else:
                        raise ValueError
                except ValueError:                    
                    print("Invalid Input, Try Again")
                    print()
                    continue 
            i += 1
            
        self.set_cube_state(cube_str)
        self.display()
        print()
        self.solve()
    
    def set_clear_state(self):
        return {"U" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                "R" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                "F" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                "D" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                "L" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                "B" : [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]}
    
    def set_solved_state(self, cube):
        l = ["U", "R", "F", "D", "L", "B"]
        col = ["Y", "R", "B", "W", "O", "G"]
        for i in range(0, 6):
            for j in range(0, 3):
                for k in range(0, 3):
                    cube[l[i]][j][k] = col[i]
        
        return cube

    def controls(self):
        print("~~~Moves~~~")
        for i in ["U", "R", "F", "D", "L", "B"]:
            print(f'{i}     {i}2     {i}\'')
        print()
        
        print("~~~Colors~~~")
        print("Y - yellow   |   R - Red")
        print("B - Blue     |   W - White")
        print("O - Orange   |   G - Green")
        print()
        
        self.main()
            
    def display(self):
        for i in range(0, 3):
            print(" "*13, end = "")
            for j in range(0, 3):
                print(f"[{self.cube['U'][i][j]}]", end = " ")
            print()
        print()
        
        for i in range(0, 3):
            for j in range(0, 3):
                print(f"[{self.cube['L'][i][j]}]", end = " ")
            print(end = " ")
            for j in range(0, 3):
                print(f"[{self.cube['F'][i][j]}]", end = " ")
            print(end = " ")
            for j in range(0, 3):
                print(f"[{self.cube['R'][i][j]}]", end = " ")
            print(end = " ")
            for j in range(0, 3):
                print(f"[{self.cube['B'][i][j]}]", end = " ")
            print()
        print()
        
        for i in range(0, 3):
            print(" "*13, end = "")
            for j in range(0, 3):
                print(f"[{self.cube['D'][i][j]}]", end = " ")
            print()
        print()
        
    def main(self):
        self.menu()
        self.cube = self.set_clear_state()
        
        try:
            ch = input("Enter your choice : ")
            ch = ch.strip()
            print()
            
            if ch == "1":
                self.cube = self.set_solved_state(self.cube)
                self.scramble()
            elif ch == "2":
                self.get_cube_scramble()
            elif ch == "3":
                self.controls()
            elif ch == "4":
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input, Try Again")
            self.main()
            
if __name__ =="__main__":
    ARCS().main()

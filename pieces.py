class Piece:
    def __init__(self, pos, camp):
        self.pos = pos
        self.camp = camp
        self.has_moved = False

    def get_pos(self):
        return self.pos

    def get_camp(self):
        return self.camp

    def move(self, pos):
        if pos in self.premove():
            if game.find_case(pos) == 0:
                self.pos = pos
            else:
                tab=player1.get_piece() + player2.get_piece()
                i=0
                while tab[i].get_pos()!=pos:
                    i+=1

                if tab[i].camp!=self.camp:
                    self.pos = pos





class Cavalier(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)

    def premove(self):
        tab = [(self.pos[0]+2, self.pos[1]+1), (self.pos[0]+1, self.pos[1]+2), (self.pos[0]-2, self.pos[1]-1), (self.pos[0]-1, self.pos[1]-2), (self.pos[0]+1, self.pos[1]-2), (self.pos[0]+2, self.pos[1]-1), (self.pos[0]-2, self.pos[1]+1),  (self.pos[0]-1, self.pos[1]+2)]
        tab= game.check_limit(tab)
        return tab
    

class Tour(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)
    
    '''
    def premove(self):
        tab=[]
        for i in range(1, 8):
            
                tab.append((self.pos[0]+i, self.pos[1]))
                tab.append((self.pos[0], self.pos[1]+i))
        return tab

    '''
    def dessine(self):
        if self.camp==2:
            window_surface.blit(tour_noir, [(self.get_pos()[1]-1)*ratio, abs((self.get_pos()[0]-8)*ratio)])
        

    def premove(self):
        tab=[]
        
        for direction in tour_directions :
            i=1
            new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])            
            while game.check_limit([new_pos]) != []:
                if game.find_case(new_pos)!=0:
                    tab.append(new_pos)
                    break                      
                tab.append(new_pos)
                i+=1
                new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])

        return tab



class Fou(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)
    
    def dessine(self):
        window_surface.blit(fou_noir, [(self.get_pos()[1]-1)*ratio, abs((self.get_pos()[0]-8)*ratio)])

    '''
    def premove(self):
        tab=[]
        for i in range(-8, 8):
            if i!=0:
                tab.append((self.pos[0]+i, self.pos[1]+i))
                tab.append((self.pos[0]+i, self.pos[1]-i))
                tab.append((self.pos[0]-i, self.pos[1]+i))
                tab.append((self.pos[0]-i, self.pos[1]-i))
        return tab

    '''
    def premove(self):
        tab=[]
        
        for direction in fou_directions :
            i=1
            new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])            
            while game.check_limit([new_pos]) != []:
                if game.find_case(new_pos)!=0:
                    tab.append(new_pos)
                    break                      
                tab.append(new_pos)
                i+=1
                new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])

        return tab


class Reine(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)
    
    '''
    def premove(self):
        tab=[]
        for i in range(-8, 8):
            if i!=0:
                tab.append((self.pos[0]+i, self.pos[1]+i))
                tab.append((self.pos[0]+i, self.pos[1]-i))
                tab.append((self.pos[0]-i, self.pos[1]+i))
                tab.append((self.pos[0]-i, self.pos[1]-i))
                tab.append((self.pos[0]+i, self.pos[1]))
                tab.append((self.pos[0], self.pos[1]+i))  
        return tab
    '''
    def premove(self):
        tab=[]
            
        for direction in fou_directions+tour_directions :
            i=1
            while game.check_limit([self.pos[0] + i * direction[0], self.pos[1] + i * direction[1]]) != [] and not game.find_case((self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])):
                tab.append((self.pos[0], self.pos[1]+i))
                i+=1
        return tab

class Roi(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)

    def premove(self):
        tab=[]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if j!=0 and i!=0:
                    tab.append((self.pos[0]+i, self.pos[1]+j))
        return tab

###ALED ON VERRA APRèS

class Pion(Piece):
    def __init__(self, pos, camp):
        super().__init__(pos, camp)

    def premove(self):
        tab=[]
        if self.camp == 1:
            if not game.find_case((self.pos[0]+1, self.pos[1])):
                tab+=(self.pos[0]+1, self.pos[1])

            if game.find_case((self.pos[0]+1, self.pos[1]+1)):
                tab+=(self.pos[0]+1, self.pos[1]+1)

            if game.find_case((self.pos[0]+1, self.pos[1]-1)):
                tab+=(self.pos[0]+1, self.pos[1]-1)
        
        else:
            if not game.find_case((self.pos[0]-1, self.pos[1])):
                tab+=(self.pos[0]-1, self.pos[1])

            if game.find_case((self.pos[0]-1, self.pos[1]+1)):
                tab+=(self.pos[0]-1, self.pos[1]+1)

            if game.find_case((self.pos[0]-1, self.pos[1]-1)):
                tab+=(self.pos[0]+1, self.pos[1]-1)
        return game.check_limit(tab)
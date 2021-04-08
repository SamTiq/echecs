import pygame

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

class Game:
    def __init__(self):
        player2.add_piece(Tour((6,2), 2))
        player2.add_piece(Fou((2,6), 2))
        '''
        player1.add_piece(Reine((1,4), 1))
        player2.add_piece(Reine((8,4), 2))

        player1.add_piece(Roi((1,5), 1))
        player2.add_piece(Roi((8,5), 2))

        for i in range(1,9,7):
            player1.add_piece(Tour((1,i), 1))
            player2.add_piece(Tour((8,i), 2))

        for i in range(2,8,5):

            player1.add_piece(Cavalier((1,i), 1))
            player2.add_piece(Cavalier((8,i), 2))

        for i in range(3,7,3):

            player1.add_piece(Fou((1,i), 1))
            player2.add_piece(Fou((8,i), 2))            
            
        for i in range(1,9):
            player1.add_piece(Pion((2,i), 1))
            player2.add_piece(Pion((7,i), 2))

    '''

    def check_limit(self, tab):
        tab_check=[]
        for i in range(len(tab)):
            if tab[i][0]<9 and tab[i][0]>0 and tab[i][1]<9 and tab[i][1]>0:
                tab_check.append(tab[i])
        return tab_check


    def find_case(self, pos):

        for piece in player1.get_piece()+ player2.get_piece():
            if piece.get_pos()==pos:
                return piece.get_camp()
        return 0
     
        
 


class Player:
    def __init__(self, pseudo, color):
        self.pseudo=pseudo
        self.color=color
        self.pieces=[]
    
    def add_piece(self, piece):
        self.pieces=self.pieces + [piece]

    def get_piece(self):
        return self.pieces

## VARIABLE ##

player1= Player("Samuel", 1)
player2= Player("Noémie", 2)

tour_directions=[(0, 1), (1, 0), (-1, 0), (0, -1)]
fou_directions=[(1, 1), (1, -1), (-1, 1), (-1, -1)]

game = Game()

print(player1.get_piece())

resolution_x = 560
resolution_y = 560

ratio = 560//8
window_surface=pygame.display.set_mode((resolution_x, resolution_y))

damier = pygame.image.load("assets/damier.jpg")
tour_noir = pygame.image.load("assets/tour_noir.png")
tour_noir.convert_alpha()
tour_noir = pygame.transform.scale(tour_noir, [ratio//2, ratio//2])
fou_noir = pygame.image.load("assets/fou_noir.png")
fou_noir.convert_alpha()
fou_noir = pygame.transform.scale(fou_noir, [ratio//2, ratio//2])
launched=True
piece_selected = None
while launched:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            launched=False

        elif event.type == pygame.MOUSEBUTTONUP:

            pos_curseur=pygame.mouse.get_pos()
            print(pos_curseur)
            pos_selected =(abs(pos_curseur[1]-560)//(560/8)+1, (pos_curseur[0]//(560/8))+1)
            if game.find_case(pos_selected)!=0:

                for piece in player1.get_piece()+player2.get_piece():
                    
                    if piece.get_pos()==pos_selected:
                        piece_selected=piece
                        potential_move = piece_selected.premove()
                        break
            else:
                piece_selected=None
        else:
            window_surface.blit(damier, [0, 0])
            for piece in player2.get_piece():
                piece.dessine()
                print([(piece.get_pos()[1]-1)*ratio, abs((piece.get_pos()[0]-8)*ratio)])
                
            
            if piece_selected!=None:
                print("test2")
                print(potential_move)
                for pos in potential_move:
                    pygame.draw.rect(window_surface, (0,0,0), pygame.Rect(((pos[1]-1)*ratio, abs((pos[0]-8)*ratio)), (30,30)))


    pygame.display.flip()
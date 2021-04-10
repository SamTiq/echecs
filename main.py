import pygame

class Piece:
    nom=""
    def __init__(self, pos, camp):
        self.pos = pos
        self.camp = camp
        self.has_moved = False
        if camp==1:
            self.couleur="blanc"
        else:
            self.couleur="noir"

    def get_pos(self):
        return self.pos

    def get_camp(self):
        return self.camp

    def move(self, pos):
        if pos in self.premove():
            self.pos=pos
            return True
        return False
    
    def dessine(self):
        window_surface.blit(pieces_dict[self.nom+'_'+self.couleur], [(self.get_pos()[1]-1)*ratio, abs((self.get_pos()[0]-8)*ratio)])


class Cavalier(Piece):
    nom="cavalier"

    def premove(self):
        tab = [(self.pos[0]+2, self.pos[1]+1), (self.pos[0]+1, self.pos[1]+2), (self.pos[0]-2, self.pos[1]-1), (self.pos[0]-1, self.pos[1]-2), (self.pos[0]+1, self.pos[1]-2), (self.pos[0]+2, self.pos[1]-1), (self.pos[0]-2, self.pos[1]+1),  (self.pos[0]-1, self.pos[1]+2)]
        tab= game.check_limit(tab)
        for pos in tab:
            if game.find_case(pos)==self.camp:
                tab.remove(pos)
        return tab
    

class Tour(Piece):
    nom="tour"           

    def premove(self):
        tab=[]
        
        for direction in tour_directions :
            i=1
            new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])            
            while game.check_limit([new_pos]) != []:
                if game.find_case(new_pos)==self.camp:
                    break
                if game.find_case(new_pos)!=0:
                    tab.append(new_pos)
                    break                      
                tab.append(new_pos)
                i+=1
                new_pos=(self.pos[0] + i * direction[0], self.pos[1] + i * direction[1])

        return tab



class Fou(Piece):
    nom="fou"
    
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
    nom="reinne"

    def premove(self):
        tab=[]
        
        for direction in fou_directions+tour_directions :
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


class Roi(Piece):
    nom="roi"

    def premove(self):
        tab=[]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if j!=0 and i!=0:
                    tab.append((self.pos[0]+i, self.pos[1]+j))
        return tab

###ALED ON VERRA APRèS

class Pion(Piece):
    nom="pion"

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
        #player2.add_piece(Tour((6,2), 2))
        #player2.add_piece(Fou((2,6), 2))
        
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

    
        for x in image_pieces:
            piece_blanc = pygame.image.load('assets/{}_blanc.png'.format(x))
            piece_noir = pygame.image.load('assets/{}_noir.png'.format(x))

            piece_blanc.convert_alpha()
            piece_noir.convert_alpha()

            pieces_dict['{}_blanc'.format(x)] = pygame.transform.scale(piece_blanc, [ratio//2, ratio//2])
            pieces_dict['{}_noir'.format(x)] = pygame.transform.scale(piece_noir, [ratio//2, ratio//2])
        print(pieces_dict)

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
pieces_dict = {}
image_pieces = ['roi', 'reinne', 'pion', 'fou', 'tour', 'cavalier']
resolution_x = 560
resolution_y = 560
damier = pygame.image.load('assets/damier.jpg')

ratio = 560//8
window_surface=pygame.display.set_mode((resolution_x, resolution_y))

game = Game()

print(player1.get_piece())



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
            for piece in player2.get_piece()+player1.get_piece():
                piece.dessine()
                print([(piece.get_pos()[1]-1)*ratio, abs((piece.get_pos()[0]-8)*ratio)])
                
            
            if piece_selected!=None:
                print("test2")
                print(potential_move)
                for pos in potential_move:
                    pygame.draw.rect(window_surface, (0,0,0), pygame.Rect(((pos[1]-1)*ratio, abs((pos[0]-8)*ratio)), (30,30)))


    pygame.display.flip()
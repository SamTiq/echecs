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
            self.has_moved=True
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
                if game.find_case(new_pos)==self.camp:
                    break
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
        
        for direction in tour_directions+fou_directions :
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


class Roi(Piece):
    nom="roi"

    def premove(self):
        tab=[]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (j!=0 or i!=0) and game.find_case((self.pos[0]+i, self.pos[1]+j))!=self.camp:
                    tab.append((self.pos[0]+i, self.pos[1]+j))
        tab=game.check_limit(tab)
        all_premove=[]
        if self.camp==1:
            player=player2
        else:
            player=player1

        for piece in player.get_piece():
            if piece.nom!="roi":
                temp=piece.premove()
                for premove in temp:
                    all_premove.append(premove)
        print(all_premove, tab)
        for element in tab:
            if element in all_premove:
                tab.remove(element)
        return tab

###ALED ON VERRA APRèS

class Pion(Piece):
    nom="pion"

    def premove(self):
        tab=[]
        if self.camp == 1:
            if game.find_case((self.pos[0]+1, self.pos[1]))==0:
                tab.append((self.pos[0]+1, self.pos[1]))
                if game.find_case((self.pos[0]+2, self.pos[1]))==0 and self.has_moved==False:
                    tab.append((self.pos[0]+2, self.pos[1]))

            if game.find_case((self.pos[0]+1, self.pos[1]+1))==2:
                tab.append((self.pos[0]+1, self.pos[1]+1))

            if game.find_case((self.pos[0]+1, self.pos[1]-1))==2:
                tab.append((self.pos[0]+1, self.pos[1]-1))
        
        else:
            if game.find_case((self.pos[0]-1, self.pos[1]))==0:
                tab.append((self.pos[0]-1, self.pos[1]))
                if game.find_case((self.pos[0]-2, self.pos[1]))==0 and self.has_moved==False:
                    tab.append((self.pos[0]-2, self.pos[1]))

            if game.find_case((self.pos[0]-1, self.pos[1]+1))==1:
                tab.append((self.pos[0]-1, self.pos[1]+1))

            if game.find_case((self.pos[0]-1, self.pos[1]-1))==1:
                tab.append((self.pos[0]-1, self.pos[1]-1))
        return game.check_limit(tab)

class Game:
    def __init__(self):
        #player1.add_piece(Reine((1,4), 1))
        #player2.add_piece(Reine((8,4), 2))

        player1.add_piece(Roi((1,5), 1))
        player2.add_piece(Roi((8,5), 2))

        #for i in range(1,9,7):
        #    player1.add_piece(Tour((1,i), 1))
        #    player2.add_piece(Tour((8,i), 2))
#
        #for i in range(2,8,5):
#
        #    player1.add_piece(Cavalier((1,i), 1))
        #    player2.add_piece(Cavalier((8,i), 2))
#
        #for i in range(3,7,3):
#
        #    player1.add_piece(Fou((1,i), 1))
        #    player2.add_piece(Fou((8,i), 2))            
        #    
        #for i in range(1,9):
        #    player1.add_piece(Pion((2,i), 1))
        #    player2.add_piece(Pion((7,i), 2))
#
    
        for x in image_pieces:
            piece_blanc = pygame.image.load('assets/{}_blanc.png'.format(x))
            piece_noir = pygame.image.load('assets/{}_noir.png'.format(x))

            piece_blanc.convert_alpha()
            piece_noir.convert_alpha()

            pieces_dict['{}_blanc'.format(x)] = pygame.transform.scale(piece_blanc, [ratio, ratio])
            pieces_dict['{}_noir'.format(x)] = pygame.transform.scale(piece_noir, [ratio, ratio])

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
     
    def find_piece(self, pos):
    
        for piece in player1.get_piece()+ player2.get_piece():
            if piece.get_pos()==pos:
                return piece
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

window_surface=pygame.display.set_mode((resolution_x, resolution_y))


damier = pygame.image.load('assets/damier.jpg')
damier.convert_alpha()


ratio = 560//8


game = Game()




launched=True
piece_selected = None
while launched:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            launched=False

        elif event.type == pygame.MOUSEBUTTONUP:

            pos_curseur=pygame.mouse.get_pos()
            pos_selected =(abs(pos_curseur[1]-560)//(560/8)+1, (pos_curseur[0]//(560/8))+1)

            if piece_selected!=None and pos_selected in piece_selected.premove():
                if game.find_case(pos_selected)!=0:
                    piece_sup = game.find_piece(pos_selected)
                    if piece_sup.camp ==1 :
                        player1.pieces.remove(piece_sup)
                    else:
                        player2.pieces.remove(piece_sup)
                piece_selected.move(pos_selected)
                piece_selected=None



            elif game.find_case(pos_selected)!=0:

                for piece in player1.get_piece()+player2.get_piece():
                    
                    if piece.get_pos()==pos_selected:
                        piece_selected=piece
                        potential_move = piece_selected.premove()
                        break
            
            else:
                piece_selected=None
                pos_selected=None
        else:
            window_surface.blit(damier, [0, 0])
            for piece in player2.get_piece()+player1.get_piece():
                piece.dessine()
                
            
            if piece_selected!=None:
                for pos in potential_move:
                    pygame.draw.rect(window_surface, pygame.Color(50, 50, 50, 128), pygame.Rect(((pos[1]-1)*ratio, abs((pos[0]-8)*ratio)), (ratio, ratio)))


    pygame.display.flip()
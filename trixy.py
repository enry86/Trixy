#!/usr/bin/python

import copy

class Player:
    def __init__(self):
        self.states = {}
        self.game = []

    def get_move(self, state):
        self.game.append(state)
        move = -1
        max = -1
        for i in range(len(state)):
            tmp = copy.deepcopy(state)
            if state[i] == 0:
                tmp[i] = 1
                if self.states.has_key(tuple(tmp)):
                    score = self.states[tuple(tmp)]
                else:
                    score = 0
                if score > max:
                    max = score 
                    move = i
        tmp = state
        tmp[move] = 1
        self.game.append(tmp)
        return move

    def close_game(self, res):
        if res == 1:
            print 'Lol, you have lost the Game'
        elif res == 2:
            print "Noes, I've lost the Game"
        else:
            print 'Wow.. none of us lost the game'
         
class Game:
    def __init__(self, sym, c_player):
        self.hs = sym
        self.c_player = c_player
        self.outcome = 0
        if sym == 'o':
            self.cs = 'x'
            self.h_turn = True
        else:
            self.cs = 'o'
            self.h_turn = False
        self.current = [0,0,0,0,0,0,0,0,0]
    
    def play(self):
        end = False
        while not end:
            if self.h_turn:
                self.h_move()
                self.h_turn = False 
            else:
                self.c_move()
                self.h_turn = True
            end, res = self.end_game()
        self.output_grid()
        self.c_player.close_game(res)
        if res == 0:
            print 'Game over... drawn'
        else:
            print 'Player', res, 'wins!'

    def c_move(self):
        print 'Computer moves...'
        m = self.c_player.get_move(self.current)
        self.current[m] = 1
    
    def h_move(self):
        self.output_grid()
        valid = False
        while not valid:
            m = raw_input('Your move: ')
            valid = self.check_move(int(m))
        self.current[int(m)] = 2
        
    def check_move(self, m):
        res = True
        if m > 9 or m < 0 or self.current[m] != 0:
            res = False
        return res

    def output_grid(self):
        s = [' ', self.cs, self.hs]
        for h in range(3):
            print '|',
            for k in range(3):
                print s[self.current[(3 * h) + k]], '|',
            if h  < 2:
                print '\n|---|---|---|'
        print '\n'

    def check_r(self, r):
        s = self.current[3 * r : (3 * r) + 3]
        if s[0] == s[1] and s[1] == s[2] and s[0] != 0:
            return True, s[0]
        else:
            return False, 0
    
    def check_c(self, c):
        n = self.current[c]
        res = True
        for i in range(3):
            res = res and self.current[c + 3 * i] == n
        if n == 0 and res == True:
            return False, 0
        else:
            return res, n
    
    def check_d(self):
        if self.current[4] == 0:
            return (False, 0)
        res = True
        d1 = [0,4,8]
        d2 = [2,4,6]
        for i in d1:
            res = res and self.current[i] == self.current[4]
        if res == False:
            res = True
            for k in d2:
                res = res and self.current[k] == self.current[4]
                print self.current[k] ==  self.current[4], res
        if res == True:
            return (True, self.current[4])
        else:
            return (False, 0)
            

    def end_game(self):
        res = (False, 0)
        for h in range(3):
            row = self.check_r(h)
            if row[0] == False:
                col = self.check_c(h)
                if col[0] == True:
                    res = col
            else:
                res = row
        if res[0] == False:
            res = self.check_d()
        if self.current.count(0) == 0 and res[0] == False:
            res = (True, 0)
        return res



        
    
def main():
    print 'Welcome to Trixy - Tic-tac-toe learning algorithm'
    pl = raw_input('Select player [x/o] ')
    if pl != 'x' and pl != 'o':
        print 'Wrong symbol, fallback to "o"'
        pl = 'o'
    new = True
    p = Player()
    while new:
        g = Game(pl, p)
        g.play()
        res = raw_input('Play again? [y/n] ')
        if res != 'y':
            new = False
    print 'Thank you for showing me your skills!'

if __name__ == '__main__':
    main()


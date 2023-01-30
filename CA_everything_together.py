# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:35:44 2023

@author: annaa
"""

import numpy as np
import random
import math
from matplotlib import pyplot

#a generic class for cellular automata
class CellularAutomaton:
    def __init__(self, cells, states, dimension, neighbours, rand):
        self.cells = cells #number of cells
        self.states = states #number of states that a cell can have
        self.dimension = dimension #dimension of the cellular automaton
        self.neighbours= neighbours #number of neighbours each cell has 
        self.rand = rand #randvoorwaarden
        
#I really don't know how to have a generic way to evaluate the CA here
#So I guess for now I'll just have specific methods in the subclasses

        

class CA1D(CellularAutomaton):
    def __init__(self,rules,cells, states, dimension, neighbours, rand):
        self.rules = rules
        self.dimension=1
        super().__init__(cells, states,dimension, neighbours, rand
#only two possible inputs voor rand: either "static" or "periodic"
#static means first and last cell aways stay in the same state
#periodic means that the last cel counts as neighbour of the first one and vice versa
#for now only really works with two states and two neighbours
        

   
    
    
    def random_firstgen(self):
    """ generates a 1D grid with random starting states """
        grid= grid=np.empty(self.cells,int)
        for i in range(self.cells):
            grid[i]=random.choice(range(0,self.states))
        return grid
    
    
    def conventional_firstgen(self):
    """creates a 1D grid with the middle cell(s) being alive, all others dead"""
        grid= grid=np.empty(self.cells,int)
        for i in range(self.cells):
            if self.cells%2==0: #if even number of cells
                if i == self.cells//2 or i== self.cells//2+1:
                    grid[i-1]=1
                else:
                    grid[i-1]=0
            else:#if uneven number of cells
                if i==self.cells//2:
                    grid[i]=1
                else:
                    grid[i]=0
        return grid
    
     
    
    #for now no method that uses this
    #but you could construct a method that uses these sums just then you'd have to change the evaluation method
    def alive_neighbours(self,grid,x):
    """this will give sum of states of neighbours"""
        neighbours=0
        for i in range (x-self.neighbours//2,x+self.neighbours//2+1):
            if i==x:
                    pass
            else:
                neighbours+=grid[i]
                
        return neighbours
    
    
    def neighbourhood(self,grid,x):
    """This shows us which of the 8 neighbourhoods x has based on the system of the rules for 1d automata"""
        if self.rand=="periodic":
            if x==0:
                if grid[x]==1:
                    if grid[self.cells-1]==1 and grid[x+1]==1:
                        return 0
                    elif grid[self.cells-1]==1 and grid[x+1]==0:
                        return 1 
                    elif grid[self.cells-1]==0 and grid[x+1]==1:
                        return 4
                    else:
                        return 5
                else:
                    if grid[self.cells-1]==1 and grid[x+1]==1:
                        return 2
                    elif grid[self.cells-1]==1 and grid[x+1]==0:
                        return 3
                    elif grid[self.cells-1]== 0 and grid[x+1]==1:
                        return 6
                    else:
                        return 7
                    
            elif x==self.cells-1:
                if grid[x]==1:
                    if grid[x-1]==1 and grid[0]==1:
                        return 0
                    elif grid[x-1]==1 and grid[0]==0:
                        return 1 
                    elif grid[x-1]==0 and grid[0]==1:
                        return 4
                    else:
                        return 5
                else:
                    if grid[x-1]==1 and grid[0]==1:
                        return 2
                    elif grid[x-1]==1 and grid[0]==0:
                        return 3
                    elif grid[x-1]== 0 and grid[0]==1:
                        return 6
                    else:
                        return 7
                
            else:
                
                if grid[x]==1:
                    if grid[x-1]==1 and grid[x+1]==1:
                        return 0
                    elif grid[x-1]==1 and grid[x+1]==0:
                        return 1 
                    elif grid[x-1]==0 and grid[x+1]==1:
                        return 4
                    else:
                        return 5
                else:
                    if grid[x-1]==1 and grid[x+1]==1:
                        return 2
                    elif grid[x-1]==1 and grid[x+1]==0:
                        return 3
                    elif grid[x-1]== 0 and grid[x+1]==1:
                        return 6
                    else:
                        return 7
           
                       
                
            
   
    def evaluation(self,grid,rounds):
    """ this function applies the rules on a grid and displays the new grid
    
    it will run as many times as you put rounds, if you want it to run indefinitely, put -1 for rounds"""
        new= grid.copy()
        
        if rounds==0:
            print("done")
        else:
            for i in range(self.cells):
                state= grid[i]
                
                if self.rand=="static":
               
                    if i==0 or i==self.cells-1:
                         new[i]=state
                    else:
                        neighbourhood=self.neighbourhood(grid,i)
                        new[i]=int(self.rules[neighbourhood])
                
                else:
                    neighbourhood=self.neighbourhood(grid,i)
                    new[i]=int(self.rules[neighbourhood])
                    
                    
            print(new)
            return self.evaluation(new,rounds-1)
        
        
        
class CA2D(CellularAutomaton):
    def __init__(self,die,born,cells, states, dimension, neighbours, rand):
        self.die = die #should be a list with all possible counts of alive cells as neighbours with wich a live cell dies
        self.born= born #should be a list with all possible counts of alive cells as neighbours with wich a dead cell becomes born
        self.dimension= 2
        self.row = int(math.sqrt(cells)) #this means, that the grid will always be quadratic 
        self.col = int(math.sqrt(cells)) #so gotta think of that when you input number of cells
        
        super().__init__(cells, states,dimension, neighbours, rand)
        
    
    def first_gen(self): 
    """creating a random starting grid"""
                         
        grid = np.empty((self.row, self.col), int)
        for i in range (self.row):
            for j in range(self.col):
                grid[i][j]= random.choice([0,1])
        return grid 
    
    
    
    def count_neighbours(self,grid,x,y):
    """counting how many neighbours are alive at position grid[x,y]  """
        neighbours=0
        for i in range (x-1,x+2):
            for j in range(y-1,y+2):
                if i==x and j==y:
                    pass
                else:
                    neighbours+=grid[i][j]
        return neighbours
    
    
    def graphic(self,grid):
    """visualizing it
    yellow is alive and purple is dead """
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(grid)

    
    
    def evaluation(self,grid,rounds):
        """implementing rules and showing the new grid
        rounds is the amount of timesteps you want it to evaluate, again put -1 as rounds for indefinite evaluation"""
        new= grid.copy()
        
        if rounds==0:
            print("done")
        else:
            for i in range(self.row-1):
                for j in range(self.col-1):
                    state = grid[i,j]
                    neighbours=self.count_neighbours(grid,i,j)
                    
                    if i==0 or j==0 or i==(self.row-1) or j==(self.col-1):
                        new[i,j]=state
                    else:
                
                        if state ==0:
                           if neighbours in self.born:
                               new[i,j]=1 
                           else:
                               new[i,j]=0 
                        else:
                            if neighbours in self.die:
                               new[i,j]=0
                            else:
                               new[i,j]=1
                                 
                   
                        
            print(new)#this can be deleted actualy was just for me to see it as numbers also
            self.graphic(new)
            return self.evaluation(new,rounds-1)
        
        
        
        
# a few examples:
    
Rule30= CA1D("00011110",30,2,1,2,"static") #rule 30 with static edges
ran= Rule30.random_firstgen() #random starting grid for rule 30
con=Rule30.conventional_firstgen() #conventional starting grid for rule 30
GameofLife=CA2D([0,1,4,5,6,7,8],[3],49,2,2,8,"static")
grid= GameofLife.first_gen() #random starting grid for Game of Life



    

import random 
import math
import pygame

class RRTMap:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        self.start=start
        self.goal=goal
        self.MapDimensions=MapDimensions
        self.Maph, self.Mapw = self.MapDimensions   # width and height

        # window settings
        self.MapWindowName='RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.Mapw,self.Maph))
        self.map.fill((255,255,255))    #background color
        self.nodeRad = 0    # node radius
        self.nodeThickness = 0   
        self.edgeThickness = 1

        self.obstables=[]
        self.obsdim = obsdim
        self.obsNumber = obsnum

        # define colors
        self.Grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.White = (255,255,255)

    def drawMap(self,obstacles):
        pygame.draw.circle(self.map,self.Green,self.start,self.nodeRad+5,0)     # start point
        pygame.draw.circle(self.map,self.Red,self.goal,self.nodeRad+10,0)     # goal point
        self.drawObs(obstacles)

    def drawPath(self):
        pass
    def drawObs(self,obstacles):
        obstaclesList = obstacles.copy()
        while (len(obstaclesList)>0):
            obstacle = obstaclesList.pop(0)
            pygame.draw.rect(self.map,self.Grey,obstacle)

class RRTGraph:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        (x,y) = start
        self.start=start
        self.goal=goal
        self.goalFlag=False
        self.maph,self.mapw = MapDimensions
        self.x = []
        self.y = []
        self.parent = []
        # initialize the tree
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)   # first element (start node)
        # the obstacle
        obstacles = []
        self.obsDim=obsdim
        self.obsNum=obsnum
        # path
        self.goalstate = None
        self.path = []


    def makeRandomRect(self):
        uppercorner_x = int(random.uniform(0,self.mapw-self.obsDim))
        uppercorner_y = int(random.uniform(0,self.maph-self.obsDim))

        return (uppercorner_x,uppercorner_y)

    def makeobs(self):
        obs = []

        for i in range(0,self.obsNum):
            rectang = None
            startGoalCol = True
            while startGoalCol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper,(self.obsDim,self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startGoalCol = True
                else:
                    startGoalCol = False
            obs.append(rectang)     # append coordinates of obstacles if not collide with start or goal
        
        self.obstacles = obs.copy()
        return obs

    def add_node(self):
        pass
    def remove_node(self):
        pass
    def add_edge(self):
        pass
    def remove_edge(self):
        pass
    def number_of_nodes(self):
        pass
    def distance(self):
        pass
    def nearest(self):
        pass
    def isFree(self):
        pass
    def crossObstacle(self):
        pass
    def connect(self):
        pass
    def step(self):
        pass
    def path_to_goal(self):
        pass
    def getPathCoords(self):
        pass
    def bias(self):
        pass
    def expand(self):
        pass
    def cost(self):
        pass

# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    #moving positon of pacman and ghost. moving picture show in the command.
    
    newPos = successorGameState.getPacmanPosition()
    #output the position of next state(x,y)
    
    newFood = successorGameState.getFood()
    #output F and T. T represents the position of food. when the food is eaten, T turns to be F.
    
    newGhostStates = successorGameState.getGhostStates()
    # change it into(x,y) by way of newGhostStates[0].getPosition()
    
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


    "*** YOUR CODE HERE ***"

    #first version
    """
    foodlist=newFood.asList()
    eaten=False
    
    #difine the current ghost state
    for ghost in newGhostStates:
        ghostPos=ghost.getPosition()
    
    #a=manhattanDistance(ghostPos,newPos)
    #print "a",a
    
    gho_dis=[]
    distance=manhattanDistance(ghostPos,newPos)
    if distance<=2:
        eaten=True
        distance_now=distance
        gho_dis.append(distance_now)
    
    #for i in range(len(foodlist)):
    #   fooddis=manhattanDistance(newPos,foodlist[i])
    #   print fooddis
    
    
    #for i in range(len(foodlist)):
    #   print foodlist[i]
    #   dismax=max([manhattanDistance(newPos,foodlist[i])])
    
    
    if eaten:
        dis=min(gho_dis)
    else:
        if len(foodlist)==0:
            dis=0
        if len(foodlist)==1:
            dis_tmp=manhattanDistance(newPos,foodlist[0])
            dis=1/dis_tmp
            foodlist.remove(foodlist[0])
        if len(foodlist)>=2:
            for i in range(len(foodlist)):
                dismax=max([manhattanDistance(newPos,foodlist[i])])
                dismin=min([manhattanDistance(newPos,foodlist[i])])
            dis=1/(dismax+dismin)
            foodlist.remove(foodlist[i])
    return dis
    """
    #second version
    
    foodlist=newFood.asList()
    eaten=False
    
    #difine the current ghost state
    for ghost in newGhostStates:
        ghostPos=ghost.getPosition()

    #a=manhattanDistance(ghostPos,newPos)
    #print "a",a

    gho_dis=[]
    distance=manhattanDistance(ghostPos,newPos)
    score_2=0
    if distance<=2:
        eaten=True
        distance_now=distance
        gho_dis.append(distance_now)
        score_2 -=distance/100

    #for i in range(len(foodlist)):
    #   fooddis=manhattanDistance(newPos,foodlist[i])
    #   print fooddis


    #for i in range(len(foodlist)):
    #   print foodlist[i]
    #   dismax=max([manhattanDistance(newPos,foodlist[i])])


    if eaten:
        dis=min(gho_dis)
    else:
        if len(foodlist)==0:
            dis=0
        if len(foodlist)==1:
            dis=manhattanDistance(newPos,foodlist[0])
        if len(foodlist)>=2:
            for i in range(len(foodlist)):
                dismax=max([manhattanDistance(newPos,foodlist[i])])
                dismin=min([manhattanDistance(newPos,foodlist[i])])
            dis=(dismax+dismin)/2

    #ghostnum=currentGameState.getNumAgents()
    #print "ghostnum",ghostnum
    #get the ghost number 3
    #print "foodlist",foodlen
    score_1=2.0/(dis+100)+3.0/(len(foodlist)+1)

    scoresum=score_1+score_2

    return scoresum
    
    #third version
    """
    foodlist=newFood.asList()
    dis=0
    
    #make the food score
    for i in range(len(foodlist)):
        foodsave=[]
        foodsave.append(manhattanDistance(newPos,foodlist[i]))
        dis=min(foodsave)
    score_1=2/(dis+100)+3/(len(foodlist)+1)
    
    #define the current ghost state and make the ghost score
    
    for ghost in newGhostStates:
        ghostPos=ghost.getPosition()
        distance=manhattanDistance(ghostPos,newPos)
        score_2=0
        if distance<=2:
            score_2 -=distance/100
    
    
    score=score_1+score_2
    
    return score
    """



#    return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
      
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"


    """
    #second version
    
    agent_index=0
    depth=0
    
    v=float('-inf')
    v_cll=[]
    
    legalaction=gameState.getLegalActions(agent_index)
    #    act=Directions.STOP
    for each_a in legalaction:
        next_a=gameState.generateSuccessor(agent_index,each_a)
        v_tmp=self.min_value(next_a,depth,agent_index+1)
        v_cll.append((v_tmp,each_a))
        v=max(v,v_tmp)
    
    for vall in v_cll:
        if v==vall[0]:
            act = vall[1]
    return act

  def max_value(self,state,depth,agent_index):
    if depth>=self.depth:
        return depth_con==1
    if state.isWin() or state.isLose or depth_con :
        return self.evaluationFunction(state)
    v=float('-inf');
    
    legalaction=state.getLegalActions(agent_index)
    for each_a in legalaction:
        next_a=state.generateSuccessor(agent_index,each_a)
        v=max(v,self.min_value(next_a,depth,agent_index+1))
    return v
        
  def min_value(self,state,depth,agent_index):
    
    #win=state.isWin()
    #lose=state.isLose()
    #print "depth",self.depth
    #print "depth",depth
    #print "depth",depth>=self.depth
    #depth_con=depth>=self.depth
    #con=win or lose or depth_con
    #print "con",con
    
    if depth>=self.depth:
        return depth_con==1
    
    if state.isWin() or state.isLose or depth_con :
        return self.evaluationFunction(state)
    v=float("inf")
    
    next_a=0
    
    legalaction=state.getLegalActions(agent_index)
    agentnum_now=state.getNumAgents()-1
    for each_a in legalaction:
        if agent_index >= agentnum_now:
            next_a=state.generateSuccessor(agent_index,each_a)
            v=min(v,self.max_value(next_a,depth+1,agent_index))
        else:
            v=min(v,self.min_value(next_a,depth,agent_index+1))
    return v
    """
    

    
    
    #Final version
    
    #initiate arguments for funciton
    agent_index=0
    depth = 0
    
    v = float('-inf')
    v_cll=[]
    
    #in minimax decision algorithm, return max min_value result
    legalaction = gameState.getLegalActions(agent_index)
    #print "actions",legalaction
    
    act=Directions.STOP
    
    for each_a in legalaction:
        next_a = gameState.generateSuccessor(agent_index, each_a)
        
        #get min_value for s,a
        v_tmp = self.min_value(next_a, agent_index+1, depth)
        v_cll.append((v_tmp,each_a))
        #print "vvv",v_tmp
        #get the max action in min_value result
        v = max(v, v_tmp)

    for vall in v_cll:
        if v == vall[0] :
            act = vall[1]
        
    return act


  def max_value(self, state, agent_index, depth):
    
    #if depth value surpass depth we set, back to evaFuc, or continue max_value
    if depth >= self.depth:
        return self.evaluationFunction(state)
        
    legalaction=state.getLegalActions(agent_index)
    #print "crrr",currentActions
    
    #when the legalaction is empty, return back to the evauFun, or get the value of v
    if len(legalaction) > 0:
        v = float('-inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        next_a = state.generateSuccessor(agent_index, each_a)
        
        #get max value in min_value results
        v = max(v,self.min_value(next_a, agent_index+1, depth))
    return v


  def min_value(self, state, agent_index, depth):
    
    #win=state.isWin()
    #lose=state.isLose()
    #print "depth",self.depth
    #print "depth",depth
    #print "depth",depth>=self.depth
    #depth_con=depth>=self.depth
    #con=win or lose or depth_con
    #print "con",con
    
    if depth >= self.depth:
        return self.evaluationFunction(state)
        
    legalaction = state.getLegalActions(agent_index)
    if len(legalaction) > 0:
        v = float('inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        if agent_index >= (state.getNumAgents()-1):
            next_a = state.generateSuccessor(agent_index, each_a)
            #print "aaaa",currentState
            depth=depth+1
            max = self.max_value(next_a, 0, depth)
            v = min(v, max)
        else:
            next_a = state.generateSuccessor(agent_index, each_a)
            v=min(v,self.min_value(next_a, agent_index+1, depth))
    
    return v


#    util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    
    #initiate arguments for funciton
    agent_index=0
    depth = 0
    
    v = float('-inf')
    v_cll=[]
    
    #in minimax decision algorithm, return max min_value result
    legalaction = gameState.getLegalActions(agent_index)
    #print "actions",legalaction
    
    act=Directions.STOP
    alpha=float('-inf')
    beta=float('inf')
    
    for each_a in legalaction:
        next_a = gameState.generateSuccessor(agent_index, each_a)
        
        #get min_value for s,a
        v_tmp = self.min_value(next_a, agent_index+1, depth,alpha,beta)
        v_cll.append((v_tmp,each_a))
        #print "vvv",v_tmp
        #get the max action in min_value result
        v = max(v, v_tmp)
    
    for vall in v_cll:
        if v == vall[0] :
            act = vall[1]
  
    return act


  def max_value(self, state, agent_index, depth,alpha,beta):
    
    #if depth value surpass depth we set, back to evaFuc, or continue max_value
    if depth >= self.depth:
        return self.evaluationFunction(state)
    
    legalaction=state.getLegalActions(agent_index)
    #print "crrr",currentActions
    
    #when the legalaction is empty, return back to the evauFun, or get the value of v
    if len(legalaction) > 0:
        v = float('-inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        next_a = state.generateSuccessor(agent_index, each_a)
        
        #get max value in min_value results
        v = max(v,self.min_value(next_a, agent_index+1, depth,alpha,beta))
        if v>=beta:
            return v
        alpha=max(alpha,v)
    return v
        
        
  def min_value(self, state, agent_index, depth,alpha,beta):

    #win=state.isWin()
    #lose=state.isLose()
    #print "depth",self.depth
    #print "depth",depth
    #print "depth",depth>=self.depth
    #depth_con=depth>=self.depth
    #con=win or lose or depth_con
    #print "con",con

    if depth >= self.depth:
        return self.evaluationFunction(state)
    
    legalaction = state.getLegalActions(agent_index)
    if len(legalaction) > 0:
        v = float('inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        if agent_index >= (state.getNumAgents()-1):
            next_a = state.generateSuccessor(agent_index, each_a)
            #print "aaaa",currentState
            depth=depth+1
            max = self.max_value(next_a, 0, depth,alpha,beta)
            v = min(v, max)
        else:
            next_a = state.generateSuccessor(agent_index, each_a)
            v=min(v,self.min_value(next_a, agent_index+1, depth,alpha,beta))
            if v<=alpha:
                return v
            beta=min(beta,v)
    return v


          
#    util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    
    #initiate arguments for funciton
    agent_index=0
    depth = 0
    
    v = float('-inf')
    v_cll=[]
    
    #in minimax decision algorithm, return max min_value result
    legalaction = gameState.getLegalActions(agent_index)
    #print "actions",legalaction
    
    act=Directions.STOP
    
    for each_a in legalaction:
        next_a = gameState.generateSuccessor(agent_index, each_a)
        
        #get min_value for s,a
        v_tmp = self.avg_value(next_a, agent_index+1, depth)
        v_cll.append((v_tmp,each_a))
        #print "vvv",v_tmp
        #get the max action in min_value result
        v = max(v, v_tmp)
    
    for vall in v_cll:
        if v == vall[0] :
            act = vall[1]
  
    return act


  def max_value(self, state, agent_index, depth):
    
    #if depth value surpass depth we set, back to evaFuc, or continue max_value
    if depth >= self.depth:
        return self.evaluationFunction(state)
    
    legalaction=state.getLegalActions(agent_index)
    #print "crrr",currentActions
    
    #when the legalaction is empty, return back to the evauFun, or get the value of v
    if len(legalaction) > 0:
        v = float('-inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        next_a = state.generateSuccessor(agent_index, each_a)
        
        #get max value in min_value results
        v = max(v,self.avg_value(next_a, agent_index+1, depth))
    return v
        
        
  def avg_value(self, state, agent_index, depth):

    #win=state.isWin()
    #lose=state.isLose()
    #print "depth",self.depth
    #print "depth",depth
    #print "depth",depth>=self.depth
    #depth_con=depth>=self.depth
    #con=win or lose or depth_con
    #print "con",con
    
    sum=0

    if depth >= self.depth:
        return self.evaluationFunction(state)
    
    legalaction = state.getLegalActions(agent_index)
    if len(legalaction) > 0:
        v = float('inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        if agent_index >= (state.getNumAgents()-1):
            next_a = state.generateSuccessor(agent_index, each_a)
            #print "aaaa",currentState
            depth=depth+1
            sum = sum+self.max_value(next_a, 0, depth)
        else:
            next_a = state.generateSuccessor(agent_index, each_a)
            sum=sum+self.avg_value(next_a, agent_index+1, depth)

        v=sum/(len(legalaction))

    return v


#    util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    we consider about the distance between pacman and food, distance between 
    ghost and pacman. then according to the distance we get to make score. 
    When pacman eat food, we use the number of ghost and length of foodlist 
    to calculate it. Then combine distance between pacman and food with it 
    get score1. 
    When designing ghost with pacman, we never intend pacman to close to ghost
    unless pacman eat a capsule. When their distance<=2, we will minus the score.
    When distance==0,but newScaredTimes>0, we encourage pacman to eat the ghost,
    so add the score under this condition.
    But there are still many problems we cannot handle, suchas when there are just
    one food nearby, pacman will stop unless the ghost is closed. 
    Also, we intend to add the capsule into our design, but when we add the capsule
    condition, and encourage pacman to eat it ,but it seems useless somethimes. 
    Pacman didn't eat it when pass by the capsule. And when we add this condition, 
    pacman seems hesitate more when he decide to eat next food.
    
  """
  "*** YOUR CODE HERE ***"
  

  newFood = currentGameState.getFood()
  foodlist=newFood.asList()
  pacPos=currentGameState.getPacmanPosition()
  ghostPos=currentGameState.getGhostStates()
  capsulPos=currentGameState.getCapsules()

  newScaredTimes = [ghostState.scaredTimer for ghostState in ghostPos]
    
  pacfood_dis=0
  score1=0
  score2=0
  score3=0

  #calculate distance between pacman and food, then back score
  for food in foodlist:
    pacfood_dis=manhattanDistance(pacPos,food)
    #foodlen=len(foodlist)+1
    #ghostnum=currentGameState.getNumAgents()-1
    #print "ghostnum",ghostnum
    #get the ghost number 3
    #print "foodlist",foodlen
    
    #use ghostnumber and foodlist length,make the function 3/foodlen
    #foodlen=len(foodlist)+1
    score1=1.0/(pacfood_dis+100)+3.0/(len(foodlist)+1)

  for capsule in capsulPos:
    cappac_dis=manhattanDistance(pacPos,capsule)
    #print cappac_dis
    #if cappac_dis==0:
    #score3+=cappac_dis*10
    if cappac_dis<=2:
        score3+=100

  #calculate distance between pacman and ghost, then back score
  for ghost in ghostPos:
    pacghost_dis=manhattanDistance(pacPos,ghost.getPosition())
    
    if pacghost_dis==0 and newScaredTimes>0:
        score2+=pacghost_dis*10
    elif pacghost_dis<=2:
        score2-=pacghost_dis*1.5
    
    score4=1.5*currentGameState.getScore()

  return score1+score2+score4+score3
  

#  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    
    #initiate arguments for funciton
    agent_index=0
    depth = 0
    
    v = float('-inf')
    v_cll=[]
    
    #in minimax decision algorithm, return max min_value result
    legalaction = gameState.getLegalActions(agent_index)
    #print "actions",legalaction
    
    act=Directions.STOP
    
    for each_a in legalaction:
        next_a = gameState.generateSuccessor(agent_index, each_a)
        
        #get min_value for s,a
        v_tmp = self.avg_value(next_a, agent_index+1, depth)
        v_cll.append((v_tmp,each_a))
        #print "vvv",v_tmp
        #get the max action in min_value result
        v = max(v, v_tmp)
    
    for vall in v_cll:
        if v == vall[0] :
            act = vall[1]
  
    return act


  def max_value(self, state, agent_index, depth):
    
    #if depth value surpass depth we set, back to evaFuc, or continue max_value
    if depth >= self.depth:
        return self.evaluationFunction(state)
    
    legalaction=state.getLegalActions(agent_index)
    #print "crrr",currentActions
    
    #when the legalaction is empty, return back to the evauFun, or get the value of v
    if len(legalaction) > 0:
        v = float('-inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        next_a = state.generateSuccessor(agent_index, each_a)
        
        #get max value in min_value results
        v = max(v,self.avg_value(next_a, agent_index+1, depth))
    return v
        
        
  def avg_value(self, state, agent_index, depth):

    #win=state.isWin()
    #lose=state.isLose()
    #print "depth",self.depth
    #print "depth",depth
    #print "depth",depth>=self.depth
    #depth_con=depth>=self.depth
    #con=win or lose or depth_con
    #print "con",con

    sum=0
    
    if depth >= self.depth:
        return self.evaluationFunction(state)

    legalaction = state.getLegalActions(agent_index)
    if len(legalaction) > 0:
        v = float('inf')
    else:
        v = self.evaluationFunction(state)
    for each_a in legalaction:
        if agent_index >= (state.getNumAgents()-1):
            next_a = state.generateSuccessor(agent_index, each_a)
            #print "aaaa",currentState
            depth=depth+1
            sum = sum+self.max_value(next_a, 0, depth)
        else:
            next_a = state.generateSuccessor(agent_index, each_a)
            sum=sum+self.avg_value(next_a, agent_index+1, depth)
        
        v=sum/(len(legalaction))
    
    return v


    util.raiseNotDefined()


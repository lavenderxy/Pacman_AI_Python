# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"


    from game import Directions
    
    ST=Directions.STOP
    
    data = util.Stack()
    data.push( (problem.getStartState(), [],[]) )
    #()as a tuple. []individually.
    passed_all=[]
    
    while not data.isEmpty():
        
        state, action, passed = data.pop()
    
        
        for (nextstate, path,cost) in problem.getSuccessors(state):
            if not problem.isGoalState(nextstate):
                if not nextstate in passed:
                    all_ac=action+[path]
                    passed_all=passed+[nextstate]
                    
                    data.push((nextstate, all_ac, passed_all ))
                    
            elif problem.isGoalState(nextstate):
                all_ac1=action+[path]      #if I don't renew it, pacman will return back to the start point. 
                return all_ac1
    
    return [ST]
    
    
    util.raiseNotDefined()





def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    
    
    from game import Directions
    
    ST=Directions.STOP
    
    data =util.Queue()
    data.push((problem.getStartState(),[]))
    passed=[]
    
    while not data.isEmpty():
        state, action =data.pop()
    
        for (nextstate, path, cost) in problem.getSuccessors(state):
            if not problem.isGoalState(nextstate):
                if not nextstate in passed:
                    all_ac=action+[path]
                    passed_all=passed+[nextstate]
                    data.push((nextstate,all_ac))
                    passed.append(nextstate)
            elif problem.isGoalState(nextstate):
                all_ac1=action+[path]
                return all_ac1

    return [ST]
    
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    
    
    
    from game import Directions
    
    ST=Directions.STOP
    
    cost=0
    data=util.PriorityQueue()
    data.push((problem.getStartState(),[]),cost)
    passed=[]
    
    while not data.isEmpty():
        state, action=data.pop()
        
        if problem.isGoalState(state):
            return action
        passed.append(state)
            
        for (nextstate, path, cost) in problem.getSuccessors(state):
            if not nextstate in passed:
                all_ac=action+[path]
                passed_all=passed+[nextstate]
                cost_all=problem.getCostOfActions(all_ac)
                data.push((nextstate,all_ac),cost_all)
            elif (nextstate in passed) and (cost_all>max([cost_all])):
                nextstate=state

    return [ST]
    


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    
    from game import Directions
    
    ST=Directions.STOP
    
    cost=0
    data=util.PriorityQueue()
    initialstate=problem.getStartState()
    data.push((initialstate,[]),heuristic(initialstate,problem))  #manhattanHeurstic return a value, so we chouldn't use problem,getStartState() here.
    passed=[]
    
    while not data.isEmpty():
        state, action = data.pop()
        
        if problem.isGoalState(state):
            return action
        passed.append(state)
        
        for (nextstate, path,cost) in problem.getSuccessors(state):
            
            if not nextstate in passed:
                all_ac=action+[path]
                passed_all=passed+[nextstate]
                heu1=heuristic(nextstate,problem)
                cost_all=problem.getCostOfActions(all_ac)+heu1
                
                data.push((nextstate,all_ac),cost_all)
            
            elif (nextstate in passed) and (cost_all>max([cost_all])):
                nextstate=state

    return [ST]
    
    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

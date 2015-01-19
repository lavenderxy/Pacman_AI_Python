# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """

    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
     
    "*** YOUR CODE HERE ***"
    """
    k=0
    state_all=self.mdp.getStates()
    #print('sssss',state)
    
    while k<=iterations:
        Vi=util.Counter()
    
        for state in state_all:
            #V[i+1]=sum_{s in state}(getQValue(state,pai_star))
            #pai_k[k]=self.getPolicy(state)
            #Vi[k]=self.values[state]
            #Qi[k]=self.getQValue(state,pai_k[k])
            #Vi[k+1]=Qi[k]
            #k=k+1
            
            pai_k=self.getPolicy(state)
            if pai_k==None:
                Vi[state]=0
            
            actions=self.mdp.getPossibleActions(state)
            if not self.mdp.isTerminal(state) or actions:
                for a in actions:
                    pai_tmp=self.getQValue(state, a)
                    ma=float('-Inf')
                    if ma<pai_tmp:
                        ma=pai_tmp
                        pai_star=a
    
                Vi[state]=pai_star
            self.values=Vi
    """
 
    for i in range(0,self.iterations):

        Vi = util.Counter()
        state_all=self.mdp.getStates()
        for state in state_all:
            
            actions = self.mdp.getPossibleActions(state)
            ma=float('-Inf')
            if not self.mdp.isTerminal(state) or actions:
                for a in actions:
                    pai_tmp = self.getQValue(state, a)
                    
                    if ma < pai_tmp:
                        ma=pai_tmp
                        pai_star=a
            
                Vi[state] = ma
    
            elif self.mdp.isTerminal(state) or not actions:
                Vi[state]=0
    
        self.values = Vi
 

    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    
    
    gamma=self.discount
    #print("gamma",gamma)
    
    #getTransitionStatesAndProbs return list of(nextState,prob)
    T=self.mdp.getTransitionStatesAndProbs(state,action)
    Q_star=0
    
    for t in T:
        nextState=t[0]

        tranpro=t[1]
        vi=self.values[nextState]
        
        r=self.mdp.getReward(state,action,nextState)

        Q_tmp=tranpro*(r+gamma*vi)
        #Q_star=sum_{s in state}(Q_tmp)
        Q_star += Q_tmp
    
    return Q_star



    #util.raiseNotDefined()

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    
    actions=self.mdp.getPossibleActions(state)
    pai_star=None
    ma=float('-Inf')
    if not self.mdp.isTerminal(state) or actions:
        #pai_star=max_{a in action}(Q_star)
        for a in actions:
            pai_tmp=self.getQValue(state, a)
    
            if ma<pai_tmp:
                ma=pai_tmp
                pai_star=a
    
        return pai_star
    elif self.mdp.isTerminal(state) or not actions:
        return None



    #util.raiseNotDefined()

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  

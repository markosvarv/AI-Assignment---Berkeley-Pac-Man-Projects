# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def find_path (current_node, parent):
    current_parent, direction = parent[current_node]
    if current_parent is None:
        return []
    else:
        return find_path(current_parent, parent) + [direction]

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    from util import Stack
    frontier = Stack()  # initialize a LIFO stack for the frontier
    start_node = problem.getStartState()
    frontier.push(start_node)  # add the start node to the frontier

    parent = {start_node: (None, None)}  # use a dictionary to keep parent of every node

    explored = set()  # use a set to keep the explored nodes

    while True:
        if frontier.isEmpty():
            return None

        current_node = frontier.pop()

        explored.add(current_node)

        if problem.isGoalState(current_node):
            return find_path(current_node, parent)

        successors = problem.getSuccessors(current_node)
        for child, direction, cost in successors:
            if child not in explored and child not in frontier.list:
                frontier.push(child)
                parent[child] = (current_node, direction)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    from util import Queue
    frontier = Queue()  # initialize a FIFO queue for the frontier
    start_node = problem.getStartState()
    frontier.push(start_node)  # add the start node to the frontier

    parent = {start_node: (None, None)}  # use a dictionary to keep parent of every node

    explored = set()  # use a set to keep the explored nodes

    while True:
        if frontier.isEmpty():
            return None

        current_node = frontier.pop()

        explored.add(current_node)

        if problem.isGoalState(current_node):
            return find_path(current_node, parent)

        successors = problem.getSuccessors(current_node)
        for child, direction, cost in successors:
            if child not in explored and child not in frontier.list:
                frontier.push(child)
                parent[child] = (current_node, direction)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue

    start_node = problem.getStartState()

    frontier = PriorityQueue()  # initialize a priority queue for the frontier
    frontier.push(start_node, 0)  # add the start node to the frontier

    parent = {start_node: (None, None)}  # use a dictionary to keep parent of every node
    g_path_costs = {}

    explored = set()  # use a set to keep the explored nodes

    g_path_costs[problem.getStartState()] = 0

    while True:

        if frontier.isEmpty():
            return None

        current_node = frontier.pop()

        explored.add(current_node)

        if problem.isGoalState(current_node):
            return find_path(current_node, parent)

        successors = problem.getSuccessors(current_node)
        for child, direction, cost in successors:
            g_cost = g_path_costs[current_node] + cost
            if child not in explored:
                if child not in g_path_costs or g_path_costs[child] > g_cost:
                    frontier.update(child, g_cost)
                    g_path_costs[child] = g_cost
                    parent[child] = (current_node, direction)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    from util import PriorityQueue

    start_node = problem.getStartState()

    frontier = PriorityQueue()  # initialize a priority queue for the frontier
    frontier.push(start_node, 0)  # add the start node to the frontier

    parent = {start_node: (None, None)}  # use a dictionary to keep parent of every node
    g_path_costs = {}

    explored = set()

    g_path_costs[problem.getStartState()] = 0

    while True:

        if frontier.isEmpty():
            return None

        current_node = frontier.pop()

        explored.add(current_node)

        if problem.isGoalState(current_node):
            return find_path(current_node, parent)

        successors = problem.getSuccessors(current_node)
        for child_node, direction, cost in successors:
            g_cost = g_path_costs[current_node] + cost
            if child_node not in explored:
                if child_node not in g_path_costs or g_path_costs[child_node] > g_cost:
                    astar_cost = g_cost + heuristic(child_node, problem)
                    g_path_costs[child_node] = g_cost
                    frontier.update(child_node, astar_cost)  # update also pushes a node in priority queue
                    parent[child_node] = (current_node, direction)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

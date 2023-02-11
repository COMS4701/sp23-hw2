import numpy as np
import random
from utils import utility, successors, Node, Tree


# ******************************************************************************
# ***************************** ASSIGNMENT BEGINS ******************************
# ******************************************************************************

## ALPHA-BETA SEARCH METHODS

def max_value(state, alpha, beta, k):
    """ Find the max value given state and return the utility and the game board
    state after the move. Please see Lecture 6 for pseudocode. 

    Args:
        state (np.ndarray): the state of the game board, mxn numpy array.
        alpha (float): the alpha value
        beta (float): the beta value
        k (int): the number of consecutive marks
    Returns:
        tuple[float, np.ndarray]: utility value and the board after the move
    """
    
    # TODO:
    return 0, state


def min_value(state, alpha, beta, k):
    """ Find the min value given state and return the utility and the game board
    state after the move. Please see Lecture 6 for pseudocode. 

    Args:
        state (np.ndarray): the state of the game board, mxn numpy array.
        alpha (float): the alpha value
        beta (float): the beta value
        k (int): the number of consecutive marks
    Returns:
        tuple[float, np.ndarray]: utility value and the board after the move
    """
    
    # TODO:
    return 0, state


## MONTE CARLO TREE SEARCH METHODS

def select(tree, state, k, alpha):
    """ Starting from state, find a terminal node or node with unexpanded 
    children. If all children of a node are in tree, move to the one with the 
    highest UCT value.

    Args:
        tree (utils.Tree): the search tree
        state (np.ndarray): the game board state
        k (int): the number of consecutive marks
        alpha (float): exploration parameter
    Returns:
        np.ndarray: the game board state
    """
    
    # TODO: 
    return state


def expand(tree, state, k):
    """ Add a child node of state into the tree if it's not terminal and return 
    tree and new state, or return current tree and state if it is terminal.

    Args:
        tree (utils.Tree): the search tree
        state (np.ndarray): the game board state
        k (int): the number of consecutive marks
    Returns:
        tuple[utils.Tree, np.ndarray]: the tree and the game state
    """
    
    # TODO:
    return tree, state


def simulate(state, player, k):
    """ Run one game rollout from state to a terminal state using random
    playout policy and return the numerical utility of the result.

    Args:
        state (np.ndarray): the game board state
        player (string): the player, `O` or `X`
        k (int): the number of consecutive marks
    Returns:
        float: the utility
    """

    # TODO:
    return 0


def backprop(tree, state, result):
    """ Backpropagate result from state up to the root. 
    All nodes on path have N, number of plays, incremented by 1. 
    If result is a win for a node's parent player, w is incremented by 1.
    If result is a draw, w is incremented by 0.5 for all nodes.

    Args:
        tree (utils.Tree): the search tree
        state (np.ndarray): the game board state
        result (float): the result / utility value

    Returns:
        utils.Tree: the game tree
    """

    # TODO: 
    return tree


# ******************************************************************************
# ****************************** ASSIGNMENT ENDS *******************************
# ******************************************************************************


def MCTS(state, player, k, rollouts, alpha):
    # MCTS main loop: Execute MCTS steps rollouts number of times
    # Then return successor with highest number of rollouts
    tree = Tree(Node(state, None, player, 0, 1))
    for i in range(rollouts):
        leaf = select(tree, state, k, alpha)
        tree, new = expand(tree, leaf, k)
        result = simulate(new, tree.get(new).player, k)
        tree = backprop(tree, new, result)
    next = None
    plays = 0
    for s in successors(state, tree.get(state).player):
        if tree.get(s).N > plays:
            plays = tree.get(s).N
            next = s
    return next


def ABS(state, player, k):
    # ABS main loop: Execute alpha-beta search
    # X is maximizing player, O is minimizing player
    # Then return best move for the given player
    if player == 'X':
        value, move = max_value(state, -float("inf"), float("inf"), k)
    else:
        value, move = min_value(state, -float("inf"), float("inf"), k)
    return value, move


def game_loop(state, player, k, Xstrat=0, Ostrat=0, rollouts=0, alpha=0, print_result=False):
    # Plays the game from state to terminal
    # If random_opponent, opponent of player plays randomly, else same strategy as player
    # rollouts and alpha for MCTS; if rollouts is 0, ABS is invoked instead
    current = player
    while utility(state, k) is None:
        if current == 'X':
            strategy = Xstrat
        else:
            strategy = Ostrat
        if strategy == 0:
            state = random.choice(successors(state, current))
        elif strategy == 1:
            _, state = ABS(state, current, k)
        else:
            state = MCTS(state, current, k, rollouts, .01)
        current = 'O' if current == 'X' else 'X'
        if print_result:
            print(state)
    return utility(state, k)


def main():
    # ********* MODIFY THE PARAMETER VALUES *********
    m = 3
    n = 3
    k = 3
   
    rollouts = 0
    alpha = 1
    
    num_games = 1
    Xstrat = 0
    Ostrat = 0
    print_result = True

    state = np.full((m, n), '.')
    player = 'X'
    
    results = {'X wins': 0, 'O wins': 0, 'draws': 0}
    for i in range(num_games):
        result = game_loop(state, player, k, Xstrat, Ostrat, rollouts, alpha, print_result)
        if result == 1:
            results['X wins'] += 1
        elif result == -1:
            results['O wins'] += 1
        else:
            results['draws'] += 1
    print(results)


if __name__ == "__main__":
    main()

import re
import random
import numpy as np


def utility(state, k):
    # Test whether state is a terminal or not; also return game score if yes
    if k_in_row(state, "X{"+str(k)+"}"):
        return 1
    if k_in_row(state, "O{"+str(k)+"}"):
        return -1
    if np.count_nonzero(state == '.') == 0:
        return 0
    return None


def k_in_row(state, regex):
    # Return a list of all consecutive board positions in state that satisfy regex
    flipped = np.fliplr(state)
    sequences = []

    for i in range(state.shape[0]):
        sequences.extend(re.findall(regex, ''.join(state[i])))
        sequences.extend(re.findall(regex, ''.join(np.diag(state, k=-i))))
        sequences.extend(re.findall(regex, ''.join(np.diag(flipped, k=-i))))

    for j in range(state.shape[1]):
        sequences.extend(re.findall(regex, ''.join(state[:, j])))
        if j != 0:
            sequences.extend(re.findall(regex, ''.join(np.diag(state, k=j))))
            sequences.extend(re.findall(regex, ''.join(np.diag(flipped, k=j))))

    return sequences


def successors(state, player):
    # Return list of successors of state and player's turn to move
    succ = []
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i, j] == '.':
                new = np.copy(state)
                new[i, j] = player
                succ.append(new)
    return succ


class Node:
    def __init__(self, state, parent, player, w=0, N=0):
        self.state = state
        self.parent = parent
        self.player = player
        self.w = w
        self.N = N


class Tree:
    def __init__(self, root):
        self.nodes = {root.state.tobytes(): root}

    def add(self, node):
        self.nodes[node.state.tobytes()] = node

    def get(self, state):
        flat_state = state.tobytes()
        if flat_state not in self.nodes:
            return None
        return self.nodes[flat_state]


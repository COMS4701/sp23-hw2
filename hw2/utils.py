from dataclasses import dataclass
from enum import Enum
import re

import numpy as np
import numpy.typing as npt


@dataclass
class Node:
    state: npt.ArrayLike
    parent: "Node"
    player: str
    w: int = 0
    N: int = 0


class Tree:
    def __init__(self, root: "Node"):
        self.nodes = {root.state.tobytes(): root}

    def add(self, node: "Node"):
        self.nodes[node.state.tobytes()] = node

    def get(self, state: npt.ArrayLike):
        flat_state = state.tobytes()
        if flat_state not in self.nodes:
            return None
        return self.nodes[flat_state]


class GameStrategy(Enum):
    RANDOM = 0
    ABS = 1
    MCTS = 2


def utility(state: npt.ArrayLike, k: int):
    # Test whether state is a terminal or not; also return game score if yes
    if k_in_row(state, "X{" + str(k) + "}"):
        return 1
    if k_in_row(state, "O{" + str(k) + "}"):
        return -1
    if np.count_nonzero(state == ".") == 0:
        return 0
    return None


def k_in_row(state: npt.ArrayLike, regex: str):
    # Return a list of all consecutive board positions in state that satisfy regex
    flipped = np.fliplr(state)
    sequences = []

    for i in range(state.shape[0]):
        sequences.extend(re.findall(regex, "".join(state[i])))
        sequences.extend(re.findall(regex, "".join(np.diag(state, k=-i))))
        sequences.extend(re.findall(regex, "".join(np.diag(flipped, k=-i))))

    for j in range(state.shape[1]):
        sequences.extend(re.findall(regex, "".join(state[:, j])))
        if j != 0:
            sequences.extend(re.findall(regex, "".join(np.diag(state, k=j))))
            sequences.extend(re.findall(regex, "".join(np.diag(flipped, k=j))))

    return sequences


def successors(state: npt.ArrayLike, player: str):
    # Return list of successors of state and player's turn to move
    succ = []
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i, j] == ".":
                new = np.copy(state)
                new[i, j] = player
                succ.append(new)
    return succ

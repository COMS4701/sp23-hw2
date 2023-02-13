import hydra
from omegaconf import DictConfig
import numpy as np

import hw2.mnk_game as mnk
from hw2.utils import GameStrategy

@hydra.main(config_path='.', config_name="mnk_configs")
def main(configs: DictConfig):
    m = configs.m
    n = configs.n
    k = configs.k

    rollouts = configs.rollouts
    alpha = configs.mcts_alpha

    num_games = configs.num_games
    Xstrat = GameStrategy(configs.x_strat)
    Ostrat = GameStrategy(configs.y_strat)
    print_result = configs.verbose

    state = np.full((m, n), ".")
    player = "X"

    results = {"X wins": 0, "O wins": 0, "draws": 0}
    
    for _ in range(num_games):
        result = mnk.game_loop(
            state, player, k, Xstrat, Ostrat, rollouts, alpha, print_result
        )
        
        if result == 1:
            results["X wins"] += 1
        elif result == -1:
            results["O wins"] += 1
        else:
            results["draws"] += 1
    
    print(results)


if __name__ == "__main__":
    main()

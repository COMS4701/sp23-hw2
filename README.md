# COMS W4701 AI HW2 Programming


### Setup
1. Create and activate your virtual environment (make sure your python is at version 3.9 or higher).
```
# using venv
python -m venv .venv
source .venv/bin/activate   # on Windows, run the corresponding script

# alternatively, using conda
conda create -n hw2env python=3.9 pip
conda activate hw2env
```

2. Install poetry
```
pip install poetry
```

3. Install the `hw2` package
```
poetry install
```

###  Running your implementation
You may run the main program with
```
python main.py
```

The main simulation we run depends on a couple configurations, defined in `mnk_configs.yaml`:
```yaml
m: 3              # the 'm' in mnk
n: 3              # the 'n' in mnk
k: 3              # the 'k' in mnk
rollouts: 0       # number of rollouts in mcts
mcts_alpha: 1     # alpha value in mcts

num_games: 1      # number of game simluations to be run
x_strat: 0        # 0: RANDOM, 1: Alpha Beta Search, 2: MCTS 
y_strat: 0        # 0: RANDOM, 1: Alpha Beta Search, 2: MCTS 

verbose: True     # to print or not to print results
```
These are automatically loaded when you run `python main.py`. If you want to modify the configs (e.g. `m, n, k`, or `num_games` etc), change the respective values directly in `mnk_configs.yaml`. They will be used automatically when you run `python main.py` again. 

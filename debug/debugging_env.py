import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Utils.atari_wrappers import make_atari

if __name__ == "__main__":
    env = make_atari("PongNoFrameskip-v4")
    env.reset()
    env.step(1)
    env.get_rng_state()
    print("debug")
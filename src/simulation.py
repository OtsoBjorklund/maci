import creamas
from environment import MusicEnvironment

from impro_agent import ImprovisingAgent


def run_simulation(num_steps, num_agents):
    env = MusicEnvironment.create(('localhost', 5555))
    for i in range(0, num_agents):
        agent = ImprovisingAgent(env, filename='Invention_1.xml', motif_length = 4, num_motifs = 10, name='Agent_' + str(i))

    sim = creamas.Simulation(env, log_folder='logs', callback=env.agents_listen_and_evaluate)
    sim.async_steps(num_steps)
    sim.end()


if __name__ == "__main__":
    run_simulation(20, 4)
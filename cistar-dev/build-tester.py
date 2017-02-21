import logging

from cistar.core.exp import SumoExperiment
from cistar.envs.loop_velocity import SimpleVelocityEnvironment
from cistar.scenarios.loop.loop_scenario import LoopScenario
from cistar.controllers.velocity_controllers import *

logging.basicConfig(level=logging.INFO)

sumo_params = {"port": 8873, "time_step":0.1}

sumo_binary = "sumo"

type_params = {"cfm": (15, make_constant_vel_model())}

env_params = {"target_velocity": 25}

net_params = {"length": 200, "lanes": 1, "speed_limit":35, "resolution": 40, "net_path":"debug/net/"}

cfg_params = {"start_time": 0, "end_time":3000, "cfg_path":"debug/cfg/"}

initial_config = {"shuffle":False}

scenario = LoopScenario("test-exp", type_params, net_params, cfg_params, initial_config)
##data path needs to be relative to cfg location
leah_sumo_params = {"port": 8873}

exp = SumoExperiment(SimpleVelocityEnvironment, env_params, sumo_binary, sumo_params, scenario)

logging.info("Experiment Set Up complete")

exp.run(1, 1000)

exp.env.terminate()

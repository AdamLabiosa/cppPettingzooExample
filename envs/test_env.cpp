#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <vector>
#include <string>

namespace py = pybind11;

std::vector<std::string> agents = {"agent0", "agent1"};
// observation space format: {lows, highs}
std::vector<std::vector<float>> obs_space = {{-1.0, -1.0, -1.0}, {1.0, 1.0, 1.0}};
// action space format: {lows, highs}
std::vector<std::vector<float>> act_space = {{-1.0, -1.0, -1.0}, {1.0, 1.0, 1.0}};

// get agent names
std::vector<std::string> get_agents() {
    return agents;
}

std::vector<std::string> getActionObsType() {
    return {"Box", "Box"};
}

// get observation space
std::vector<std::vector<float>> getObservationSpace() {
    return obs_space;
}

// get action space
std::vector<std::vector<float>> getActionSpace() {
    return act_space;
}

std::vector<float> get_obs(const std::string& agent_name) {
    float obs1 = 1.0;
    float obs2 = 0.5;
    float obs3 = -1.0;

    // TODO: Implement function to get observations for the given agent
    std::vector<float> observations = {obs1, obs2, obs3};
    return observations;
}


std::tuple<py::dict, py::dict> reset() {
    py::dict observations;
    py::dict infos;
    for (auto agent_name : agents) {
        observations[agent_name.c_str()] = py::cast(get_obs(agent_name));
        infos[agent_name.c_str()] = py::cast("");
    }
    return std::make_tuple(observations, infos);
}

std::tuple<py::dict, py::dict, py::dict, py::dict, py::dict> step(py::dict actions) {
    py::dict observations;
    py::dict rewards;
    py::dict terminated;
    py::dict truncated;
    py::dict info;

    // count to 1000
    for (int i = 0; i < 10000; i++) {
        int x = 0;
    }

    for (auto agent_name : agents) {
        observations[agent_name.c_str()] = py::cast(get_obs(agent_name));
        rewards[agent_name.c_str()] = py::cast(0.0);
        terminated[agent_name.c_str()] = py::cast(false);
        truncated[agent_name.c_str()] = py::cast(false);
        // info[agent_name.c_str()] = py::cast("");
    }
    info = py::dict();
    return std::make_tuple(observations, rewards, terminated, truncated, info);
}



PYBIND11_MODULE(test_env, m) {
    m.def("reset", &reset, "Reset the environment and return initial observations and infos");
    m.def("step", &step, "Step the environment and return observations, rewards, dones, infos, and actions");
    m.def("get_agents", &get_agents, "Get the list of agents");
    m.def("getObservationSpace", &getObservationSpace, "Get the observation space");
    m.def("getActionSpace", &getActionSpace, "Get the action space");
    m.def("getActionObsType", &getActionObsType, "Get the observation and action space type");
}


# DQN for Traffic Signal Control Notes

## Overview

Deep Q-Networks can be used to learn traffic signal control policies. The agent observes the traffic state, chooses a signal phase, receives a reward, and updates an action-value function. The goal is to reduce congestion measures such as queue length, waiting time, or delay.

A DQN implementation often contains several components: replay buffer, online Q-network, target network, exploration strategy, state representation, and reward design. These components are related, but each one answers a different engineering question.

## Replay Buffer

The replay buffer stores past transitions of the form state, action, reward, next state, and done flag. During training, the agent samples mini-batches from this buffer instead of learning only from the newest transition. This breaks temporal correlation and improves data efficiency.

In a traffic signal task, replay can expose the model to diverse traffic patterns. The same training batch may contain rush-hour queues, low-flow periods, and phase switching events.

## Target Network

The target network is a delayed copy of the online Q-network used to compute the bootstrapped target value. Because it is updated less frequently than the online network, the target value changes more slowly and training becomes more stable.

This mechanism reduces oscillation in Q-learning because the model is not chasing a target that moves after every gradient update. In traffic signal control, this stability is important because noisy rewards and changing traffic demand can already make learning unstable.

## Exploration Strategy

An epsilon-greedy policy chooses a random action with probability epsilon and the greedy action otherwise. At the beginning of training, a high epsilon encourages exploration of different signal phases. Later, epsilon is reduced so the agent can exploit the learned value function.

Exploration must be handled carefully in traffic control. Too much random switching can produce unrealistic or unsafe signal behavior, while too little exploration may trap the agent in a poor local policy.

## Reward Design

The reward function defines what the traffic controller optimizes. Common choices include negative queue length, negative waiting time, change in delay, or a weighted combination of several traffic metrics. A reward that is too noisy can slow learning, while a reward that ignores fairness may improve one direction and harm another.

Reward design is often domain-specific. The best reward depends on the simulator, intersection layout, phase constraints, and evaluation metric.

## Chunking Risk

This document is useful for testing chunk_too_large and wrong_section_hit failures. If a single chunk mixes replay buffer, target network, exploration, and reward design, a query about target network stability may be diluted by unrelated DQN components.

A local patch can re-chunk only the `Target Network` section and keep the heading with the body. This should improve retrieval for questions about why the target network stabilizes DQN training.

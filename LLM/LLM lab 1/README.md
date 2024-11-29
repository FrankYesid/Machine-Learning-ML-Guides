# Lab 1: Constructing a ReAct Agent from Scratch

Welcome to this lab, where we will explore how to build a ReAct (Reasoning and Acting) agent from the ground up using **Amazon Bedrock** and **Anthropic's Claude model**. 

The **ReAct approach** integrates reasoning (e.g., chain-of-thought prompting) with acting (e.g., generating action plans) in a seamless, interleaved fashion. This methodology was introduced in the paper [*ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629).

![ReAct approach](../assets/lab1_1.png)

The architecture of the ReAct agent in this lab is depicted below. The primary components include:
- **User Input**
- **System Prompt**
- **Language Model**
- **Identified Action**
- **Execution Tool** (triggered by the action)

![Agent structure](../assets/lab1_2.png) 
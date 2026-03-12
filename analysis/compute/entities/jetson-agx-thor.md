---
layout: default
title: Jetson AGX Thor
name: Jetson AGX Thor
category: individuals
compute: 2.07e+15
stakeholders: 1
---

## Description

Jetson AGX Thor is NVIDIA's high-end Jetson platform for next-generation robotics and edge AI.
NVIDIA materials publish up to 2070 FP4 TFLOPS AI compute for the platform.[^nvidia-jetson-thor]

## Scope

This entry records 2.07e+15 operations per second using the published 2070 AI-compute figure in
dataset notation.[^nvidia-jetson-thor]
Because the public value is framed as FP4 AI compute rather than strict dense INT8 TOPS, this row
is provisional for cross-entry comparability.

**Total compute:** 2.07e+15 operations per second (provisional, mixed-precision vendor metric).

## Implications

Thor-class edge modules may close part of the gap between embedded systems and datacenter-class AI
inference nodes. The normalization method should be explicit whenever this entry is compared with
dense INT8-only hardware rows.

## Works Cited

[^nvidia-jetson-thor]: NVIDIA. "Jetson AGX Thor." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/>.

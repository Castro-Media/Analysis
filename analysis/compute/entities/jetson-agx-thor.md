---
layout: default
title: Jetson AGX Thor
name: Jetson AGX Thor
category: individuals
compute: 1.035e+15
compute_metric: dense_int8_tops
compute_note: "Converted from 2070 FP4 TFLOPS using FP4 to FP8/INT8 scaling of /2."
stakeholders: 1
---

## Description

Jetson AGX Thor is NVIDIA's high-end Jetson platform for next-generation robotics and edge AI.
NVIDIA materials publish up to 2070 FP4 TFLOPS AI compute for the platform.[^nvidia-jetson-thor]

## Scope

This entry converts the published 2070 FP4 TFLOPS figure to the dense INT8 scale. Using the report
precision rule where FP4 throughput is 2x FP8/INT8 throughput, the dense INT8-equivalent value is
1035 TOPS, or 1.035e+15 operations per second.[^nvidia-jetson-thor]

**Total compute:** 1.035e+15 dense INT8 operations per second.

## Implications

Thor-class edge modules may close part of the gap between embedded systems and datacenter-class AI
inference nodes while remaining comparable to the rest of this report on the dense INT8 scale.

## Works Cited

[^nvidia-jetson-thor]: NVIDIA. "Jetson AGX Thor." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/>.

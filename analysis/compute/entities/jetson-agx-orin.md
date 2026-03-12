---
layout: default
title: Jetson AGX Orin
name: Jetson AGX Orin
category: individuals
compute: 1.375e+14
compute_metric: dense_int8_tops
compute_note: "Converted from published 275 sparse TOPS to dense INT8 scale by dividing by 2."
stakeholders: 1
---

## Description

Jetson AGX Orin is a newer embedded AI module line designed for robotics and autonomous systems.
NVIDIA publishes AI performance at up to 275 TOPS.[^nvidia-jetson-orin]

## Scope

This row converts the published 275 TOPS figure to the dense INT8 scale. The report applies a
2:4 sparsity removal factor of /2, yielding 137.5 dense INT8 TOPS or 1.375e+14 operations per
second.[^nvidia-jetson-orin]

**Total compute:** 1.375e+14 dense INT8 operations per second.

## Implications

AGX Orin substantially increases edge AI throughput versus Xavier-class hardware, enabling larger
models and higher concurrency at the edge while preserving comparability on the dense INT8 scale.

## Works Cited

[^nvidia-jetson-orin]: NVIDIA. "Jetson AGX Orin." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/>.

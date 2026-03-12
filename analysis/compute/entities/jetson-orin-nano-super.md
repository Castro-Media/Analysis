---
layout: default
title: Jetson Orin Nano Super
name: Jetson Orin Nano Super
category: individuals
compute: 3.35e+13
compute_metric: dense_int8_tops
compute_note: "Converted from published 67 sparse INT8 TOPS to dense INT8 scale by dividing by 2."
stakeholders: 1
---

## Description

The NVIDIA Jetson Orin Nano Super Developer Kit is an edge AI development platform designed for
robotics and embedded AI applications. NVIDIA publishes AI performance at 67 sparse INT8 TOPS for
this kit.[^nvidia-jetson-orin-nano-super]

## Scope

This entry converts the published 67 sparse INT8 TOPS to the dense INT8 scale used in this report.
Applying the sparsity removal rule (/2) yields 33.5 dense INT8 TOPS, or 3.35e+13 operations per
second.[^nvidia-jetson-orin-nano-super]

**Total compute:** 3.35e+13 dense INT8 operations per second.

## Implications

This platform provides accessible on-device AI capability for individual developers and small teams
while remaining within edge power and thermal constraints. Its compute capacity supports meaningful
real-time inference workflows without requiring datacenter infrastructure.

## Works Cited

[^nvidia-jetson-orin-nano-super]: NVIDIA. "Jetson Orin Nano Developer Kit." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin-nano/>.

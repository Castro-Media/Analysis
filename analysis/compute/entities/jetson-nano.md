---
layout: default
title: NVIDIA Jetson Nano
name: NVIDIA Jetson Nano
category: individuals
compute: 4.72e+11
compute_metric: non_int8_proxy
compute_note: "Vendor publishes 472 GFLOPS accelerated compute; stored as a proxy value."
stakeholders: 1
---

## Description

The NVIDIA Jetson Nano is an entry-level edge AI module for hobbyist robotics and embedded projects.
NVIDIA publishes Jetson Nano performance as 472 GFLOPS accelerated compute, not as INT8 TOPS.[^nvidia-jetson-nano]

## Scope

A single Jetson Nano is provisionally tracked at 4.72e+11 operations per second by mapping the
published 472 GFLOPS figure into the dataset scientific notation format.[^nvidia-jetson-nano]
Because this is not a vendor INT8 TOPS metric, this row is a proxy rather than a strict dense
INT8 measurement.

**Total compute:** 4.72e+11 operations per second (proxy from vendor GFLOPS figure).

## Implications

The module enables experimentation with vision and robotics on personal budgets, but
its limited throughput restricts model size and real-time performance compared with newer Jetson
modules. Individuals can prototype edge AI applications yet must optimize carefully.

## Works Cited

[^nvidia-jetson-nano]: NVIDIA. "Jetson Nano." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/>.

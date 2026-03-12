---
layout: default
title: NVIDIA Jetson Nano
name: NVIDIA Jetson Nano
category: individuals
compute: 9.44e+11
compute_metric: dense_int8_tops
compute_note: "Converted from 472 GFLOPS FP16-equivalent throughput using FP16 to INT8 factor x2."
stakeholders: 1
---

## Description

The NVIDIA Jetson Nano is an entry-level edge AI module for hobbyist robotics and embedded
projects. NVIDIA publishes Jetson Nano performance as 472 GFLOPS accelerated compute.[^nvidia-jetson-nano]

## Scope

A single Jetson Nano is normalized to 9.44e+11 dense INT8 operations per second by applying the
report conversion rule from FP16-equivalent throughput to INT8 throughput (x2) to the published
472 GFLOPS figure.[^nvidia-jetson-nano]

**Total compute:** 9.44e+11 dense INT8 operations per second.

## Implications

The module enables experimentation with vision and robotics on personal budgets, but
its limited throughput restricts model size and real-time performance compared with newer Jetson
modules. Individuals can prototype edge AI applications yet must optimize carefully.

## Works Cited

[^nvidia-jetson-nano]: NVIDIA. "Jetson Nano." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/>.

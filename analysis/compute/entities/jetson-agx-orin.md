---
layout: default
title: Jetson AGX Orin
name: Jetson AGX Orin
category: individuals
compute: 2.75e+14
compute_metric: vendor_ai_tops
compute_note: "Uses vendor-published AI TOPS (275 TOPS); comparability to strict dense INT8 is provisional."
stakeholders: 1
---

## Description

Jetson AGX Orin is a newer embedded AI module line designed for robotics and autonomous systems.
NVIDIA publishes AI performance at up to 275 TOPS.[^nvidia-jetson-orin]

## Scope

This row stores the published 275 TOPS figure as 2.75e+14 operations per second in dataset
notation.[^nvidia-jetson-orin]
The published value is vendor AI TOPS, so direct dense INT8 comparability with older entries
should be treated as provisional.

**Total compute:** 2.75e+14 operations per second (vendor AI TOPS based).

## Implications

AGX Orin substantially increases edge AI throughput versus Xavier-class hardware, enabling larger
models and higher concurrency at the edge. Normalization consistency is important when comparing
this row with dense-only INT8 entries.

## Works Cited

[^nvidia-jetson-orin]: NVIDIA. "Jetson AGX Orin." Accessed 2026. <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/>.

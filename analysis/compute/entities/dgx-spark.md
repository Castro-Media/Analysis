---
layout: default
title: NVIDIA DGX Spark
name: NVIDIA DGX Spark
category: corporations
compute: 2.5e+14
stakeholders: 1
---

## Description

NVIDIA markets DGX Spark as a rack-scale Blackwell platform that integrates fifth-generation Tensor Cores, positioning the system for FP4 and FP8 accelerated workloads while bundling system management software and enterprise support.[^nvidia-dgx-spark]

## Scope

### DGX Spark rack configuration

NVIDIA quotes "up to 1 PFLOP FP4 (with sparsity)" for DGX Spark's fifth-generation Tensor Cores.[^nvidia-dgx-spark] NVIDIA's Blackwell architecture brief shows FP4 throughput running at twice FP8, establishing 1 PFLOP FP4 (sparse) as 0.5 PFLOP FP4 dense and 0.25 PFLOP FP8 dense.[^nvidia-blackwell] NVIDIA's HGX Blackwell specifications equate FP8 TFLOPS and INT8 TOPS on the same Tensor Cores, so 0.25 PFLOP FP8 dense translates directly to roughly 250 dense INT8 TOPS per system.[^nvidia-hgx] Applying the dataset's dense counting rule yields the reported 2.5e+14 INT8 operations per second.

Independent testing indicates early DGX Spark units can throttle, delivering nearer to 125–200 sustained INT8 TOPS under thermal or power limits; plan capacity with that utilization caveat even though peak dense throughput remains 2.5e+14 ops/s.[^toms-hardware]

**Total compute:** 2.5e+14 dense INT8 TOPS attributable to a single DGX Spark system pending broader fleet inventory data.

## Implications

DGX Spark supplies Blackwell-class accelerators in a turnkey rack, giving a single operator access to quarter-petaflop FP8 density for enterprise AI development. If sustained output lags the advertised peak as early reports suggest, operators must budget additional racks or aggressive cooling to meet real-world deployment targets, tempering the strategic advantage otherwise gained from Blackwell's FP4/FP8 versatility.[^toms-hardware]

## Works Cited

[^nvidia-dgx-spark]: NVIDIA. "NVIDIA DGX Spark." Accessed 2025. <https://www.nvidia.com/en-us/products/workstations/dgx-spark/>.
[^nvidia-blackwell]: NVIDIA. "NVIDIA RTX Blackwell GPU Architecture." 2024. <https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf>.
[^nvidia-hgx]: NVIDIA. "NVIDIA HGX Platform." Accessed 2025. <https://www.nvidia.com/en-us/data-center/hgx/>.
[^toms-hardware]: Tom's Hardware. "Users question DGX Spark performance." 2025. <https://www.tomshardware.com/tech-industry/semiconductors/users-question-dgx-spark-performance>.

---
layout: default
title: NVIDIA Tesla P40
name: NVIDIA Tesla P40
category: individuals
compute: 4.7e+13
stakeholders: 1
---

## Description

The NVIDIA Tesla P40 is a data center accelerator aimed at deep learning.
It pairs moderate compute throughput with 24 GB of memory and is obtainable
on the secondary market by individual operators.

## Scope

A single Tesla P40 offers 4.7×10^13 dense INT8 operations per second
(≈47 INT8 TOPS). NVIDIA lists 11.75 FP32 TFLOPS in the datasheet; using
the ×4 rule to convert FP32 to INT8 yields this compute figure.[^1]

**Total compute:** 4.7×10^13 INT8 operations per second.

## Implications

The card's large memory helps run sizable models on personal hardware, but
its compute is far behind modern accelerators.
Individuals can experiment with training and inference without renting
cloud GPUs, though workloads remain limited.

## Works Cited

[^1]: NVIDIA, "NVIDIA Tesla P40 Datasheet," 2016.


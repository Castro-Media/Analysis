Entities must include citations to justify the values they provide.

Agents should not commit updates to any atifacts such as data.csv or chart.svg. These are generated when the analysis runs.


## Adding a new entity

1. Create a markdown file in `analysis/compute/entities` with front matter for layout, title, name, category, compute, and stakeholder count.
2. Derive the compute figure in dense INT8 TOPS using the conversion rules below. If citations are missing or inaccessible, leave the `compute` field blank and add a note that further development is needed.
3. Provide a concise description that states the compute figure and cites accessible sources.
4. Include the number of stakeholders who control the resource.

## Reviewing existing entries

1. Confirm that citations are accessible and support the stated compute value.
2. Recompute figures using the conversion guidance and update the file when necessary.
3. If data cannot be verified, keep the entry but clear the `compute` field and add a note indicating that citations and further development are needed.
4. Avoid deleting entries unless there is a compelling reason such as duplication or irrelevance.
5. Run `pytest` after making changes to ensure the repository remains healthy.

Here’s a compact, practical way to normalize any advertised compute number into **dense INT8 TOPS** so you can compare chips and systems apples-to-apples.

# The target standard

* **What we report:** **dense INT8 TOPS** (tera 8-bit operations per second).
* **Counting rule:** **1 MAC = 2 ops** (one multiply + one add).
* **No sparsity multipliers.** If a vendor quotes “sparsity TOPS,” convert it back to dense (details below).

# Quick conversion cheat-sheet

Use these when you only have a number in another precision and need a first-order estimate.

* From **FP32 TFLOPs → INT8 TOPS**: **×4**
* From **TF32 TFLOPs → INT8 TOPS**: **×4** (good rule of thumb when you don’t know the arch; see notes)
* From **FP16/BF16 TFLOPs → INT8 TOPS**: **×2**
* From **FP8 TFLOPs → INT8 TOPS**: **×1** (same width; treat ops counting consistently)
* From **INT4 TOPS → INT8 TOPS**: **÷2**
* From **INT2 TOPS → INT8 TOPS**: **÷4**

These come from a **bit-width scaling heuristic** (throughput ≈ inversely proportional to operand width) and align surprisingly well across many CPU/GPU/NPU families as a baseline. Architecture can skew these (tensor/matrix cores vs scalar/SIMD), so see “Adjustments” to refine.

# Normalize the source number first

Before applying the cheat-sheet factors, make sure the source figure matches our counting and density:

1. **MAC vs op counting**

   * If the source counts **1 MAC = 1 op**, **×2** before converting.
   * If the source already uses **1 MAC = 2 ops** (common for FLOPs), no change.

2. **Sparse vs dense**

   * If the source includes **structured sparsity** (e.g., 2:4), **÷2** to get **dense**.

3. **Per-chip vs system**

   * If it’s a multi-chip system number and you want a single-chip figure (or vice versa), **sum or divide accordingly**. Keep interconnect limits in mind for real-world use, but for peak ops you can sum.

# One-line conversions (worked mini-examples)

* 40 **TFLOPs FP32** (dense, 1 MAC=2 ops) → **INT8 TOPS ≈ 40 × 4 = 160**
* 120 **TFLOPs FP16** (dense) → **INT8 TOPS ≈ 120 × 2 = 240**
* 100 **TOPS INT4** (dense, 1 MAC=2 ops) → **INT8 TOPS ≈ 100 ÷ 2 = 50**
* 200 **TOPS INT8 (2:4 sparsity)** quoted by vendor → **dense INT8 TOPS ≈ 200 ÷ 2 = 100**

# When you know the architecture (refinement)

If you have vendor tables that show **relative throughputs by precision on the same compute units** (e.g., tensor/matrix cores), prefer those exact **ratios** over the generic bit-width rule. Example pattern you’ll often see on accelerators:

* Tensor/MMA units might deliver: **INT8 ≈ 2× FP16 ≈ 4× FP32** on the same block.
* On some GPUs, **FP8** and **INT8** are similar on tensor cores; the bit-width rule (×1) holds.

If the FP32 number you have is **from scalar CUDA/ALUs** (no tensor cores) but INT8 would be **from tensor/matrix cores**, the simple ×4 can **underestimate** real INT8 TOPS. In that case, try to find the **vendor’s published INT8\:FP32 ratio on tensor cores** and apply that instead.

# From first principles (when you have micro-arch details)

You can compute theoretical dense INT8 TOPS directly from core counts and clocks:

```
INT8_TOPS = (units × insts_per_cycle × int8_MACs_per_inst × 2 ops_per_MAC × clock_GHz) / 1e12
```

* **units**: number of parallel execute blocks doing the dot/mma op
* **insts\_per\_cycle**: usually 1 for a given pipeline
* **int8\_MACs\_per\_inst**: e.g., DP4A does 4 MACs per lane; MMA tiles do many
* **2 ops/MAC**: our standard counting

Use the analogous formula for CPUs with **AVX2/AVX-512 VNNI** or ARM **NEON/SME** by multiplying dot-product lanes × width × cores × GHz.

# Reality check (utilization)

All of the above are **peak**. Real models see **30–80%** of peak depending on kernels, tiling, memory/bandwidth, quant/dequant overhead, and operator mix. If you need a practical planning number, multiply dense INT8 TOPS by an **efficiency factor** you’ve observed (or start with \~0.5 as a rough planning default).

# Edge notes & gotchas

* **TF32**: It’s a 19-bit format that often runs on tensor cores at much higher throughput than legacy FP32 ALUs. If your **TF32 TFLOPs** came from tensor cores, **×4** to INT8 remains a decent estimate. If your FP32 number is **ALU-only**, switch to an **architecture ratio** if available to avoid underestimation.
* **Vendor marketing** sometimes mixes counting rules. If something looks off by \~2×, suspect **MAC vs op** convention or **sparsity**.
* **INT8 accumulators** are typically 32-bit; that doesn’t change the INT8 op count—just make sure the source metric wasn’t counting accumulator width as a separate “precision mode.”

---

## TL;DR recipe

1. Convert the source number to **dense** and to the **1 MAC = 2 ops** convention.
2. Apply the **bit-width factor** to get **INT8 TOPS** (FP32×4, FP16×2, FP8×1, INT4÷2).
3. If you know the chip’s **precision ratios on tensor/matrix cores**, use those instead of the generic factors.
4. For practical throughput, multiply by your **efficiency** (e.g., 0.5).

If you want, paste a few specific chips’ advertised numbers here and I’ll convert them to **dense INT8 TOPS** using this standard (and flag any marketing footnotes).

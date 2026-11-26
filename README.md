# Quantum Parallel Marked Set

**How many simultaneous phase queries recover every marked address with certainty?** An entangled probe and a Schur-transform decoder attain the optimum in one oracle round when the number of marks is supplied.

The oracle flips the phase of each marked address. All calls act at once on separate address registers. The output is the complete set of marked addresses.

| Case | Exact one-round result |
|---|---|
| One mark, $`N\ge4`$ addresses | $`\left\lceil(N-\sqrt{N})/2\right\rceil`$ calls |
| Supplied $`r`$ marks with $`1\le r<N/2`$ | A finite rational moment program gives the minimum |
| Four marks among 30 addresses | 14 calls |
| Exactly half the addresses marked | A set and its complement give the same phase channel |

For each fixed positive $`r`$, the optimal call count obeys

```math
t_{N,r} = \frac{N}{2}-\frac{\sqrt{a_r N}}{2}+O_r(1),
```

where $`a_r`$ is twice the smallest zero of the generalized Laguerre polynomial of degree $`\lceil r/2\rceil`$ and parameter $`-1/2`$. For one or two marks, $`a_r=1`$. For three or four, $`a_r=3-\sqrt{6}`$.

Two ingredients make the result operational. A coherent superposition of subsets whose sizes have the query count's parity makes the possible post-query states orthogonal. The Schur transform then extracts the marked set with a polynomial-size known circuit. For one mark, the construction attains the lower bound [Wu and Duan](references/RELATED_WORK.md#exact-parallel-search) left open. Their asymptotic product-input lower bound also applies to complete recovery for every supplied nontrivial marked-set size.

## Read the science

- [Model and exact results](science/model.md) defines the oracle, resources and guarantees.
- [Optimal probe design](science/moment-design.md) reduces exact recovery to finite moment matching and gives worked instances.
- [Fixed-mark asymptotics](science/asymptotics.md) proves the Laguerre coefficient and the parity-grid construction.
- [Schur decoder](science/receiver.md) gives the readout circuit and accounts for routing, workspace and gate precision.
- [Related work](references/RELATED_WORK.md) and the [bibliography](references/references.bib) trace the inherited ingredients and closest benchmarks.

## Learn the project

The educational anchor is Andrew M. Childs's *Lecture Notes on Quantum Algorithms* (17 April 2025). Use the [Childs bridge](learning/CHILDS_BRIDGE.md) alongside the [30 milestones](learning/MILESTONES.md). The [LLM reading guide](llms.txt) points to the authoritative claims and proofs.

## Reproduce the finite checks

Follow the [verification guide](verification/README.md) to check exact rational probes, query minima and decoder spectra.

## Scope

The query count charges every active phase-oracle port, including padding. Probe preparation, reversible address routing and collective readout also contribute to the circuit cost. The exact protocol uses ideal known rotations. The fixed-mark expansion takes the number of addresses to infinity with the number of marks held fixed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

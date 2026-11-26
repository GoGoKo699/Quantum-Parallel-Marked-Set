# Optimal probe design

[Model](model.md) · [Asymptotics](asymptotics.md) · [Decoder](receiver.md)

## From queries to subset sizes

Write any purified probe in the computational basis of the $`t`$ query registers. An ordered address tuple $`\boldsymbol i`$ acquires the phase $`(-1)^{|A\cap S(\boldsymbol i)|}`$, where $`S(\boldsymbol i)`$ contains exactly the addresses appearing an odd number of times. Let $`p(S)`$ be the sum of squared norms of the tuple amplitudes with that subset. The overlap of the two output states is

```math
\langle\psi_A|\psi_B\rangle
   =\sum_Sp(S)(-1)^{|(A\mathbin{\triangle}B)\cap S|}.
```

Even when the readout has an ancilla, perfect discrimination requires orthogonal states. Purifying a mixed protocol and retaining the extra register can only help, so the zero-overlap condition is necessary for arbitrary preprocessing. It is sufficient since the distinct pure output states can be projected onto their orthogonal rays. The [decoder](receiver.md) implements that discrimination using known gates.

The available subset sizes are $`0\le k\le\min\{N,t\}`$ with $`k\equiv t\pmod 2`$. To realize one subset, query each of its elements once and fill the remaining ports with pairs of repeated calls to a fixed address. Each pair contributes phase one. If a subset distribution makes all overlaps zero, its average under index permutations does too. Averaging therefore replaces it by a distribution uniform within each Hamming layer. Use a *coherent* superposition of those layer states and their weights to implement it in a single run.

## The finite moment program

Let $`w_k`$ be the probability of layer $`k`$, and define the binary Krawtchouk polynomial by

```math
K_d^{N}(k)=\sum_{h=0}^{d}(-1)^h
   \binom{k}{h}\binom{N-k}{d-h}.
```

The normalized layer average for a symmetric difference of size $`d`$ is $`K_d^N(k)/\binom Nd`$. To see this, fix a size-$`k`$ subset, sample a uniform size-$`d`$ set and condition on the size of their intersection. Permutation invariance exchanges this average with that over the original random $`k`$-subset.

For $`1\le r \lt N/2`$, all sizes $`2,4,\ldots,2r`$ occur as symmetric differences of two promised inputs. This gives the following exact feasibility test at $`t`$:

```math
w_k\ge0,\qquad \sum_k w_k=1,\qquad
\sum_k w_k K_{2j}^{N}(k)=0\quad(1\le j\le r).
```

The sum uses only the available parity layers. The forward implication follows from symmetrization and the necessary overlap test. For the reverse implication, prepare the incidence register in $`\sum_k\sqrt{w_k}|D_k\rangle`$, where $`|D_k\rangle`$ is the uniform normalized size-$`k`$ subset state. Route it into the query ports with paired padding. After the oracle and reversible address uncomputation, apply the explicit readout.

For the moment interpretation, set $`x_k=(N-2k)^2/N`$ and let $`\mu_N`$ be the law of $`(N-2B)^2/N`$ with $`B\sim\mathrm{Bin}(N,1/2)`$. The even Krawtchouk polynomials through index $`2r`$ have distinct degrees $`0,\ldots,r`$ as polynomials of $`x_k`$. This follows from their standard coefficient generating function $`(1-z)^k(1+z)^{N-k}`$, which gives degree $`d`$ in $`k`$ with nonzero leading coefficient and parity $`(-1)^d`$ under $`k\mapsto N-k`$. Under uniform subsets every nonconstant parity has expectation zero. Thus the same linear system is precisely

```math
\sum_k w_k x_k^j = \int x^j\,d\mu_N(x)
\qquad(0\le j\le r).
```

There are at most $`N+1`$ weights. Use the integer Krawtchouk form for exact rational linear programming. All coefficients have polynomial bit length in $`N`$. An extreme feasible point uses at most $`r+1`$ layers, since any larger support has a nonzero null direction that preserves the equations. Feasibility is monotone in $`t`$: an additional fixed-address query multiplies each output by a global sign. A feasible $`t\le N-1`$ always exists for this range of $`r`$. At $`t=N-1`$, use uniform subsets of parity $`t\bmod 2`$. Every tested difference is a proper nonempty subset, so its parity is balanced even conditional on total parity.

## One-mark formula

For $`r=1`$ the only moment equation is that the average of $`c_k=((N-2k)^2-N)/(N(N-1))`$ vanish. If $`t \lt (N-\sqrt{N})/2`$, every available layer has positive $`c_k`$. For $`N\ge5`$ take $`t=\lceil(N-\sqrt{N})/2\rceil`$. This lies at most at $`N/2`$ and is at least two. Then $`c_t\le0 \lt c_{t-2}`$, and the weight on layer $`t`$ is $`c_{t-2}/(c_{t-2}-c_t)`$. If $`c_t=0`$ the single layer suffices. At $`N=4`$ layer one gives zero. At $`N=3`$ layer one gives $`-1/3`$, and the two-call layers zero and two can be mixed to give zero.

## Worked finite cases

For $`N=25`$, 10 calls suffice for one mark using only layer 10. For two marks, at 10 calls the smallest allowed $`x_k`$ is one. Mean one forces concentration at that smallest node, yielding zero variance and violating the second moment target, whose variance is $`2-2/N`$. At 11 calls the layer sizes 11, 9 and 7, with weights $`219/280`$, $`7/60`$ and $`17/168`$, solve the two moment constraints.

For $`N=30`$ and four marks, 13 calls force $`x\ge 8/15`$. The factors at $`24/5`$ and $`128/15`$ correspond to consecutive grid points. Their product is nonnegative on the grid, and so is the first factor below. The binomial moments give

```math
\mathbb E_{\mu_{30}}\!\left[(X-8/15)(X-24/5)(X-128/15)\right]
   =-\frac{54}{125}.
```

A distribution on the 13-call grid would give a nonnegative expectation. At 14 calls the following weights solve all four Krawtchouk equations exactly.

| Layer size | Weight |
|---:|---:|
| 14 | $`8955/16384`$ |
| 12 | $`2555/8192`$ |
| 10 | $`987/8192`$ |
| 8 | $`585/32768`$ |
| 6 | $`105/32768`$ |

The [finite checks](../verification/README.md) reproduce the weights and minima by rational arithmetic.

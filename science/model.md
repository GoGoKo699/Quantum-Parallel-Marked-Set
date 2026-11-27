# Model and results

[Repository](../README.md) · [Probe design](moment-design.md) · [Decoder](receiver.md)

Let the addresses be $`[N]=\{1,\ldots,N\}`$, and let $`A\subseteq[N]`$ be the unknown marked set with a supplied size $`|A|=r`$. The only unknown operation is the ordinary phase oracle

```math
O_A|i\rangle=(-1)^{[i\in A]}|i\rangle.
```

A one-round protocol prepares a joint state of $`t`$ separate address registers and any workspace, applies $`O_A^{\otimes t}`$, and performs an $`A`$-independent readout. The output must equal $`A`$ with probability one for each promised set. Each oracle port counts as one call. An unused binary address encoding outside $`[N]`$ is unavailable to the oracle. No oracle-controlled bypass or response qubit is supplied.

Write $`t_{N,r}`$ for the fewest calls in this model.

## Main results

1. **Finite optimum.** For $`1\le r \lt N/2`$, the [moment program](moment-design.md#the-finite-moment-program) determines $`t_{N,r}`$ exactly and gives an explicit optimal probe. At most $`r+1`$ subset sizes suffice.
2. **Single mark.** For $`N\ge4`$, the optimum is $`\lceil(N-\sqrt{N})/2\rceil`$. At $`N=3`$ it is two.
3. **Fixed number of marks.** For every fixed positive $`r`$, [the two-sided asymptotic law](asymptotics.md) is

```math
t_{N,r}=\frac{N}{2}-\frac{\sqrt{a_r N}}{2}+O_r(1),
\qquad
L_{\lceil r/2\rceil}^{(-1/2)}(a_r/2)=0,
```

   where the smallest positive root is used. The proof also supplies an optimal-order sequence of discrete probes.

4. **Explicit readout.** The [Schur decoder](receiver.md) implements the measurement for every exact probe from the program, with polynomially many known gates and ideal rotations. The necessary query registers use $`t\lceil\log_2N\rceil`$ qubits. Gates outside the single oracle layer are accounted for separately.
5. **Other cardinalities.** The empty and full sets are known from their cardinality alone. At $`N=2r \gt 0`$, disjoint complementary inputs yield $`O_{A^{\mathrm c}}=-O_A`$ and therefore the same channel. For $`N/2 \lt r \lt N`$, recover the complementary set of size $`N-r`$ and complement the output.

## Flagged query-port erasure

The [erasure extension](flagged-erasure.md) keeps the same bare oracle and
removes an arbitrary queried port immediately after the simultaneous layer.
The receiver learns which port was lost and can access an explicitly charged
protected register. For five addresses and one mark, three calls are necessary
and sufficient, a protected qutrit suffices, and a protected qubit for classical
identification is open. Coherent recovery of the queried mark states requires
exactly a qutrit. The results above assume all queried ports reach the receiver.

## Comparisons within the model

For **product probes across query ports**, a necessary condition for recovery is to distinguish every pair $`C\cup\{i\},C\cup\{j\}`$, where $`i\ne j`$ and $`C`$ avoids both addresses. The pair induces exactly the single-mark relative diagonal unitary, regardless of $`C`$. The pair conditions used in [Wu and Duan's product-state lower bound](../references/RELATED_WORK.md#exact-parallel-search) therefore apply, giving an asymptotic lower bound of $`2N/3+o(N)`$ for product probes. One can also convert any product probe with local ancillas into a product of address-only pure probes with the same overlap factors, by keeping the address marginal probabilities as squared amplitudes. The full-set task inherits this lower bound. For fixed $`r`$ the entangled procedure uses asymptotically at most three quarters of the calls required by any such probe.

A classical bit-query protocol that reads one membership bit per address needs $`N-1`$ queries for exact recovery at any nontrivial weight. If two addresses remain unseen, one can assign a valid observed pattern with $`r-1`$ marks on the observed set and exchange the one remaining mark between the two unseen addresses. With $`N-1`$ queried bits the supplied count determines the last. This comparison grants the classical protocol an explicit bit response. The single-round restriction is on the oracle layer, so standard multi-round quantum search and repeated Grover-based enumeration use a different resource.

## Proof route

The oracle acts on an ordered query tuple depends only on the addresses occurring an odd number of times. Permutation symmetry then converts orthogonality into moment constraints on the number of odd addresses. The exact program solves those constraints on the available discrete grid. At fixed $`r`$, quadrature supplies both an obstruction and positive weights near the limiting endpoint. The decoder uses the same permutation symmetry to compress the known layer dependence into the spin magnetic register.

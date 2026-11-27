# Exact parallel search after one flagged erasure

[Repository](../README.md) · [Lossless model](model.md) · [Verification](../verification/README.md#flagged-erasure)

For five addresses, three simultaneous calls are necessary and sufficient when one arbitrary port is erased. A protected qutrit suffices, and exact identification requires protected quantum memory. Whether a protected qubit suffices for exact classical identification remains open. For the stronger task of coherently recovering superpositions of the five queried states, a qutrit is optimal. For six or more addresses, three calls fail for every protected memory dimension.

## Model

One unknown address $`m`$ is marked among $`N`$. The bare phase oracle is $`O_m|a\rangle=(-1)^{[a=m]}|a\rangle`$. Prepare $`q`$ address registers and a protected register of dimension $`d`$, all independent of $`m`$. Apply $`O_m`$ once on each address register in parallel. Trace out one address register immediately after the layer. The receiver knows the lost port position and can access the protected register and surviving query registers. It must identify $`m`$ with certainty for every marked address and lost port. There is no controlled bypass, no operation between the query layer and loss, and no additional stored quantum system. Each query counts even if its port is erased. Known preparation and receiver operations are separate costs.

An arbitrary pure probe has coefficients $`v_{\boldsymbol a}\in\mathbb C^d`$ at the address tuples $`\boldsymbol a`$. Pure probes suffice for feasibility because any mixed probe that works gives an exact receiver on each pure component in a preparation decomposition. For a fixed lost port $`i`$, expand its partial trace in the address basis. The mixed output for mark $`m`$ is a sum of outer products of subnormalized survivor vectors $`\psi_{m,a}^{(i)}`$ indexed by the hidden lost address $`a`$. The oracle phase on the erased port is a global sign on its summand, so omit it in $`\psi_{m,a}^{(i)}`$.

Exact decoding requires the supports for distinct marks to be orthogonal. Equivalently, $`\langle\psi_{m,a}^{(i)},\psi_{n,b}^{(i)}\rangle=0`$ for every $`m\ne n`$ and every $`a,b`$. The position flag supplies $`i`$. The address indices $`a,b`$ occur in the proof through the partial trace.

## The Gram identities at five addresses

For three ports, a survivor pair has either two equal addresses (parity $`0`$) or some unordered pair $`e`$ of distinct addresses. For a fixed lost position, let $`G_0`$ and $`G_e`$ be the Gram matrices on the hidden address labels. Sum contribution from the five equal survivor pairs in $`G_0`$, and the two orders of $`e`$ in $`G_e`$. Take matrix entries as inner products of the corresponding tag vectors. Their sum $`H=G_0+\sum_eG_e`$ has the rank of the lost port's reduced state.

For marked addresses $`m\ne n`$, the condition is
```math
G_0+\sum_e(-1)^{|e\cap\{m,n\}|}G_e=0.
```
At $`N=5`$ the coefficient matrix on the ten edges is $`J-2A`$, where $`A`$ is the adjacency matrix for edges of $`K_5`$ sharing one endpoint. Its eigenvalues are $`-2,-2,4`$, on the constant direction, the nonconstant vertex-incidence subspace, and its orthogonal complement. Thus the unique solution in terms of $`H`$ is
```math
G_0=H/6,\qquad G_e=H/12\quad\text{for every }e.
```
Each $`G_e`$ is a Gram matrix of vectors in an ordered-pair space of dimension $`2d`$. Consequently $`\mathrm{rank}H\le2d`$ for each possible lost port.

### The forced tuple weights

Write $`s_i(a)=H_i(a,a)`$ and $`S(a)=\sum_i s_i(a)`$. Let $`z(a)=\|v_{aaa}\|^2`$. For $`x\ne y`$ let $`p_i(x;y)`$ be the squared norm of the tuple with the singleton address $`x`$ at $`i`$ and $`y`$ at both other ports. For hidden address $`y`$ at port $`j`$, the diagonal entry of $`G_{\{x,y\}}`$ gives $`\sum_{i\ne j}p_i(x;y)=s_j(y)/12`$. Solving these three equations yields $`p_i(x;y)=(S(y)-2s_i(y))/24`$. The diagonal of $`G_0`$ then gives
```math
z(x)+\sum_{y\ne x}p_i(x;y)=s_i(x)/6,\qquad
2s_i(x)+S(x)=1+24z(x).
```
Sum over $`x`$ and use normalization and positivity. All $`z(x)`$ vanish. The last identity then implies $`s_i(x)=1/5`$ and $`p_i(x;y)=1/120`$. For an all-distinct tuple, its squared norm and that of the tuple obtained by swapping the two surviving slots sum to $`1/60`$. Thus the only remaining freedom in squared norms is an alternating term on each unordered triple.

### Why a protected quantum register is necessary

For any fixed lost port, restrict the survivor columns to equal pairs. Let $`M`$ have row index $`a`$ and columns $`(b,u)`$, with entries the $`u`$-th tag component of $`v_{a,b,b}`$ in that port order. Its rank $`R`$ is at most $`\mathrm{rank}H_i`$. With $`M_b`$ the $`b`$ block and $`P(a,b)=\|v_{a,b,b}\|^2`$, one has
```math
P(a,b)=(M_bM_b^\dagger)_{aa},\qquad P=(J-I)/120.
```
All the matrices $`M_bM_b^\dagger`$ are supported on the same $`R`$-dimensional column space. The real space of Hermitian matrices on that support has dimension $`R^2`$, so $`\mathrm{rank}P\le R^2`$. But $`P`$ has rank five, forcing $`\mathrm{rank}H_i\ge3`$. Together the bounds give $`d\ge2`$. A register dephased in a fixed basis before the receiver uses it is equivalent to a mixture of no-memory branches with an available classical label, and each branch would have to work. This also rules out such a classical record. If even one reduced query state is diagonal, its rank is five, and the upper rank bound instead gives $`d\ge3`$.

## A qutrit construction

Label the addresses $`0,1,2,3,4`$ and use a tag with basis $`A,B,C`$. Put zero amplitude on the five all-equal tuples. Each remaining tuple amplitude has norm $`1/\sqrt{120}`$. The normalized tag at a tuple is as follows.

- If address $`b`$ occurs twice and address $`a`$ once, use $`A,A,B,-B`$ for $`a-b\equiv1,2,3,4`$ modulo five, respectively.
- For an all-distinct ordered tuple $`t`$, use the following tag.

```math
\mathrm{sgn}(t)\left(\frac{|A\rangle}{\sqrt3}
    +\sqrt{\frac23}\,\omega^{f(t)}|C\rangle\right),\qquad
\omega=e^{2\pi i/3}.
```

The sign is its permutation parity relative to increasing address order. Set $`f(t)`$ to the zero-based position of the largest address plus $`\mathrm{sgn}(t)g(\mathrm{sort}t)`$, modulo three. The table below defines $`g`$.

| $`g`$ | Increasing address triples |
| --- | --- |
| 0 | 012, 023, 034, 124 |
| 1 | 013, 024, 123, 234 |
| 2 | 014, 134 |

For each distinct survivor pair, the two repeated-address rows occupy the symmetric orientation direction with distinct tags $`A`$ and $`B`$. The three all-distinct rows have an antisymmetric $`A`$ component, orthogonal to those repeated rows. Across the three possible all-distinct hidden addresses, $`f`$ in one fixed orientation takes each of $`0,1,2`$ once. The sum of the two orientation values of $`f`$ is constant modulo three. These two finite properties follow by checking the table on the 30 choices of lost port and survivor pair. Hence two different all-distinct rows in the concatenated two-order tag space have inner products proportional to $`2/3+(2/3)(\omega+\omega^{-1})=0`$. Every row has squared norm $`2/120`$. Therefore each $`G_e=I/60`$.

For equal survivors the diagonal entries are $`4/120`$. Distinct hidden addresses can share repeated-tuple tags for a fixed repeated address only when the hidden addresses are neighbors modulo five. Then there are two collisions, one in tag $`A`$ and one in tag $`B`$. Their signs cancel. Thus $`G_0=I/30`$, and the exact Gram identities hold.

For port flag $`i`$, the projector for mark $`m`$ is $`5\sum_a |\psi_{m,a}^{(i)}\rangle\langle\psi_{m,a}^{(i)}|`$. Each summand uses the known construction and a candidate mark. The supports are mutually orthogonal and the positive complementary projector completes the measurement. A known unitary extending the normalized vectors to an orthonormal basis implements this measurement in the finite survivor space. The [exact verifier](../verification/check_flagged_erasure.py) checks all 750 inter-mark branch overlaps in exact arithmetic.

## Coherent recovery costs exactly one qutrit

Let $`|\Psi_m\rangle=O_m^{\otimes3}|\Psi\rangle`$ be the full queried state for mark $`m`$. Exact classical identification asks for the label $`m`$ for each of these states. Coherent recovery asks for a decoder taking every superposition $`\sum_m c_m|\Psi_m\rangle`$ to the logical state $`\sum_m c_m|m\rangle`$ after loss. The decoder must preserve relative phases and entanglement with a reference.

Exact erasure correction on this span requires that the erased port alone have an input-independent reduced state. This is the complementary-channel form of the [Knill–Laflamme condition](https://doi.org/10.1103/PhysRevA.55.900). If $`\rho_i`$ is the pre-query marginal on the lost port, the marginal for each queried state is $`O_m\rho_i O_m`$. These matrices must coincide for every mark. For two distinct coordinates $`a,b`$, mark $`a`$ negates the $`(a,b)`$ matrix element and any mark outside $`\{a,b\}`$ leaves it fixed. Thus $`\rho_i`$ is diagonal. Its five diagonal entries are each $`1/5`$ by the Gram identities and forced tuple weights, so $`5=\mathrm{rank}\rho_i\le2d`$ and $`d\ge3`$.

For the qutrit construction, define $`|\phi_{m,a}^{(i)}\rangle=\sqrt{5}(-1)^{[a=m]}|\psi_{m,a}^{(i)}\rangle`$. At each fixed lost position these 25 vectors are orthonormal. A receiver isometry on their span sends them to $`|m\rangle|a\rangle`$. Extend it to a known unitary using spare output space. After applying the receiver isometry on its two surviving addresses and tag, the joint state becomes $`|m\rangle`$ tensored with the same entangled state of erased port and receiver's second output for every $`m`$. Linearity yields coherent decoding. This proves $`d=3`$ is attained for coherent recovery.

## Other address counts and promises

- **A finite probability feasibility test.** For one erased port, any number of phase queries and any fixed promise of marked sets, solve for a nonnegative probability on address tuples. For each erased position, each hidden address and each pair of distinct promised marked sets, impose a zero signed sum on the diagonal conditional survivor distribution. These linear equations are necessary by support orthogonality. They are sufficient with a protected register of dimension $`N`$: attach the sum of all tuple addresses modulo $`N`$ as a coherent orthogonal tag. At fixed survivors, distinct hidden addresses then have distinct tags, so all off-diagonal Gram conditions vanish term by term. The tag also makes every same-mark erased marginal diagonal and independent of the mark. Cross-mark erased reductions vanish by support orthogonality. Therefore these equations decide unrestricted feasibility for coherent recovery as well as identification. The small-dimension problem still involves the full Gram matrices.
- **Three calls at six addresses.** The eigenvalues of the edge sign matrix are $`-1,-4,4`$, so $`G_0=G_e=H/16`$. Average the diagonal probabilities over address and port permutations. With a fixed lost address, each incident pair forces the two-equal tuple weights to be $`1/192`$. The five such equal-survivor contributions already exceed the equal-survivor allowance of $`1/96`$. The implied total weight on all-equal tuples is $`-3/32`$, which is impossible.
- **Three calls at seven or more addresses.** Sum the diagonal conditions over all pairs of marked addresses. The coefficient of the equal-survivor sector is $`\binom N2`$. Every distinct-survivor sector has coefficient $`\binom N2-4(N-2)>0`$. A nonzero positive distribution cannot satisfy that sum.
- **Two marks at five addresses.** With two marks, pairs of promised sets realize symmetric differences of sizes two and four. The size-two conditions force the same Gram ratios. A size-four difference gives six positive and four negative edge signs, leaving the nonzero matrix $`G_0+2G_e=H/3`$. Thus three calls fail even with unrestricted protected memory.
- **Two calls at five addresses.** After one loss, one queried register survives. Its zero-overlap condition requires normalized address weights $`p_m+p_n=1/2`$ for every pair $`m\ne n`$. It follows that every weight is $`1/4`$, inconsistent with normalization on five addresses. A protected tag cannot alter this diagonal condition.

For the remaining singleton cases with three calls, one address is trivial and at two addresses the oracles differ by global phase. At three addresses, use three equal-amplitude two-address probes with a different omitted address on each port. Any pair of marks is distinguished by either of the two ports omitting one of those marks, so one useful port survives. At four addresses an equal-amplitude four-address probe distinguishes every singleton in one call, and any surviving port suffices. Hence five addresses form the only case at this query and loss budget in which exact identification is feasible and needs protected quantum memory.

## Connection to continuous-phase retrieval

The [phase-gate erasure companion](https://github.com/GoGoKo699/Quantum-Phase-Gate-Erasure/blob/main/science/flagged-search.md)
uses the same partial-trace expansion to analyze exact delayed application of
a continuous phase gate. The branchwise criterion changes with the output.
Here branches for different marks must have orthogonal supports. In delayed
gate retrieval the accepted branches all implement the same rank-one Choi
map for the supplied phase. Once a discrete mark is identified, the receiver
can synthesize its known reflection on later data. This use of classical
identification has a finite promise and supplies protected quantum memory
during the initial loss.

## The protected-qubit case

At five addresses, a protected qubit for classical identification would
require every lost-port marginal to have rank three or four and nonzero
off-diagonal entries in the address basis. The minimum dimension for
classical identification is either two or three.

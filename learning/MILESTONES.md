# 30 milestones for one-round marked-set recovery

The first **12 milestones** build the access model, exact discrimination criterion, and symmetry tools. The next **18 milestones** develop the lossless probe and decoder, then follow what changes after flagged loss. The [Watrous bridge](WATROUS_BRIDGE.md) maps the reading from John Watrous’s *The Theory of Quantum Information* (Cambridge University Press, 2018).

## Route through the project

| Milestones | Connection |
|---|---|
| [M01](#m01-the-unknown-marked-set)–[M05](#m05-exact-discrimination) | The access model, promise, and exact readout |
| [M06](#m06-address-tuples-and-parity)–[M12](#m12-the-complete-one-round-problem) | Parity, symmetry, and the complete operational question |
| [M13](#m13-reducing-a-general-probe)–[M18](#m18-finite-optimality-with-several-marks) | An exact finite characterization and its feasible probes |
| [M19](#m19-the-lower-edge-of-the-grid)–[M23](#m23-the-fixed-r-query-law) | Lower bound, parity grid, and the fixed-weight law |
| [M24](#m24-equivariance-of-a-layer-map)–[M26](#m26-lossless-readout-and-resources) | Schur sectors, exact decoding, and circuit cost |
| [M27](#m27-tracing-out-a-queried-port)–[M30](#m30-what-recovery-requires) | Lost branches, protected memory, and coherence |

## Phase I — Background and preliminaries

### M01 The unknown marked set

**Central question.** What is known before making a query?

**Understanding target.** Describe the unknown subset of N addresses, its supplied size r, and the task of outputting every member.

**Prerequisites.** None within this map.

**Conceptual connection.** The fixed-weight promise specifies a family of candidate oracles. It also lets the decoder use the known output weight.

**Canonical sources.** [Model and results](../science/model.md) · [Watrous §§2.1–2.3, 3.1](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

### M02 A bare phase query

**Central question.** How does a mark change a superposition?

**Understanding target.** Explain how a query adds a sign to the amplitude at a marked address and how interference reveals a relative sign.

**Prerequisites.** [M01](#m01-the-unknown-marked-set).

**Conceptual connection.** Unitary conjugation represents the bare oracle as a channel. An address phase affects interference between different addresses.

**Canonical sources.** [Model and results](../science/model.md) · [Watrous §§2.1–2.3, 3.1](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

### M03 Global phase and complements

**Central question.** When are different marked sets operationally identical?

**Understanding target.** Show why complementary marked sets induce the same channel and identify the balanced-weight obstruction.

**Prerequisites.** [M01](#m01-the-unknown-marked-set), [M02](#m02-a-bare-phase-query).

**Conceptual connection.** The project has exactly N valid addresses. A known phase reference would change the accessible operations and the complement argument.

**Canonical sources.** [Model and results](../science/model.md) · [Watrous §§2.1–2.3, 3.1](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

### M04 One layer and many calls

**Central question.** Which operations can occur between unknown calls?

**Understanding target.** Read the tensor power of the oracle as one simultaneous layer. Track t as the number of ports, and distinguish the known preparation and reception circuits.

**Prerequisites.** [M02](#m02-a-bare-phase-query), [M03](#m03-global-phase-and-complements).

**Conceptual connection.** Sequential Grover search uses known reflections between queries. Its query scale answers a different scheduling and output question.

**Canonical sources.** [Model and results](../science/model.md) · [Watrous §§2.1–2.3, 3.1](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

### M05 Exact discrimination

**Central question.** What does certainty require of the output states?

**Understanding target.** Use the Gram matrix to decide whether a family of pure states can be identified perfectly. Read diagonal ones as normalization and off-diagonal zeros as perfect distinguishability.

**Prerequisites.** [M01](#m01-the-unknown-marked-set), [M04](#m04-one-layer-and-many-calls).

**Conceptual connection.** The oracle analysis can target pairwise overlaps. A realization still needs a known receiver.

**Canonical sources.** [Model and results](../science/model.md) · [Schur receiver and resources](../science/receiver.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M06 Address tuples and parity

**Central question.** Which part of a t-port tuple determines its phase?

**Understanding target.** Track addresses with odd multiplicity and derive the available subset sizes from t and its parity.

**Prerequisites.** [M02](#m02-a-bare-phase-query), [M04](#m04-one-layer-and-many-calls).

**Conceptual connection.** Repeated queries contribute in pairs to the sign, while both uses still consume oracle ports.

**Canonical sources.** [Model and results](../science/model.md) · [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M07 Differences between candidates

**Central question.** Which addresses matter to the overlap of two outputs?

**Understanding target.** Get the overlap sign from the symmetric difference of the candidate sets. Explain why distinct sets of weight r produce difference sizes from 2 through 2r in even steps.

**Prerequisites.** [M01](#m01-the-unknown-marked-set), [M05](#m05-exact-discrimination), [M06](#m06-address-tuples-and-parity).

**Conceptual connection.** All common marks contribute two signs and cancel. The possible difference sizes determine how many constraints the design must enforce.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M08 Averaging address permutations

**Central question.** What can be simplified by relabeling addresses?

**Understanding target.** Explain how a permutation moves both candidate labels and probe subsets. Distinguish a uniform distribution inside a fixed-size layer from arbitrary weights across layers.

**Prerequisites.** [M05](#m05-exact-discrimination), [M07](#m07-differences-between-candidates).

**Conceptual connection.** Transitivity on subsets of each size produces one unknown weight per accessible size. The relabeling acts on query addresses and promised outputs together.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M09 Signed intersection counts

**Central question.** How often does a uniformly chosen subset contribute a negative sign?

**Understanding target.** Count intersections of a fixed difference set with a uniform k-subset. Connect the alternating hypergeometric count to the corresponding Krawtchouk polynomial.

**Prerequisites.** [M06](#m06-address-tuples-and-parity), [M07](#m07-differences-between-candidates), [M08](#m08-averaging-address-permutations).

**Conceptual connection.** A signed counting problem converts orthogonality into linear equations with known coefficients.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M10 Moments and positive weights

**Central question.** What does it mean to reproduce a distribution's low-order moments?

**Understanding target.** Interpret each moment as a weighted average of powers at the nodes. See why normalized nonnegative weights, support constraints and agreement through a fixed degree each have separate roles.

**Prerequisites.** [M08](#m08-averaging-address-permutations), [M09](#m09-signed-intersection-counts).

**Conceptual connection.** The project can match the binomial target on fewer nodes than that target distribution uses. The agreement controls only the specified polynomial tests.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M11 Spin and permutation labels

**Central question.** What changes when a qubit tensor product is expressed in a Schur basis?

**Understanding target.** Identify a spin sector, its magnetic coordinate, and a multiplicity coordinate. Explain how fixed Hamming weight fixes the magnetic coordinate within compatible spin sectors.

**Prerequisites.** [M01](#m01-the-unknown-marked-set), [M08](#m08-averaging-address-permutations).

**Conceptual connection.** Permutation symmetry separates the action on the address labels from a small coordinate that the decoder can rotate.

**Canonical sources.** [Schur receiver and resources](../science/receiver.md) · [Watrous §7.1 and the decoder](WATROUS_BRIDGE.md#symmetry-and-the-decoder)

### M12 The complete one-round problem

**Central question.** How do access, exactness and all resource counts fit together?

**Understanding target.** Describe the chain from a probe independent of the input to a fixed parallel layer and a known decoder that returns the complete marked set. Identify the promise, t-port cost and scope of the exact guarantee.

**Prerequisites.** [M03](#m03-global-phase-and-complements), [M04](#m04-one-layer-and-many-calls), [M05](#m05-exact-discrimination), [M06](#m06-address-tuples-and-parity), [M10](#m10-moments-and-positive-weights), [M11](#m11-spin-and-permutation-labels).

**Conceptual connection.** This chain connects probe feasibility to a separate realization of the receiver and separates both from physical implementation costs.

**Canonical sources.** [Model and results](../science/model.md) · [Finite moment design](../science/moment-design.md) · [Schur receiver and resources](../science/receiver.md) · [Watrous §§2.1–2.3, 3.1](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

## Phase II — Narrative and innovation

### M13 Reducing a general probe

**Central question.** How can arbitrary address and workspace superpositions enter the lower bound?

**Understanding target.** Expand a general pure probe in the address tuple basis after including any purification. Show how squared norm assigned to each parity subset determines the full output Gram matrix.

**Prerequisites.** [M05](#m05-exact-discrimination), [M06](#m06-address-tuples-and-parity), [M07](#m07-differences-between-candidates), [M12](#m12-the-complete-one-round-problem).

**Conceptual connection.** The converse permits arbitrary correlations across ports and ancillary quantum systems.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M14 A symmetric probe suffices

**Central question.** Why can feasibility be decided with only layer weights?

**Understanding target.** Average the parity distributions under all address permutations and prove that all required vanishing overlaps survive. Construct a coherent state from a valid averaged distribution.

**Prerequisites.** [M08](#m08-averaging-address-permutations), [M13](#m13-reducing-a-general-probe).

**Conceptual connection.** Averaging an exact feasible Gram condition leaves an exact design at the same port count. The realization prepares a single coherent probe.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Schur receiver and resources](../science/receiver.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M15 The exact moment program

**Central question.** Why does matching r moments enforce every needed zero?

**Understanding target.** Use symmetry under k and N−k to regard the even Krawtchouk constraints as a triangular basis in X. Check that the binomial moments produce all required signed cancellations.

**Prerequisites.** [M09](#m09-signed-intersection-counts), [M10](#m10-moments-and-positive-weights), [M14](#m14-a-symmetric-probe-suffices).

**Conceptual connection.** The problem becomes a finite linear program with rational coefficients on physical parity layers.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M16 From weights to a phase probe

**Central question.** How do nonnegative weights reach all t ports?

**Understanding target.** Prepare weighted Dicke layers, compute an address tuple from the incidence string, and pad it with repeat pairs. Undo the address computation after the diagonal query.

**Prerequisites.** [M06](#m06-address-tuples-and-parity), [M14](#m14-a-symmetric-probe-suffices), [M15](#m15-the-exact-moment-program).

**Conceptual connection.** Because the oracle modifies the phase and preserves the computed addresses, uncomputation puts the oracle's information in the incidence register.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Schur receiver and resources](../science/receiver.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M17 Optimal recovery of one mark

**Central question.** Why do at most two layers attain the single-mark bound?

**Understanding target.** Use the affine overlap in the squared distance from N/2 to prove the ceiling bound and locate a same-parity sign change. Explain the N=3 and N=4 cases.

**Prerequisites.** [M05](#m05-exact-discrimination), [M15](#m15-the-exact-moment-program), [M16](#m16-from-weights-to-a-phase-probe).

**Conceptual connection.** At N=6, the empty and size-two layers cancel with weights 1/16 and 15/16. The general construction exposes why the lower bound of Wu and Duan is attained.

**Canonical sources.** [Model and results](../science/model.md) · [Finite moment design](../science/moment-design.md) · [Worked circuit](WATROUS_BRIDGE.md#bare-queries-and-exact-discrimination)

### M18 Finite optimality with several marks

**Central question.** How does the method decide an exact minimum for a given N and r?

**Understanding target.** Search for the first feasible t using the rational constraints, and read a nonnegative solution as a certificate. Use a fixed-address extra port to explain monotonicity of feasibility.

**Prerequisites.** [M15](#m15-the-exact-moment-program), [M16](#m16-from-weights-to-a-phase-probe), [M17](#m17-optimal-recovery-of-one-mark).

**Conceptual connection.** Few-layer certificates can be checked with rational arithmetic. The exact finite criterion still applies when the fixed-r asymptotics are a poor estimate.

**Canonical sources.** [Finite moment design](../science/moment-design.md) · [Watrous §7.1](WATROUS_BRIDGE.md#parity-and-averaging)

### M19 The lower edge of the grid

**Central question.** Which part of the parity grid determines an asymptotic obstruction?

**Understanding target.** Find the lowest squared-distance node when t is at most N/2. Use nonnegativity of a polynomial of the form (X−L) times a square to bound the possible lower edge L.

**Prerequisites.** [M10](#m10-moments-and-positive-weights), [M15](#m15-the-exact-moment-program), [M18](#m18-finite-optimality-with-several-marks).

**Conceptual connection.** A feasible moment match reproduces the polynomial's expectation. The argument uses a sign on every available node, including those carrying zero weight.

**Canonical sources.** [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M20 A quadrature node gives the bound

**Central question.** Why does a smallest quadrature node appear?

**Understanding target.** Interpret the minimum Rayleigh quotient as the smallest eigenvalue of multiplication by X compressed to an appropriate polynomial space. Relate its size to the required port count.

**Prerequisites.** [M10](#m10-moments-and-positive-weights), [M19](#m19-the-lower-edge-of-the-grid).

**Conceptual connection.** The Gaussian quadrature rule uses the same moments as the compressed multiplication matrix. Its first node locates the lower bound.

**Canonical sources.** [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M21 Odd r and positive bracketing

**Central question.** How are continuous quadrature nodes replaced by accessible nodes?

**Understanding target.** Bracket separated Gaussian nodes on both sides using the parity grid. Explain how Lagrange cardinal polynomials assign exact moments and why each positive own-node contribution dominates its cross terms.

**Prerequisites.** [M15](#m15-the-exact-moment-program), [M19](#m19-the-lower-edge-of-the-grid), [M20](#m20-a-quadrature-node-gives-the-bound).

**Conceptual connection.** Bracketing absorbs the discreteness into bounded slack in t at fixed r. Simply moving each node to the closest layer would generally change the target moments.

**Canonical sources.** [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M22 Even r and a far endpoint

**Central question.** How can one more matched moment keep all weights nonnegative?

**Understanding target.** Use a fixed largest grid node and a tilted measure to obtain a Radau rule. Check its nearby bracket weights and explain why the far endpoint weight is positive.

**Prerequisites.** [M19](#m19-the-lower-edge-of-the-grid), [M20](#m20-a-quadrature-node-gives-the-bound), [M21](#m21-odd-r-and-positive-bracketing).

**Conceptual connection.** The extra degree of exactness comes from adding one node. Parity-conditioned binomial moments provide an unchanged finite target for the needed degrees.

**Canonical sources.** [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M23 The fixed-r query law

**Central question.** What sets the leading saving below N/2 calls?

**Understanding target.** Connect convergence of the standardized binomial even moments to a chi-square law, then connect its first Gaussian node to a Laguerre zero. Combine the lower bound with grid-feasible designs.

**Prerequisites.** [M18](#m18-finite-optimality-with-several-marks), [M20](#m20-a-quadrature-node-gives-the-bound), [M21](#m21-odd-r-and-positive-bracketing), [M22](#m22-even-r-and-a-far-endpoint).

**Conceptual connection.** The leading saving scales as the square root of N and depends on fixed r. The parity-grid construction controls the bounded remainder for that limit.

**Canonical sources.** [Fixed-weight asymptotics](../science/asymptotics.md) · [Parity and averaging](WATROUS_BRIDGE.md#parity-and-averaging)

### M24 Equivariance of a layer map

**Central question.** How does each signed incidence layer inherit permutation symmetry?

**Understanding target.** Regard the map from a marked incidence state to an encoded layer as an intertwiner. Explain why incompatible representation sectors cannot mix.

**Prerequisites.** [M11](#m11-spin-and-permutation-labels), [M14](#m14-a-symmetric-probe-suffices), [M16](#m16-from-weights-to-a-phase-probe).

**Conceptual connection.** Schur’s lemma makes each compatible sector respond through a known scalar while preserving its multiplicity information.

**Canonical sources.** [Schur receiver](../science/receiver.md) · [Watrous §7.1 and the decoder](WATROUS_BRIDGE.md#symmetry-and-the-decoder)

### M25 Sector responses and normalization

**Central question.** What does the receiver compute before it ever sees the mark?

**Understanding target.** Explain how singlet pairs and a signed sum on the remaining symmetric bits give a layer scalar. Use the identity output Gram matrix to show that each resulting magnetic vector has norm one.

**Prerequisites.** [M09](#m09-signed-intersection-counts), [M15](#m15-the-exact-moment-program), [M24](#m24-equivariance-of-a-layer-map).

**Conceptual connection.** The finite moment program certifies an isometry. The known magnetic vector in each sector is the part of the isometry the decoder rotates.

**Canonical sources.** [Schur receiver](../science/receiver.md) · [Watrous §7.1 and the decoder](WATROUS_BRIDGE.md#symmetry-and-the-decoder)

### M26 Lossless readout and resources

**Central question.** How does the decoder extract every marked address?

**Understanding target.** Transform to Schur coordinates, rotate the magnetic state conditional on spin, and invert the transform. Track how the receiver uses the preserved multiplicity register. Account separately for oracle calls, address routing, workspace and exact known rotations.

**Prerequisites.** [M04](#m04-one-layer-and-many-calls), [M16](#m16-from-weights-to-a-phase-probe), [M23](#m23-the-fixed-r-query-law), [M25](#m25-sector-responses-and-normalization).

**Conceptual connection.** The lossless result combines probe optimality with a constructive readout. The gate precision guarantee describes compilation of the known circuit.

**Canonical sources.** [Schur receiver and resources](../science/receiver.md) · [Verification](../verification/README.md) · [Watrous §7.1 and the decoder](WATROUS_BRIDGE.md#symmetry-and-the-decoder)

### M27 Tracing out a queried port

**Central question.** What information does the flag provide, and what remains hidden?

**Understanding target.** Expand the erased register in the address basis and trace it out. Identify which sign is global inside each summand. Explain why exact readout must separate the supports of candidate mixed states.

**Prerequisites.** [M04](#m04-one-layer-and-many-calls), [M05](#m05-exact-discrimination), [M13](#m13-reducing-a-general-probe).

**Conceptual connection.** Every lost-address branch contributes positively to a candidate state. Orthogonality of supports requires all cross-mark branch overlaps to vanish.

**Canonical sources.** [Erasure model](../science/flagged-erasure.md#model) · [Watrous §§2.1, 3.1](WATROUS_BRIDGE.md#from-a-lost-port-to-branch-supports)

### M28 Matrix-valued parity constraints

**Central question.** How does the scalar parity moment method change after loss?

**Understanding target.** Group survivor tuples by parity and retain the hidden address indices in a Gram matrix. Derive the common matrix ratios for five addresses and the bound on each lost-port rank. Follow the forced repeated-tuple weights to the no-quantum-memory obstruction.

**Prerequisites.** [M07](#m07-differences-between-candidates), [M15](#m15-the-exact-moment-program), [M27](#m27-tracing-out-a-queried-port).

**Conceptual connection.** A protected tag of dimension d supplies two copies of its space for each distinct pair of survivor addresses. The Gram matrix carries branch coherences in addition to its diagonal probabilities.

**Canonical sources.** [Gram identities and converse](../science/flagged-erasure.md#the-gram-identities-at-five-addresses) · [Watrous §§2.1, 3.1](WATROUS_BRIDGE.md#from-a-lost-port-to-branch-supports)

### M29 Constructing the protected qutrit probe

**Central question.** How does a three-level tag separate the hidden-address rows?

**Understanding target.** Trace the symmetric repeated-address rows, the antisymmetric component on distinct triples, and the cube-root phase choices. Verify why equal surviving addresses require signed cancellation and why the tag gives exact mark supports.

**Prerequisites.** [M26](#m26-lossless-readout-and-resources), [M27](#m27-tracing-out-a-queried-port), [M28](#m28-matrix-valued-parity-constraints).

**Conceptual connection.** The table of known tag phases is a finite constructive certificate. Its orthogonal supports give a fixed receiver for each loss flag.

**Canonical sources.** [Qutrit construction](../science/flagged-erasure.md#a-qutrit-construction) · [Exact checks](../verification/README.md#flagged-erasure) · [Watrous §§2.3, 3.1](WATROUS_BRIDGE.md#the-qutrit-and-coherent-recovery)

### M30 What recovery requires

**Central question.** When do label recovery and coherent recovery have different memory costs?

**Understanding target.** Reconstruct the lossless result from the oracle model to the Schur readout, then state the exact five-address flagged-loss guarantees. Explain why coherent decoding requires the erased port to be independent of the logical input and why this forces three protected levels. Identify the open qubit case for classical identification.

**Prerequisites.** [M12](#m12-the-complete-one-round-problem), [M23](#m23-the-fixed-r-query-law), [M26](#m26-lossless-readout-and-resources), [M28](#m28-matrix-valued-parity-constraints), [M29](#m29-constructing-the-protected-qutrit-probe).

**Conceptual connection.** The lossless layer and the lossy receiver use the same ordinary phase oracle. Their exactness conditions are applied to different accessible subsystems. Delayed continuous-phase retrieval uses the same partial trace with a channel-valued success criterion.

**Canonical sources.** [Lossless model](../science/model.md) · [Coherent recovery](../science/flagged-erasure.md#coherent-recovery-costs-exactly-one-qutrit) · [Watrous §§2.2, 3.1](WATROUS_BRIDGE.md#the-qutrit-and-coherent-recovery)

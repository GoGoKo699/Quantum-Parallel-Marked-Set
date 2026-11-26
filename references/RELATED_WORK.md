# Related work

[Repository](../README.md) · [Model and results](../science/model.md) · [Bibliography](references.bib)

## Exact parallel search

[Xiaodi Wu and Runyao Duan, *Exact quantum search by parallel unitary discrimination schemes*](https://doi.org/10.1103/PhysRevA.78.012303), Physical Review A 78, 012303 (2008), use ordinary phase oracles in one parallel layer. Their Theorem 2 gives the entangled lower bound for one mark; their discussion asks whether it is tight and exhibits small cases. Their product-input bounds are asymptotically tight. The [two-layer probe](../science/moment-design.md#one-mark-formula) attains the entangled bound with integer rounding for every size from four onward. The same product-input converse applies to the complete marked-set task because it contains single exchanges between pairs of promised sets. [Preprint, Theorems 1 and 2 and the discussion following Theorem 2](https://arxiv.org/pdf/0709.3627)

## Exact nonadaptive queries and interrogation

[Ashley Montanaro, Richard Jozsa and Graeme Mitchison, *On exact quantum query complexity*](https://doi.org/10.1007/s00453-013-9826-8), Algorithmica 71, 775–796 (2015), formulate weighted parity constraints for exact nonadaptive querying and study symmetric Boolean outputs. Their query model includes a null address. The present full-output promise instead gives all even pairwise difference distances through twice the prescribed weight, with parity fixed by the number of bare phase calls. Solving those constraints gives the positive moment design and its threshold. [Preprint](https://arxiv.org/abs/1111.0475)

[Wim van Dam, *Quantum oracle interrogation*](https://arxiv.org/abs/quant-ph/9805006), FOCS 1998, develops coherent subset phase encoding to recover arbitrary strings at bounded error. [Stacey Jeffery, Frédéric Magniez and Ronald de Wolf](https://arxiv.org/abs/1309.6116) analyze parallel quantum queries, including parallel interrogation and the tradeoff between width and query rounds. Here the weight promise and exact recovery require a different layer distribution and receiver.

[The group and coset discrimination results of Copeland and Pommersheim](https://doi.org/10.22331/q-2021-03-07-403) illustrate why representation theory is effective for symmetric oracle families. The fixed-weight sets used here form an orbit under address permutations. The oracle family itself is generally neither a group nor a group coset under composition. Permutation covariance here reduces each layer to scalar actions within the weight subspaces.

## Decoder and multi-round comparison

[Dave Bacon, Isaac Chuang and Aram Harrow](https://arxiv.org/abs/quant-ph/0407082) supply the efficient quantum Schur transform used for known gates. The [receiver](../science/receiver.md) calculates the signed action of each subset layer and uses it to select the magnetic rotation. Gaussian quadrature and generalized Laguerre polynomials use the standard conventions in the [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/3.5).

[Joran van Apeldoorn, Sander Gribling and Harold Nieuwboer, *Basic quantum subroutines: finding multiple marked elements and summing numbers*](https://doi.org/10.22331/q-2024-03-14-1284), Quantum 8, 1284 (2024), give nearly gate-optimal recovery of all marked addresses when the oracle can be queried through many rounds. Their query scaling is proportional to the square root of the product of the address count and mark count. The result here minimizes total calls within the one-round restriction.

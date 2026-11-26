# Fixed-mark asymptotics

[Model](model.md) · [Finite moment program](moment-design.md) · [Decoder](receiver.md)

For fixed $`r\ge1`$, set $`m=\lceil r/2\rceil`$. Let $`a_r`$ be twice the smallest zero of $`L_m^{(-1/2)}`$. In this regime

```math
t_{N,r}=\frac{N}{2}-\frac{\sqrt{a_rN}}{2}+O_r(1).
```

The lower bound uses a polynomial that is nonnegative on the allowed probe grid. The upper bound replaces each node of a quadrature by a pair of allowed grid points, solving the moment equations with positive weights.

## The limiting measure

The moment target $`\mu_N`$ is the law of $`N^{-1}(\sum_{\ell=1}^{N}\xi_\ell)^2`$ with independent symmetric signs $`\xi_\ell`$. For each fixed $`j`$, the $`j`$th moment equals the Gaussian-square moment plus $`O_j(N^{-1})`$. In the expansion of the $`2j`$th power, the leading terms contain exactly $`j`$ distinct indices, each twice. Their normalized count tends to $`(2j-1)!!`$ with error $`O_j(N^{-1})`$. Every other nonzero term has at most $`j-1`$ distinct indices. The limit is the chi-square distribution with one degree of freedom, whose density is proportional to $`x^{-1/2}e^{-x/2}`$. Under $`x=2z`$ its degree-$`m`$ orthogonal polynomial is a nonzero multiple of $`L_m^{(-1/2)}(z)`$.

Matrices of fixed-size moment inner products converge at rate $`O_r(N^{-1})`$. The limit is positive definite because the limiting measure has a positive density on every open subinterval of $`(0,\infty)`$. Consequently the coefficients and simple roots of the monic degree-$`m`$ orthogonal polynomials converge at that rate. The Gaussian quadrature weights, determined by the first $`m`$ moment equations on the $`m`$ distinct nodes, converge to positive weights.

## Converse

The case $`t \gt N/2`$ already obeys the lower bound. Otherwise every available grid point is at least $`L=(N-2t)^2/N`$. If exact recovery is possible, the moment equations imply

```math
\int (x-L)q(x)^2\,d\mu_N(x)\ge0
\qquad \text{for every real } q \text{ with } \deg q\le m-1.
```

This uses degree at most $`2m-1\le r`$. The smallest possible ratio $`\int xq^2\,d\mu_N/\int q^2\,d\mu_N`$ is the smallest $`m`$-node Gaussian quadrature node. Indeed, the quadrature is exact for both integrals, so this ratio is a weighted average of its nodes. The degree-$`m-1`$ Lagrange cardinal polynomial at the smallest node attains that node. Thus $`L\le a_r+O_r(N^{-1})`$, which yields the lower bound on $`t`$ up to a bounded term.

## Matching discrete probes for odd r

When $`r=2m-1`$ use the $`m`$-point Gaussian quadrature for $`\mu_N`$. Write its nodes and weights as $`g_i,\beta_i`$. The grid indexed by $`k=t,t-2,\ldots`$ has spacing $`\Theta_r(N^{-1/2})`$ near each node. To see this, the positive square root of $`x_k`$ advances by $`4/\sqrt N`$ at each grid step, and all the limiting nodes are strictly positive and finite. Choose $`t`$ within an $`O_r(1)`$ additive allowance above the lower bound. Increasing $`t`$ by a bounded number moves the bottom node far enough below $`g_1`$ to take grid points on both sides. Other nodes have a positive limiting separation from the bottom and from each other, so the same bracketing is possible there.

Let $`\ell_i \lt g_i \lt u_i`$ be selected grid pairs, with both gaps comparable to $`h=N^{-1/2}`$. Skip an excessively near grid point if needed. For each of the $`2m`$ selected nodes set its weight to the integral of its Lagrange cardinal polynomial. This reproduces all moments through degree $`2m-1`$. The sign follows by applying the original Gaussian formula to each cardinal polynomial. At its bracket's own Gaussian node the value is

```math
\frac{u_i-g_i}{u_i-\ell_i}\bigl(1+O_r(h)\bigr)
\quad\text{or}\quad
\frac{g_i-\ell_i}{u_i-\ell_i}\bigl(1+O_r(h)\bigr).
```

Each positive fraction is bounded away from zero. At all other Gaussian nodes, the numerator contains two factors of order $`h`$ and the denominator contains one, and all remaining factors are bounded. The cross contributions are therefore $`O_r(h)`$. The original Gaussian weights have positive limits, so every selected weight is positive for sufficiently large $`N`$.

## Matching discrete probes for even r

When $`r=2m`$, choose even $`t`$. Rounding to even adds at most one call to the construction and makes the endpoint $`R=N`$ available at layer zero. Tilt the target measure by

```math
d\nu_N(x)=(1-x/R)\,d\mu_N(x).
```

It is nonnegative on the entire support of $`\mu_N`$. Its fixed moments have the same limits and convergence rates. Let $`g_i,\gamma_i`$ be its Gaussian nodes and weights. For any $`p`$ of degree at most $`2m`$, write $`p(x)=p(R)+(x-R)q(x)`$ and apply Gaussian quadrature to $`q`$. This gives a Gauss–Radau rule for $`\mu_N`$ with $`m`$ lower nodes $`g_i`$, lower weights $`\beta_i=\gamma_i/(1-g_i/R) \gt 0`$ and the fixed endpoint $`R`$. The lower weights tend to the positive chi-square quadrature weights.

Use the even grid to bracket all the lower nodes as before and keep $`R`$ fixed. Integrate the new cardinal polynomials, now of degree $`2m`$. The preceding positivity argument applies at the lower nodes with an extra factor $`(g_j-R)/(x_i-R)=1+O_r(N^{-1})`$. Here $`x_i`$ is the selected lower grid point for the cardinal polynomial. The fixed endpoint contributes zero to all lower weights. The new weight at the endpoint has numerator and denominator

```math
w_R=
\frac{\int \prod_{i=1}^{m}(x-\ell_i)(x-u_i)\,d\mu_N(x)}
     {\prod_{i=1}^{m}(R-\ell_i)(R-u_i)}.
```

The denominator is positive. The numerator converges to the expectation of the squared monic degree-$`m`$ limiting orthogonal polynomial under the limiting measure, which is strictly positive. Thus every fitted weight is eventually positive, the first $`2m`$ moments match exactly and the probe is realizable. Choosing even $`t`$ leaves the asymptotic remainder unchanged. The [finite program](moment-design.md#the-finite-moment-program) covers all parities and sizes independently of the sufficiently-large-$`N`$ proof.

## Coefficients

| Number of marks | Limiting smallest node |
|---|---|
| One or two | 1 |
| Three or four | $`3-\sqrt{6}`$ |

The threshold coefficient applies for fixed $`r`$ as $`N`$ increases. The constants used to separate, bracket and control the nodes may depend on $`r`$.

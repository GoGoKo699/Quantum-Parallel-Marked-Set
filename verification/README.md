# Verification

[Repository](../README.md) · [Moment design](../science/moment-design.md) · [Decoder](../science/receiver.md)

From the repository root, run with Python 3.10 or later.

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_parallel_marked_sets.py
```

The script enumerates rational basic supports for 100 finite marked-set instances. It checks the first feasible call budget, exact Krawtchouk cancellations, the one-mark formula, and normalization of every represented Schur sector. It also reproduces the 30-address example.

An independent calculation assembles the layer matrices directly from signed intersections and checks 86 Gram spectra against their predicted eigenvalues. A separate exact enumeration checks the signs of 176 Schur matrix elements. The finite examples support the reduction and the decoder. The [asymptotic proof](../science/asymptotics.md) establishes the fixed-mark threshold.

The exhaustive rational support enumeration is a small-instance verification method. Use the rational linear program in [the proof](../science/moment-design.md#the-finite-moment-program) to compute designs at larger parameters.

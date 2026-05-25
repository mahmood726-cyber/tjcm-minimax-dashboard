# TJCM 12.0: Topological Jensen-Compensated Meta-Variance

Epistemic-minimax & graph-agnostic bound framework for meta-analyses with heavy imputation. Demonstrates a constructive lower bound of evidence (CLBE) that resists synthetic-consensus formation when imputed covariates dominate.

**Live dashboard:** <https://mahmood726-cyber.github.io/tjcm-minimax-dashboard/>

## What it does

Can we mathematically prevent the creation of synthetic consensus when global health institutions rely on heavily imputed data algorithms? The framework analyses the epistemic topology of 50 clinical trials with simulated imputed covariates, and combines:

- **Graph-Agnostic Adversarial Bounds** — worst-case envelope over plausible imputation graphs.
- **Constructive Lower Bound of Evidence (CLBE)** — a guaranteed-floor pooled estimate that is invariant to imputation choices.
- **Lyapunov-adjusted Martingale Deficits** — robustness check against chaotic biological mutations.
- **Financial Jaccard Index** — robustness check against financial manipulation in funding networks.

In the demo, a naive meta-analytic consensus of 6.2 million cases reduces to an epistemically guaranteed CLBE of 540,000 cases.

## Run

Open `index.html` in any modern browser. No build step.

For local development:

```bash
python -m http.server 8000
# then open http://localhost:8000/
```

## Test

```bash
python -m pytest -q
```

Tests live under `tests/`.

## Limitation

The framework is bounded strictly by the accuracy of the foundational adversarial prior mapping of the data-generation process. Garbage priors in, garbage CLBE out — the floor is constructive, not magic.

## License

See `LICENSE` (MIT).

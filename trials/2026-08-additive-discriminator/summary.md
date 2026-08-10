# Additive-Doctrine Discriminator Trial — Results

## Arm means

| Arm | Echo mean | Pairwise overlap mean |
|---|---|---|
| current | 0.1698 | 0.6427 |
| additive | 0.1647 | 0.6428 |
| stopslop | 0.1812 | 0.6078 |

## Cross-arm deltas (vs current)

| Comparison | Echo delta | Divergence delta |
|---|---|---|
| additive | -0.0051 | +0.0001 |
| stopslop | +0.0114 | -0.0349 |

## Consistency (additive vs current)

- Echo: additive lower in 3/4 character×model combinations
- Pairwise overlap: additive lower in 2/4 character×model combinations

## Per-model breakdown

### sonnet-5

| Arm | Echo mean | Pairwise overlap mean |
|---|---|---|
| current | 0.1593 | 0.6592 |
| additive | 0.1630 | 0.6533 |
| stopslop | 0.1702 | 0.5940 |

### opus-4-6

| Arm | Echo mean | Pairwise overlap mean |
|---|---|---|
| current | 0.1804 | 0.6262 |
| additive | 0.1665 | 0.6323 |
| stopslop | 0.1923 | 0.6215 |

## Per-character breakdown

### nadja

| Arm | Echo mean | Pairwise overlap mean |
|---|---|---|
| current | 0.1748 | 0.6381 |
| additive | 0.1615 | 0.6205 |
| stopslop | 0.1808 | 0.5894 |

### kallya

| Arm | Echo mean | Pairwise overlap mean |
|---|---|---|
| current | 0.1649 | 0.6473 |
| additive | 0.1679 | 0.6651 |
| stopslop | 0.1817 | 0.6261 |

## Per-cell detail

| Cell | Echo mean | Echo rate | Pairwise overlap mean |
|---|---|---|---|
| kallya/additive/opus-4-6 | 0.1724 | 0.0000 | 0.6493 |
| kallya/additive/sonnet-5 | 0.1635 | 0.0000 | 0.6808 |
| kallya/current/opus-4-6 | 0.1784 | 0.0000 | 0.6329 |
| kallya/current/sonnet-5 | 0.1515 | 0.0000 | 0.6617 |
| kallya/stopslop/opus-4-6 | 0.1958 | 0.0000 | 0.6452 |
| kallya/stopslop/sonnet-5 | 0.1676 | 0.0000 | 0.6070 |
| nadja/additive/opus-4-6 | 0.1605 | 0.0000 | 0.6153 |
| nadja/additive/sonnet-5 | 0.1625 | 0.0000 | 0.6257 |
| nadja/current/opus-4-6 | 0.1824 | 0.0000 | 0.6195 |
| nadja/current/sonnet-5 | 0.1672 | 0.0000 | 0.6567 |
| nadja/stopslop/opus-4-6 | 0.1888 | 0.0000 | 0.5978 |
| nadja/stopslop/sonnet-5 | 0.1728 | 0.0000 | 0.5810 |

# Bootstrap seed rerun

## Overview

The project-cluster bootstrap was repeated for 10,000 iterations with seed `123456`. All 10,000 micro-metric replicates were defined.

## Critical issues

None.

## Important issues addressed

1. The script default and manuscript method now use seed `123456`.
2. The article reports the reproduced percentile ranges: precision `0.798`--`0.931`, recall `0.820`--`0.913`, and F1 `0.820`--`0.912`.
3. The supplementary command states `--bootstrap 10000 --seed 123456` explicitly.

## Verification

- `python3 analysis/localisation_robustness.py /home/kristoi/masters-thesis`
- `make paper`
- The IoU sensitivity procedure was outside the requested rerun and its values remain unchanged.

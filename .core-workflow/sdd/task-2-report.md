## Task 2 Report: Generation phase (Claude API)

**Status: DONE**

### Changes

- `trials/2026-08-additive-discriminator/run_trial.py`:
  - Added `anthropic` import (guarded with try/except).
  - Added `SYSTEM_PROMPT` constant.
  - Added `generate_one()` — single API call, returns text.
  - Added `generate_all()` — iterates matrix x runs, writes files, returns dict.
  - Updated `__main__` block to call `generate_all()` when not `--detect-only`.

- `trials/2026-08-additive-discriminator/test_runner.py`:
  - Added `test_generate_one_calls_api` — verifies API call kwargs and return.
  - Added `test_generate_all_creates_files` — verifies 36 files created via mock.

### Checks

All 9 tests pass (7 Task 1 + 2 Task 2).

### Interfaces produced for Task 3

- `generate_one(client, model, prompt, max_tokens, temperature) -> str`
- `generate_all(matrix, runs, out_dir, dry_run) -> dict[str, str]`

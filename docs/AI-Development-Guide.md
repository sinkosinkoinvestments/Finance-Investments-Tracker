# AI Development Guide

## Purpose

This guide tells Codex and other AI coding agents how to work in this repository.

## Product intent

Finance Investments Tracker is a family wealth planning and forecasting platform.

It should prioritise:

- Clear financial modelling
- Scenario comparison
- Reproducible forecasts
- Data-driven configuration
- Static deployment where possible
- Explainable assumptions

## Working principles

- Keep changes small and reviewable.
- Prefer feature branches and pull requests for non-trivial work.
- Do not hard-code personal financial values in UI components.
- Store assumptions and scenario data in YAML or snapshot files.
- Keep calculation logic separate from rendering logic.
- Keep forecasts deterministic and reproducible.
- Do not expose API keys or secrets in frontend code.

## Preferred architecture

```text
YAML scenario files
  -> parser and validation layer
  -> calculation engine
  -> generated forecast output
  -> dashboard UI
```

## Coding rules

- Calculation functions should be pure where practical.
- Avoid coupling financial logic to components.
- Use clear names for financial concepts.
- Keep assumptions visible.
- Prefer simple deterministic modelling before adding advanced simulations.
- Add tests for the calculation engine before expanding UI complexity.

## API integration rules

- API data must be optional.
- API data should be cached or snapshotted before being used in forecasts.
- Scenario YAML remains the source of truth.
- Do not place API keys in browser-side code.
- If an API requires a secret, use a backend, serverless worker, GitHub Actions, or manual import.

## Review checklist

Before marking work complete, check:

- Does the change preserve scenario reproducibility?
- Are assumptions documented?
- Are source values stored outside the UI?
- Are calculations testable?
- Are secrets avoided?
- Does the dashboard remain mobile-friendly?
- Are docs updated if the architecture changes?

## Things to avoid

- Do not turn the app into financial advice software.
- Do not add fragile live-only API dependencies.
- Do not make forecasts depend on data that cannot be reproduced later.
- Do not mix personal financial data into reusable components.
- Do not introduce a backend until the static model is proven insufficient.

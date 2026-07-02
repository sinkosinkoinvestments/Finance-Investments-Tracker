# Architecture

## Architecture goal

Finance Investments Tracker should be a data-driven forecasting dashboard where assumptions and scenarios are stored in source files, calculations are deterministic, and output pages can be deployed as a static website.

## Recommended approach

Use a simple frontend-first architecture:

```text
YAML source files
    ↓
Data loading / parsing layer
    ↓
Calculation engine
    ↓
Scenario comparison model
    ↓
Dashboard UI
```

## Suggested repository structure

```text
/
├── README.md
├── AGENTS.md
├── docs/
│   ├── 01-Requirements.md
│   ├── 02-Architecture.md
│   ├── 03-Roadmap.md
│   ├── 04-Sprints.md
│   ├── 05-Decisions.md
│   ├── 06-Data-Model.md
│   ├── 07-Integrations.md
│   ├── 08-Testing.md
│   └── 09-Deployment.md
├── scenarios/
│   ├── base.yml
│   ├── cooroy-1-8m.yml
│   ├── high-etf-contributions.yml
│   └── conservative-debt-reduction.yml
├── src/
│   ├── data/
│   ├── calculations/
│   ├── scenarios/
│   ├── components/
│   └── pages/
└── public/
```

If the current repo already uses a different structure, adapt this gradually rather than forcing a disruptive rewrite.

## Core modules

### 1. Source data module

Responsibilities:

- Load YAML scenario files.
- Validate required fields.
- Normalize contribution frequencies.
- Normalize dates and target years.
- Convert scenario inputs into a consistent internal model.

### 2. Calculation engine

Responsibilities:

- Project asset balances over time.
- Project debt balances over time.
- Apply contributions by frequency.
- Estimate income streams.
- Apply growth rates and interest rates.
- Produce yearly projection rows.

The calculation engine should be framework-independent so it can be tested separately from the UI.

### 3. Scenario engine

Responsibilities:

- Run one or more scenarios.
- Compare outputs across scenarios.
- Surface key differences:
  - Net worth
  - Investable assets
  - Annual income at target date
  - Debt at target date
  - Cash buffer

### 4. Dashboard UI

Responsibilities:

- Display current position.
- Display projected balances.
- Compare scenarios.
- Show assumptions.
- Show warnings and caveats.

## Data flow

```text
scenario.yml
  → parseScenario()
  → validateScenario()
  → runForecast()
  → buildDashboardModel()
  → render pages/charts/tables
```

## Calculation principles

- Keep assumptions visible.
- Avoid hidden constants.
- Avoid hard-coding personal financial figures in components.
- Keep scenario source files as the source of truth.
- Prefer simple deterministic calculations before adding complex modelling.

## Security and privacy

- Do not commit API keys, banking credentials, or private account logins.
- Avoid storing personally identifying details unless required.
- Treat YAML inputs as sensitive financial planning data.
- If hosted publicly, avoid including real private values unless protected by Cloudflare Access or another authentication layer.

## Deployment direction

Preferred deployment path:

```text
GitHub repository
    ↓
Cloudflare Pages
    ↓
Cloudflare Access if private
```

GitHub Pages remains acceptable for public or non-sensitive versions.

## Future architecture options

Later versions may add:

- Server-side API layer.
- Authenticated private data storage.
- Automatic price feeds.
- Open Banking feeds.
- Exportable PDF reports.
- Snapshot history.

These should be deferred until the static dashboard and scenario engine are reliable.

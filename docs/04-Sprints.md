# Sprints

## Sprint 1: Foundation and documentation

Status: In progress

Goal: Define the product before implementation.

Deliverables:

- Requirements document
- Architecture document
- Data model document
- Roadmap
- Integration strategy
- AI development guide
- Initial scenario specification

Acceptance criteria:

- The project purpose is clear.
- Core data inputs are documented.
- Scenario-driven forecasting is documented.
- API integration strategy is documented.
- Codex has enough context to begin implementation.

## Sprint 2: Scenario schema and sample data

Goal: Create the first working YAML scenarios.

Deliverables:

- `/scenarios/base.yml`
- `/scenarios/cooroy-1-8m.yml`
- YAML validation rules
- Sample snapshot files
- README section explaining how scenarios work

Acceptance criteria:

- A human can edit a scenario without touching code.
- Scenario values are clearly named.
- Contributions, assets, liabilities, income, and goals are represented.

## Sprint 3: Forecast engine MVP

Goal: Convert scenario YAML into deterministic forecast outputs.

Deliverables:

- Scenario parser
- Frequency normaliser
- Asset projection logic
- Debt projection logic
- Contribution handling
- Yearly forecast rows
- Basic tests

Acceptance criteria:

- Forecast engine can run at least one scenario.
- Output includes year, asset values, debt values, net worth, income, expenses, and goal progress.
- Calculations are separate from UI components.

## Sprint 4: Dashboard MVP

Goal: Display the forecast in a static web dashboard.

Deliverables:

- Overview page
- Assets page
- Debt page
- Cashflow page
- Forecast page
- Assumptions page

Acceptance criteria:

- Dashboard can be deployed as a static site.
- Dashboard reads generated scenario output.
- Mobile layout is usable.

## Sprint 5: Scenario comparison

Goal: Compare multiple scenarios side by side.

Deliverables:

- Scenario selector
- Comparison table
- Net worth comparison chart
- Target income comparison chart
- Risk/assumption comparison

Acceptance criteria:

- At least two scenarios can be compared.
- Differences are easy to understand.

## Sprint 6: API and snapshot integrations

Goal: Add optional external data enrichment.

Deliverables:

- Market price snapshot format
- Interest rate snapshot format
- Data adapter pattern
- Manual import flow
- Optional scheduled refresh design

Acceptance criteria:

- API data does not break scenario reproducibility.
- Manual values remain supported.
- No secrets are exposed in frontend code.

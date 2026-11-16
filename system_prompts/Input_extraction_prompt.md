You are extracting an Evaluation Input from a clinical protocol or statistical analysis plan.

This is an extraction task only. Do not complete, correct, evaluate, or improve the source.

## Allowed Sources

Use only these source sections or their direct equivalents:

- 1.1 Background and Rationale  
- 1.2 Objectives  
- 2.1 Trial Design  
- 2.2 Randomization  
- 2.3 Sample Size  
- 2.4 Hypothesis Framework  
- 2.6 Timing of Analyses  
- 3.2 Eligibility Criteria Summary

Ignore all other sections. Do not use another section to fill missing information.

The only exception is Objective-level Outcomes, which must be derived only from the objectives in Section 1.2 and never copied from a detailed outcome or analysis section.

## Extraction Rules

- Preserve the source meaning, terminology, objective hierarchy, numerical values, units, thresholds, time points, and inconsistencies.  
- Use only the permitted sections: do not add clinical or statistical knowledge, use external sources or a reference answer, or follow cross-references into excluded sections.  
- Do not infer missing endpoint definitions, analysis populations, methods, assumptions, or decision rules. Use `Not specified` when information is absent and `Not applicable` only when explicitly stated or necessarily implied by the study design.  
- Keep different sample-size calculations and protocol versions separate. Include calculation assumptions only when explicitly linked to sample-size determination; never substitute final-analysis parameters.  
- Distinguish formal statistical interim analyses from operational safety, cohort, or dose-escalation reviews.  
- **Remove citations, page numbers, filenames, URLs, DOIs, and source notes.**

## Objective-Level Outcomes

Maintain a one-to-one mapping:

- `P1`, `P2`, … for primary objectives and outcomes.  
- `S1`, `S2`, … for secondary objectives and outcomes.

Include only the measurement or response domain stated in the corresponding objective. Retain a comparison, time point, or threshold only when it appears in that objective.

Do not add detailed endpoint definitions, statistical methods, populations, estimands, formulas, missing-data rules, or success criteria.

If an objective does not state a measurement or response domain, write:

`Not specified from this objective.`

## Required Output

Return only the completed Markdown below.

# Evaluation Input

## 1.1 Background and Rationale

## 1.2 Objectives

### Primary Objectives

### Secondary/Exploratory Objectives

## 2.1 Trial Design

### Design Type

### Allocation Ratio

### Intervention Summary

## 2.2 Randomization

**Method&nbsp;**

## 2.3 Sample Size

### Planned Sample Size

## 2.4 Hypothesis Framework

Preserve only the supplied hypothesis structure, testing sequence, and decision rules. Do not create new hypotheses.

## 2.5 Timing of Analyses

Preserve the supplied final-analysis timing, data cutoff or database-lock requirements, data readiness, and assessment timing.

## 3.2 Eligibility Criteria Summary

### Inclusion Criteria

### Exclusion Criteria


Before returning, verify silently that every extracted fact comes from an allowed section and that no missing information was inferred.

## Benchmark

\[PASTE BENCHMARK HERE\]
# Evaluation Input

## 1.1 Background and Rationale

IgA nephropathy (IgAN) is a common glomerulonephritis; progressive renal failure occurs in a substantial proportion of clinically affected patients. STOP IgAN evaluates whether adding immunosuppression to optimized, comprehensive supportive care improves clinically important renal outcomes in patients at risk for progression.

## 1.2 Objectives

### Primary Objectives

- **P1 Objective:** Evaluate efficacy of immunosuppressive therapy added to comprehensive supportive therapy for inducing clinical remission in progressive IgAN.
  - **P1 Outcome:** Clinical remission in progressive IgAN.
- **P2 Objective:** Compare treatments for the number of patients with GFR loss greater than or equal to 15 mL/min.
  - **P2 Outcome:** Number of patients with GFR loss greater than or equal to 15 mL/min, compared between treatments.

### Secondary/Exploratory Objectives

Secondary objectives are not reported as separately labelled objectives; secondary efficacy endpoints are specified. No exploratory objectives are reported.

## 2.1 Trial Design

### Design Type

Randomized, prospective, multicenter, open-label, two-arm parallel-group therapeutic trial, with a 6-month run-in phase and 36-month treatment/follow-up phase.

### Allocation Ratio

1:1 (74 planned per treatment).

### Intervention Summary

All consented patients enter optimized supportive care during run-in:

- BP target below 125/75 mmHg.
- ACE inhibitor first line, with ARB if intolerant.
- Statin therapy.
- Low-sodium counseling and, if GFR <60 mL/min, protein intake 0.8 g/kg/day.

Randomization requires proteinuria >0.75 g/d after run-in. If GFR at week -1 is <90 mL/min, run-in GFR loss must be ≤30%; any GFR loss is permitted if week -1 GFR is ≥90 mL/min. Proteinuria >3.5 g/d is also identified as a run-in dropout condition.

- **Treatment S:** Continue optimized supportive therapy.
- **Treatment I:** Identical supportive care plus:
  - For GFR ≥60 mL/min: methylprednisolone 1 g IV daily for 3 days at months 1, 3, and 5 and prednisolone 0.5 mg/kg every 48 hours for 6 months.
  - For GFR 30–60 mL/min: cyclophosphamide 1.5 mg/kg/day for 3 months with tapered prednisolone, then azathioprine 1.5 mg/kg/day plus prednisolone through 3 years.

Vitamin D/calcium are recommended with corticosteroids; cotrimoxazole pneumocystis prophylaxis and Mesna prophylaxis are recommended with cyclophosphamide.

## 2.2 Randomization

**Method&nbsp;**

Central, web-based randomization using a PHP 5.2 tool and PostgreSQL database, with minimization. Stratification factors are baseline GFR and baseline proteinuria. Blocking is not specified.

## 2.3 Sample Size

### Planned Sample Size

- **Planned enrollment:** 148 randomized patients, 74 per group.
- **Calculation outcome:** First hierarchically ordered primary endpoint, full clinical remission at 3 years; binary remission proportion.
- **Assumed control-arm remission:** Less than 5% under standard/supportive therapy.
- **Assumed treatment-arm remission:** 25% under combined/immunosuppressive therapy after 3 years.
- **Target difference:** 5% versus 25%, approximately 20 percentage points.
- **Variability assumption:** Not applicable to the binary proportion calculation.
- **Significance level:** Two-sided 5%, adjusted for two interim looks by O'Brien-Fleming monitoring.
- **Power:** 80%.
- **Calculation test:** Chi-square (F2) test with continuity correction. Stratification-factor distributions were unavailable for the calculation; the unstratified calculation was considered conservative relative to the planned stratified logistic-regression analysis.
- **Required number of events:** Not specified.
- **Non-inferiority/equivalence margin:** Not applicable; superiority testing.
- **Dropout/non-adherence inflation:** 10%; increased from 60 to 74 patients per group, adding 14 per group.
- **Design effect/clustering:** Not applicable; individually randomized trial. Center is not a stratification variable because of small per-center sample sizes.
- **Basis for assumptions:** Experience with initial IgAN presentations over preceding years.
- **Sample-size re-estimation:** Not specified.
- **Recruitment amendment:** Recruitment duration extended by one year to October 2014.
- **Calculation software:** Addplan 3.1.

## 2.4 Hypothesis Framework

Two independent primary endpoints are tested hierarchically: first full clinical remission, then GFR loss ≥15 mL/min only if the first endpoint is significant.

For each endpoint, the null hypothesis is equal treatment-group rates, or equal means for continuous secondary outcomes, versus a two-sided difference.

## 2.5 Timing of Analyses

- **Final efficacy analysis:** At the third stage/information rate 1.00, after patients are evaluable at 36 months.
- **Final report:** To be submitted within one year after study end.
- **Data cutoff/database-lock requirements:** Not specified.
- **Run-in assessments:** Six visits over months -6 to -0.25.
- **Study-phase assessments:** Sixteen visits at months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36. Urine and renal assessments are scheduled at baseline and selected follow-up visits, including month 36.

## 3.2 Eligibility Criteria Summary

### Inclusion Criteria

- Men or women aged 18–70 years.
- Nephropathologist-confirmed primary mesangioproliferative IgAN.
- Proteinuria >0.75 g/d within 12 weeks before or at run-in start.
- At least one additional ESRD risk factor:
  - Hypertension: ambulatory BP >140/90 mmHg or antihypertensive use.
  - Impaired renal function: creatinine clearance or estimated GFR <90 mL/min.

### Exclusion Criteria

- Known study-drug allergy/intolerance, except ACE-inhibitor intolerance permitting ARB.
- Pregnancy, breastfeeding, or inadequate contraception.
- Contraindication to immunosuppression: acute/chronic infection including hepatitis/HIV, malignancy, leukocytopenia/thrombocytopenia, prednisolone/azathioprine allergy, GI bleeding/ulcer, or need for permanent immunosuppression.
- Prior immunosuppression.
- Rapidly progressive/crescentic (>50% glomeruli) or minimal-change IgAN variants.
- Secondary IgAN or another chronic renal disease.
- GPT >3-fold normal.
- Mean of three creatinine-clearance measurements <30 mL/min.
- Alcohol/drug abuse.
- Mental incapacity or expected noncompliance.
- Concurrent/recent trial participation.
- Dependency.
- Sponsor/investigator employment.
- Legal institutional commitment.

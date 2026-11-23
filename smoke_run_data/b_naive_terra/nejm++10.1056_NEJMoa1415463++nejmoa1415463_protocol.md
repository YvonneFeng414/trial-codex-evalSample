# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

[Provided] IgA nephropathy (IgAN) is a common glomerulonephritis. A substantial proportion of clinically affected patients develop progressive renal failure.

[Provided] The study evaluates whether immunosuppression added to optimized comprehensive supportive care improves renal outcomes in patients at risk of progression.

### 1.2 Objectives

[Provided] **P1:** Evaluate immunosuppressive therapy added to supportive therapy for inducing clinical remission in progressive IgAN.

[Provided] **P2:** Compare treatments for the number of patients with GFR loss ≥15 mL/min.

[Provided] Secondary efficacy endpoints are specified, but secondary objectives are not separately labelled. No exploratory objectives are reported.

## 2. Study Methods

### 2.1 Trial Design

[Provided] This is a randomized, prospective, multicenter, open-label, two-arm parallel-group therapeutic trial. A 6-month run-in precedes a 36-month treatment and follow-up phase. Allocation is 1:1.

[Provided] All consented patients receive optimized supportive care during run-in: blood pressure target below 125/75 mmHg; an ACE inhibitor first line, with an ARB if intolerant; statin therapy; low-sodium counseling; and, if GFR is <60 mL/min, protein intake of 0.8 g/kg/day.

[Provided] Randomization requires proteinuria >0.75 g/day after run-in. If week −1 GFR is <90 mL/min, run-in GFR loss must be ≤30%; any run-in GFR loss is permitted if week −1 GFR is ≥90 mL/min. Proteinuria >3.5 g/day is identified as a run-in dropout condition.

[Provided] **Treatment S:** Continue optimized supportive therapy.

[Provided] **Treatment I:** Receive identical supportive care plus immunosuppression:

- [Provided] For GFR ≥60 mL/min: methylprednisolone 1 g intravenously daily for 3 days at months 1, 3, and 5, plus prednisolone 0.5 mg/kg every 48 hours for 6 months.
- [Provided] For GFR 30–60 mL/min: cyclophosphamide 1.5 mg/kg/day for 3 months with tapered prednisolone, followed by azathioprine 1.5 mg/kg/day plus prednisolone through 3 years.
- [Provided] Vitamin D and calcium are recommended with corticosteroids. Cotrimoxazole pneumocystis prophylaxis and Mesna prophylaxis are recommended with cyclophosphamide.

[Clarification Required] Specify the regimen at exactly 60 mL/min, which falls in both stated ranges, and the approach if GFR is below 30 mL/min at regimen selection. These decisions determine treatment assignment.

[Clarification Required] Specify when proteinuria >3.5 g/day triggers run-in dropout and how it interacts with the post-run-in randomization criterion. This determines which patients proceed to randomization.

### 2.2 Randomization

[Provided] Randomization is central and web-based, using a PHP 5.2 tool and PostgreSQL database with minimization. Baseline GFR and baseline proteinuria are stratification factors. Blocking is not specified.

[Clarification Required] Define the baseline measurements, factor categories, minimization algorithm, tie handling, and any random component or blocking. These details are needed to implement and reproduce allocation.

[Proposed] Restrict access to allocation operations and record allocation transactions. Rationale: this supports allocation integrity; it assumes the central system permits access controls and audit records.

### 2.3 Sample Size

[Provided] The planned sample is 148 randomized patients, 74 per group. The calculation concerns the first hierarchically ordered primary endpoint: the binary proportion in full clinical remission at 3 years.

[Provided] Control-arm remission was assumed to be less than 5% and immunosuppression-arm remission 25%. The target comparison was 5% versus 25%, approximately 20 percentage points. No separate variability assumption applies to the binary proportion calculation.

[Provided] The calculation used a two-sided 5% significance level, adjusted for two interim looks by O’Brien–Fleming monitoring, 80% power, and a chi-square (F2) test with continuity correction. The unstratified calculation was considered conservative relative to the planned stratified logistic-regression analysis because stratification-factor distributions were unavailable.

[Provided] A 10% dropout/non-adherence inflation was stated, increasing the target from 60 to 74 patients per group, an addition of 14 per group. Assumptions were based on experience with initial IgAN presentations over preceding years. Addplan 3.1 was used.

[Clarification Required] Reconcile the stated 10% inflation with the increase from 60 to 74 per group; that increase is not 10%. This matters for interpreting the target and its allowance for missing outcomes.

[Provided] No required event count or sample-size re-estimation is specified. The design is individually randomized, with no clustering design effect; center is not a stratification variable because of small per-center sample sizes. A non-inferiority or equivalence margin is not applicable to the superiority design.

[Provided] Recruitment was extended by one year to October 2014.

[Clarification Required] Decide whether sample-size re-estimation is permitted and, if so, specify its rules and impact on error control. No such procedure is supplied.

### 2.4 Hypothesis Framework

[Provided] The two primary endpoints are tested hierarchically: full clinical remission first, followed by GFR loss ≥15 mL/min only if the first endpoint is significant.

[Provided] For each endpoint, the null is equal treatment-group rates, or equal means for continuous secondary outcomes, against a two-sided difference.

[Clarification Required] Define the treatment effect of interest, including how intercurrent events and death affect each endpoint. This is necessary to make the hypotheses and missing-data strategy operational.

### 2.5 Statistical Interim Analyses

[Provided] The sample-size calculation accounts for two interim looks using O’Brien–Fleming monitoring. The final efficacy analysis is the third stage, at information rate 1.00.

[Clarification Required] Specify interim information fractions, boundaries or spending functions, test statistics, stopping rules, and who reviews interim results. These determine the actual sequential testing procedure.

[Clarification Required] Specify how interim testing of P2 proceeds if P1 becomes significant before the final stage, including whether follow-up and testing continue after an early decision. The hierarchy and overall error control depend on these rules.

[Proposed] Validate the combined hierarchical and group-sequential procedure before outcome review, including its behavior with the planned regression and missing-data methods. Rationale: each primary test must retain appropriate error control; this assumes the monitoring rules can be finalized in advance.

### 2.6 Timing of Analyses

[Provided] The final efficacy analysis occurs at the third stage, information rate 1.00, after patients are evaluable at 36 months. The final report is to be submitted within one year after study end.

[Provided] Six run-in visits occur over months −6 to −0.25. Sixteen study-phase visits occur at months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36. Urine and renal assessments are scheduled at baseline and selected follow-up visits, including month 36.

[Clarification Required] Specify interim-analysis dates or triggers, the study-end definition, data cutoff, database-lock requirements, and assessment windows. These decisions govern when analyses and the report can be completed.

[Proposed] Arrange the month 5 methylprednisolone administration independently of the listed visit schedule. Rationale: month 5 dosing is specified but month 5 is not a listed study visit; this assumes Treatment I patients requiring that dose can attend.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

[Provided] The planned significance level is two-sided 5%, with adjustment for two interim looks. P2 is tested only if P1 is significant.

[Proposed] Report treatment-effect estimates with confidence intervals that account for sequential monitoring where applicable; identify ordinary intervals as descriptive if not adjusted. Rationale: monitoring affects inferential interpretation; this assumes a validated interval method is available for the finalized design.

[Clarification Required] Specify the exact adjusted significance thresholds and confidence-interval construction. Without them, definitive primary inference cannot be reproduced.

### 3.2 Protocol Deviations

[Proposed] Prespecify deviations, including eligibility, treatment, and assessment deviations, and review their importance before final outcome analysis. Rationale: consistent classification supports interpretation; this assumes adequate documentation is available.

[Proposed] Do not exclude randomized patients from the primary population solely for a deviation. Rationale: this preserves the randomized comparison; it assumes the proposed primary population is adopted.

### 3.3 Analysis Populations

[Proposed] Use all randomized patients, analyzed by assigned group, as the primary analysis population. Rationale: this preserves randomization; it assumes the study adopts an intention-to-treat approach.

[Proposed] Define a supplementary per-protocol population using prespecified major deviations, and analyze safety among patients who start randomized-phase treatment according to treatment received. Rationale: these populations support adherence and safety interpretation; this assumes treatment exposure and deviations can be established.

[Clarification Required] Approve the population definitions and rules for treatment switching or partial exposure. These decisions affect denominators and interpretation.

## 4. Trial Population

### 4.1 Screening Data

[Provided] Screening eligibility includes proteinuria measured within 12 weeks before or at run-in start. All consented patients enter supportive care during run-in.

[Proposed] Record screening eligibility, consent, run-in assessments, reasons for screen failure or run-in dropout, and randomization status. Rationale: a disposition account is needed; this assumes these records may be retained under applicable consent and privacy requirements.

### 4.2 Eligibility Criteria Summary

[Provided] Inclusion requires:

- [Provided] Men or women aged 18–70 years.
- [Provided] Nephropathologist-confirmed primary mesangioproliferative IgAN.
- [Provided] Proteinuria >0.75 g/day within 12 weeks before or at run-in start.
- [Provided] At least one additional ESRD risk factor: ambulatory blood pressure >140/90 mmHg or antihypertensive use; or creatinine clearance or estimated GFR <90 mL/min.

[Provided] Exclusion criteria are:

- [Provided] Known study-drug allergy or intolerance, except ACE-inhibitor intolerance permitting an ARB.
- [Provided] Pregnancy, breastfeeding, or inadequate contraception.
- [Provided] Contraindication to immunosuppression: acute or chronic infection including hepatitis or HIV; malignancy; leukocytopenia or thrombocytopenia; prednisolone or azathioprine allergy; gastrointestinal bleeding or ulcer; or need for permanent immunosuppression.
- [Provided] Prior immunosuppression.
- [Provided] Rapidly progressive/crescentic IgAN involving >50% of glomeruli, or minimal-change IgAN variants.
- [Provided] Secondary IgAN or another chronic renal disease.
- [Provided] GPT >3-fold normal.
- [Provided] Mean of three creatinine-clearance measurements <30 mL/min.
- [Provided] Alcohol or drug abuse; mental incapacity or expected noncompliance; concurrent or recent trial participation; dependency; sponsor or investigator employment; or legal institutional commitment.

[Provided] Post-run-in randomization requirements and the proteinuria dropout condition are stated in Section 2.1.

[Clarification Required] Define the reference measurement and calculation for percentage run-in GFR loss, the timing of the three creatinine-clearance measurements, and the meaning of “recent” trial participation. These details affect eligibility decisions.

### 4.3 Recruitment

[Provided] The planned randomized enrollment is 148, and recruitment was extended to October 2014.

[Clarification Required] Specify recruitment procedures, participating centers, and any center-level targets. These operational details are not supplied and are needed for implementation.

### 4.4 Withdrawal and Follow-up

[Proposed] Distinguish treatment discontinuation from withdrawal from follow-up and seek scheduled outcome and safety data after treatment discontinuation where permitted. Rationale: continued follow-up reduces missing data; this assumes consent and applicable requirements allow collection.

[Clarification Required] Specify withdrawal procedures and permitted use of previously collected data. This determines what information may enter analysis after withdrawal.

### 4.5 Baseline Characteristics

[Proposed] Summarize baseline demographics, eligibility-related clinical characteristics, GFR, proteinuria, blood pressure, and relevant treatments by randomized group, without significance tests for baseline imbalance. Rationale: descriptive summaries contextualize the comparison; this assumes these data are collected.

[Clarification Required] Define the baseline time point and measurement selection rules for each variable, particularly the minimization factors. These rules affect adjustment and reproducibility.

## 5. Analysis

### 5.1 Primary Outcomes

[Provided] **P1:** Full clinical remission at 3 years is the first primary endpoint and the sample-size calculation outcome. The objective describes clinical remission in progressive IgAN.

[Clarification Required] Define full clinical remission, its measurements and assessment window, and whether it is identical to the clinical remission in P1. Without an operational definition, patients cannot be classified.

[Provided] **P2:** The number of patients with GFR loss ≥15 mL/min is compared between treatments and tested only after P1 is significant.

[Clarification Required] Define the GFR measurement method, reference value, assessment window, and whether loss is assessed at 36 months or by occurrence during follow-up. These choices determine P2 classification.

### 5.2 Secondary Outcomes

[Provided] Secondary efficacy endpoints are specified, but their identities and definitions are not included in the supplied information. No exploratory objectives are reported.

[Clarification Required] Supply the secondary endpoints, measurement times, analysis methods, and any multiplicity rules. They cannot otherwise be analyzed as prespecified outcomes.

### 5.3 Analysis Methods

[Provided] Stratified logistic regression was planned; the continuity-corrected chi-square test was used for sample-size calculation.

[Proposed] For each binary primary endpoint, summarize events and denominators by assigned group and fit logistic regression with treatment and the baseline minimization factors. Report the treatment effect and confidence interval, alongside group proportions. Rationale: this reflects the planned adjusted comparison; it assumes endpoint definitions and factor coding are finalized.

[Proposed] Prespecify the regression test statistic and a separation-robust contingency method, and validate their sequential properties. Rationale: rare remission may cause unstable estimates; this assumes the selected methods can be calibrated to the monitoring plan.

[Clarification Required] Specify factor coding, the primary effect measure, and the definitive test and sequential implementation. These choices are needed to reproduce the primary analysis.

### 5.4 Missing Data

[Proposed] Summarize missingness by group, visit, outcome, and documented reason. Use observed outcomes after treatment discontinuation where permitted. Rationale: missingness patterns inform interpretation; this assumes follow-up data and reasons are recorded.

[Proposed] For otherwise defined but missing primary outcomes, use a prespecified multiple-imputation analysis incorporating treatment, baseline factors, and relevant observed follow-up data, with sensitivity analyses for departures from its missing-at-random assumption. Rationale: this avoids relying solely on complete cases; it assumes sufficient predictive data and a validated sequential implementation.

[Clarification Required] Decide how death and other events that may make an outcome undefined are handled, and distinguish them from ordinary missing measurements. This is necessary to define the estimand and avoid imputing clinically undefined outcomes without justification.

[Clarification Required] Specify imputation models, handling of missing baseline factors, sensitivity-analysis assumptions, and rules for data unavailable after consent withdrawal. These decisions can materially affect results.

### 5.5 Additional Analyses

[Proposed] Provide supplementary per-protocol analyses and descriptive summaries by baseline GFR and proteinuria, clearly identified as nonprimary. Rationale: these may aid interpretation of adherence and clinical heterogeneity; they assume adequate subgroup data and should not replace randomized primary inference.

[Clarification Required] Specify any planned subgroup comparisons and whether they are inferential. No exploratory objectives or subgroup testing rules are supplied.

### 5.6 Harms

[Proposed] Collect and summarize adverse and serious adverse events, deaths, infections, malignancies, and treatment discontinuations or modifications by treatment received. Rationale: immunosuppression requires safety assessment; this assumes systematic safety collection is feasible.

[Clarification Required] Define safety collection periods, event definitions and grading, attribution, reporting obligations, and treatment-modification rules. These are needed for consistent safety monitoring and reporting.

### 5.7 Software and References

[Provided] Addplan 3.1 was used for the sample-size calculation. Randomization uses PHP 5.2 and PostgreSQL.

[Clarification Required] Specify the software and versions for statistical analysis and the procedures for validation and reproducibility. These are not supplied.

[Proposed] Archive analysis code, specifications, and version information with the final outputs. Rationale: this supports reproducibility; it assumes appropriate secure storage is available.

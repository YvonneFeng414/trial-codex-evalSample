# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

- **[Provided]** IgA nephropathy (IgAN) is a common glomerulonephritis, and progressive renal failure occurs in a substantial proportion of clinically affected patients. The study evaluates whether adding immunosuppression to optimized, comprehensive supportive care improves clinically important renal outcomes in patients at risk for progression.

### 1.2 Objectives

- **[Provided]** **P1 primary objective:** Evaluate the efficacy of immunosuppressive therapy added to comprehensive supportive therapy for inducing clinical remission in progressive IgAN. The corresponding outcome is clinical remission in progressive IgAN.
- **[Provided]** **P2 primary objective:** Compare treatments for the number of patients with GFR loss greater than or equal to 15 mL/min. The corresponding outcome is the number of patients meeting that threshold, compared between treatments.
- **[Provided]** The two primary endpoints are tested hierarchically: full clinical remission first, followed by GFR loss ≥15 mL/min only if the first endpoint is significant.
- **[Provided]** Secondary objectives are not reported as separately labelled objectives. Secondary efficacy endpoints are indicated but are not enumerated in the supplied study details. No exploratory objectives are reported.
- **[Clarification Required]** The operational definition of full clinical remission, including its component measures, thresholds, and assessment time point, is missing. This is essential to classify participants and conduct the first confirmatory test.
- **[Clarification Required]** The specific secondary efficacy endpoints are missing. Their definitions, time points, and analysis methods are needed to complete the prespecified analysis plan.

## 2\. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a randomized, prospective, multicenter, open-label, two-arm, parallel-group therapeutic trial with a 6-month run-in phase and a 36-month treatment/follow-up phase.
- **[Provided]** Planned allocation is 1:1, with 74 patients planned per treatment group.
- **[Provided]** All consented patients enter optimized supportive care during run-in. Supportive care comprises a blood-pressure target below 125/75 mmHg; an ACE inhibitor as first-line therapy, with an ARB if ACE-inhibitor intolerant; statin therapy; low-sodium counseling; and, if GFR is <60 mL/min, protein intake of 0.8 g/kg/day.
- **[Provided]** Randomization requires proteinuria >0.75 g/day after run-in. If GFR at week −1 is <90 mL/min, run-in GFR loss must be ≤30%; any GFR loss is permitted if week −1 GFR is ≥90 mL/min. Proteinuria >3.5 g/day is identified as a run-in dropout condition.
- **[Clarification Required]** The reference measurement and calculation for run-in GFR loss, as well as the exact timing and measurement rule for post-run-in proteinuria, are not specified. These decisions affect eligibility and reproducibility of randomization.
- **[Clarification Required]** The handling of the proteinuria >3.5 g/day run-in dropout condition, including the measurement time point and any confirmation rule, is not described. This matters for consistent run-in discontinuation decisions.
- **[Provided]** **Treatment S:** Continue optimized supportive therapy.
- **[Provided]** **Treatment I:** Continue identical supportive care and add immunosuppressive therapy. For GFR ≥60 mL/min, treatment is methylprednisolone 1 g intravenously daily for 3 days at months 1, 3, and 5, and prednisolone 0.5 mg/kg every 48 hours for 6 months. For GFR 30–60 mL/min, treatment is cyclophosphamide 1.5 mg/kg/day for 3 months with tapered prednisolone, followed by azathioprine 1.5 mg/kg/day plus prednisolone through 3 years.
- **[Provided]** Vitamin D/calcium are recommended with corticosteroids. Cotrimoxazole prophylaxis against Pneumocystis and Mesna prophylaxis are recommended with cyclophosphamide.
- **[Clarification Required]** The GFR assessment time used to select the Treatment I regimen, and the handling of a GFR exactly at a regimen boundary or changing during treatment, are not specified. These decisions affect treatment assignment and consistency of care.
- **[Clarification Required]** Details of the prednisolone taper for the GFR 30–60 mL/min regimen, and the dosing or duration of its prednisolone component, are not provided. These are needed to implement the regimen consistently.
- **[Proposed]** Record supportive-care and study-drug exposure, dose changes, interruptions, and adherence throughout follow-up. **Rationale:** This supports interpretation of treatment effects in an open-label trial. **Assumption:** These data can be collected without changing the specified treatment regimens.

### 2.2 Randomization

- **[Provided]** Randomization is central and web-based, using a PHP 5.2 tool and PostgreSQL database, with minimization. Stratification factors are baseline GFR and baseline proteinuria. Blocking is not specified.
- **[Clarification Required]** The minimization algorithm, any random component, the categories or functional form for the stratification factors, and the allocation-concealment implementation are not specified. These details affect reproducibility and assessment of allocation procedures.

### 2.3 Sample Size

- **[Provided]** Planned enrollment is 148 randomized patients, 74 per group. The calculation is based on the first hierarchically ordered primary endpoint: full clinical remission at 3 years, treated as a binary proportion.
- **[Provided]** The assumed control-arm remission rate is <5% under standard/supportive therapy; the assumed treatment-arm rate is 25% under combined/immunosuppressive therapy after 3 years. The target difference is approximately 20 percentage points (5% versus 25%).
- **[Provided]** The calculation uses 80% power and a two-sided 5% significance level adjusted for two interim looks by O’Brien–Fleming monitoring. The calculation test is a chi-square (F2) test with continuity correction. Variability is not applicable to the binary proportion calculation.
- **[Provided]** Stratification-factor distributions were unavailable for the calculation; the unstratified calculation was considered conservative relative to the planned stratified logistic-regression analysis.
- **[Provided]** A 10% dropout/non-adherence inflation was applied, increasing the planned sample from 60 to 74 patients per group, adding 14 per group. Required event count is not specified. A non-inferiority/equivalence margin is not applicable because the trial uses superiority testing.
- **[Provided]** Design effect/clustering is not applicable because this is an individually randomized trial. Center is not a stratification variable because per-center sample sizes are small. Sample-size re-estimation is not specified.
- **[Provided]** The assumptions are based on experience with initial IgAN presentations over preceding years. Sample-size calculations used Addplan 3.1.
- **[Provided]** Recruitment duration was extended by one year to October 2014.
- **[Clarification Required]** The precise remission definition used to generate the sample-size assumptions is not stated. This must be reconciled with the endpoint definition used in the trial analysis.
- **[Clarification Required]** The handling of the stated <5% control assumption in the calculation and the exact unrounded calculation inputs are not given. These matter for reproducing the sample-size calculation.

### 2.4 Hypothesis Framework

- **[Provided]** The two primary endpoints are independent and tested hierarchically: full clinical remission first, then GFR loss ≥15 mL/min only if the first endpoint is significant.
- **[Provided]** For each endpoint, the null hypothesis is equal treatment-group rates; for continuous secondary outcomes, the null is equal treatment-group means. The alternative is a two-sided difference.
- **[Clarification Required]** The significance criterion that defines a significant first endpoint for proceeding to the second endpoint is not fully specified, particularly in relation to the interim monitoring boundaries. This matters for controlling the confirmatory testing procedure.

### 2.5 Statistical Interim Analyses

- **[Provided]** The sample-size significance level accounts for two interim looks using O’Brien–Fleming monitoring. The final efficacy analysis is the third stage, at information rate 1.00.
- **[Clarification Required]** The timing and information fractions of the two interim looks, the applicable O’Brien–Fleming boundaries, the decision rules for stopping early, and the roles permitted to review interim results are not specified. These are needed to implement monitoring and interpret the final significance threshold.
- **[Clarification Required]** It is not specified whether interim looks cover both primary endpoints or only the sample-size endpoint, nor how the hierarchical testing sequence is applied at interim analyses. This affects multiplicity control and stopping decisions.

### 2.6 Timing of Analyses

- **[Provided]** The final efficacy analysis is planned at the third stage/information rate 1.00, after patients are evaluable at 36 months. The final report is to be submitted within one year after study end.
- **[Provided]** Run-in assessments comprise six visits from month −6 through month −0.25. Study-phase assessments comprise 16 visits at months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36.
- **[Provided]** Urine and renal assessments are scheduled at baseline and selected follow-up visits, including month 36.
- **[Clarification Required]** The calendar timing of interim analyses, the database-lock and data-cutoff requirements, and the definition of study end are not specified. These are needed to determine analysis readiness and the report deadline.
- **[Clarification Required]** The exact visits and procedures for urine and renal assessments are not listed. This matters for endpoint ascertainment and handling assessments outside the scheduled window.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The sample-size calculation uses a two-sided 5% significance level, adjusted for two interim looks using O’Brien–Fleming monitoring. The study uses superiority testing.
- **[Proposed]** Report effect estimates with two-sided 95% confidence intervals and report the interim-adjusted decision against the applicable monitoring boundary. **Rationale:** Effect estimates and intervals communicate magnitude and precision alongside hypothesis tests. **Assumption:** A 95% interval is suitable for descriptive reporting; confirmatory decisions remain governed by the specified monitoring and hierarchy rules.
- **[Clarification Required]** The final critical boundary or alpha-spending rule, and whether confidence intervals are to be adjusted for interim monitoring and hierarchical testing, are not specified. These choices determine confirmatory interpretation.

### 3.2 Protocol Deviations

- **[Proposed]** Maintain a record of protocol deviations, including eligibility, run-in, treatment, follow-up, and outcome-assessment deviations, with timing and disposition. **Rationale:** A documented record supports transparent population definitions and sensitivity analyses. **Assumption:** These categories can be applied without changing trial conduct.
- **[Proposed]** Preserve randomized treatment assignment for the primary intention-to-treat analysis regardless of treatment received or adherence. **Rationale:** This maintains the randomized comparison. **Assumption:** Participants can be analyzed according to their recorded randomized assignment.
- **[Clarification Required]** Definitions of major/minor deviations and criteria for any per-protocol exclusions are not supplied. These decisions affect population membership and interpretation of supportive analyses.

### 3.3 Analysis Populations

- **[Proposed]** Define the primary intention-to-treat population as all randomized participants analyzed according to randomized group. **Rationale:** This preserves the benefits of randomization. **Assumption:** Randomization records and participant outcome data are available for all randomized participants.
- **[Proposed]** Define a per-protocol population before unblinded outcome analysis, based on prespecified adherence and deviation rules, and use it for supportive analyses only. **Rationale:** This can assess sensitivity to major protocol departures. **Assumption:** The study team can specify objective rules before reviewing treatment outcomes.
- **[Proposed]** Define the safety population as randomized participants who receive at least one dose of assigned study treatment, analyzed by treatment received. **Rationale:** This aligns safety summaries with exposure. **Assumption:** Treatment exposure is recorded and this population definition is suitable for the trial.
- **[Clarification Required]** The study-specific analysis-population definitions, including handling of participants who are randomized but never treated, are not provided. They are needed to ensure reproducible denominators.

## 4\. Trial Population

### 4.1 Screening Data

- **[Proposed]** Maintain a screening record of consent, eligibility status, screen failure, and reasons for non-enrollment, with run-in and randomization eligibility recorded separately. **Rationale:** This describes participant flow and the effect of run-in selection. **Assumption:** Screening and run-in decisions can be documented consistently.
- **[Clarification Required]** Screening totals, screen-failure categories, and the planned screening-data collection procedures are not supplied. These matter for reporting participant flow and evaluating recruitment.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria are men or women aged 18–70 years; nephropathologist-confirmed primary mesangioproliferative IgAN; proteinuria >0.75 g/day within 12 weeks before or at run-in start; and at least one additional ESRD risk factor: hypertension (ambulatory BP >140/90 mmHg or antihypertensive use) or impaired renal function (creatinine clearance or estimated GFR <90 mL/min).
- **[Provided]** Exclusion criteria are known study-drug allergy/intolerance, except ACE-inhibitor intolerance permitting ARB; pregnancy, breastfeeding, or inadequate contraception; contraindication to immunosuppression (acute/chronic infection including hepatitis/HIV, malignancy, leukocytopenia/thrombocytopenia, prednisolone/azathioprine allergy, GI bleeding/ulcer, or need for permanent immunosuppression); prior immunosuppression; rapidly progressive/crescentic disease (>50% glomeruli) or minimal-change IgAN variants; secondary IgAN or another chronic renal disease; GPT >3-fold normal; mean of three creatinine-clearance measurements <30 mL/min; alcohol/drug abuse; mental incapacity or expected noncompliance; concurrent/recent trial participation; dependency; sponsor/investigator employment; and legal institutional commitment.
- **[Clarification Required]** Operational definitions and assessment procedures for “recent” trial participation, dependency, inadequate contraception, expected noncompliance, and the timing/reference range for GPT are not specified. These may affect consistent eligibility decisions.

### 4.3 Recruitment

- **[Provided]** The trial is multicenter, plans 148 randomized participants in a 1:1 allocation, and had its recruitment duration extended by one year to October 2014.
- **[Clarification Required]** Recruitment start date, participating centers, recruitment status, and actual enrollment are not supplied. These are needed to describe recruitment progress and reconcile planned versus achieved enrollment.
- **[Proposed]** Report numbers screened, entering run-in, meeting post-run-in randomization criteria, randomized, and completing follow-up. **Rationale:** These stages distinguish initial eligibility from run-in attrition. **Assumption:** The corresponding participant-flow data are collected.

### 4.4 Withdrawal and Follow-up

- **[Provided]** The study phase includes follow-up through month 36, with scheduled assessments at 16 specified visits from month 0 through month 36.
- **[Clarification Required]** Withdrawal criteria, withdrawal categories, follow-up after treatment discontinuation, and procedures for obtaining outcomes after withdrawal from treatment are not specified. These decisions affect missing outcome data and interpretation of treatment effects.
- **[Proposed]** Where consent and applicable procedures permit, seek scheduled outcome data after study-treatment discontinuation. **Rationale:** Continued outcome ascertainment can reduce missing follow-up while preserving the randomized comparison. **Assumption:** Participants may remain in follow-up after stopping treatment.

### 4.5 Baseline Characteristics

- **[Provided]** Baseline GFR and baseline proteinuria are randomization stratification factors.
- **[Proposed]** Summarize baseline demographic and clinical characteristics by randomized group, including the stratification factors, without relying on baseline significance tests. **Rationale:** Descriptive summaries characterize the enrolled groups and document the minimization factors. **Assumption:** These baseline data are collected and defined before unblinded analysis.
- **[Clarification Required]** The baseline variables, measurement definitions, and categorization cut points for GFR and proteinuria are not specified. These are needed for consistent reporting and implementation of stratified analyses.

## 5\. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The first primary outcome is full clinical remission at 3 years, a binary remission proportion for the sample-size calculation. It is the first endpoint in the hierarchical testing sequence.
- **[Provided]** The second primary outcome is the number of patients with GFR loss ≥15 mL/min, compared between treatments. It is tested only if the first endpoint is significant.
- **[Clarification Required]** The clinical-remission criteria and assessment window are missing. Without them, the primary binary outcome cannot be classified consistently.
- **[Clarification Required]** The reference value and time period for GFR loss, whether “loss” means an absolute change from baseline, the GFR measurement method, and any confirmation requirement are not specified. These determine who meets the second primary outcome.

### 5.2 Secondary Outcomes

- **[Provided]** Secondary efficacy endpoints are indicated, but are not enumerated in the supplied study details. For continuous secondary outcomes, the stated null hypothesis is equal treatment-group means versus a two-sided difference.
- **[Clarification Required]** The endpoint names, definitions, measurement times, analysis populations, and ordering or multiplicity approach for secondary outcomes are not supplied. These are required to specify and interpret secondary analyses.

### 5.3 Analysis Methods

- **[Provided]** The planned analysis for the remission endpoint is described as stratified logistic regression, with baseline GFR and baseline proteinuria as stratification factors. The unstratified chi-square calculation was considered conservative relative to that planned analysis.
- **[Proposed]** Analyze the remission endpoint using logistic regression with treatment group and the prespecified baseline GFR and proteinuria stratification factors; report group-specific proportions and a treatment effect estimate with confidence interval. **Rationale:** This is consistent with the stated planned stratified logistic-regression analysis. **Assumption:** The stratification factors and their analysis coding can be prespecified from the randomization implementation.
- **[Proposed]** Analyze the binary GFR-loss endpoint using logistic regression with treatment group and the same baseline stratification factors; report group-specific proportions and a treatment effect estimate with confidence interval. **Rationale:** A binary-outcome model is appropriate for the stated threshold endpoint and aligns the analysis with the planned stratified approach. **Assumption:** The endpoint is classified as a binary outcome for each participant at the defined assessment time.
- **[Proposed]** For any specified continuous secondary outcomes, report treatment-group summaries and between-group mean differences with confidence intervals, using a model that accounts for the prespecified design factors where appropriate. **Rationale:** This corresponds to the stated equal-means hypothesis for continuous secondary outcomes. **Assumption:** The eventual endpoint list and measurement schedules support these analyses.
- **[Clarification Required]** The exact model specification, coding of baseline strata, covariate handling, and analysis time point for each primary endpoint are not fully specified. These decisions affect reproducibility and the treatment-effect estimates.

### 5.4 Missing Data

- **[Clarification Required]** The planned handling of missing primary and secondary outcomes, missed visits, and withdrawal-related data is not specified. This matters because missing outcomes may affect endpoint classification and treatment comparisons.
- **[Proposed]** Describe the amount, timing, and reasons for missingness by treatment group, and conduct a prespecified sensitivity analysis for missing primary outcomes. **Rationale:** Missingness summaries and sensitivity analyses show how conclusions may depend on unavailable outcomes. **Assumption:** Reasons for missing data are recorded and a suitable sensitivity method can be selected before outcome review.
- **[Proposed]** Use multiple imputation as a possible primary missing-data approach only if a missing-at-random assumption is defensible, with sensitivity analyses examining departures from that assumption. **Rationale:** This provides a model-based approach while acknowledging uncertainty about unobserved outcomes. **Assumption:** Relevant predictors of missingness and outcome are collected; the method remains subject to prespecification.

### 5.5 Additional Analyses

- **[Proposed]** Conduct a per-protocol analysis as supportive to the intention-to-treat primary analysis, using the population and deviation rules prespecified before unblinded outcome analysis. **Rationale:** This assesses whether major protocol departures materially affect interpretation. **Assumption:** Objective criteria can be agreed in advance.
- **[Clarification Required]** Any prespecified subgroup analyses, treatment-effect modifiers, or additional sensitivity analyses are not identified. Their selection and multiplicity handling matter for interpretation and avoidance of unplanned inference.

### 5.6 Harms

- **[Provided]** Treatment I includes corticosteroid-based regimens and, for GFR 30–60 mL/min, cyclophosphamide followed by azathioprine and prednisolone. Vitamin D/calcium, cotrimoxazole, and Mesna prophylaxis are recommended in the circumstances described for those treatments.
- **[Proposed]** Summarize harms by randomized group and by treatment received, including participant counts and event counts, and describe serious events and treatment discontinuations attributed to harms. **Rationale:** These summaries allow comparison of safety experience and treatment tolerability. **Assumption:** Harms, seriousness, and treatment discontinuation are collected systematically.
- **[Clarification Required]** Harms definitions, collection period, severity grading, causal attribution, coding conventions, reporting timelines, and safety oversight procedures are not specified. These are needed for consistent safety surveillance and reporting.

### 5.7 Software and References

- **[Provided]** Addplan 3.1 was used for the sample-size calculation. The central web-based randomization tool uses PHP 5.2 and a PostgreSQL database.
- **[Clarification Required]** Statistical analysis software and version are not specified. This information is needed for reproducibility.
- **[Proposed]** Record the software and version used for each analysis and retain analysis code and outputs. **Rationale:** This supports reproducibility and auditability. **Assumption:** The analysis environment and code can be retained.
- **[Clarification Required]** No bibliography or study-specific reference list is supplied. Any protocol reference requirements must be determined separately.

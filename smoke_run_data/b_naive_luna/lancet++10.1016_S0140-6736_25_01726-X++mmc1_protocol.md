# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** POInT is a phase IIb primary-prevention trial in genetically at-risk infants. It tests whether sustained oral exposure to insulin during the usual period of initiation of beta-cell autoimmunity induces immune tolerance and reduces beta-cell autoimmunity and diabetes.

### 1.2 Objectives

- **[Provided]** **Primary objective (P1):** Determine whether daily oral insulin from age 4–7 months to age 3 years reduces cumulative incidence of beta-cell autoantibodies and diabetes in childhood. The stated outcome is cumulative incidence of beta-cell autoantibodies and diabetes in childhood.
- **[Provided]** **Secondary objective (S1):** Compare development of any persistent confirmed beta-cell autoantibody, persistent confirmed IAA, persistent confirmed GADA, and dysglycaemia or diabetes. These are the stated S1 outcomes.
- **[Provided]** **Exploratory objective (S2):** Assess treatment effects in subgroups and in immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures; assess type 1 diabetes and progression from seroconversion to clinical type 1 diabetes. These are the stated S2 outcomes.
- **[Clarification Required]** The operational definitions of “persistent,” “confirmed,” dysglycaemia, seroconversion, clinical diabetes, and the childhood assessment horizon are not specified. These decisions are needed to identify events consistently and determine endpoint timing and analysis.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is an investigator-initiated, multicentre, multinational, randomized, double-blind, placebo-controlled, phase IIb primary-prevention study with 1:1 allocation to oral insulin or placebo.
- **[Provided]** A parent administers one oral capsule daily, preferably between 07:00 and 10:00. Treatment ends the day before the age-3 visit or with clinical diabetes.
- **[Provided]** The oral-insulin regimen is 7.5 mg for 2 months, then 22.5 mg for 2 months, then 67.5 mg until age 3 years. The capsule contains human recombinant insulin crystals plus microcrystalline cellulose to a total capsule weight of 200 mg, in a 0.5-mL hard gelatin capsule.
- **[Provided]** The placebo is a matching microcrystalline-cellulose capsule given daily until age 3 years.
- **[Clarification Required]** The protocol does not specify whether or how treatment is resumed after a temporary interruption, how dose changes or missed doses are managed, or how adherence is measured. These decisions affect treatment exposure summaries and any per-protocol analyses.

### 2.2 Randomization

- **[Provided]** The study-drug manufacturer uses package-number randomization; a separate randomization list assigns multiples to the same arm. The allocation ratio is 1:1.
- **[Provided]** Stratification factors and use of minimization or blocking are not specified.
- **[Clarification Required]** The sequence-generation details, package-number implementation, allocation-concealment procedures, and handling of package discrepancies are not specified. These are needed to document the randomization process and assess deviations.
- **[Clarification Required]** Any stratification or blocking decisions must be confirmed before specifying adjusted analyses; the supplied information does not identify such factors.

### 2.3 Sample Size

- **[Provided]** Planned allocation was 1,050 infants, 1:1. The original design projected 1,040; completed enrollment was 1,050.
- **[Provided]** The original calculation outcome was persistent confirmed multiple beta-cell autoantibodies or diabetes, analyzed as a time-to-event/hazard-rate outcome. The control assumption was a 7.5% event probability at 3.5 years, corresponding under an exponential distribution to hazard 0.02227; the treatment assumption was a halved hazard of 0.011135, a target 50% risk reduction/hazard-rate reduction.
- **[Provided]** The original calculation used a two-sided overall significance level of 0.05, 80% power, and a two-sided log-rank test of equal hazard rates. It required complete follow-up for 832 children, uniformly randomized over 3.5 years and followed for another 3.5 years. A 20% dropout allowance yielded 1,040 children to be randomized.
- **[Provided]** The calculation was based on expected primary-outcome frequency, the exponential hazard model, accrual and follow-up assumptions, and anticipated dropout. All randomized children, including those contributing observation time to dropout, contribute to the primary analysis.
- **[Provided]** In the October 2021 blinded update, observed blinded dropout, accrual, and event-rate information were used. The placebo hazard used in the re-estimate was 0.02456, with a halved treatment-hazard scenario of 0.01228. Projected power was 81.3% under the observed total hazard and halved treatment hazard.
- **[Provided]** The updated calculation extrapolated dropout of 12% (95% CI 8–15%). Completed accrual was 3.17 years with 3.25-year follow-up. The calculation used PROC POWER in SAS 9.4, based on the Lakatos formula. No power issue was judged to prevent trial end six months after last treatment.
- **[Provided]** The required number of events was not specified. A non-inferiority/equivalence margin was not applicable because the framework is superiority; design effect/clustering was not applicable because this is an individually randomized trial.
- **[Clarification Required]** The design assumptions specify the calculation endpoint, but the protocol does not fully specify how that endpoint maps to the P1 outcome of cumulative incidence of beta-cell autoantibodies and diabetes in childhood. Confirming this mapping is important for interpreting the sample-size justification and final primary analysis.

### 2.4 Hypothesis Framework

- **[Provided]** Primary and secondary endpoints are superiority endpoints. The primary null compares equal hazard rates, and the primary confirmatory comparison is oral insulin versus placebo for persistent confirmed multiple beta-cell autoantibodies or diabetes.
- **[Provided]** The sample-size calculation used a two-sided overall significance level of 0.05 and a two-sided log-rank test of equal hazard rates.
- **[Proposed]** For the confirmatory primary comparison, test the null hypothesis of equal event hazards between assigned groups against the two-sided alternative of unequal hazards. **Rationale:** this matches the stated primary null and sample-size test. **Assumption:** the confirmatory endpoint is the specified time-to-event outcome of persistent confirmed multiple beta-cell autoantibodies or diabetes.
- **[Clarification Required]** The testing hierarchy and multiplicity procedure for the secondary endpoints are not specified. These decisions matter for which secondary findings, if any, can be considered confirmatory.

### 2.5 Statistical Interim Analyses

- **[Provided]** A blinded sample-size update was conducted in October 2021 using observed blinded dropout, accrual, and event-rate information.
- **[Clarification Required]** Whether any formal interim efficacy or safety analyses, stopping rules, or independent monitoring arrangements were planned is not specified. These decisions affect error control, trial oversight, and interpretation of early stopping.
- **[Clarification Required]** The supplied description does not state whether the October 2021 update included any unblinded treatment comparison. Confirming this is necessary to characterize its role and assess whether it affected the planned final analysis.

### 2.6 Timing of Analyses

- **[Provided]** The final analysis was planned after the observation period ending six months after the last participant’s last treatment day, expected June 2024, and after final data export and quality control. Database lock was October 23, 2024.
- **[Provided]** The assessment schedule includes eight intervention visits from baseline through age 3 years and up to nine post-age-3 follow-up visits. Blood for autoantibodies is collected at every visit.
- **[Provided]** Persistent-autoantibody-positive children undergo OGTTs from age 3 years at six-month intervals.
- **[Clarification Required]** The precise timing and data cut used for each final endpoint analysis, including how assessments after the last treatment day are incorporated, are not specified. This affects follow-up duration, censoring, and the population included in the final dataset.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The original sample-size calculation used a two-sided overall significance level of 0.05.
- **[Proposed]** Use two-sided tests and report 95% confidence intervals for treatment-effect estimates. **Rationale:** these align with the two-sided design calculation and provide uncertainty estimates. **Assumption:** the 0.05 level is also intended for the primary final analysis.
- **[Clarification Required]** The confidence level and multiplicity-adjusted significance thresholds for secondary and exploratory comparisons are not specified. These decisions are needed to distinguish inferential claims from descriptive results.

### 3.2 Protocol Deviations

- **[Proposed]** Document deviations before treatment-code release, classify them by type and potential effect on outcome assessment or treatment exposure, and retain randomized participants in the primary analysis. **Rationale:** this supports transparent reporting while preserving the randomized comparison. **Assumption:** the primary analysis remains based on assigned treatment as stated for all randomized children.
- **[Clarification Required]** No deviation categories or criteria for major deviations are supplied. These decisions matter for any per-protocol or sensitivity analyses and should be specified without using observed outcomes to define exclusions.

### 3.3 Analysis Populations

- **[Provided]** All randomized children, including those contributing observation time to dropout, contribute to the primary analysis.
- **[Proposed]** Define the primary analysis population as all randomized children analyzed according to assigned arm. **Rationale:** this operationalizes the stated inclusion of all randomized children in the primary analysis. **Assumption:** assignment, rather than treatment received, determines the primary comparison.
- **[Proposed]** Use a per-protocol population only for supportive sensitivity analyses, with membership criteria finalized before unblinding. **Rationale:** it can assess robustness to major protocol deviations without replacing the randomized comparison. **Assumption:** suitable deviation criteria and exposure data can be established.
- **[Clarification Required]** The safety population and any per-protocol eligibility criteria are not specified. These decisions matter for assigning participants to safety summaries and defining supportive analyses.

## 4. Trial Population

### 4.1 Screening Data

- **[Provided]** Eligibility includes age, genetic risk, solid-food introduction, parental written consent, and the stated clinical and trial-related exclusions.
- **[Clarification Required]** The screening dataset, screening-failure categories, and numbers screened or excluded are not supplied. These are needed to describe participant flow and assess how enrolled participants relate to the eligible population.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria are age 4–7 months; greater than 10% risk of developing multiple beta-cell autoantibodies by age 6 years; introduction of solid food; and parental written consent.
- **[Provided]** For children without a first-degree history of type 1 diabetes, eligibility requires DR3/DR4-DQ8 or DR4-DQ8/DR4-DQ8 plus a genetic-risk score greater than 14.4.
- **[Provided]** For children with a first-degree history of type 1 diabetes, eligibility requires HLA DR4 and DQ8 without DRB1*1501 or DQB1*0503.
- **[Provided]** Exclusion criteria are an interfering disease or treatment; a condition associated with poor compliance; an unsafe medical condition; diabetes at recruitment; or participation in another clinical trial.
- **[Clarification Required]** The methods for calculating the stated risk threshold and genetic-risk score, and the detailed interpretation of the HLA criteria, are not specified. These details are needed to reproduce eligibility determinations.

### 4.3 Recruitment

- **[Provided]** The study is investigator-initiated, multicentre, and multinational. Completed enrollment was 1,050 infants.
- **[Clarification Required]** Recruitment countries, sites, recruitment dates, and recruitment procedures are not supplied. These details are needed to describe the recruitment context and participant flow.

### 4.4 Withdrawal and Follow-up

- **[Provided]** Treatment ends the day before the age-3 visit or with clinical diabetes. The assessment schedule includes up to nine post-age-3 follow-up visits.
- **[Provided]** The original sample-size calculation allowed for 20% dropout; the October 2021 blinded update extrapolated dropout of 12% (95% CI 8–15%).
- **[Clarification Required]** Rules for withdrawal from treatment versus withdrawal from follow-up, continued assessments after treatment discontinuation, and reasons for loss to follow-up are not specified. These decisions affect endpoint ascertainment and censoring.
- **[Clarification Required]** The age-3 visit and the final treatment day are not further defined for participants who discontinue treatment early or develop clinical diabetes. This matters for consistent treatment-exposure and follow-up definitions.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize baseline characteristics by randomized arm using descriptive statistics appropriate to each variable, without significance testing to assess baseline balance. **Rationale:** descriptive summaries characterize the randomized groups without treating chance differences as evidence of treatment effects. **Assumption:** baseline variables are available in the locked dataset.
- **[Clarification Required]** The baseline variables to be collected and reported are not listed. This decision matters for the clinical description of the study population and any planned covariate-adjusted analyses.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The P1 outcome is cumulative incidence of beta-cell autoantibodies and diabetes in childhood.
- **[Provided]** The primary confirmatory comparison is oral insulin versus placebo for persistent confirmed multiple beta-cell autoantibodies or diabetes; this was also the outcome used in the original sample-size calculation.
- **[Clarification Required]** The relationship between the broader P1 outcome and the confirmatory multiple-autoantibody-or-diabetes endpoint is not specified. The primary endpoint, event definition, and any relationship between these outcome formulations must be confirmed to ensure a single interpretable confirmatory analysis.
- **[Clarification Required]** The definitions of persistent and confirmed multiple autoantibodies, event date, diabetes ascertainment, and endpoint censoring time are not supplied. These decisions determine event classification and analysis time.

### 5.2 Secondary Outcomes

- **[Provided]** The secondary outcomes are development of any persistent confirmed beta-cell autoantibody, persistent confirmed IAA, persistent confirmed GADA, and dysglycaemia or diabetes.
- **[Provided]** Exploratory outcomes include immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures; type 1 diabetes; and progression from seroconversion to clinical type 1 diabetes.
- **[Clarification Required]** The measurement schedule and definitions for dysglycaemia, each persistent-autoantibody outcome, seroconversion, and progression to clinical type 1 diabetes are not fully specified. These are needed to define analysis datasets and endpoint timing.

### 5.3 Analysis Methods

- **[Provided]** The primary null compares equal hazard rates, and the original sample-size calculation specified a two-sided log-rank test of equal hazard rates.
- **[Proposed]** Analyze the confirmatory time-to-event endpoint by randomized arm using a two-sided log-rank test and report the treatment hazard ratio with a 95% confidence interval. **Rationale:** the log-rank test matches the stated sample-size test and hazard-based hypothesis; the hazard ratio quantifies the comparison. **Assumption:** the confirmatory outcome is the specified time-to-event endpoint and event and censoring times can be derived.
- **[Proposed]** Display event-free estimates over follow-up and use a Cox proportional-hazards model as a supporting effect-estimation method; assess the proportional-hazards assumption and interpret the hazard ratio cautiously if it is not supported. **Rationale:** these methods complement the log-rank comparison and describe the time-to-event pattern. **Assumption:** the available follow-up and event counts support estimation.
- **[Proposed]** Analyze secondary time-to-event outcomes using corresponding time-to-first-event methods and report estimates with confidence intervals; summarize longitudinal measures by randomized arm using repeated-measures methods that account for within-participant correlation. **Rationale:** this matches event outcomes and repeated longitudinal measurements. **Assumption:** endpoint definitions, measurement times, and data structure are confirmed before analysis.
- **[Clarification Required]** Covariates for adjusted analyses, the time origin, censoring rules, and any age-based or visit-based time scale are not specified. These decisions affect model interpretation and must be fixed before treatment-code release.
- **[Clarification Required]** The endpoint-specific analysis methods for dysglycaemia, diabetes, autoantibody outcomes, and longitudinal measures are not fully specified. These choices matter because outcome types and measurement schedules may require different estimands and models.

### 5.4 Missing Data

- **[Proposed]** For time-to-event analyses, censor participants at the last date on which endpoint status is adequately assessed, and describe the extent and reasons for missing assessments and loss to follow-up. **Rationale:** this uses available follow-up without treating an unobserved event status as event-free indefinitely. **Assumption:** adequate assessment dates and censoring reasons are recorded.
- **[Proposed]** For longitudinal analyses, report missingness by visit and arm and use methods that accommodate incomplete repeated measurements, with sensitivity analyses if missingness may depend on unobserved outcomes. **Rationale:** incomplete follow-up can affect longitudinal comparisons. **Assumption:** the chosen model’s missing-data assumptions are stated and assessed as far as possible.
- **[Clarification Required]** No missing-data strategy, endpoint ascertainment rule for missed visits, or sensitivity-analysis plan is specified. These decisions are important because incomplete assessments may affect event classification and treatment-effect estimates.

### 5.5 Additional Analyses

- **[Provided]** Exploratory objective S2 includes treatment effects in subgroups and assessment of immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures, type 1 diabetes, and progression from seroconversion to clinical type 1 diabetes.
- **[Proposed]** Treat subgroup and additional biomarker analyses as exploratory, report estimates with confidence intervals, and avoid interpreting subgroup-specific significance tests without considering treatment-by-subgroup interaction. **Rationale:** exploratory analyses and multiple comparisons can produce unstable findings. **Assumption:** subgroup definitions and relevant measures are specified before analysis.
- **[Clarification Required]** Subgroups, interaction tests, biomarker variables, and any multiplicity-control strategy are not specified. These decisions are required to define the analyses and appropriately qualify their interpretation.

### 5.6 Harms

- **[Proposed]** Summarize collected adverse events by randomized arm, including counts and participant-level frequencies, and describe serious events separately if collected. **Rationale:** arm-specific summaries provide a transparent safety overview. **Assumption:** adverse-event data are collected and can be assigned to participants and treatment periods.
- **[Clarification Required]** Adverse-event definitions, collection periods, seriousness and severity criteria, and planned safety analyses are not supplied. These decisions matter for consistent safety reporting and interpretation.

### 5.7 Software and References

- **[Provided]** The October 2021 sample-size update used PROC POWER in SAS 9.4 and was based on the Lakatos formula.
- **[Clarification Required]** Statistical software and version for the final analyses are not specified. This information is needed for reproducibility.

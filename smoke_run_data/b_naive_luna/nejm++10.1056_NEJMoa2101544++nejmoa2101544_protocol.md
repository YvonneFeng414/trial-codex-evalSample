# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** ENSEMBLE (VAC31518COV3001) is a phase 3 study of Ad26.COV2.S, a recombinant replication-incompetent adenovirus type 26 vector encoding SARS-CoV-2 spike protein, to assess prevention of SARS-CoV-2-mediated COVID-19 in adults aged 18 years or older.

### 1.2 Objectives

- **[Provided]** The primary objective (P1) is to demonstrate the efficacy of Ad26.COV2.S versus placebo in preventing first molecularly confirmed moderate-to-severe/critical COVID-19 in SARS-CoV-2-seronegative adults, separately for onset at least Day 15 and at least Day 29.

- **[Provided]** The P1 outcome is first molecularly confirmed moderate-to-severe/critical COVID-19 with onset at least Day 15 and, separately, at least Day 29, comparing Ad26.COV2.S versus placebo.

- **[Provided]** The secondary/exploratory objective (S1) is to evaluate prevention of severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; burden of symptomatic disease; asymptomatic/undetected infection; and all SARS-CoV-2 infection.

- **[Provided]** S2 is to evaluate SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, unsolicited AEs, and immunogenicity.

- **[Provided]** S3 is exploratory and is to explore viral load, immune correlates, functional/molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.

- **[Clarification Required]** Operational definitions, assessment rules, and analysis windows are not supplied for several secondary and exploratory outcomes. These are needed to determine endpoint ascertainment and analysis populations consistently.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a randomized, double-blind, placebo-controlled phase 3 study in adults aged ≥18 years, with 1:1 allocation to Ad26.COV2.S or placebo.

- **[Provided]** Group 1 receives one Day-1 0.5-mL injection of Ad26.COV2.S at 5×10^10 viral particles, supplied at 1×10^11 vp/mL.

- **[Provided]** Group 2 receives one Day-1 0.5-mL injection of 0.9% sodium chloride placebo.

- **[Clarification Required]** The duration of blinded treatment, procedures for maintaining the blind, and any unblinding rules are not specified. These decisions matter for conduct and interpretation of efficacy and safety assessments.

### 2.2 Randomization

- **[Provided]** A central computer-generated randomization schedule is prepared before the study under sponsor supervision using randomly permuted blocks; no minimization is reported.

- **[Provided]** Randomization is stratified by vaccination unit (site/mobile unit), age (≥18 to <60 years; ≥60 years), and absence or presence of comorbidities associated or potentially associated with progression to severe COVID-19.

- **[Clarification Required]** Block sizes, allocation concealment procedures, and handling of any randomization-system failure are not specified. These details matter for implementation and auditability.

### 2.3 Sample Size

- **[Provided]** After Protocol Amendment 3, planned enrollment is approximately 40,000 participants, reduced from a previous maximum of approximately 60,000 based on observed/modelled incidence.

- **[Provided]** Sample-size calculations concern first molecularly confirmed moderate-to-severe/critical COVID-19 in per-protocol (PP) participants, separately for onset ≥Day 15 and ≥Day 29. The endpoint is time-to-first-event/incident case.

- **[Provided]** The assumed control-arm value is null VE 30%, the assumed treatment-arm VE is 60%, and the target is VE 60% versus a null lower bound of 30%.

- **[Provided]** The one-sided significance level is 2.5%. Planned power is approximately 90%; power is 86.22% with the truncated SPRT through 154 events at VE 60%.

- **[Provided]** The assumed test framework is a truncated sequential probability ratio test (SPRT) using a conditional exact binomial framework, beginning at the 20th event. The required total is 154 co-primary events.

- **[Provided]** A non-inferiority/equivalence margin is not applicable; the co-primary superiority hypotheses test VE >30%.

- **[Provided]** No numerical dropout/non-adherence inflation is reported; epidemiologic uncertainty and potential dropouts informed the maximum enrollment. A design effect/clustering adjustment is not applicable because this is an individually randomized trial.

- **[Provided]** Assumptions included 1.4% moderate/severe incidence for the first 3 months, a 50% reduction in month 4, a 62% reduction thereafter, and 10% seroprevalence. Later epidemiologic modeling supported reduction to approximately 40,000 participants.

- **[Provided]** Enrollment was intended to support a high probability of an efficacy signal within 8 months and a sufficient likelihood of five placebo severe cases.

- **[Provided]** gsDesign version 3.1.1 was used for SPRT boundary code; other sample-size software is not specified.

- **[Clarification Required]** The relationship between the 154 total co-primary events and the event count required for each timing-window test is not stated. This matters for interpreting the design target and analysis timing.

### 2.4 Hypothesis Framework

- **[Provided]** For each co-primary endpoint, the null hypothesis is H0: VE≤30% and the alternative is H1: VE>30%, tested at one-sided 2.5%.

- **[Provided]** Success requires both co-primary tests to succeed and, for each timing window, a severe/critical VE point estimate ≥50% with at least five placebo severe/critical events.

- **[Provided]** Conditional on primary success, confirmatory secondary tests use H0: VE≤0% versus H1: VE>0% under graphical multiple-testing control.

- **[Provided]** The graphical sequence evaluates BOD, medical intervention, all infection, and asymptomatic/undetected infection, subject to their endpoint/population windows.

- **[Provided]** Secondary alpha is based on a single-interim Pocock/Wang–Tsiatis Δ=.5 information fraction derived from Day-29 primary events (154 target). The medical-intervention rationale uses 23 events; all-infection testing requires at least 15,000 available Day-71 samples; asymptomatic testing requires all participants to have ≥6-month follow-up.

- **[Clarification Required]** The meaning of BOD, the exact graphical weights and alpha-recycling rules, and the endpoint/population windows for each secondary test are not specified. These decisions are necessary to implement the multiplicity procedure and identify which participants contribute to each test.

### 2.5 Statistical Interim Analyses

- **[Provided]** A signal before 8-week median follow-up triggers an analysis at that median-follow-up timepoint.

- **[Provided]** Secondary alpha is based on a single-interim Pocock/Wang–Tsiatis Δ=.5 information fraction derived from Day-29 primary events (154 target).

- **[Clarification Required]** The definition of an efficacy “signal,” the precise interim trigger and decision boundary, and whether the 8-week median-follow-up analysis is the specified secondary interim are not supplied. These matter for analysis timing, type I error control, and whether analyses can affect study conduct.

- **[Clarification Required]** No complete interim-analysis plan, including monitoring responsibilities, stopping rules, or alpha-spending details for the co-primary endpoints, is provided. These are needed to implement sequential testing reproducibly.

### 2.6 Timing of Analyses

- **[Provided]** The final analysis follows the last participant’s month-12 visit or earlier discontinuation. The end-of-study analysis follows all month-24 visits or earlier discontinuation.

- **[Provided]** eCOA symptom surveillance occurs at least twice weekly until the later of year 1 or the primary analysis, and then every 2 weeks. Symptomatic episodes trigger serial testing/procedures.

- **[Provided]** Immunogenicity Subset sampling occurs at baseline, Day 29, Day 71, month 6, year 1, month 18, and year 2.

- **[Provided]** Asymptomatic-infection serology occurs at baseline, Day 71, month 6, and year 1. The co-primary efficacy windows are Day 15 and Day 29.

- **[Clarification Required]** Data cutoff and database-lock requirements are not specified. These decisions matter for defining the data included in each analysis and ensuring consistent analysis timing.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** Each co-primary hypothesis is tested at one-sided 2.5%; confirmatory secondary hypotheses use the stated graphical multiple-testing control, conditional on primary success.

- **[Proposed]** Report effect estimates with confidence intervals alongside hypothesis-test results (rationale: estimates convey precision and magnitude as well as statistical significance; assumption: an interval method compatible with the sequential and multiplicity-adjusted testing will be selected before database lock).

- **[Clarification Required]** The confidence-interval method and confidence level, including adjustment for sequential testing and multiplicity, are not specified. This matters because nominal intervals may not have coverage consistent with the testing procedure.

### 3.2 Protocol Deviations

- **[Proposed]** Define major deviations and analysis-impacting deviations before treatment-code unblinding, document them by participant and treatment group, and summarize their frequency and reasons (rationale: prespecification reduces the risk of outcome-informed exclusions; assumption: deviations can be identified from study records).

- **[Clarification Required]** Criteria for classifying major deviations, and the review process and timing for those classifications, are not supplied. These decisions affect PP membership and interpretation of the primary analysis.

### 3.3 Analysis Populations

- **[Provided]** The sample-size calculation is based on PP participants.

- **[Clarification Required]** The PP population definition, including required vaccination, baseline serostatus, follow-up, and protocol-adherence conditions, is not specified. This matters because it is the population used for the stated sample-size calculation and primary objective.

- **[Proposed]** Use an intention-to-treat population consisting of all randomized participants, analyzed according to assigned group, for supportive efficacy analyses (rationale: this preserves randomized assignment and provides a complementary estimate; assumption: randomization and treatment assignment are recorded for all randomized participants).

- **[Proposed]** Use a safety population consisting of participants who receive study injection, analyzed according to treatment received (rationale: this aligns safety summaries with exposure; assumption: actual treatment received is available and can be determined).

- **[Clarification Required]** The intended primary and secondary analysis populations beyond the PP population used in sample-size calculations are not specified. This matters for the estimand, interpretation, and consistency of endpoint-specific results.

## 4. Trial Population

### 4.1 Screening Data

- **[Clarification Required]** Screening variables, screening-failure categories, and the screening disposition dataset are not specified. These are needed to describe participant flow and assess how the enrolled population relates to the eligible population.

- **[Proposed]** Summarize screened, eligible, randomized, and vaccinated participants, with reasons for non-enrollment where recorded (rationale: this provides a transparent account of participant disposition; assumption: these counts and reasons can be collected).

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria include adults aged ≥18 years who provide informed consent and can comply with study procedures; stable/well-controlled illness and stable medication dose for ≥12 weeks, where applicable; and verifiable identity/contactability and ability to complete eCOA questionnaires.

- **[Provided]** For participants of childbearing potential, protocol-compliant contraception is required from consent through 3 months after vaccination; hormonal contraception must have been initiated ≥28 days before vaccination. Highly sensitive urine pregnancy tests must be negative at screening and immediately before vaccination.

- **[Provided]** Participants must not donate blood or bone marrow through 3 months after vaccination.

- **[Provided]** Exclusion criteria include acute clinically significant illness or temperature ≥38.0°C within 24 hours; serious vaccine/excipient allergy or anaphylaxis; immunologically relevant autoimmune disease or immunodeficiency; chronic/recurrent systemic corticosteroids; antineoplastic/immunomodulating therapy or radiotherapy; immunoglobulin within 3 months or blood products within 4 months; live vaccine within 28 days or non-live vaccine within 14 days; and prior coronavirus vaccine.

- **[Provided]** Further exclusions include recent investigational drug/device/vaccine; pregnancy, breastfeeding, or pregnancy plan; a condition compromising safety or assessments; contraindication to IM injection or blood draw; uncontrolled HIV; serious psychiatric illness or substance abuse; and inability to communicate or adhere.

- **[Provided]** Exclusions also include stage-specific high-risk comorbidities, recent malignancy, acute polyneuropathy, surgery, or active hepatitis. Ocular/topical/inhaled steroids and stable non-immunomodulator treatment may be permitted; smoking is not a comorbidity.

- **[Clarification Required]** Exact definitions and look-back periods for “recent” investigational products, malignancy, surgery, and the other summarized exclusions, as well as the stage-specific high-risk comorbidity criteria, are not supplied. These are needed to apply eligibility consistently.

### 4.3 Recruitment

- **[Clarification Required]** Recruitment locations, recruitment period, recruitment procedures, and enrollment targets by site or vaccination unit are not specified. These decisions matter for operational planning and interpretation of the enrolled population.

### 4.4 Withdrawal and Follow-up

- **[Provided]** The stated final analysis follows the last participant’s month-12 visit or earlier discontinuation; the end-of-study analysis follows all month-24 visits or earlier discontinuation.

- **[Provided]** Symptom surveillance is conducted at least twice weekly by eCOA until the later of year 1 or primary analysis, then every 2 weeks; symptomatic episodes trigger serial testing/procedures.

- **[Clarification Required]** Withdrawal categories, reasons, continued follow-up after intervention discontinuation, and procedures for obtaining outcomes after withdrawal are not specified. These decisions affect follow-up completeness and handling of incomplete outcome data.

### 4.5 Baseline Characteristics

- **[Provided]** Randomization is stratified by vaccination unit (site/mobile unit), age (≥18 to <60; ≥60 years), and absence/presence of comorbidities associated or potentially associated with progression to severe COVID-19. Baseline serostatus defines the primary objective population as SARS-CoV-2-seronegative adults.

- **[Proposed]** Summarize available baseline characteristics by randomized group, including the randomization strata and baseline serostatus (rationale: these describe the randomized groups and the primary objective population; assumption: these variables are collected and available for analysis).

- **[Clarification Required]** The complete set of baseline variables and their collection methods are not specified. This matters for interpreting comparability and supporting any adjusted or subgroup analyses.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The co-primary outcomes are first molecularly confirmed moderate-to-severe/critical COVID-19 with onset at least Day 15 and, separately, at least Day 29, in SARS-CoV-2-seronegative adults, comparing Ad26.COV2.S with placebo.

- **[Provided]** Co-primary success requires both tests to reject H0: VE≤30% in favor of H1: VE>30%, with one-sided 2.5% significance for each, and, for each timing window, severe/critical VE point estimate ≥50% with at least five placebo severe/critical events.

- **[Clarification Required]** The full case definition for molecular confirmation and moderate-to-severe/critical COVID-19, event adjudication procedures, onset-date rules, and handling of recurrent episodes are not specified. These decisions determine whether an event qualifies for the primary endpoint.

### 5.2 Secondary Outcomes

- **[Provided]** S1 outcomes are severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; burden of symptomatic disease; asymptomatic/undetected infection; and all SARS-CoV-2 infection.

- **[Provided]** S2 outcomes are SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, unsolicited AEs, and immunogenicity.

- **[Provided]** S3 exploratory outcomes are viral load, immune correlates, functional/molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.

- **[Clarification Required]** Endpoint definitions, assessment windows, analysis populations, and methods of ascertainment for the secondary and exploratory outcomes are not supplied in full. These decisions matter for defining estimands and interpreting comparisons.

### 5.3 Analysis Methods

- **[Provided]** The sample-size framework specifies a truncated SPRT using a conditional exact binomial framework, beginning at the 20th event; the sample-size calculation requires 154 total co-primary events.

- **[Proposed]** Use the truncated conditional exact binomial SPRT for the co-primary hypothesis tests if confirmed as the intended final inferential method (rationale: this is the test framework stated for sample-size planning; assumption: the planning method is intended to govern primary analysis as well). Apply the specified null VE of 30%, one-sided 2.5% level, and both co-primary success requirements.

- **[Clarification Required]** The SPRT boundaries, event-allocation statistic, truncation implementation, and method for evaluating each timing window are not supplied. These are required to reproduce the primary test and determine a definitive result.

- **[Proposed]** Provide descriptive time-to-event summaries and treatment-effect estimates for each co-primary endpoint, with the estimation method prespecified before unblinding (rationale: descriptive estimates complement the sequential hypothesis test; assumption: event and censoring dates are sufficiently complete for the chosen method).

- **[Clarification Required]** The time origin, censoring rules, and method for estimating VE are not specified. These decisions affect risk sets, effect estimates, and their interpretation.

- **[Provided]** Confirmatory secondary testing is conditional on primary success and follows the stated graphical sequence: BOD, medical intervention, all infection, and asymptomatic/undetected infection, subject to endpoint/population windows. The medical-intervention rationale uses 23 events; all-infection testing requires at least 15,000 available Day-71 samples; asymptomatic testing requires all participants to have ≥6-month follow-up.

- **[Proposed]** Summarize other secondary and exploratory outcomes descriptively unless they are included in the confirmatory graphical procedure (rationale: this distinguishes confirmatory from exploratory evidence; assumption: no additional confirmatory testing scheme is intended).

- **[Clarification Required]** Statistical methods for viral RNA load, immunogenicity, symptom burden, frailty, transcriptomics, and other non-confirmatory outcomes are not specified. Their measurement scales, analysis populations, and multiplicity approach are needed to select suitable methods.

### 5.4 Missing Data

- **[Clarification Required]** Missing-data assumptions and procedures for missing endpoint assessments, serology, eCOA reports, and follow-up are not specified. This matters because missingness can affect case ascertainment, analysis populations, and the validity of efficacy and safety estimates.

- **[Proposed]** Report the extent and reasons for missing data by treatment group and outcome, and conduct sensitivity analyses for missing primary-outcome information if the primary analysis depends on incomplete follow-up (rationale: transparent reporting and sensitivity analysis assess the potential impact of missingness; assumption: missingness and its reasons can be characterized).

### 5.5 Additional Analyses

- **[Provided]** Baseline age and absence/presence of comorbidities associated or potentially associated with progression to severe COVID-19 are randomization stratification factors. The primary objective is in SARS-CoV-2-seronegative adults; S1 also includes outcomes regardless of baseline serostatus.

- **[Proposed]** Report treatment-effect estimates by prespecified randomization strata and baseline serostatus as supportive analyses, with interaction assessments treated as exploratory unless otherwise specified (rationale: these factors are part of randomization or define stated outcome populations; assumption: subgroup sample sizes and endpoint data permit estimation).

- **[Clarification Required]** No additional subgroup list, subgroup hypotheses, or interaction-testing rules are specified. These are needed to distinguish prespecified analyses from post hoc exploration.

### 5.6 Harms

- **[Provided]** Safety outcomes include SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, and unsolicited AEs.

- **[Proposed]** Summarize harms by treatment group using participant counts and proportions, with event counts and severity or relatedness summaries where those attributes are collected (rationale: descriptive summaries present the frequency and nature of observed harms; assumption: these safety attributes are captured in study records).

- **[Clarification Required]** Definitions, collection windows, severity grading, relatedness assessment, and coding procedures for the safety outcomes are not specified. These decisions are necessary for consistent safety tabulation and interpretation.

### 5.7 Software and References

- **[Provided]** gsDesign version 3.1.1 was used for SPRT boundary code; other sample-size software is not specified.

- **[Clarification Required]** Statistical analysis software and version(s), and any additional analysis-program validation requirements, are not specified. These details matter for reproducibility.

- **[Clarification Required]** No references are supplied, and none are required to state the study facts in this framework. Any study-specific reference list or citation requirement would need to be decided separately.

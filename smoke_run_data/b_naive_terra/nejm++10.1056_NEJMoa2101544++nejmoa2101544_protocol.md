# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** This phase 3 study evaluates prevention of SARS-CoV-2-mediated COVID-19 in adults aged 18 years or older using Ad26.COV2.S, a recombinant replication-incompetent adenovirus type 26 vector encoding SARS-CoV-2 spike protein.

### 1.2 Objectives

**[Provided]** The primary objective is to demonstrate efficacy versus placebo against first molecularly confirmed moderate-to-severe/critical COVID-19 in baseline-seronegative adults, separately for onset from Day 15 and from Day 29.

**[Provided]** Secondary objectives address severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; burden of symptomatic disease (BOD); asymptomatic/undetected infection; and all SARS-CoV-2 infection.

**[Provided]** Secondary safety and immunogenicity objectives address serious adverse events (SAEs), medically attended adverse events (MAAEs), MAAEs leading to discontinuation, reactogenicity, unsolicited adverse events (AEs), and immunogenicity.

**[Provided]** Exploratory objectives address viral load, immune correlates, functional and molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a randomized, double-blind, placebo-controlled phase 3 study with 1:1 allocation. Each participant receives one 0.5-mL Day-1 injection: Ad26.COV2.S at 5×10^10 viral particles, supplied at 1×10^11 viral particles/mL, or 0.9% sodium chloride placebo.

**[Clarification Required]** Blinding procedures, emergency unblinding, and procedures for maintaining allocation concealment after assignment are unspecified; these are needed to protect and document trial integrity.

### 2.2 Randomization

**[Provided]** A central computer-generated schedule is prepared before the study under sponsor supervision using randomly permuted blocks. No minimization is reported.

**[Provided]** Stratification factors are vaccination unit (site or mobile unit), age (≥18 to <60 years; ≥60 years), and absence or presence of comorbidities associated or potentially associated with progression to severe COVID-19.

### 2.3 Sample Size

**[Provided]** After Protocol Amendment 3, planned enrollment was approximately 40,000, reduced from a previous maximum of approximately 60,000 based on observed and modeled incidence. Epidemiologic uncertainty and potential dropouts informed maximum enrollment; no numerical dropout inflation was reported.

**[Provided]** The calculation concerns first molecularly confirmed moderate-to-severe/critical COVID-19 in per-protocol (PP) participants, separately for onset from Day 15 and Day 29. It uses a time-to-first-event/incident-case endpoint, null vaccine efficacy (VE) of 30%, assumed VE of 60%, one-sided 2.5% significance, and 154 total co-primary events.

**[Provided]** Approximately 90% power was planned; power through 154 events is 86.22% at VE 60% with the truncated sequential probability ratio test (SPRT). The exact conditional binomial SPRT begins at the 20th event. No continuous-outcome variability parameter was reported.

**[Provided]** Incidence assumptions were 1.4% moderate/severe incidence during the first three months, a 50% reduction in month 4, a 62% reduction thereafter, and 10% seroprevalence. Later epidemiologic modeling supported enrollment of approximately 40,000.

**[Provided]** Enrollment was intended to support a high probability of an efficacy signal within eight months and a sufficient likelihood of five placebo severe cases. Clustering is not applicable to this individually randomized trial; no non-inferiority or equivalence margin applies.

**[Clarification Required]** Whether the 154-event target and sequential boundaries apply independently to each co-primary window, and how overlapping events count, must be specified to implement monitoring.

### 2.4 Hypothesis Framework

**[Provided]** For each co-primary endpoint, H0: VE≤30% is tested against H1: VE>30% at one-sided 2.5%.

**[Provided]** Overall primary success requires both co-primary tests to succeed and, for each timing window, a severe/critical VE point estimate ≥50% with at least five placebo severe/critical events.

**[Provided]** Conditional on primary success, confirmatory secondary hypotheses test H0: VE≤0% versus H1: VE>0% under graphical multiple-testing control. The graphical sequence evaluates BOD, medical intervention, all infection, and asymptomatic/undetected infection, subject to their endpoint and population windows.

**[Provided]** Secondary alpha is based on a single-interim Pocock/Wang–Tsiatis Δ=.5 information fraction derived from Day-29 primary events against a 154-event target. The medical-intervention rationale uses 23 events; all-infection testing requires at least 15,000 available Day-71 samples; asymptomatic testing requires all participants to have ≥6-month follow-up.

**[Clarification Required]** The graph’s initial alpha allocations, transfer weights, endpoint/population windows, interim timing, numerical boundaries, and handling of unmet information requirements are unspecified. These decisions are necessary for reproducible confirmatory testing and error control.

### 2.5 Statistical Interim Analyses

**[Provided]** The co-primary monitoring framework is a truncated SPRT beginning at the 20th event and continuing through 154 events. A signal before eight-week median follow-up triggers an analysis at that median-follow-up timepoint.

**[Clarification Required]** The numerical SPRT boundaries, event-check schedule, definition of a signal, stopping rules, monitoring responsibilities, and treatment of findings before the eight-week analysis are unspecified; these govern interim decisions and preservation of trial integrity.

### 2.6 Timing of Analyses

**[Provided]** Final analysis follows the last participant’s month-12 visit or earlier discontinuation. End-of-study analysis follows all month-24 visits or earlier discontinuation.

**[Provided]** Electronic clinical outcome assessment (eCOA) symptom surveillance occurs at least twice weekly until the later of year 1 or primary analysis, then every two weeks. Symptomatic episodes trigger serial testing and procedures.

**[Provided]** Immunogenicity Subset sampling occurs at baseline, Day 29, Day 71, month 6, year 1, month 18, and year 2. Asymptomatic-infection serology occurs at baseline, Day 71, month 6, and year 1.

**[Clarification Required]** Primary-analysis timing beyond the specified event monitoring, data cutoffs, and database-lock requirements are unspecified; these determine which observations enter each analysis.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** Each co-primary test uses one-sided 2.5% significance. Confirmatory secondary testing is conditional on primary success and governed by the specified graphical framework.

**[Proposed]** Report effect estimates with confidence intervals, distinguishing confirmatory from descriptive results. Rationale: intervals communicate precision; this assumes the interval method is compatible with the applicable sequential design.

**[Clarification Required]** Confidence levels, sequentially adjusted interval methods, and numerical secondary critical values are unspecified; these affect interpretation and consistency with testing.

### 3.2 Protocol Deviations

**[Proposed]** Document deviations and classify important deviations before unblinding. Rationale: consistent classification supports population definitions; this assumes deviation review can be performed blinded.

**[Clarification Required]** Deviation categories and their effects on PP eligibility are unspecified; they can change the primary analysis population.

### 3.3 Analysis Populations

**[Provided]** The sample-size calculation uses PP participants, and the primary objective concerns baseline-seronegative adults.

**[Proposed]** Summarize randomized participants by assigned group and safety outcomes by treatment received. Rationale: these provide complementary allocation and exposure summaries; this assumes treatment receipt is recorded.

**[Clarification Required]** Exact PP, efficacy, safety, subset, and baseline-serostatus definitions are unspecified, including handling of missing baseline tests and events before each efficacy window. These determine denominators and eligibility for analyses.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Summarize numbers screened, eligible, randomized, and not randomized, with available reasons. Rationale: this describes participant flow; this assumes screening disposition is captured.

### 4.2 Eligibility Criteria Summary

**[Provided]** Eligible participants are adults aged ≥18 years who consent, can comply with procedures, have verifiable identity and contactability, and can complete eCOA questionnaires. Illness and medication dose must be stable or well controlled for ≥12 weeks where applicable.

**[Provided]** Participants of childbearing potential must use protocol-compliant contraception from consent through three months after vaccination; hormonal contraception must start ≥28 days before vaccination. Highly sensitive urine pregnancy tests must be negative at screening and immediately before vaccination. Blood and bone-marrow donation is prohibited through three months after vaccination.

**[Provided]** Exclusions include acute clinically significant illness or temperature ≥38.0°C within 24 hours; serious vaccine or excipient allergy/anaphylaxis; immunologically relevant autoimmune disease or immunodeficiency; chronic or recurrent systemic corticosteroids; antineoplastic or immunomodulating therapy or radiotherapy; immunoglobulin within three months or blood products within four months; live vaccine within 28 days or non-live vaccine within 14 days; prior coronavirus vaccine; and recent investigational drug, device, or vaccine.

**[Provided]** Other exclusions include pregnancy, breastfeeding or pregnancy plan; a condition compromising safety or assessments; contraindication to intramuscular injection or blood draw; uncontrolled HIV; serious psychiatric illness or substance abuse; inability to communicate or adhere; and stage-specific high-risk comorbidities, recent malignancy, acute polyneuropathy, surgery, or active hepatitis.

**[Provided]** Ocular, topical, and inhaled steroids and stable non-immunomodulator treatment may be permitted. Smoking is not a comorbidity.

**[Clarification Required]** Stage-specific restrictions and the definitions or lookback periods for criteria described as recent, high-risk, stable, or immunologically relevant are unspecified; consistent eligibility adjudication requires them.

### 4.3 Recruitment

**[Provided]** Planned enrollment after Amendment 3 was approximately 40,000 participants.

**[Clarification Required]** Recruitment locations, dates, and methods are unspecified; they are needed for operational planning and assessment of generalizability.

### 4.4 Withdrawal and Follow-up

**[Provided]** Participants may discontinue before the month-12 final-analysis visit or month-24 end-of-study visit.

**[Proposed]** Record withdrawal dates, reasons, and whether follow-up data remain available. Rationale: these support participant-flow and missing-data assessment; this assumes the information can be collected.

**[Clarification Required]** Withdrawal procedures, permitted continued follow-up, and censoring rules are unspecified; they affect observation time and endpoint ascertainment.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize baseline characteristics by randomized group, including age, comorbidity status, and SARS-CoV-2 serostatus. Rationale: these characterize groups and key stratification or eligibility variables; this assumes the measurements are available.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The co-primary outcomes are first molecularly confirmed moderate-to-severe/critical COVID-19 with onset from Day 15 and, separately, from Day 29, comparing Ad26.COV2.S with placebo in baseline-seronegative adults.

**[Clarification Required]** Molecular confirmation, severity classification, onset-date rules, and adjudication procedures are unspecified; these are necessary for consistent event identification.

### 5.2 Secondary Outcomes

**[Provided]** Secondary efficacy outcomes comprise severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; BOD; asymptomatic/undetected infection; and all SARS-CoV-2 infection.

**[Provided]** Secondary safety and immunogenicity outcomes and exploratory outcomes are those listed in Section 1.2.

**[Clarification Required]** Endpoint definitions, measurement scales, assessment windows, populations, and ascertainment rules for secondary and exploratory outcomes are unspecified; these are needed to calculate and interpret their results.

### 5.3 Analysis Methods

**[Provided]** The sample-size test uses a truncated SPRT in an exact conditional binomial framework. Primary success also requires the severe/critical criteria in Section 2.4.

**[Proposed]** Report event counts, follow-up, VE estimates, and confidence intervals by efficacy window and group. Rationale: these make the comparison interpretable; this assumes event dates and observation time are available.

**[Clarification Required]** The VE estimator, exact conditioning and exposure adjustment, sequential implementation, censoring, and method for the severe/critical VE estimate are unspecified; these can alter estimates and decisions.

**[Proposed]** Summarize continuous, categorical, and time-to-event secondary outcomes using measures appropriate to their scales, and label nongated analyses descriptive. Rationale: this avoids implying unsupported confirmatory conclusions; this assumes endpoint definitions will be finalized.

### 5.4 Missing Data

**[Proposed]** Summarize missing baseline tests, endpoint assessments, and follow-up by group and reason where available. Rationale: missingness may affect comparability and ascertainment; this assumes missingness and reasons are recorded.

**[Clarification Required]** Primary and secondary missing-data rules, including missing serostatus, unconfirmed illness, incomplete follow-up, and sensitivity analyses, are unspecified; these affect estimands and potential bias.

### 5.5 Additional Analyses

**[Proposed]** Explore efficacy by age and comorbidity strata, reporting estimates and uncertainty without treating these analyses as confirmatory. Rationale: these are randomization strata; this assumes sufficient events are available.

**[Clarification Required]** Methods and populations for immune correlates, antibody characteristics, transcriptomics, symptoms, frailty, and clinical severity are unspecified; their scientific interpretation depends on these choices.

### 5.6 Harms

**[Provided]** Safety objectives include SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, and unsolicited AEs.

**[Proposed]** Summarize participants with each safety event by treatment received and provide event severity and relationship where recorded. Rationale: this supports comparison of harms; this assumes safety coding and attribution are available.

**[Clarification Required]** Safety collection periods, reactogenicity definitions, severity grading, coding conventions, and reporting procedures are unspecified; these determine comparability and completeness of harm summaries.

### 5.7 Software and References

**[Provided]** gsDesign version 3.1.1 was used for SPRT boundary code; other sample-size software was not specified.

**[Clarification Required]** Software and versions for the remaining analyses are unspecified; recording them is necessary for reproducibility.

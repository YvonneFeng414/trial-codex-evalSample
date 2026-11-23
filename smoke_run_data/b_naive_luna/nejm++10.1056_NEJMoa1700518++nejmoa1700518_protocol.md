# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** After initial anticoagulation for DVT or PE, recurrent VTE remains clinically important. Long-term VKA therapy is effective but carries bleeding, monitoring, and dose-adjustment burden; ASA has modest recurrence-prevention efficacy. This study evaluates whether reduced-dose rivaroxaban can maintain efficacy while improving safety, using ASA as comparator.

### 1.2 Objectives

- **[Provided]** **Primary objective (P1):** Evaluate the superiority of rivaroxaban 10 mg and 20 mg versus ASA 100 mg for fatal or nonfatal symptomatic recurrent VTE. The primary outcome is fatal or nonfatal symptomatic recurrent VTE, comparing each rivaroxaban dose versus ASA 100 mg.
- **[Provided]** **Secondary objective (S1):** Evaluate the superiority of each rivaroxaban dose versus ASA for fatal/nonfatal symptomatic recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism. The outcome is this composite, comparing each rivaroxaban dose versus ASA.
- **[Provided]** **Principal safety objective (S2):** Document the incidence of major bleeding.
- **[Provided]** **Secondary safety objective (S3):** Document the incidence of CRNM bleeding.
- **[Provided]** **Additional study objectives:** S4 (a), evaluate the composite of nonfatal symptomatic VTE and all-cause mortality; S5 (b), evaluate the composite of major bleeding and recurrent VTE; and S6 (c), evaluate the composite of major bleeding, recurrent VTE, MI, ischemic stroke, and systemic non-CNS embolism. These objectives are not labeled exploratory in the Evaluation Input.
- **[Provided]** Exploratory analyses describe composites of the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations, and net clinical benefit.
- **[Clarification Required]** Definitions of recurrent VTE, symptomatic venous thrombosis in other locations, major bleeding, CRNM bleeding, and net clinical benefit are not supplied. These definitions matter for consistent event adjudication and analysis.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a Phase III, multicenter, randomized, double-blind, double-dummy, active-comparator, event-driven trial. All efficacy and safety events are adjudicated centrally, and final analyses use adjudication results.
- **[Provided]** Allocation is 1:1:1 to oral once-daily treatment with food: rivaroxaban 10 mg, rivaroxaban 20 mg, or ASA 100 mg. Double-dummy supplies comprise one rivaroxaban-or-placebo tablet and one ASA-or-placebo tablet daily.
- **[Provided]** Nominal treatment duration is 12 months, although final randomized patients may receive only 6 months. Six months’ medication is initially supplied; IxRS determines at visit 4 whether a further six months is supplied. Last randomized patients receive no second supply.
- **[Provided]** Treatment may restart after temporary interruption if total treatment does not exceed 12 months. The first dose is given at least 24 hours after previous VTE treatment.
- **[Provided]** For patients receiving VKA, INR >3.0 delays randomization; INR 2.5–3.0 permits randomization but delays first intake until the next day; INR <2.5 permits dosing.
- **[Provided]** A missed dose may be made up only on the same day; double dosing is not allowed.
- **[Clarification Required]** The detailed treatment-emergency, permanent-discontinuation, and dose-interruption procedures are not specified. These matter for consistent treatment management and exposure classification.

### 2.2 Randomization

- **[Provided]** Randomization is performed centrally through an interactive voice/web response system (IxRS), which assigns a unique randomization number identifying treatment allocation. The investigator provides study-center identification and the DVT/PE presentation.
- **[Provided]** Randomization is stratified by country and investigator-reported index event: DVT only versus PE with or without DVT.
- **[Clarification Required]** Minimization or blocking procedures are not specified. This matters for documenting the allocation procedure and any relevant analysis considerations.

### 2.3 Sample Size

- **[Provided]** The planned sample size is approximately 950 patients per arm (2,850 total), subject to adjustment using observed overall primary-event incidence.
- **[Provided]** The sample-size calculation outcome is the confirmed primary efficacy outcome of fatal or nonfatal symptomatic recurrent VTE, analyzed as a time-to-first-event survival outcome. At least 80 confirmed primary efficacy outcomes are required.
- **[Provided]** The ASA control event rate is assumed to be 5% per year, modeled exponentially. The treatment-effect assumptions are HR 0.30 for rivaroxaban 20 mg versus ASA and HR 0.40 for rivaroxaban 10 mg versus ASA.
- **[Provided]** The design uses two-sided alpha 0.05 for sequential superiority tests and 90% power. A 10,000-trial simulation estimated joint Cox-regression power of 0.901.
- **[Provided]** The assumed test is a stratified Cox proportional-hazards superiority analysis with the upper 95% CI bound below 1; stratified log-rank testing is supportive. The design is for superiority; a non-inferiority/equivalence margin is not applicable.
- **[Provided]** Simulations used exponential event, discontinuation, and withdrawal processes. The annual treatment-discontinuation assumption is 10%, and the annual loss-to-follow-up/withdrawn-consent assumption is 1%. Last subjects receive 6 months’ treatment. After simulated discontinuation, simulated event time uses inferior-control treatment; losses before the simulated event are censored.
- **[Provided]** The 20-mg effect assumption derives from an adjusted indirect comparison of EINSTEIN Extension and pooled ASA evidence: estimated HR 0.264 (95% CI 0.12–0.59), with HR 0.30 selected conservatively. The 10-mg assumption reflects orthopedic rivaroxaban and apixaban extended-treatment evidence; HR 0.40, a 60% reduction, was set versus an expected HR 0.30 from the reduced-dose rationale.
- **[Provided]** The blinded pooled sample-size projection uses observed primary-event incidence and adjusts enrollment. It iterates total N until the probability of at least 80 total events is at least 0.50, with alternatives such as a probability of about 0.80 also presented.
- **[Provided]** The sample-size calculation used a SAS Macro by Shih and three-arm simulations. The simulations ran 10,000 trials, applied administrative censoring at one year/end of trial, selected trials/observation time reaching the event target, and fit Cox and log-rank tests. Joint power is defined as both the 20-mg/ASA and 10-mg/ASA HR 95% CI upper bounds being ≤1; estimated joint power was 0.901.
- **[Provided]** A separate variability parameter is not specified. A design effect/clustering adjustment is not applicable because the trial is individually randomized and non-clustered.
- **[Clarification Required]** The maximum enrollment, permitted adjustment range, and operational timing of blinded sample-size projections are not specified. These matter for implementing the event-driven adjustment without ambiguity.

### 2.4 Hypothesis Framework

- **[Provided]** A fixed sequence controls familywise error: first test H0: HR(20 mg/ASA) = 1 versus two-sided H1: HR ≠ 1; only if significant, test H0: HR(10 mg/ASA) = 1 versus two-sided H1: HR ≠ 1. Each test is two-sided at 0.05.
- **[Provided]** Rivaroxaban 20 mg is superior if its HR 95% CI upper bound is <1. Rivaroxaban 10 mg is superior only if 20 mg is superior and the 10-mg HR 95% CI upper bound is <1.
- **[Derived]** If the 20-mg comparison is not significant, the 10-mg comparison is not tested as a confirmatory test under the stated fixed sequence.

### 2.5 Statistical Interim Analyses

- **[Provided]** A blinded pooled projection based on observed primary-event incidence is used to adjust enrollment as described in Section 2.3.
- **[Clarification Required]** Whether any unblinded interim efficacy or futility analysis is planned is not specified. This matters for alpha control, trial conduct, and access to treatment-comparison results.

### 2.6 Timing of Analyses

- **[Provided]** SAP revisions are issued before database lock. Final analyses use adjudicated outcomes through each patient’s individual intended treatment limit.
- **[Provided]** Standard intended treatment limits are day 353, the visit day if it falls on days 353–367, or day 367; defined administrative shortening rules also apply.
- **[Provided]** Assessments occur at baseline, Day 1, Day 30±7, Day 90±7, Day 180±7, Day 270±7, Day 360±7, and a 30±7-day post-treatment observation visit. Potential outcomes and adverse events are elicited at all contacts.
- **[Provided]** Visit 7 may be by telephone or clinic and occurs early, 30±7 days after stopping, after premature discontinuation. Other visits continue after premature treatment stop unless participation is refused. Investigators may arrange additional visits.
- **[Clarification Required]** The exact database-lock date and the detailed administrative shortening rules are not supplied. These matter for reproducibility of the analysis cutoff and event-at-risk period.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The sequential superiority tests use two-sided alpha 0.05. The stated superiority decision rule is an HR 95% CI upper bound <1 for each comparison, subject to the fixed sequence.
- **[Proposed]** Report treatment-effect estimates with 95% confidence intervals and corresponding two-sided p-values for the primary comparisons. Rationale: this presents effect magnitude and uncertainty alongside the prespecified decision rule. Assumption: the SAP will use a confidence-interval method consistent with the specified stratified Cox model.
- **[Clarification Required]** Multiplicity control and inferential status for outcomes other than the sequential primary comparisons are not specified. This matters for interpretation of secondary and additional outcome p-values.

### 3.2 Protocol Deviations

- **[Proposed]** Document deviations by type and assess their potential effect on eligibility, treatment exposure, follow-up, and outcome ascertainment before database lock. Rationale: transparent deviation assessment supports interpretable analysis populations. Assumption: deviation review can be conducted without access to unblinded treatment comparisons.
- **[Proposed]** Retain randomized participants in the primary analysis according to randomized assignment, irrespective of treatment discontinuation or protocol deviations. Rationale: this preserves the randomized comparison. Assumption: a randomized-assignment primary analysis is acceptable for the primary estimand.
- **[Clarification Required]** Criteria for major deviations, exclusions from any per-protocol analysis, and the timing and governance of deviation review are not supplied. These matter for reproducibility and for defining any supportive population.

### 3.3 Analysis Populations

- **[Proposed]** Use all randomized participants in their randomized groups for the primary efficacy analysis. Rationale: this preserves randomized assignment. Assumption: all randomized participants can be included in the primary analysis regardless of treatment received.
- **[Proposed]** Define a safety population as randomized participants who receive at least one dose, analyzed according to treatment received. Rationale: safety summaries should reflect actual exposure. Assumption: exposure and treatment received can be reliably established.
- **[Proposed]** Use a per-protocol population only as a supportive analysis population, with membership rules prespecified before database lock. Rationale: this can assess robustness without replacing the randomized primary comparison. Assumption: deviation criteria can be finalized before treatment comparisons are unblinded.
- **[Clarification Required]** The study-specific definitions of the efficacy, safety, and per-protocol populations are not supplied. These matter because population membership can change the analysis set and interpretation.

## 4. Trial Population

### 4.1 Screening Data

- **[Proposed]** Summarize screened, eligible, randomized, and non-randomized participants, including reasons for screen failure when recorded. Rationale: this describes participant flow and selection. Assumption: screening disposition and reasons are collected.
- **[Clarification Required]** The screening variables and required disposition categories are not specified. These matter for the content and completeness of screening summaries.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria are confirmed symptomatic DVT and/or PE; receipt of 6–12 months of anticoagulation without an interruption longer than 1 week; and written consent.
- **[Provided]** Exclusion criteria are: (1) being below the country-specific legal lower age limit; (2) indication for therapeutic-dose anticoagulants; (3) hypersensitivity to investigational or comparator therapy; (4) any contraindication in local investigational/comparator labeling; (5) indication for antiplatelet therapy or conventional NSAID; (6) hepatic disease with coagulopathy and clinically relevant bleeding risk; (7) calculated CrCl <30 mL/min; (8) active bleeding or anticoagulant-contraindicating high bleeding risk; (9) life expectancy <6 months; (10) systemic strong dual CYP3A4/P-gp inhibitors, including HIV protease inhibitors, ketoconazole, itraconazole, voriconazole, or posaconazole; (11) childbearing potential without proper contraception, pregnancy, or breastfeeding; and (12) investigational drug/device study participation within 30 days before randomization.
- **[Clarification Required]** The calculation method and timing for CrCl, and the operational definitions of high bleeding risk, proper contraception, and childbearing potential, are not supplied. These matter for consistent eligibility decisions.

### 4.3 Recruitment

- **[Provided]** The study is multicenter, and randomization stratification includes country and investigator-reported index event.
- **[Clarification Required]** Recruitment countries, sites, recruitment period, and recruitment procedures are not supplied. These matter for describing the study setting and participant accrual.

### 4.4 Withdrawal and Follow-up

- **[Provided]** Visit 7 may be conducted by telephone or clinic and occurs 30±7 days after stopping treatment following premature discontinuation. Other visits continue after premature treatment stop unless participation is refused; investigators may arrange additional visits.
- **[Provided]** Potential outcomes and adverse events are elicited at all contacts, and final analyses use adjudicated outcomes through each patient’s individual intended treatment limit.
- **[Clarification Required]** Withdrawal categories and rules for continuing outcome follow-up after treatment discontinuation or withdrawal of treatment consent are not fully specified. These matter for participant conduct and event ascertainment.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize baseline characteristics by randomized treatment group using descriptive statistics appropriate to the recorded variable type. Rationale: this characterizes the randomized groups without relying on significance tests for baseline balance. Assumption: baseline data are collected and the summary variables are prespecified in the SAP.
- **[Clarification Required]** The baseline variables to be collected and summarized are not supplied. This matters for the content of baseline tables and any planned adjusted or subgroup analyses.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary outcome is fatal or nonfatal symptomatic recurrent VTE, comparing rivaroxaban 10 mg versus ASA 100 mg and rivaroxaban 20 mg versus ASA 100 mg.
- **[Provided]** The primary outcome for the sample-size calculation is confirmed fatal or nonfatal symptomatic recurrent VTE, analyzed as time to first event.
- **[Clarification Required]** The specific event components, diagnostic criteria, and event-onset dating rules for the primary outcome are not supplied. These matter for endpoint consistency and time-to-event analysis.

### 5.2 Secondary Outcomes

- **[Provided]** The secondary efficacy outcome (S1) is fatal/nonfatal symptomatic recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism, comparing each rivaroxaban dose versus ASA.
- **[Provided]** The principal safety outcome (S2) is incidence of major bleeding; the secondary safety outcome (S3) is incidence of CRNM bleeding.
- **[Provided]** Additional outcomes are S4 (a), nonfatal symptomatic VTE and all-cause mortality; S5 (b), major bleeding and recurrent VTE; and S6 (c), major bleeding, recurrent VTE, MI, ischemic stroke, and systemic non-CNS embolism.
- **[Clarification Required]** The event-counting rules and time windows for S1–S6, including how recurrent events and components occurring on the same date are handled, are not supplied. These matter for endpoint derivation and analysis.

### 5.3 Analysis Methods

- **[Proposed]** Analyze the primary time-to-first-event outcome with a Cox proportional-hazards model stratified by country and investigator-reported index event, and estimate each rivaroxaban-versus-ASA HR with a 95% CI. Rationale: this aligns with the stated sample-size test and randomization strata. Assumption: the prespecified stratified Cox model is appropriate for the final primary analysis.
- **[Provided]** The fixed-sequence comparison tests 20 mg versus ASA first and, only if significant, 10 mg versus ASA; stratified log-rank testing is supportive.
- **[Proposed]** For S1 and S4–S6, report treatment-group estimates and confidence intervals using time-to-first-event analyses if those outcomes are defined as time to first composite event. Rationale: this gives a consistent descriptive approach for composite outcomes. Assumption: time to first occurrence is the intended analysis for these outcomes.
- **[Proposed]** Summarize S2 and S3 by randomized group as participant incidence, with descriptive confidence intervals. Rationale: this directly describes incidence as stated in the objectives. Assumption: the principal summary counts participants with at least one event; recurrent-event summaries may be added if prespecified.
- **[Clarification Required]** The analysis methods for S1–S6, including whether they are confirmatory or descriptive and how multiplicity is handled, are not specified. These matter for interpreting treatment comparisons beyond the primary endpoint.
- **[Clarification Required]** The chosen estimand, censoring rules for the primary time-to-event analysis, and assessment of proportional hazards are not specified. These matter for interpreting the HR and defining participant follow-up in the model.

### 5.4 Missing Data

- **[Provided]** In sample-size simulations, participants lost to follow-up before the simulated event are censored.
- **[Proposed]** For the primary time-to-event analysis, censor participants without a confirmed event at their last known event-free assessment, subject to the prespecified individual intended treatment limit. Rationale: this provides a clear risk-time rule for participants with incomplete event follow-up. Assumption: last known event-free status and assessment dates are available.
- **[Proposed]** Do not impute unobserved clinical events for the primary analysis; describe the amount and timing of incomplete outcome follow-up by treatment group. Rationale: this avoids asserting unobserved events as facts. Assumption: adjudicated events are analyzed only when sufficient information is available.
- **[Clarification Required]** The final missing-outcome, missing-covariate, and censoring procedures are not specified. These matter because they can affect estimates, precision, and the interpretation of follow-up.

### 5.5 Additional Analyses

- **[Provided]** Exploratory analyses describe composites of the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations, and net clinical benefit.
- **[Proposed]** Present exploratory analyses as supportive and interpret them with their uncertainty, without treating them as confirmatory unless a multiplicity strategy is prespecified. Rationale: the input identifies these analyses as exploratory but supplies no confirmatory testing plan. Assumption: no additional alpha allocation is intended unless established in the SAP.
- **[Clarification Required]** The component definitions, treatment contrasts, analysis methods, and any planned subgroup analyses for the exploratory outcomes are not supplied. These matter for reproducibility and interpretation.

### 5.6 Harms

- **[Provided]** Major bleeding and CRNM bleeding are safety objectives, and all safety events are adjudicated centrally; final analyses use adjudication results. Potential adverse events are elicited at all contacts.
- **[Proposed]** Present safety outcomes by randomized group and, as a supportive summary, by treatment received and exposure duration. Rationale: randomized-group summaries preserve comparability, while exposure summaries contextualize safety observations. Assumption: treatment exposure duration can be derived consistently.
- **[Clarification Required]** The collection, coding, seriousness/severity classification, relatedness assessment, and reporting rules for adverse events beyond the stated bleeding objectives are not supplied. These matter for comprehensive safety reporting.

### 5.7 Software and References

- **[Provided]** The sample-size calculation used a SAS Macro by Shih and three-arm simulations.
- **[Clarification Required]** Statistical software and version for the final analyses are not specified. This matters for reproducibility.
- **[Clarification Required]** No reference list or bibliographic details are supplied. The underlying study-specific facts and assumptions are presented here without adding external references.

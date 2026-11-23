# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** Recurrent VTE remains clinically important after initial anticoagulation for DVT or PE. Long-term VKA therapy is effective but entails bleeding, monitoring, and dose-adjustment burdens; ASA has modest recurrence-prevention efficacy.
- **[Provided]** The study evaluates whether reduced-dose rivaroxaban can maintain efficacy while improving safety, using ASA as comparator.

### 1.2 Objectives

- **[Provided]** P1: Evaluate superiority of rivaroxaban 10 mg and 20 mg versus ASA 100 mg for fatal or nonfatal symptomatic recurrent VTE.
- **[Provided]** S1: Evaluate superiority of each rivaroxaban dose versus ASA for fatal or nonfatal symptomatic recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism.
- **[Provided]** S2, the principal safety objective, is to document major bleeding incidence; S3, the secondary safety objective, is to document clinically relevant nonmajor (CRNM) bleeding incidence.
- **[Provided]** Additional objectives are S4(a), the composite of nonfatal symptomatic VTE and all-cause mortality; S5(b), major bleeding and recurrent VTE; and S6(c), major bleeding, recurrent VTE, MI, ischemic stroke, and systemic non-CNS embolism.
- **[Provided]** Exploratory analyses describe composites of the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations and net clinical benefit.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a phase III, multicenter, randomized, double-blind, double-dummy, active-comparator, event-driven trial with 1:1:1 allocation.
- **[Provided]** Treatment is oral once daily with food: rivaroxaban 10 mg, rivaroxaban 20 mg, or ASA 100 mg. Double-dummy supplies comprise one rivaroxaban-or-placebo tablet and one ASA-or-placebo tablet daily.
- **[Provided]** Nominal treatment duration is 12 months, although final randomized patients may receive only 6 months. Six months’ medication is initially supplied; IxRS determines at visit 4 whether a further six months is supplied. The last randomized patients receive no second supply.
- **[Provided]** The first dose is at least 24 hours after previous VTE treatment. With VKA, INR >3.0 delays randomization; INR 2.5–3.0 permits randomization but delays first intake until the next day; INR <2.5 permits dosing.
- **[Provided]** A missed dose may be made up only on the same day; double dosing is not allowed. Treatment may restart after temporary interruption if total treatment does not exceed 12 months.
- **[Provided]** All efficacy and safety events are centrally adjudicated, and final analyses use adjudication results.
- **[Clarification Required]** Define the adjudication procedures and operational event definitions. These are needed for consistent classification of efficacy and safety events.
- **[Clarification Required]** Define how the 12-month treatment limit is measured after interruptions. This determines whether treatment can restart and when it must end.

### 2.2 Randomization

- **[Provided]** A central interactive voice/web response system (IxRS) assigns a unique randomization number identifying treatment allocation. The investigator supplies the study-center identification and DVT/PE presentation.
- **[Provided]** Randomization is stratified by country and investigator-reported index event: DVT only versus PE with or without DVT. Minimization or blocking is not specified.
- **[Clarification Required]** Specify allocation implementation, including any blocking or minimization and allocation-concealment procedures. These affect reproducibility and assessment of allocation integrity.

### 2.3 Sample Size

- **[Provided]** Approximately 950 patients per arm, 2,850 total, are planned, subject to adjustment using observed overall primary-event incidence. At least 80 confirmed primary efficacy outcomes are required.
- **[Provided]** The calculation uses time to first confirmed fatal or nonfatal symptomatic recurrent VTE. ASA is assumed to have an exponentially modeled event rate of 5% per year; assumed HRs versus ASA are 0.30 for rivaroxaban 20 mg and 0.40 for rivaroxaban 10 mg.
- **[Provided]** The assumed analysis is a stratified Cox superiority analysis using an upper 95% CI bound below 1, with stratified log-rank testing supportive. Sequential tests use two-sided alpha 0.05. Target power is 90%; 10,000-trial simulation estimated joint Cox power of 0.901.
- **[Provided]** Simulations use exponential event, treatment-discontinuation, and withdrawal processes, with annual discontinuation of 10% and loss to follow-up or withdrawn consent of 1%. Last subjects receive 6 months’ treatment. After simulated discontinuation, simulated event time uses inferior-control treatment; losses before the simulated event are censored.
- **[Provided]** Simulations apply administrative censoring at one year or end of trial, select trials or observation time reaching the event target, and fit Cox and log-rank tests. Joint power is defined as both dose-versus-ASA HR 95% CI upper bounds ≤1.
- **[Provided]** The 20-mg assumption derives from an adjusted indirect comparison of prior extension and pooled ASA evidence: HR 0.264, 95% CI 0.12–0.59; HR 0.30 was conservative. The 10-mg assumption reflects orthopedic rivaroxaban and apixaban extended-treatment evidence: HR 0.40, a 60% reduction, was set versus an expected HR 0.30 from the reduced-dose rationale.
- **[Provided]** Blinded pooled projection iterates total enrollment until the probability of at least 80 total events is at least 0.50; alternatives such as probability about 0.80 are also presented. Calculation uses a SAS Macro by Shih and three-arm simulations.
- **[Provided]** No separate variability parameter is specified. A non-inferiority or equivalence margin is not applicable, and no cluster design effect applies to this individually randomized, non-clustered trial.

### 2.4 Hypothesis Framework

- **[Provided]** First test H0: HR(20 mg/ASA) = 1 versus two-sided H1: HR ≠ 1. Only if the 20-mg comparison is significant is H0: HR(10 mg/ASA) = 1 tested against two-sided H1: HR ≠ 1.
- **[Provided]** Each test is two-sided at 0.05. The 20-mg dose is superior if its HR 95% CI upper bound is <1; the 10-mg dose is superior only if 20 mg is superior and its own upper bound is <1.

### 2.5 Statistical Interim Analyses

- **[Provided]** Blinded pooled event-incidence projection may adjust enrollment.
- **[Proposed]** Do not conduct an interim efficacy hypothesis test; use the blinded projection for enrollment planning only. This avoids introducing an unplanned efficacy look and assumes no efficacy stopping rule is adopted.
- **[Clarification Required]** Specify any independent safety monitoring, interim safety reviews, and stopping rules. These determine how emerging risks or other reasons for early termination are handled.

### 2.6 Timing of Analyses

- **[Provided]** SAP revisions are issued before database lock. Final analyses use adjudicated outcomes through each patient’s individual intended treatment limit. Standard limits are day 353, visit day if day 353–367, or day 367; defined administrative shortening rules also apply.
- **[Provided]** Assessments occur at baseline, Day 1, Day 30±7, Day 90±7, Day 180±7, Day 270±7, Day 360±7, and a 30±7-day post-treatment observation visit. Potential outcomes and adverse events are elicited at all contacts.
- **[Provided]** After premature discontinuation, visit 7 occurs early, 30±7 days after stopping, by telephone or clinic. Other visits continue unless participation is refused; investigators may arrange additional visits.
- **[Clarification Required]** Specify the conditions selecting each standard treatment limit, the administrative shortening rules, and day-numbering conventions. These determine each patient’s analysis cutoff.
- **[Clarification Required]** Specify the operational event-driven closeout and database-lock timing. The event target alone does not establish when follow-up or enrollment ends.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The primary fixed sequence uses two-sided 0.05 tests and 95% CIs, with superiority requiring the relevant upper CI bound <1 and, for 10 mg, prior 20-mg superiority.
- **[Proposed]** Report effect estimates with two-sided 95% CIs and nominal p-values for other comparative analyses without claiming familywise-controlled significance. This distinguishes descriptive or supportive results from the specified primary sequence; it assumes no further multiplicity procedure is adopted.

### 3.2 Protocol Deviations

- **[Proposed]** Record deviations and classify important deviations before unblinding, including eligibility, dosing, and follow-up deviations. Summarize them by randomized group; this supports interpretation and assumes classifications can be made without treatment knowledge.
- **[Clarification Required]** Define the final important-deviation criteria and any consequences for sensitivity populations. These decisions affect reproducibility and interpretation.

### 3.3 Analysis Populations

- **[Proposed]** Define the primary efficacy population as all randomized patients analyzed as randomized, regardless of treatment discontinuation or subsequent treatment. This preserves randomized comparisons and assumes outcome follow-up is available.
- **[Proposed]** Define the safety population as patients receiving at least one dose, summarized according to treatment received. This describes exposed patients and assumes actual treatment can be determined.
- **[Clarification Required]** Specify safety-group assignment for patients who receive more than one active regimen or otherwise receive incorrect treatment. Assignment affects safety denominators and comparisons.

## 4. Trial Population

### 4.1 Screening Data

- **[Proposed]** Summarize numbers screened, randomized, treated, and not randomized, with available reasons for nonrandomization. This supports assessment of selection and assumes screening data are collected.
- **[Clarification Required]** Specify the screening log and whether data are collected for all screened individuals. This determines what screening summaries are feasible.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion requires confirmed symptomatic DVT and/or PE; 6–12 months of anticoagulation without interruption >1 week; and written consent.
- **[Provided]** Exclusions include being below the country-specific legal lower age limit; an indication for therapeutic-dose anticoagulants; hypersensitivity to investigational or comparator therapy; or any contraindication in local investigational/comparator labeling.
- **[Provided]** Exclusions also include an indication for antiplatelet therapy or conventional NSAID; hepatic disease with coagulopathy and clinically relevant bleeding risk; calculated CrCl <30 mL/min; active bleeding or anticoagulant-contraindicating high bleeding risk; or life expectancy <6 months.
- **[Provided]** Exclusions also include systemic strong dual CYP3A4/P-gp inhibitors—HIV protease inhibitors, ketoconazole, itraconazole, voriconazole, or posaconazole—and childbearing potential without proper contraception, pregnancy, or breastfeeding.
- **[Provided]** Participation in an investigational drug or device study within 30 days before randomization is excluded.

### 4.3 Recruitment

- **[Provided]** The trial is multicenter, with approximately 2,850 patients initially planned.
- **[Clarification Required]** Specify recruitment locations, dates, and enrollment procedures. These are needed to operationalize recruitment and describe the recruited population.

### 4.4 Withdrawal and Follow-up

- **[Provided]** Other scheduled visits continue after premature treatment stop unless participation is refused; an early post-treatment visit occurs 30±7 days after stopping.
- **[Proposed]** Record treatment discontinuation, withdrawal of consent, and loss to follow-up separately, with dates and available reasons. This distinguishes stopping treatment from stopping observation and assumes collection is permitted.
- **[Clarification Required]** Specify permissible data collection after each type of consent withdrawal and procedures for tracing patients lost to follow-up. These affect outcome ascertainment and censoring.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize baseline demographics, index-event category, relevant clinical history, prior anticoagulation, renal function, and other collected prognostic characteristics by randomized group. This describes comparability and assumes these variables are collected.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary outcome is fatal or nonfatal symptomatic recurrent VTE, comparing each rivaroxaban dose with ASA.
- **[Proposed]** Analyze time from randomization to first adjudicated primary event through the individual intended treatment limit, including events after treatment discontinuation. This estimates the randomized treatment-policy comparison and assumes such follow-up is available.
- **[Clarification Required]** Specify how event dates and fatal VTE are determined when timing or cause is uncertain. These decisions affect event counts and time-to-event analyses.

### 5.2 Secondary Outcomes

- **[Provided]** S1 is the composite of fatal or nonfatal symptomatic recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism, comparing each dose with ASA.
- **[Provided]** S2 and S3 are incidence of major bleeding and CRNM bleeding, respectively. S4 is nonfatal symptomatic VTE or all-cause mortality; S5 is major bleeding or recurrent VTE; S6 is major bleeding, recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism.
- **[Provided]** Exploratory analyses describe composites involving the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations and net clinical benefit.
- **[Clarification Required]** Specify the recurrent-VTE definitions for S5 and S6 and the components and construction of exploratory net clinical benefit. These determine which events contribute to each outcome.

### 5.3 Analysis Methods

- **[Proposed]** Fit a Cox model with treatment indicators for both doses versus ASA, stratified by the joint country and index-event categories; report HRs and 95% CIs and apply the primary fixed sequence. This uses the randomization factors and assumes adequate information within strata.
- **[Proposed]** Use stratified log-rank tests as supportive analyses and summarize event counts and estimated time-to-event curves by group. These aid interpretation and assume event timing is sufficiently recorded.
- **[Proposed]** Analyze S1 and the additional composites by time to first adjudicated component, reporting component counts as well as composite results. This avoids counting a patient twice in the composite and assumes component dates are available.
- **[Proposed]** Summarize major and CRNM bleeding with patient counts and percentages by treatment; supplement with time-to-first-event estimates where feasible. This describes incidence and timing, assuming adequate event dates and follow-up.
- **[Proposed]** Assess proportional hazards and, if questionable, supplement HRs with prespecified time-specific survival or restricted mean event-free time contrasts. This provides interpretable alternatives and assumes a common evaluable time horizon.
- **[Proposed]** For outcomes other than all-cause mortality composites, censor at non-outcome death in the Cox analysis and assess competing-risk cumulative incidence as a sensitivity analysis. This separates cause-specific hazards from absolute incidence and assumes death dates and causes are available.
- **[Clarification Required]** Specify the safety analysis risk window, including whether and how the post-treatment observation visit contributes. The supplied intended-treatment limit does not fully define safety exposure and follow-up windows.

### 5.4 Missing Data

- **[Proposed]** Censor patients without an observed primary event at their last adequate outcome assessment, no later than their intended treatment limit; do not impute unobserved events in the primary analysis. This uses observed follow-up and assumes censoring is noninformative conditional on model factors.
- **[Proposed]** Summarize missingness and follow-up duration by group, and perform prespecified sensitivity analyses for informative loss, including plausible event-rate departures after loss. This assesses robustness and assumes departure scenarios can be specified before unblinding.
- **[Clarification Required]** Specify rules for partially known event and assessment dates. These affect event ordering and censoring times.

### 5.5 Additional Analyses

- **[Proposed]** Summarize primary outcomes by index-event category and other prespecified, adequately populated baseline subgroups, reporting estimates and uncertainty without confirmatory claims. This explores consistency and assumes sufficient events.
- **[Proposed]** Prespecify blinded handling of sparse Cox strata and sensitivity analyses for important deviations. This reduces unstable estimation and assesses robustness; it assumes a defensible pooling rule can be agreed before unblinding.

### 5.6 Harms

- **[Provided]** Potential adverse events are elicited at all contacts, and safety events are centrally adjudicated.
- **[Proposed]** Summarize adverse events, serious adverse events, bleeding, deaths, and treatment discontinuations due to adverse events by treatment received. This provides a broader safety profile and assumes those data are collected.
- **[Clarification Required]** Specify adverse-event definitions, collection and reporting periods, severity grading, and expedited reporting procedures. These are necessary for consistent safety surveillance.

### 5.7 Software and References

- **[Provided]** Sample-size calculations use a SAS Macro by Shih and three-arm simulations.
- **[Proposed]** Document the software, versions, and validated analysis programs used for final analyses before reporting. This supports reproducibility and assumes suitable software is available.

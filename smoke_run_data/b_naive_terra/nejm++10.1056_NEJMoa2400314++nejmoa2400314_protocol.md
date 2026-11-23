# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Acute ischemic stroke (AIS) produces neurologic impairment, disability and mortality. This phase III study evaluates reteplase, a bolus-administered genetically engineered recombinant human tissue-type plasminogen activator derivative, against alteplase for AIS treated within 4.5 hours of symptom onset.

### 1.2 Objectives

**[Provided]** The primary objective is to evaluate reteplase versus alteplase effectiveness, operationalized as the difference in the proportions with modified Rankin Scale (mRS) 0–1 at day 90.

**[Provided]** The secondary objective is to evaluate safety and secondary functional and neurologic outcomes, including favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, adverse events (AEs), serious adverse events (SAEs) and death. Exploratory objectives were not separately labelled.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a multicenter, prospective, randomized, open-label, blinded-endpoint, positive active-controlled, parallel-group phase III noninferiority trial in Chinese patients with AIS within 4.5 hours of onset. Allocation is 1:1 to reteplase or alteplase.

**[Provided]** Thrombolysis must begin within 4.5 hours of last known well. Reteplase is administered as an 18 mg intravenous bolus followed by a second 18 mg intravenous bolus 30±5 minutes after completion of the first; each injection lasts at least 2 minutes.

**[Provided]** Alteplase is administered at 0.9 mg/kg intravenously, maximum 90 mg: 10% as a bolus within 1 minute and the remainder infused over 60 minutes.

### 2.2 Randomization

**[Provided]** An independent statistician generates random numbers in SAS 9.4 or higher. After eligibility is established, the investigator obtains allocation through an interactive web response system (IWRS). Random numbers of withdrawn participants are retained and cannot be replaced or reused. Initial random-number seed parameters are retained.

**[Provided]** SAP v1.0 describes simple stratified randomization without naming factors. Final Protocol V2.2 specifies variable-block 1:1 randomization without describing stratification. No individual stratification factor is reported.

**[Clarification Required]** Reconcile the implemented randomization method, including whether stratification was used and the applicable block specifications. This affects allocation documentation and any design-adjusted analysis.

### 2.3 Sample Size

**[Provided]** The planned sample is 1,412 participants, 706 per group. The calculation uses day-90 mRS 0–1, an alteplase rate of 62.5%, a true reteplase-to-alteplase risk ratio (RR) of 1.05, a noninferiority margin of 0.93, one-sided alpha of 0.025 and a lower confidence bound above 0.93 as the noninferiority criterion.

**[Provided]** The margin was derived from a historical alteplase-versus-placebo lower 95% confidence bound RR of 1.15 with preservation fraction \(f=0.5\). Variability and design-effect assumptions are not applicable to the stated binary proportion/RR calculation.

**[Provided]** Protocol V2.2 and SAP v1.0 specify 80% power with approximately 15% dropout/non-adherence inflation; SAP v1.1 specifies 85% power with 3% inflation. Calculation software is not specified.

**[Clarification Required]** Reconcile the power and inflation assumptions and document the calculation method before analysis. The discrepancies affect verification of the planned sample size.

**[Provided]** There is no primary endpoint event-count requirement. The safety rationale assumes symptomatic intracranial hemorrhage (sICH) at 1% and death at 5%, with more than 99% probability of observing at least one death or sICH.

### 2.4 Hypothesis Framework

**[Provided]** The primary hypotheses are \(H_0: RR\leq0.93\) versus \(H_1: RR>0.93\), where RR is the day-90 mRS 0–1 rate for reteplase divided by that for alteplase.

**[Provided]** Noninferiority is concluded at one-sided \(P<0.025\) or if the lower 95% RR confidence bound is greater than 0.93. Superiority is then concluded if the lower RR confidence bound is greater than 1.

### 2.5 Statistical Interim Analyses

**[Provided]** Original Protocol V1.0 planned Mehta–Pocock sample-size re-estimation conditional on interim efficacy of 50%–80%. Protocol V2.2 does not retain that procedure; SAP v1.0 and v1.1 state that there is no interim efficacy analysis.

**[Clarification Required]** Settle the version-specific interim-analysis conflict before execution. If re-estimation is retained, define the interim efficacy measure, timing, procedure and error-control implications; these determine the valid final analysis.

### 2.6 Timing of Analyses

**[Provided]** Final analysis occurs after the entire trial ends and after database lock, protocol-violation identification and treatment unblinding.

**[Provided]** Assessments are scheduled at screening/day 1, 24 hours±2 hours, 72 hours±6 hours, day 8±1 day, day 31±3 days and day 91±7 days. NIHSS is assessed at baseline, 24 hours and day 8; mRS and Barthel Index are assessed at day 31 and day 91, with blinded endpoint evaluation at follow-up.

**[Clarification Required]** Define how the day-91 visit window represents the day-90 primary endpoint, including selection among multiple assessments and handling assessments outside the window. This determines the primary outcome assigned to each participant.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The primary noninferiority test uses one-sided alpha 0.025 and a 95% RR confidence interval, with the decision rules in Section 2.4.

**[Proposed]** Report two-sided 95% confidence intervals for treatment effects and treat secondary analyses as descriptive, without confirmatory multiplicity claims. Rationale: this distinguishes the specified primary testing sequence from other comparisons; it assumes no additional confirmatory secondary testing strategy is adopted.

### 3.2 Protocol Deviations

**[Proposed]** Document and classify deviations, including eligibility, treatment timing or administration, and endpoint assessment deviations, before treatment unblinding. Rationale: classification supports interpretable population definitions; it assumes sufficient records are available.

**[Clarification Required]** Define which deviations exclude participants from the per-protocol population and how disputed classifications are resolved. These decisions can materially affect noninferiority results.

### 3.3 Analysis Populations

**[Proposed]** Use all randomized participants, analyzed as allocated, for the primary efficacy population; use a prespecified per-protocol population as supportive. Rationale: the two populations assess robustness to different biases in a noninferiority trial; this assumes randomized participants can be identified reliably.

**[Proposed]** Include participants receiving any study thrombolytic in the safety population, analyzed according to treatment received. Rationale: this describes observed exposure and harms; it assumes actual treatment is recorded.

**[Clarification Required]** Specify treatment classification for participants receiving both agents or an otherwise ambiguous exposure. This matters for safety denominators and attribution.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Summarize numbers screened, eligible, randomized and not randomized, with available reasons for screening failure. Rationale: this describes selection into the trial; it assumes screening records are maintained.

### 4.2 Eligibility Criteria Summary

**[Provided]** Inclusion requires age 18–80 years; WHO-defined AIS within 4.5 hours of last known well; NIHSS 4–25 before thrombolysis; agreement to contraception where applicable; ability to comply; and participant or guardian consent.

**[Provided]** Exclusions include non-ascertainable onset; weight <45 or >120 kg; pre-stroke mRS≥2; NIHSS consciousness item 1a≥2; hemorrhage, imaging or anticoagulation risks; uncontrolled blood pressure; out-of-range glucose; large infarction; important hepatic or other comorbidity; planned or received endovascular treatment; interfering treatments; recent trial participation; pregnancy or lactation; and investigator-determined barriers to compliance.

**[Clarification Required]** Specify the operational thresholds and definitions for the qualitative exclusions, including imaging, anticoagulation, blood pressure, glucose, comorbidity, interfering treatment and recent trial participation. They are needed for consistent eligibility determination.

### 4.3 Recruitment

**[Proposed]** Recruit eligible patients at participating centers and document consent and eligibility before randomization. Rationale: this supports consistent enrollment; it assumes the consent process can be completed within the treatment window.

**[Clarification Required]** Specify participating centers, recruitment dates and any recruitment targets by center. These are needed for an operational recruitment plan.

### 4.4 Withdrawal and Follow-up

**[Proposed]** Record withdrawal dates and reasons and distinguish stopping treatment from stopping follow-up; seek permitted outcome follow-up when treatment is discontinued. Rationale: this limits avoidable missing data; it assumes continued follow-up is authorized.

**[Proposed]** Retain already collected data subject to applicable consent and requirements. Rationale: this preserves information while respecting participant rights; it assumes retention is permitted.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize baseline demographics, stroke severity, pre-stroke mRS, relevant clinical characteristics and time from last known well to treatment by randomized group, including missing counts. Rationale: this describes comparability and the enrolled population; it assumes these data are collected.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary outcome is the difference between groups in the proportion with mRS 0–1 at day 90. The primary hypothesis and decision rules use the corresponding reteplase-to-alteplase RR.

**[Proposed]** Estimate both the absolute proportion difference and RR, with 95% confidence intervals, in the randomized population. Rationale: this reports the stated outcome and supports the specified hypothesis test; it assumes the day-90 assessment rule is resolved.

**[Proposed]** Count participants known to have died before the primary assessment as not having mRS 0–1. Rationale: death is incompatible with an excellent functional outcome; it assumes death ascertainment covers the relevant endpoint time.

### 5.2 Secondary Outcomes

**[Provided]** Secondary outcomes include favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, AEs, SAEs and death.

**[Clarification Required]** Define the favorable-function threshold, NIHSS improvement measure or responder threshold, hemorrhage and sICH definitions, and observation periods for each outcome. These determine the secondary estimands and event counts.

### 5.3 Analysis Methods

**[Proposed]** For the primary binary endpoint, estimate the RR using an unadjusted log-link model with robust standard errors and a 95% interval on the log-RR scale; report group counts and proportions and the absolute difference. Apply the specified noninferiority and subsequent superiority rules to the RR interval. Rationale: this directly targets the specified RR; it assumes independent participants and an estimable model.

**[Proposed]** Analyze the per-protocol population with the same effect measures and compare its direction and precision with the randomized-population results. Rationale: concordance is informative for noninferiority robustness; it assumes per-protocol criteria are finalized before unblinding.

**[Proposed]** Summarize mRS categories and Barthel Index at days 31 and 91, and NIHSS and change from baseline at 24 hours and day 8, by group. Rationale: these summaries use the scheduled assessments; they assume scores are collected consistently.

**[Proposed]** Summarize binary secondary outcomes and harms by group with counts, proportions and effect estimates where feasible. Rationale: this makes treatment contrasts interpretable; it assumes outcome definitions and observation periods are finalized.

**[Clarification Required]** Specify any required covariate adjustment, center handling and fallback for nonestimable primary models. These choices affect inference, particularly if the implemented randomization differs from the documented descriptions.

### 5.4 Missing Data

**[Proposed]** For the primary randomized-population analysis, use multiple imputation for missing primary binary outcomes, separately by treatment group, using available baseline and follow-up predictors; combine log-RR estimates and variances across imputations. Rationale: this retains randomized participants; it assumes outcomes are missing at random conditional on included predictors.

**[Proposed]** Prespecify imputation predictors, number of imputations, diagnostics and seed before unblinding, and report missingness by group and reason. Rationale: this makes the analysis reproducible; it assumes missingness information is adequately recorded.

**[Proposed]** Assess robustness with complete-case and unfavorable/favorable missing-outcome scenarios by treatment group. Rationale: these expose sensitivity to departures from the primary missing-data assumption; they assume the scenarios are interpretable for the observed missingness.

**[Clarification Required]** Define handling of intercurrent events, including non-study treatment and withdrawal, and the availability of outcomes after them. These decisions determine the primary estimand and the scope of imputation.

### 5.5 Additional Analyses

**[Proposed]** Explore treatment effects by baseline age and NIHSS severity using prespecified categories and treatment-by-subgroup interactions, reporting intervals without confirmatory claims. Rationale: this may reveal effect heterogeneity; it assumes adequate subgroup data and acknowledges limited precision.

**[Clarification Required]** Specify subgroup cutoffs and any other required sensitivity or center analyses before unblinding. Unspecified choices can lead to selective interpretation.

### 5.6 Harms

**[Proposed]** Summarize hemorrhage, sICH, AEs, SAEs and deaths in the safety population by treatment received, including event counts and affected-participant counts where applicable. Rationale: these address the stated safety objective; it assumes events and exposure are reliably recorded.

**[Clarification Required]** Define AE severity, seriousness, treatment-emergent status, causality procedures and safety follow-up duration. These are necessary for consistent harm classification and denominators.

### 5.7 Software and References

**[Provided]** Randomization numbers are generated using SAS 9.4 or higher. Sample-size calculation software is not specified.

**[Proposed]** Document the software versions, analysis code and retained seeds used for final analyses. Rationale: this supports reproducibility; it assumes the analysis environment is controlled and archived.

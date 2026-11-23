# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** Acute ischemic stroke (AIS) causes neurologic impairment, disability, and mortality. This phase III study evaluates reteplase, a genetically engineered recombinant human tissue-type plasminogen activator derivative administered as a bolus, against alteplase in patients with AIS treated within 4.5 hours of symptom onset.

### 1.2 Objectives

- **[Provided]** **Primary objective (P1):** Evaluate reteplase versus alteplase effectiveness for AIS within 4.5 hours, operationalized as the difference in the proportion of participants with modified Rankin Scale (mRS) 0–1 at day 90. The specified primary outcome is the difference in those proportions between treatment groups.

- **[Provided]** **Secondary objective (S1):** Evaluate safety and secondary functional and neurologic outcomes of reteplase versus alteplase, including favorable function, mRS distribution, National Institutes of Health Stroke Scale (NIHSS) improvement, Barthel Index, hemorrhage, adverse events (AEs), serious adverse events (SAEs), and death outcomes.

- **[Provided]** Exploratory objectives were not reported as a separately labelled objective.

- **[Clarification Required]** The primary objective specifies a difference in proportions, while the formal hypothesis and sample-size calculation use a risk ratio (RR). The primary inferential effect measure must be selected because the measure determines the estimand, confidence interval, and noninferiority decision.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a multicenter, prospective, randomized, open-label, blinded-endpoint-assessment, positive active-controlled, parallel-group phase III noninferiority trial in Chinese patients with AIS within 4.5 hours of onset. Participants are allocated 1:1 to reteplase or alteplase.

- **[Provided]** Thrombolysis must begin within 4.5 hours of last known well. Reteplase is given as an 18 mg intravenous (IV) bolus followed by a second 18 mg IV bolus 30±5 minutes after completion of the first; each injection lasts at least 2 minutes. Alteplase is given as 0.9 mg/kg IV (maximum 90 mg), with 10% given as a bolus within 1 minute and the remainder infused over 60 minutes.

### 2.2 Randomization

- **[Provided]** An independent statistician generates random numbers using SAS 9.4 or higher. After eligibility is established, the investigator obtains the allocation through the interactive web response system (IWRS). Random numbers assigned to withdrawn participants are retained and cannot be replaced or reused. Initial random-number seed parameters are retained.

- **[Provided]** SAP v1.0 describes simple stratified randomization without naming factors. Final Protocol V2.2 specifies variable-block 1:1 randomization without describing stratification. No individual stratification factor is reported.

- **[Clarification Required]** The governing randomization method—stratified or variable-block without stratification—and any stratification factors must be confirmed. This affects implementation, documentation, and any stratified analysis.

### 2.3 Sample Size

- **[Provided]** The planned sample size is 1,412 participants, with 706 per group. The calculation is based on the binary excellent functional outcome of mRS 0–1 at day 90 after treatment.

- **[Provided]** The assumed alteplase primary efficacy proportion is 62.5%, and the assumed true reteplase:alteplase efficacy RR is 1.05. The noninferiority margin is RR 0.93, derived from the historical alteplase-versus-placebo lower 95% confidence interval (CI) RR of 1.15 using f=0.5. Variability is not applicable to the binary proportion/RR calculation, and clustering/design effect is not applicable.

- **[Provided]** The calculation assumes one-sided alpha 0.025 and a one-sided noninferiority RR test, with noninferiority demonstrated by a lower CI bound above 0.93. Protocol V2.2 and SAP v1.0 state 80% power and approximately 15% dropout/non-adherence inflation; SAP v1.1 states 85% power and 3% dropout/non-adherence inflation. These discrepancies require reconciliation before analysis.

- **[Provided]** There is no event-count requirement for the primary binary endpoint. The safety rationale estimates sICH at 1% and death at 5%, with a greater than 99% probability of observing at least one death or sICH. Assumption bases are prior alteplase trials and Phase II reteplase data, SITS-MOST for sICH, and NOR-TEST for death.

- **[Provided]** The 1:1 sample-size plan targets noninferiority for day-90 mRS 0–1 while providing substantial probability of observing key safety events. The calculation software was not specified.

- **[Clarification Required]** The approved power and dropout/non-adherence inflation assumptions must be identified and the sample-size calculation confirmed. The conflicting values could affect whether the planned enrollment supports the intended power.

- **[Clarification Required]** The calculation software and reproducible calculation specifications are not reported. These are needed to verify and document the planned sample size.

### 2.4 Hypothesis Framework

- **[Provided]** The primary hypothesis is H0: RR≤0.93 versus H1: RR>0.93, where RR is the day-90 mRS 0–1 rate in the reteplase group divided by that in the alteplase group. Noninferiority is concluded at one-sided P<0.025 or when the lower RR 95% CI bound is >0.93. Superiority is then concluded if the lower RR CI bound is >1.

- **[Proposed]** Pending confirmation of the primary effect measure, use the stated RR hypothesis and decision thresholds for the primary inferential test, and report the between-group proportion difference as a supportive estimate. This aligns the provisional test with the stated sample-size framework; the assumption is that the RR framework governs until the primary-effect-measure discrepancy is resolved.

### 2.5 Statistical Interim Analyses

- **[Provided]** Original Protocol V1.0 planned Mehta–Pocock sample-size re-estimation conditional on interim efficacy of 50%–80%. Protocol V2.2 does not retain that procedure. SAP v1.0 and v1.1 state that there is no interim efficacy analysis.

- **[Clarification Required]** The governing decision on interim efficacy analysis and sample-size re-estimation must be confirmed before study execution or analysis. The documents conflict, and the choice affects trial conduct and potentially the interpretation of the final analysis.

- **[Clarification Required]** Interim safety-review procedures and any stopping rules are not specified. Their absence or presence matters for participant protection and operational oversight.

### 2.6 Timing of Analyses

- **[Provided]** Final analysis is conducted after the entire trial ends and after database lock, protocol-violation identification, and treatment unblinding.

- **[Provided]** The assessment schedule is Screening/Day 1 (D1), 24h±2h, 72h±6h, D8±1 day, D31±3 days, and D91±7 days. NIHSS is assessed at baseline, 24 hours, and D8. mRS and Barthel Index are assessed at D31 and D91, with blinded endpoint evaluation at follow-up.

- **[Clarification Required]** The primary outcome is described as day 90, while the scheduled follow-up is D91±7 days. The nominal endpoint day and rules for using assessments within the visit window must be confirmed because they define the primary outcome time point.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The primary noninferiority framework uses one-sided alpha 0.025. Noninferiority requires one-sided P<0.025 or a lower RR 95% CI bound >0.93; superiority is tested after noninferiority and requires a lower RR CI bound >1.

- **[Proposed]** Report treatment-effect estimates with two-sided 95% CIs for descriptive and secondary analyses, unless a different interval is required by the approved SAP. This provides a consistent summary of precision; the assumption is that two-sided 95% intervals are acceptable for outcomes without a supplied inferential rule.

- **[Clarification Required]** Multiplicity control and the confirmatory status of secondary outcomes are not specified. These decisions matter because multiple inferential tests can increase the chance of false-positive conclusions.

### 3.2 Protocol Deviations

- **[Provided]** Protocol-violation identification precedes treatment unblinding and final analysis.

- **[Proposed]** Define deviation categories, severity, and the process for blinded review before treatment unblinding; document each deviation and its impact on analysis populations. This supports reproducible population definitions; the assumption is that the study team can complete adjudication without access to treatment allocation.

- **[Clarification Required]** Criteria for major deviations and exclusions from any per-protocol analysis are not supplied. They matter because post hoc or treatment-aware classification could bias a noninferiority assessment.

### 3.3 Analysis Populations

- **[Proposed]** Define a full analysis set comprising all randomized participants analyzed according to assigned group, a per-protocol set comprising eligible participants without prespecified major deviations, and a safety set comprising participants analyzed according to treatment received. This permits complementary efficacy and safety summaries; the assumptions are that randomization defines the efficacy assignment and exposure defines safety attribution.

- **[Clarification Required]** The protocol does not specify analysis populations or detailed membership rules. These rules, particularly for noninferiority analyses, must be approved before unblinding because exclusions can affect treatment comparisons.

## 4. Trial Population

### 4.1 Screening Data

- **[Provided]** Screening/Day 1 is a scheduled assessment point.

- **[Clarification Required]** Screening variables, screening-failure reasons, and screening disposition summaries are not specified. They matter for documenting eligibility and describing participant flow and the population to which results apply.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria are age 18–80 years; World Health Organization-defined AIS within 4.5 hours of last known well; NIHSS 4–25 before thrombolysis; agreement to contraception where applicable; ability to comply; and consent from the participant or guardian.

- **[Provided]** Exclusion criteria are non-ascertainable onset; weight <45 or >120 kg; pre-stroke mRS≥2; NIHSS consciousness item 1a≥2; hemorrhage/imaging/anticoagulation risks; uncontrolled blood pressure; out-of-range glucose; large infarction; important hepatic or other comorbidity; planned or received endovascular treatment; interfering treatments; recent trial participation; pregnancy/lactation; and investigator-determined barriers to compliance.

- **[Clarification Required]** Operational definitions, measurement procedures, and thresholds for several exclusions—including hemorrhage/imaging/anticoagulation risks, uncontrolled blood pressure, out-of-range glucose, large infarction, important comorbidity, interfering treatments, and recent trial participation—are not provided. They matter for consistent eligibility decisions across centers.

### 4.3 Recruitment

- **[Provided]** The study is multicenter and enrolls Chinese patients with AIS within 4.5 hours of onset.

- **[Clarification Required]** Recruitment sites, recruitment dates, and enrollment procedures are not specified. These details matter for operational planning and describing participant accrual.

### 4.4 Withdrawal and Follow-up

- **[Provided]** Random numbers of withdrawn participants are retained and cannot be replaced or reused. The scheduled assessments are Screening/D1, 24h±2h, 72h±6h, D8±1 day, D31±3 days, and D91±7 days.

- **[Proposed]** Continue outcome follow-up, where permitted, after treatment discontinuation or study-treatment withdrawal, and document the reason and timing of withdrawal. This can reduce missing outcome data; the assumption is that continued follow-up is consistent with consent and applicable study procedures.

- **[Clarification Required]** Withdrawal categories, follow-up after withdrawal, and handling of participants who discontinue assigned treatment are not defined. These decisions affect participant disposition and completeness of outcome data.

### 4.5 Baseline Characteristics

- **[Provided]** Baseline NIHSS is assessed; the eligibility range before thrombolysis is 4–25. No other baseline variables are specified.

- **[Proposed]** Summarize baseline characteristics by randomized group using descriptive statistics, without baseline significance testing. This describes group comparability without treating chance imbalances as tests of randomization; the assumption is that relevant baseline variables are collected in the study dataset.

- **[Clarification Required]** The baseline variables to be collected and summarized are not listed. A prespecified list is needed for consistent reporting.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary outcome is the difference between treatment groups in the proportion of participants with mRS 0–1 at day 90.

- **[Provided]** The sample-size and hypothesis frameworks instead specify the day-90 mRS 0–1 RR and noninferiority margin RR 0.93.

- **[Proposed]** Subject to confirmation of the primary effect measure and endpoint day, estimate the treatment effect for mRS 0–1 and report group-specific proportions with a CI. If RR is confirmed as primary, apply the stated RR noninferiority and subsequent superiority rules; also report the proportion difference. This retains the supplied decision thresholds while making the objective’s stated difference interpretable; the assumptions are that the RR framework is approved and the D91 visit window supplies the day-90 assessment.

- **[Clarification Required]** The primary effect measure, endpoint day, and handling of assessments outside the scheduled follow-up window must be finalized. They directly determine the primary endpoint and whether the stated noninferiority rule addresses the primary objective.

### 5.2 Secondary Outcomes

- **[Provided]** Secondary outcomes include favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, AEs, SAEs, and death outcomes for reteplase versus alteplase. mRS and Barthel Index are assessed at D31 and D91; NIHSS is assessed at baseline, 24 hours, and D8.

- **[Clarification Required]** Definitions and analysis time points are not supplied for favorable function, NIHSS improvement, hemorrhage outcomes, AEs/SAEs, or death outcomes. The favorable-function threshold and hemorrhage definitions in particular are needed for reproducible outcome classification and comparison.

### 5.3 Analysis Methods

- **[Proposed]** For the binary primary endpoint under an RR framework, estimate the RR and its lower 95% CI using a method appropriate for binary data, with the treatment groups compared as randomized. This directly supports the stated RR decision rule; the assumption is that the RR is confirmed as the primary measure.

- **[Proposed]** Report the primary risk difference as a complementary estimate with a CI. This reflects the primary objective’s stated contrast; the assumption is that both effect measures can be reported without changing the prespecified primary decision rule.

- **[Proposed]** Summarize mRS distribution at each scheduled assessment and compare groups using an ordinal method if the scale and data support it. This preserves information across mRS categories; the assumption is that category-level mRS data are available and an ordinal model is appropriate.

- **[Proposed]** Analyze NIHSS at 24 hours and D8 in relation to baseline, and report Barthel Index by scheduled assessment using methods suited to its observed scale and distribution. This uses the supplied assessment schedule; the assumption is that scale scoring and analysis conventions are confirmed before database lock.

- **[Proposed]** Summarize binary safety outcomes by group with event counts and proportions and, where suitable, comparative estimates with CIs. This gives transparent safety descriptions; the assumption is that event definitions and safety observation periods are prespecified.

- **[Clarification Required]** Covariate adjustment, model specifications, and handling of center effects are not stated. These decisions matter for reproducibility and may affect precision or estimates; any adjustment should be prespecified and consistent with the confirmed randomization method.

- **[Clarification Required]** Outcome definitions, scoring conventions, and the statistical hierarchy for secondary outcomes are not specified. These must be resolved before analysis to avoid outcome-dependent choices.

### 5.4 Missing Data

- **[Clarification Required]** The supplied information does not specify missing-outcome handling, missing-data assumptions, or sensitivity analyses. This matters because missing outcomes can alter both effect estimates and noninferiority conclusions.

- **[Proposed]** Report missingness and reasons by group and assessment time, and conduct sensitivity analyses for the primary endpoint under plausible assumptions about missing outcomes. This makes the potential influence of missing data visible; the assumption is that reasons for missingness can be collected and the sensitivity methods prespecified before unblinding.

### 5.5 Additional Analyses

- **[Proposed]** Treat any subgroup or other additional efficacy analyses as exploratory unless a confirmatory hierarchy is approved in advance, and report estimates with CIs rather than relying only on subgroup-specific significance tests. This limits overinterpretation of unplanned comparisons; the assumption is that no confirmatory subgroup plan has been supplied.

- **[Clarification Required]** Prespecified subgroup variables and any required sensitivity analyses are not identified. Their definitions must be agreed before analysis if they are intended to inform conclusions.

### 5.6 Harms

- **[Provided]** The sample-size safety rationale uses estimated sICH incidence of 1% and death incidence of 5%, and estimates a greater than 99% probability of observing at least one death or sICH. These are planning estimates, not reported study results.

- **[Proposed]** Summarize AEs, SAEs, hemorrhage, and deaths by treatment group, including counts and proportions; present timing and severity where collected. This supports transparent safety comparison; the assumptions are that relevant event details are collected and definitions are prespecified.

- **[Clarification Required]** Safety observation periods, event coding and severity conventions, and the definition of sICH are not specified. These decisions matter for consistent event ascertainment and interpretation.

### 5.7 Software and References

- **[Provided]** Random-number generation is performed by an independent statistician using SAS 9.4 or higher, with initial seed parameters retained. Sample-size assumptions are based on prior alteplase trials and Phase II reteplase data, with SITS-MOST used for sICH and NOR-TEST for death.

- **[Clarification Required]** Statistical analysis software and version are not specified. They should be documented to support reproducibility.

- **[Proposed]** Archive the analysis programs, software/version information, and key outputs with the final analysis documentation. This supports verification and reproducibility; the assumption is that these materials can be retained under study procedures.

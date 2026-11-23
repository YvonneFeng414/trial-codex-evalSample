# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale

Acute ischemic stroke (AIS) produces neurologic impairment, disability and mortality. This phase III study evaluates genetically engineered recombinant human tissue-type plasminogen activator derivative (reteplase), a bolus-administered thrombolytic, against alteplase for AIS treated within 4.5 hours of symptom onset.

### 1.2 Objectives

**Primary Objectives**

- Evaluate reteplase versus alteplase effectiveness for AIS within 4.5 hours, operationalized as the difference in the proportion with mRS 0–1 at day 90.

**Secondary Objectives**

- Evaluate safety and secondary functional and neurologic outcomes of reteplase versus alteplase, including favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, AE/SAE and death outcomes.

**Exploratory Objectives**

Not reported in protocol as a separately labelled objective.

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Multicenter, prospective, randomized, open-label with blinded endpoint assessment, positive active-controlled parallel-group phase III noninferiority trial in Chinese patients with AIS within 4.5 hours of onset.
- **Allocation Ratio:** 1:1 reteplase:alteplase.
- **Intervention Summary:** Thrombolysis must begin within 4.5 hours of last known well.
  - Reteplase group: 18 mg IV bolus followed by a second 18 mg IV bolus 30±5 minutes after completion of the first; each injection lasts at least 2 minutes.
  - Alteplase group: 0.9 mg/kg IV (maximum 90 mg), 10% as a bolus within 1 minute and the remainder infused over 60 minutes.

### 2.2 Randomization

- **Method:** An independent statistician generates the random numbers in SAS 9.4 or higher. After eligibility, the investigator uses IWRS to obtain the allocation; random numbers of withdrawn participants are retained and cannot be replaced or reused.
- **Stratification Factors:** SAP v1.0 describes simple stratified randomization but names no factors. Final Protocol V2.2 instead specifies variable-block 1:1 randomization without describing stratification; no individual factor is reported.
- **Minimization or Blocking:** Variable-block randomization in a 1:1 ratio; the initial random-number seed parameters are retained.

### 2.3 Sample Size

- **Planned Sample Size:** 1,412 participants, 706 per group.
- **Outcome Used for Calculation:** Proportion with mRS 0–1 at day 90 after treatment.
- **Outcome Type:** Binary excellent functional outcome.
- **Assumed Control-Arm Value:** Alteplase primary efficacy proportion 62.5%.
- **Assumed Treatment-Arm Value:** Assumed true reteplase:alteplase efficacy RR 1.05.
- **Target Difference / Effect Size:** NI margin is RR 0.93; it was derived from historical alteplase versus placebo lower 95% CI RR 1.15 with f=0.5.
- **Variability Assumption:** Not applicable for the binary proportion/RR calculation.
- **Alpha (Significance Level):** One-sided 0.025.
- **Power:** 80% in Protocol V2.2 and SAP v1.0. SAP v1.1 instead reports 85%; this discrepancy is retained for reconciliation before analysis.
- **Statistical Test Assumed:** One-sided noninferiority RR test, with NI demonstrated by lower CI bound above 0.93.
- **Required Number of Events:** No event-count requirement for the primary binary endpoint. The safety rationale estimates sICH 1% and death 5%, with >99% probability of observing at least one death or sICH.
- **Non-Inferiority / Equivalence Margin:** RR 0.93.
- **Dropout / Non-Adherence Inflation:** Approximately 15% in Protocol V2.2/SAP v1.0; SAP v1.1 reports 3%, a discrepancy requiring reconciliation.
- **Design Effect / Clustering:** Not applicable to sample-size calculation; clustering is addressed as a random center effect in analysis.
- **Basis for Assumptions:** Prior alteplase trials and Phase II reteplase data; SITS-MOST for sICH and NOR-TEST for death.
- **Sample Size Re-Estimation / Amendments:** Original Protocol V1.0 planned Mehta–Pocock re-estimation conditional on interim efficacy 50%–80%. V2.2 does not retain that interim procedure, and SAP v1.0/v1.1 state no interim efficacy analysis; this version-specific conflict must be settled before execution.
- **Software Used for Calculation:** Not reported in protocol.
- **Sample Size Rationale:** The 1:1 sample targets NI for day-90 mRS 0–1 while providing substantial probability of observing key safety events.

### 2.4 Hypothesis Framework

The primary hypothesis is H0: RR≤0.93 versus H1: RR>0.93, where RR is the day-90 mRS 0–1 rate in reteplase divided by that in alteplase. NI is concluded at one-sided P<0.025 or lower RR 95% CI bound >0.93; superiority is then concluded if the lower RR CI bound is >1.

### 2.5 Statistical Interim Analyses

- **Interim Analyses Planned:** Original Protocol V1.0 specifies one IDMC efficacy analysis after 60% complete day-90 mRS. V2.2 does not retain an interim procedure, while SAP v1.0 and final SAP v1.1 state no interim efficacy analysis; v1.1 retains regular unblinded DSMB safety tables. This conflict is not resolved in the supplied documents.
- **Stopping Guidelines:** V2.2 retains an IDMC for cumulative-data safety assessment; its procedures and operating cycle are in its charter. Final SAP v1.1 says DSMB safety concerns may lead to a modification/stop recommendation, with the Steering Committee and sponsor deciding whether to act. V2.2’s broader termination criteria include risk–benefit concerns, noncompliance, design errors, slow recruitment, and authority/ethics direction.
- **Alpha Spending or Adjustment:** Original Protocol V1.0 alone specifies O’Brien–Fleming one-sided spending of approximately .00381 interim and .02380 final. This superseded efficacy-interim design was cancelled before V2.2 and is not an active multiplicity adjustment; final SAP v1.1 specifies no interim efficacy analysis.

### 2.6 Timing of Analyses

- **Final Analysis Timing:** Conduct after end of the entire trial and after database lock, protocol-violation identification and treatment unblinding.
- **Outcome Assessment Schedule:** Screening/D1; 24h±2h; 72h±6h; D8±1d; D31±3d; and D91±7d. NIHSS is assessed at baseline, 24h and D8; mRS and Barthel at D31 and D91, with blinded endpoint evaluation at follow-up.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **Alpha Level:** Unless otherwise specified, two-sided alpha .05 and two-sided 95% CIs apply; the primary NI comparison uses one-sided alpha .025.
- **Multiplicity Adjustment:** SAP v1.1 states no adjustment is required because there is one primary efficacy outcome and one treatment comparison; all secondary efficacy outcomes are unadjusted and exploratory.
- **Confidence Intervals:** Primary and secondary effect estimates use 95% CIs; the primary decision uses the lower RR CI bound against 0.93 and then 1.

### 3.2 Protocol Deviations

- **Adherence Definition:** Compliance is determined from recorded number, date, actual dose, and administration start/end times.
- **Adherence Assessment:** Record exposure, dosing interval/duration, interruptions and infusion reactions; calculate adherence as actual dose/planned dose ×100%, categorized <80%, 80%–120% or >120%. PPS review separately considers main-eligibility failure, seriously interfering concomitant treatment, poor compliance and early permanent discontinuation.
- **Protocol Deviation Definition:** Serious violations are not exhaustively pre-specified; their definition is confirmed at data review.
- **Protocol Deviation Reporting:** Study personnel document deviations and explanations. Emergency deviations are promptly reported to the ethics committee and sponsor, and to regulatory authorities when necessary. CRA monitoring reports communicate deviations, deficiencies, actions and conclusions to the sponsor. Final deviations are discussed before lock and documented in data-review minutes; SAP v1.0 classifies deviations as mild or major, tabulates all and major deviations by treatment, provides listings, and identifies reasons for analysis-set exclusion.

### 3.3 Analysis Populations

- **Intention-to-Treat:** Modified ITT includes randomized participants who received at least one trial-drug dose and basically met main eligibility; analyze according to randomized group.
- **Per Protocol:** PPS includes participants completing the study without serious protocol violation; analyze according to treatment received when treatment was received throughout. It is the secondary efficacy population.
- **Other Populations:** The randomized population (all randomized participants) is used for disposition and denominator reporting. Safety Set includes randomized, treated participants with evaluable post-treatment safety data and is analyzed as treated.

## 4. Trial Population

### 4.1 Screening Data

Screening captures informed consent; demographics; weight; medical, treatment and allergy history; pre-stroke mRS and NIHSS; cranial CT/MRI; glucose, hematology, biochemistry, coagulation and pregnancy testing as applicable; ECG; eligibility; randomization; concomitant treatment; and AEs. Screening failures are participants who withdraw between consent and randomization; list them with reasons, record demographics, failure reason, eligibility information and any SAE in the eCRF, and exclude them from other analyses. Post-onset external CT and blood-count findings may be accepted, and traceable post-onset assessments obtained before consent can be used as screening data rather than repeated.

### 4.2 Eligibility Criteria Summary

Eligible participants are 18–80 years, have WHO-defined AIS within 4.5 hours of last known well, NIHSS 4–25 before thrombolysis, agree to contraception where applicable, can comply, and provide participant or guardian consent. Exclusions include non-ascertainable onset, weight <45 or >120 kg, pre-stroke mRS≥2, NIHSS consciousness item 1a≥2, hemorrhage/imaging/anticoagulation risks, uncontrolled blood pressure, out-of-range glucose, large infarction, important hepatic or other comorbidity, planned/received endovascular treatment, interfering treatments, recent trial participation, pregnancy/lactation, and investigator-determined barriers to compliance.

### 4.3 Recruitment

The study plans to recruit 1,412 Chinese participants with AIS within 4.5 hours at multiple centers. The original protocol projected conduct from October 2021 through March 2025.

### 4.4 Withdrawal and Follow-up

- **Withdrawal Levels:** Voluntary withdrawal includes consent withdrawal or loss to follow-up after at least three contact attempts. Investigator withdrawal may follow pregnancy, post-randomization discovery of non-AIS, or another investigator-determined need before thrombolysis.
- **Withdrawal Data Collection:** Complete subsequent safety and efficacy visits where possible; record the reason, last visit, and available data in medical records/eCRF. Follow AEs through recovery, improvement, stabilization, or loss to follow-up.
- **Reasons for Withdrawal:** Under V2.2, withdrawal reasons include consent withdrawal, loss to follow-up, pregnancy, post-randomization ineligibility/non-AIS, and other investigator-determined conditions; withdrawn participants are neither replaced nor re-enrolled. Original V1.0 additionally classified endovascular treatment as voluntary withdrawal with no further follow-up, and permitted investigator withdrawal for serious deviation, allergy, AE-related inability to continue, and post-treatment ineligibility. The V2.2 rules are the current protocol rules.

### 4.5 Baseline Characteristics

- **Baseline Variables:** Birth date, sex, nationality/ethnicity, weight, disease characteristics, medical and medication history, allergy history, pre-stroke mRS, baseline NIHSS, vital signs, imaging, laboratory tests and ECG are collected before randomization or dosing as scheduled. SAP summaries additionally identify onset duration (minutes), thrombolytic time-window category, baseline NIHSS and mRS categories, TOAST classification and localization diagnosis by treatment group.
- **Summary Methods:** Continuous variables: n, mean, SD, median, minimum and maximum (or mean±SD/median[IQR] in final SAP); categorical/ordinal variables: n and percentage, with missing values excluded from percentages unless stated otherwise.

## 5. Analysis

### 5.1 Primary Outcomes

**Outcome: Excellent functional outcome at day 90**

- **Definition:** Proportion of participants with mRS score 0–1 (no symptoms or no significant disability) at 90 days after treatment.
- **Measurement Units:** Binary responder status derived from the ordinal mRS 0–6 scale.
- **Timing of Measurement:** Day 91±7 days after thrombolysis; mRS follow-up is assessed by an independent blinded endpoint evaluator.
- **Transformations / Derived Variables:** Main estimand is the reteplase:alteplase response RR; death by the corresponding visit is assigned mRS 6 before deriving the mRS 0–1 response. Other lytic/defibrase use and acute-stroke endovascular treatment are composite-strategy nonresponse; antiplatelet/anticoagulant use within 24h and incomplete/nonconforming treatment use treatment-policy observed outcome.

### 5.2 Secondary Outcomes

**Outcome: NIHSS major neurologic improvement at 24 hours and day 7**

- **Definition:** NIHSS ≤1 or a decrease of ≥4 points from baseline. Protocol V2.2 and SAP v1.1 outcome definition assess this at 24 hours and day 7; SAP v1.1 objectives inconsistently says “at 90 days,” which is retained as a source discrepancy.
- **Measurement Units:** Binary responder derived from NIHSS score.
- **Timing of Measurement:** 24h±2h and D8±1 day after thrombolysis.
- **Transformations / Derived Variables:** Also analyze absolute NIHSS change from baseline at 24h and D7; death by a corresponding visit is assigned NIHSS 42. Under alternate composite handling, the SAP v1.0 applies the stated conservative rule when post-event NIHSS is ≤ baseline or baseline is missing; treatment-policy handling continues observed post-event scores.

**Outcome: Favorable functional outcome at day 90**

- **Definition:** Proportion with mRS 0–2.
- **Measurement Units:** Binary responder derived from mRS 0–6.
- **Timing of Measurement:** Day 91±7 days.
- **Transformations / Derived Variables:** Treatment-policy analysis uses observed post-event mRS. The alternate composite strategy applies the primary-estimand event handling; for mRS 0–2, subjects with a composite-strategy event are direct nonresponders.

**Outcome: Ordinal mRS distribution/shift**

- **Definition:** Distribution of mRS categories 0–6 and continuous change at days 30 and 90.
- **Measurement Units:** Ordinal mRS score 0–6, where 6 is death.
- **Timing of Measurement:** D31±3d and D91±7d, blinded evaluation.
- **Transformations / Derived Variables:** Death by visit is assigned mRS 6. Treatment-policy handling retains observed mRS; alternate composite handling carries mRS ≤3 forward as 3, retains values >3, and assigns missing post-event values as the median of same-type nonmissing mRS. Ordinal logistic analysis estimates common OR, and a day-90 distribution bar chart is planned.

**Outcome: Barthel Index response at day 90**

- **Definition:** Proportion with Barthel Index ≥95.
- **Measurement Units:** Binary responder from Barthel Index score.
- **Timing of Measurement:** Day 91±7d; blind follow-up evaluation.
- **Transformations / Derived Variables:** Death by visit is nonresponse. Treatment-policy handling continues and uses observed day-90 Barthel; alternate composite handling assigns direct failure after the composite event rather than using post-event Barthel.

### 5.3 Analysis Methods

- **Primary Analysis Methods:** In mITT, summarize each group and estimate reteplase:alteplase RR by log-binomial regression with center random effect; use robust Poisson if nonconvergent. Estimate risk difference with identity-binomial regression and NI P with Farrington–Manning score test. NI requires lower RR CI>0.93; superiority requires lower RR CI>1. For secondary efficacy outcomes, use the same binary framework for binary endpoints, ordinal logistic regression for ordinal mRS, and rank-sum for ordinal/categorical outcomes or t-test/nonparametric rank-sum for continuous outcomes; final SAP also specifies Wilcoxon rank-sum for ordinal and chi-square/Fisher exact for categorical comparisons as appropriate.
- **Covariate Adjustment:** SAP v1.0 GEE sensitivity analysis includes age, baseline NIHSS, visit and treatment-by-visit interaction. Its NIHSS-change MMRM includes treatment, visit, age, baseline NIHSS and treatment-by-visit interaction. Final SAP v1.1 specifies center as random effect.
- **Assumption Checks:** Formal assumption checks are not reported for log-binomial, Poisson, ordinal logistic or MMRM models. Reported nonconvergence contingencies are described separately below.
- **Alternative Methods if Assumptions Fail:** Use robust Poisson when log-binomial does not converge. For NIHSS MMRM, if unstructured covariance does not converge, consider Toeplitz or AR(1) and use the structure with smallest AIC.
- **Sensitivity Analyses:** PPS is the secondary efficacy population. For the primary outcome, SAP v1.0 specifies FCS multiple imputation, nonresponder imputation, LOCF, complete-case/no-imputation and tipping-point analyses; repeat under alternate intercurrent-event strategies. Supplementary treatment-policy analysis uses observed day-90 mRS after other lytic/defibrase or endovascular treatment.
- **Subgroup Analyses:** Final SAP v1.1 prespecifies age ≤60/>60, sex, admission NIHSS ≤7/>7, pre-index-stroke mRS, onset-to-needle <3/≥3h, and bridging thrombectomy. SAP v1.0 additionally specifies age 18–60/>60, thrombolysis window ≤3/3–4.5h, baseline mRS 0/1, and exploratory demographic, baseline-disease, and pre-existing/concomitant-disease subgroups if data permit. Assess treatment-by-subgroup interaction.

### 5.4 Missing Data

- **Missing Data Assumptions:** The amendment/change record adds an MNAR sensitivity-analysis description. SAP v1.0 specifies robustness through tipping-point analysis; it does not name a MAR model in the supplied body. General percentages exclude missing values unless otherwise specified.
- **Handling Methods:** Version-specific rules are as follows. V2.2 specifies MI for missing day-90 mRS and sensitivity under different assumptions. SAP v1.0 specifies FCS logistic MI with five completed data sets, PROC MI/MIANALYZE and seed 752571; its model includes treatment, baseline mRS, postbaseline mRS response, age, thrombolysis time, baseline/postbaseline NIHSS and sICH. SAP v1.0 robustness analyses are NRI, LOCF, complete-case/no-imputation and tipping-point analysis, repeated under alternate intercurrent-event strategies. Its outcome-specific derivations assign mRS 6 for death, NIHSS 42 for death, and Barthel nonresponse for death; it separately specifies composite-event nonresponse/carry-forward and treatment-policy observed values. Final SAP v1.1 calls the primary analysis complete case without imputation, then also states FCS logistic-regression MI of day-90 mRS. Thus V2.2 MI, v1.0 sensitivity rules, and v1.1 stated primary rules conflict and require controlled pre-analysis reconciliation; no unstated rule is selected here.

### 5.5 Additional Analyses

Additional analyses include treatment-by-subgroup interactions, alternate intercurrent-event strategies, analyses of risk ratios/risk differences for binary secondary endpoints, ordinal logistic mRS shift analysis, and Kaplan–Meier survival through day 90 with median survival and 95% CI.

### 5.6 Harms

- **Adverse Event Definitions:** An AE is an adverse medical event after trial drug, not necessarily causal. Pre-treatment AEs occur after consent/before dose and are listed but not summarized as TEAEs. TEAEs are post-treatment events or worsening pre-existing symptoms. SAEs include death, life threat, congenital anomaly, persistent/significant disability or organ-function damage, hospitalization/prolongation, and other important medical events. Final SAP v1.1 designates sICH within 36 hours as the primary safety outcome; other safety outcomes are all-cause death at 7 and 90 days, SITS-MOST/ECASS III sICH, ISTH major and clinically relevant nonmajor bleeding within 90 days, and AE/SAE within 90 days.
- **Safety Analysis Methods:** Analyze SS as treated. Important clinical events (sICH, other significant hemorrhage and all-cause death) undergo independent CEC adjudication. Code events with MedDRA v25.1 and summarize TEAEs/TRAE/SAEs/AESIs by treatment, SOC/PT and highest CTCAE grade per subject; include grade ≥3, dose reduction, temporary interruption, permanent discontinuation, SUSAR, ISTH major/clinically relevant nonmajor/minor bleeding, and ECASS III/SITS-MOST sICH. Assess all-cause death at 7 and 90 days and ALT≥3×ULN with TBIL≥2×ULN and creatinine ≥3× baseline or ≥4 mg/dL within 7 days. Summarize causes and windows of death, censoring and 90-day Kaplan–Meier survival; for common bleeding PTs, summarize time to first event, outcome and duration. Summarize scheduled/unscheduled laboratory, vital-sign, ECG, imaging and physical-examination results and shifts/lists as specified.
- **Grading Scales and Causality:** Grade severity by NCI CTCAE v5.0, grades 1–5. Causality categories are certainly/probably/possibly related or possibly/certainly unrelated. AESIs include sICH, ISTH major bleeding, ALT≥3×ULN with TBIL≥2×ULN, and creatinine ≥3× baseline or ≥4 mg/dL within 7 days. SITS-MOST and ECASS III define sICH; ISTH defines major, clinically relevant nonmajor, and mild bleeding.

### 5.7 Software and References

- **Statistical Software:** SAS 9.4 or higher for randomization and data processing/summarization/analysis; final SAP v1.1 names SAS 9.4 for analysis.
- **Other Referenced Documents:** Protocol CRAD-001-03 V2.2 (17 Nov 2022); SAP v1.0 (7 Aug 2023); final academic SAP v1.1 (15 Aug 2023). The IDMC/DSMB charter, independent CEC charter, and separate TLF template are referenced but not included in this document.

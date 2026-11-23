# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale

Acute ischemic stroke (AIS) produces neurologic impairment, disability and mortality. This phase III study evaluates genetically engineered recombinant human tissue-type plasminogen activator derivative (reteplase), a bolus-administered thrombolytic, against alteplase for AIS treated within 4.5 hours of symptom onset. *(Source: Protocol V2.2 Background and Study Design, pages 103–114; SAP v1.1 Introduction, page 279)*

### 1.2 Objectives

**Primary Objectives**

- Evaluate reteplase versus alteplase effectiveness for AIS within 4.5 hours, operationalized as the difference in the proportion with mRS 0–1 at day 90. *(Source: Protocol V2.2 Objectives and endpoints, pages 103, 120; SAP v1.1 Objectives, page 280)*

**Secondary Objectives**

- Evaluate safety and secondary functional and neurologic outcomes of reteplase versus alteplase, including favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, AE/SAE and death outcomes. *(Source: Protocol V2.2 endpoints, pages 120–121; SAP v1.1 Objectives, pages 280–281)*

**Exploratory Objectives**

Not reported in protocol as a separately labelled objective. *(Source: pages 1–287 reviewed)*

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Multicenter, prospective, randomized, open-label with blinded endpoint assessment, positive active-controlled parallel-group phase III noninferiority trial in Chinese patients with AIS within 4.5 hours of onset. *(Source: Protocol V2.2 Study Design, pages 113–114; SAP v1.1 Study Overview, page 279)*
- **Allocation Ratio:** 1:1 reteplase:alteplase. *(Source: Protocol V2.2 Study Design, page 113; SAP v1.1 Study Design, page 279)*
- **Intervention Summary:** Thrombolysis must begin within 4.5 hours of last known well.
  - Reteplase group: 18 mg IV bolus followed by a second 18 mg IV bolus 30±5 minutes after completion of the first; each injection lasts at least 2 minutes.
  - Alteplase group: 0.9 mg/kg IV (maximum 90 mg), 10% as a bolus within 1 minute and the remainder infused over 60 minutes. *(Source: Protocol V2.2 Trial Grouping and Dosing, pages 118–120; SAP v1.1 Study Design, page 279)*

### 2.2 Randomization

- **Method:** An independent statistician generates the random numbers in SAS 9.4 or higher. After eligibility, the investigator uses IWRS to obtain the allocation; random numbers of withdrawn participants are retained and cannot be replaced or reused. *(Source: Protocol V2.2 Subject Allocation and Numbering, pages 137–138; SAP v1.0 Randomization, page 255)*
- **Stratification Factors:** SAP v1.0 describes simple stratified randomization but names no factors. Final Protocol V2.2 instead specifies variable-block 1:1 randomization without describing stratification; no individual factor is reported. *(Source: SAP v1.0 Randomization and Blinding, page 255; Protocol V2.2 Subject Allocation and Numbering, pages 137–138; pages 1–287 reviewed)*
- **Minimization or Blocking:** Variable-block randomization in a 1:1 ratio; the initial random-number seed parameters are retained. *(Source: Protocol V2.2 Subject Allocation and Numbering, pages 137–138)*

### 2.3 Sample Size

- **Planned Sample Size:** 1,412 participants, 706 per group. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167; SAP v1.0 Sample Size, pages 254–255)*
- **Outcome Used for Calculation:** Proportion with mRS 0–1 at day 90 after treatment. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167; SAP v1.0 Sample Size, page 254)*
- **Outcome Type:** Binary excellent functional outcome. *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*
- **Assumed Control-Arm Value:** Alteplase primary efficacy proportion 62.5%. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167; SAP v1.0 Sample Size, page 254)*
- **Assumed Treatment-Arm Value:** Assumed true reteplase:alteplase efficacy RR 1.05. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*
- **Target Difference / Effect Size:** NI margin is RR 0.93; it was derived from historical alteplase versus placebo lower 95% CI RR 1.15 with f=0.5. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167; SAP v1.0 Sample Size, page 254)*
- **Variability Assumption:** Not applicable for the binary proportion/RR calculation. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*
- **Alpha (Significance Level):** One-sided 0.025. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*
- **Power:** 80% in Protocol V2.2 and SAP v1.0. SAP v1.1 instead reports 85%; this discrepancy is retained for reconciliation before analysis. *(Source: Protocol V2.2, page 167; SAP v1.0, page 254; SAP v1.1, pages 282–283)*
- **Statistical Test Assumed:** One-sided noninferiority RR test, with NI demonstrated by lower CI bound above 0.93. *(Source: SAP v1.0 Statistical Hypotheses, pages 255–257; SAP v1.1 Statistical Hypotheses, page 282)*
- **Required Number of Events:** No event-count requirement for the primary binary endpoint. The safety rationale estimates sICH 1% and death 5%, with >99% probability of observing at least one death or sICH. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*
- **Non-Inferiority / Equivalence Margin:** RR 0.93. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*
- **Dropout / Non-Adherence Inflation:** Approximately 15% in Protocol V2.2/SAP v1.0; SAP v1.1 reports 3%, a discrepancy requiring reconciliation. *(Source: Protocol V2.2, page 167; SAP v1.0, page 254; SAP v1.1, page 283)*
- **Design Effect / Clustering:** Not applicable to sample-size calculation; clustering is addressed as a random center effect in analysis. *(Source: SAP v1.1 Multicenter Data, page 284)*
- **Basis for Assumptions:** Prior alteplase trials and Phase II reteplase data; SITS-MOST for sICH and NOR-TEST for death. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167; SAP v1.0 Sample Size, pages 254–255)*
- **Sample Size Re-Estimation / Amendments:** Original Protocol V1.0 planned Mehta–Pocock re-estimation conditional on interim efficacy 50%–80%. V2.2 does not retain that interim procedure, and SAP v1.0/v1.1 state no interim efficacy analysis; this version-specific conflict must be settled before execution. *(Source: original Protocol V1.0 Interim Analysis, pages 25, 36; Protocol V2.2 Statistical Analysis, pages 121–124; SAP v1.0 and SAP v1.1, pages 275, 282)*
- **Software Used for Calculation:** Not reported in protocol. *(Source: pages 1–287 reviewed)*
- **Sample Size Rationale:** The 1:1 sample targets NI for day-90 mRS 0–1 while providing substantial probability of observing key safety events. *(Source: Protocol V2.2 Statistical Hypothesis and Sample Size Estimation, page 167)*

### 2.4 Hypothesis Framework

The primary hypothesis is H0: RR≤0.93 versus H1: RR>0.93, where RR is the day-90 mRS 0–1 rate in reteplase divided by that in alteplase. NI is concluded at one-sided P<0.025 or lower RR 95% CI bound >0.93; superiority is then concluded if the lower RR CI bound is >1. *(Source: SAP v1.0 Estimand and primary analysis, pages 255–257, 263–264; SAP v1.1 Statistical Hypotheses and Primary Analysis, pages 282, 285)*

### 2.5 Statistical Interim Analyses

- **Interim Analyses Planned:** Original Protocol V1.0 specifies one IDMC efficacy analysis after 60% complete day-90 mRS. V2.2 does not retain an interim procedure, while SAP v1.0 and final SAP v1.1 state no interim efficacy analysis; v1.1 retains regular unblinded DSMB safety tables. This conflict is not resolved in the supplied documents. *(Source: original Protocol V1.0 Interim Analysis, pages 25, 36; Protocol V2.2 Statistical Analysis, pages 121–124; SAP v1.0 Planned Analysis, page 275; SAP v1.1 Interim Analyses, pages 282, 286)*
- **Stopping Guidelines:** V2.2 retains an IDMC for cumulative-data safety assessment; its procedures and operating cycle are in its charter. Final SAP v1.1 says DSMB safety concerns may lead to a modification/stop recommendation, with the Steering Committee and sponsor deciding whether to act. V2.2’s broader termination criteria include risk–benefit concerns, noncompliance, design errors, slow recruitment, and authority/ethics direction. *(Source: Protocol V2.2 IDMC and Early Termination, pages 114, 117–118; SAP v1.1 Interim Analyses, page 282)*
- **Alpha Spending or Adjustment:** Original Protocol V1.0 alone specifies O’Brien–Fleming one-sided spending of approximately .00381 interim and .02380 final. This superseded efficacy-interim design was cancelled before V2.2 and is not an active multiplicity adjustment; final SAP v1.1 specifies no interim efficacy analysis. *(Source: original Protocol V1.0 Interim Analysis, pages 25, 36; Protocol amendment summary, pages 211–218; SAP v1.1 Interim Analyses and Multiplicity, pages 282, 284)*

### 2.6 Timing of Analyses

- **Final Analysis Timing:** Conduct after end of the entire trial and after database lock, protocol-violation identification and treatment unblinding. *(Source: SAP v1.0 Planned Analyses, pages 255, 275; SAP v1.1 Planned Analyses, page 282)*
- **Outcome Assessment Schedule:** Screening/D1; 24h±2h; 72h±6h; D8±1d; D31±3d; and D91±7d. NIHSS is assessed at baseline, 24h and D8; mRS and Barthel at D31 and D91, with blinded endpoint evaluation at follow-up. *(Source: Protocol V2.2 Trial Flow Chart and procedures, pages 125–126, 145–147)*

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **Alpha Level:** Unless otherwise specified, two-sided alpha .05 and two-sided 95% CIs apply; the primary NI comparison uses one-sided alpha .025. *(Source: Protocol V2.2 Statistical Analysis, page 167; SAP v1.1 Statistical Hypotheses, page 282)*
- **Multiplicity Adjustment:** SAP v1.1 states no adjustment is required because there is one primary efficacy outcome and one treatment comparison; all secondary efficacy outcomes are unadjusted and exploratory. *(Source: SAP v1.1 General Principles and Multiplicity, page 284)*
- **Confidence Intervals:** Primary and secondary effect estimates use 95% CIs; the primary decision uses the lower RR CI bound against 0.93 and then 1. *(Source: SAP v1.0 Primary Analysis, pages 263–264; SAP v1.1 Primary and Secondary Analyses, pages 285–286)*

### 3.2 Protocol Deviations

- **Adherence Definition:** Compliance is determined from recorded number, date, actual dose, and administration start/end times. *(Source: Protocol V2.2 Medication Compliance, page 135)*
- **Adherence Assessment:** Record exposure, dosing interval/duration, interruptions and infusion reactions; calculate adherence as actual dose/planned dose ×100%, categorized <80%, 80%–120% or >120%. PPS review separately considers main-eligibility failure, seriously interfering concomitant treatment, poor compliance and early permanent discontinuation. *(Source: Protocol V2.2 Medication Compliance, page 144; SAP v1.0 Medication Adherence and Drug Exposure, page 262; SAP v1.1 Analysis Sets, page 283)*
- **Protocol Deviation Definition:** Serious violations are not exhaustively pre-specified; their definition is confirmed at data review. *(Source: SAP v1.1 Analysis Sets, page 283)*
- **Protocol Deviation Reporting:** Study personnel document deviations and explanations. Emergency deviations are promptly reported to the ethics committee and sponsor, and to regulatory authorities when necessary. CRA monitoring reports communicate deviations, deficiencies, actions and conclusions to the sponsor. Final deviations are discussed before lock and documented in data-review minutes; SAP v1.0 classifies deviations as mild or major, tabulates all and major deviations by treatment, provides listings, and identifies reasons for analysis-set exclusion. *(Source: Protocol V2.2 Data Review Meeting and Compliance/Deviations, pages 171, 176–177; SAP v1.0 Protocol Deviation and Subject Distribution, pages 259–260)*

### 3.3 Analysis Populations

- **Intention-to-Treat:** Modified ITT includes randomized participants who received at least one trial-drug dose and basically met main eligibility; analyze according to randomized group. *(Source: Protocol V2.2 ITT, page 167; SAP v1.0 Estimand, page 255; SAP v1.1 Analysis Sets, page 283)*
- **Per Protocol:** PPS includes participants completing the study without serious protocol violation; analyze according to treatment received when treatment was received throughout. It is the secondary efficacy population. *(Source: SAP v1.1 Analysis Sets, page 283)*
- **Other Populations:** The randomized population (all randomized participants) is used for disposition and denominator reporting. Safety Set includes randomized, treated participants with evaluable post-treatment safety data and is analyzed as treated. *(Source: Protocol V2.2 Safety Set, pages 167–168; SAP v1.0 Analysis Data Set and Subject Distribution, pages 258–260; SAP v1.1 Analysis Sets, pages 283–284)*

## 4. Trial Population

### 4.1 Screening Data

Screening captures informed consent; demographics; weight; medical, treatment and allergy history; pre-stroke mRS and NIHSS; cranial CT/MRI; glucose, hematology, biochemistry, coagulation and pregnancy testing as applicable; ECG; eligibility; randomization; concomitant treatment; and AEs. Screening failures are participants who withdraw between consent and randomization; list them with reasons, record demographics, failure reason, eligibility information and any SAE in the eCRF, and exclude them from other analyses. Post-onset external CT and blood-count findings may be accepted, and traceable post-onset assessments obtained before consent can be used as screening data rather than repeated. *(Source: Protocol V2.2 Trial Flow Chart Notes and Screening/Allocation, pages 125–128, 141–145; SAP v1.0 Subject Distribution, pages 259–260)*

### 4.2 Eligibility Criteria Summary

Eligible participants are 18–80 years, have WHO-defined AIS within 4.5 hours of last known well, NIHSS 4–25 before thrombolysis, agree to contraception where applicable, can comply, and provide participant or guardian consent. Exclusions include non-ascertainable onset, weight <45 or >120 kg, pre-stroke mRS≥2, NIHSS consciousness item 1a≥2, hemorrhage/imaging/anticoagulation risks, uncontrolled blood pressure, out-of-range glucose, large infarction, important hepatic or other comorbidity, planned/received endovascular treatment, interfering treatments, recent trial participation, pregnancy/lactation, and investigator-determined barriers to compliance. *(Source: Protocol V2.2 Inclusion and Exclusion Criteria, pages 115–117)*

### 4.3 Recruitment

The study plans to recruit 1,412 Chinese participants with AIS within 4.5 hours at multiple centers. The original protocol projected conduct from October 2021 through March 2025. *(Source: Protocol V2.2 Study Design, pages 113–114; original Protocol Synopsis, page 25)*

### 4.4 Withdrawal and Follow-up

- **Withdrawal Levels:** Voluntary withdrawal includes consent withdrawal or loss to follow-up after at least three contact attempts. Investigator withdrawal may follow pregnancy, post-randomization discovery of non-AIS, or another investigator-determined need before thrombolysis. *(Source: Protocol V2.2 Early Withdrawal Criteria, page 117)*
- **Withdrawal Data Collection:** Complete subsequent safety and efficacy visits where possible; record the reason, last visit, and available data in medical records/eCRF. Follow AEs through recovery, improvement, stabilization, or loss to follow-up. *(Source: Protocol V2.2 Withdrawal and AE Follow-up, pages 135–138, 160–165)*
- **Reasons for Withdrawal:** Under V2.2, withdrawal reasons include consent withdrawal, loss to follow-up, pregnancy, post-randomization ineligibility/non-AIS, and other investigator-determined conditions; withdrawn participants are neither replaced nor re-enrolled. Original V1.0 additionally classified endovascular treatment as voluntary withdrawal with no further follow-up, and permitted investigator withdrawal for serious deviation, allergy, AE-related inability to continue, and post-treatment ineligibility. The V2.2 rules are the current protocol rules. *(Source: Protocol V2.2 Early Withdrawal and Allocation, pages 117, 137–138; original Protocol V1.0 Withdrawal, page 40)*

### 4.5 Baseline Characteristics

- **Baseline Variables:** Birth date, sex, nationality/ethnicity, weight, disease characteristics, medical and medication history, allergy history, pre-stroke mRS, baseline NIHSS, vital signs, imaging, laboratory tests and ECG are collected before randomization or dosing as scheduled. SAP summaries additionally identify onset duration (minutes), thrombolytic time-window category, baseline NIHSS and mRS categories, TOAST classification and localization diagnosis by treatment group. *(Source: Protocol V2.2 Trial Flow Chart and detailed indicators, pages 125–126, 145–153; SAP v1.0 Demographic and Baseline Characteristics, page 260)*
- **Summary Methods:** Continuous variables: n, mean, SD, median, minimum and maximum (or mean±SD/median[IQR] in final SAP); categorical/ordinal variables: n and percentage, with missing values excluded from percentages unless stated otherwise. *(Source: Protocol V2.2 Statistical Analysis, page 167; SAP v1.1 General Principles, page 284)*

## 5. Analysis

### 5.1 Primary Outcomes

**Outcome: Excellent functional outcome at day 90** *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*

- **Definition:** Proportion of participants with mRS score 0–1 (no symptoms or no significant disability) at 90 days after treatment. *(Source: Protocol V2.2 endpoints, page 120; mRS Appendix, pages 83–84)*
- **Measurement Units:** Binary responder status derived from the ordinal mRS 0–6 scale. *(Source: SAP v1.1 Outcomes, page 281; Protocol V2.2 mRS Appendix, pages 83–84)*
- **Timing of Measurement:** Day 91±7 days after thrombolysis; mRS follow-up is assessed by an independent blinded endpoint evaluator. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Transformations / Derived Variables:** Main estimand is the reteplase:alteplase response RR; death by the corresponding visit is assigned mRS 6 before deriving the mRS 0–1 response. Other lytic/defibrase use and acute-stroke endovascular treatment are composite-strategy nonresponse; antiplatelet/anticoagulant use within 24h and incomplete/nonconforming treatment use treatment-policy observed outcome. *(Source: SAP v1.0 Main Estimand and Main Analysis, pages 255–258, 263)*

### 5.2 Secondary Outcomes

**Outcome: NIHSS major neurologic improvement at 24 hours and day 7** *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*

- **Definition:** NIHSS ≤1 or a decrease of ≥4 points from baseline. Protocol V2.2 and SAP v1.1 outcome definition assess this at 24 hours and day 7; SAP v1.1 objectives inconsistently says “at 90 days,” which is retained as a source discrepancy. *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Objectives and Outcomes, pages 280–281)*
- **Measurement Units:** Binary responder derived from NIHSS score. *(Source: Protocol V2.2 NIHSS Appendix, pages 85–92)*
- **Timing of Measurement:** 24h±2h and D8±1 day after thrombolysis. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Transformations / Derived Variables:** Also analyze absolute NIHSS change from baseline at 24h and D7; death by a corresponding visit is assigned NIHSS 42. Under alternate composite handling, the SAP v1.0 applies the stated conservative rule when post-event NIHSS is ≤ baseline or baseline is missing; treatment-policy handling continues observed post-event scores. *(Source: SAP v1.0 Secondary Estimands, pages 265–268)*

**Outcome: Favorable functional outcome at day 90** *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*

- **Definition:** Proportion with mRS 0–2. *(Source: Protocol V2.2 endpoints, page 120)*
- **Measurement Units:** Binary responder derived from mRS 0–6. *(Source: Protocol V2.2 mRS Appendix, pages 83–84)*
- **Timing of Measurement:** Day 91±7 days. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Transformations / Derived Variables:** Treatment-policy analysis uses observed post-event mRS. The alternate composite strategy applies the primary-estimand event handling; for mRS 0–2, subjects with a composite-strategy event are direct nonresponders. *(Source: SAP v1.0 Secondary Estimands, pages 267–268)*

**Outcome: Ordinal mRS distribution/shift** *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*

- **Definition:** Distribution of mRS categories 0–6 and continuous change at days 30 and 90. *(Source: Protocol V2.2 endpoints, page 120)*
- **Measurement Units:** Ordinal mRS score 0–6, where 6 is death. *(Source: Protocol V2.2 mRS Appendix, pages 83–84)*
- **Timing of Measurement:** D31±3d and D91±7d, blinded evaluation. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Transformations / Derived Variables:** Death by visit is assigned mRS 6. Treatment-policy handling retains observed mRS; alternate composite handling carries mRS ≤3 forward as 3, retains values >3, and assigns missing post-event values as the median of same-type nonmissing mRS. Ordinal logistic analysis estimates common OR, and a day-90 distribution bar chart is planned. *(Source: SAP v1.0 Secondary Estimands, pages 268–269; SAP v1.1 Secondary Analyses, pages 285–286)*

**Outcome: Barthel Index response at day 90** *(Source: Protocol V2.2 endpoints, page 120; SAP v1.1 Outcomes, page 281)*

- **Definition:** Proportion with Barthel Index ≥95. *(Source: Protocol V2.2 endpoints, page 120)*
- **Measurement Units:** Binary responder from Barthel Index score. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Timing of Measurement:** Day 91±7d; blind follow-up evaluation. *(Source: Protocol V2.2 Flow Chart, pages 125–126)*
- **Transformations / Derived Variables:** Death by visit is nonresponse. Treatment-policy handling continues and uses observed day-90 Barthel; alternate composite handling assigns direct failure after the composite event rather than using post-event Barthel. *(Source: SAP v1.0 Secondary Estimands, pages 269–270)*

### 5.3 Analysis Methods

- **Primary Analysis Methods:** In mITT, summarize each group and estimate reteplase:alteplase RR by log-binomial regression with center random effect; use robust Poisson if nonconvergent. Estimate risk difference with identity-binomial regression and NI P with Farrington–Manning score test. NI requires lower RR CI>0.93; superiority requires lower RR CI>1. For secondary efficacy outcomes, use the same binary framework for binary endpoints, ordinal logistic regression for ordinal mRS, and rank-sum for ordinal/categorical outcomes or t-test/nonparametric rank-sum for continuous outcomes; final SAP also specifies Wilcoxon rank-sum for ordinal and chi-square/Fisher exact for categorical comparisons as appropriate. *(Source: Protocol V2.2 Efficacy Analysis, pages 168–169; SAP v1.1 General Considerations and Efficacy Analyses, pages 284–286)*
- **Covariate Adjustment:** SAP v1.0 GEE sensitivity analysis includes age, baseline NIHSS, visit and treatment-by-visit interaction. Its NIHSS-change MMRM includes treatment, visit, age, baseline NIHSS and treatment-by-visit interaction. Final SAP v1.1 specifies center as random effect. *(Source: Protocol V2.2 Efficacy Analysis, pages 168–169; SAP v1.0 Adjustment and sensitivity analyses, pages 259, 263–267; SAP v1.1 pages 284–286)*
- **Assumption Checks:** Formal assumption checks are not reported for log-binomial, Poisson, ordinal logistic or MMRM models. Reported nonconvergence contingencies are described separately below. *(Source: pages 1–287 reviewed)*
- **Alternative Methods if Assumptions Fail:** Use robust Poisson when log-binomial does not converge. For NIHSS MMRM, if unstructured covariance does not converge, consider Toeplitz or AR(1) and use the structure with smallest AIC. *(Source: SAP v1.0 Secondary Estimands, pages 265–267; SAP v1.1 Primary Analysis, page 285)*
- **Sensitivity Analyses:** PPS is the secondary efficacy population. For the primary outcome, SAP v1.0 specifies FCS multiple imputation, nonresponder imputation, LOCF, complete-case/no-imputation and tipping-point analyses; repeat under alternate intercurrent-event strategies. Supplementary treatment-policy analysis uses observed day-90 mRS after other lytic/defibrase or endovascular treatment. *(Source: Protocol V2.2 Efficacy Analysis, pages 168–169; SAP v1.0 pages 260, 264–270; SAP v1.1 page 283)*
- **Subgroup Analyses:** Final SAP v1.1 prespecifies age ≤60/>60, sex, admission NIHSS ≤7/>7, pre-index-stroke mRS, onset-to-needle <3/≥3h, and bridging thrombectomy. SAP v1.0 additionally specifies age 18–60/>60, thrombolysis window ≤3/3–4.5h, baseline mRS 0/1, and exploratory demographic, baseline-disease, and pre-existing/concomitant-disease subgroups if data permit. Assess treatment-by-subgroup interaction. *(Source: SAP v1.0 Subgroup Analysis, pages 259, 265; SAP v1.1 Objectives and Subgroup Analyses, pages 280, 286)*

### 5.4 Missing Data

- **Missing Data Assumptions:** The amendment/change record adds an MNAR sensitivity-analysis description. SAP v1.0 specifies robustness through tipping-point analysis; it does not name a MAR model in the supplied body. General percentages exclude missing values unless otherwise specified. *(Source: Protocol amendment summary, page 240; SAP v1.0 Missing Data and Sensitivity Analysis, pages 260, 266; Protocol V2.2 Statistical Analysis, page 167)*
- **Handling Methods:** Version-specific rules are as follows. V2.2 specifies MI for missing day-90 mRS and sensitivity under different assumptions. SAP v1.0 specifies FCS logistic MI with five completed data sets, PROC MI/MIANALYZE and seed 752571; its model includes treatment, baseline mRS, postbaseline mRS response, age, thrombolysis time, baseline/postbaseline NIHSS and sICH. SAP v1.0 robustness analyses are NRI, LOCF, complete-case/no-imputation and tipping-point analysis, repeated under alternate intercurrent-event strategies. Its outcome-specific derivations assign mRS 6 for death, NIHSS 42 for death, and Barthel nonresponse for death; it separately specifies composite-event nonresponse/carry-forward and treatment-policy observed values. Final SAP v1.1 calls the primary analysis complete case without imputation, then also states FCS logistic-regression MI of day-90 mRS. Thus V2.2 MI, v1.0 sensitivity rules, and v1.1 stated primary rules conflict and require controlled pre-analysis reconciliation; no unstated rule is selected here. *(Source: Protocol V2.2 Efficacy Analysis, page 168; SAP v1.0 Missing Data and Sensitivity Analyses, pages 260, 264–270; SAP v1.1 Missing Data and Primary Analysis, pages 284–285)*

### 5.5 Additional Analyses

Additional analyses include treatment-by-subgroup interactions, alternate intercurrent-event strategies, analyses of risk ratios/risk differences for binary secondary endpoints, ordinal logistic mRS shift analysis, and Kaplan–Meier survival through day 90 with median survival and 95% CI. *(Source: Protocol V2.2 Safety Analysis, page 169; SAP v1.0 pages 264–270, 273–275; SAP v1.1 pages 285–286)*

### 5.6 Harms

- **Adverse Event Definitions:** An AE is an adverse medical event after trial drug, not necessarily causal. Pre-treatment AEs occur after consent/before dose and are listed but not summarized as TEAEs. TEAEs are post-treatment events or worsening pre-existing symptoms. SAEs include death, life threat, congenital anomaly, persistent/significant disability or organ-function damage, hospitalization/prolongation, and other important medical events. Final SAP v1.1 designates sICH within 36 hours as the primary safety outcome; other safety outcomes are all-cause death at 7 and 90 days, SITS-MOST/ECASS III sICH, ISTH major and clinically relevant nonmajor bleeding within 90 days, and AE/SAE within 90 days. *(Source: Protocol V2.2 AE Definitions and Safety Endpoints, pages 120–121, 154–162; SAP v1.0 Safety Analysis, pages 270–271; SAP v1.1 Objectives and Outcomes, pages 280–281)*
- **Safety Analysis Methods:** Analyze SS as treated. Important clinical events (sICH, other significant hemorrhage and all-cause death) undergo independent CEC adjudication. Code events with MedDRA v25.1 and summarize TEAEs/TRAE/SAEs/AESIs by treatment, SOC/PT and highest CTCAE grade per subject; include grade ≥3, dose reduction, temporary interruption, permanent discontinuation, SUSAR, ISTH major/clinically relevant nonmajor/minor bleeding, and ECASS III/SITS-MOST sICH. Assess all-cause death at 7 and 90 days and ALT≥3×ULN with TBIL≥2×ULN and creatinine ≥3× baseline or ≥4 mg/dL within 7 days. Summarize causes and windows of death, censoring and 90-day Kaplan–Meier survival; for common bleeding PTs, summarize time to first event, outcome and duration. Summarize scheduled/unscheduled laboratory, vital-sign, ECG, imaging and physical-examination results and shifts/lists as specified. *(Source: Protocol V2.2 CEC and Safety Endpoints, pages 114, 120–121; SAP v1.0 pages 270–275; SAP v1.1 pages 280–281, 286)*
- **Grading Scales and Causality:** Grade severity by NCI CTCAE v5.0, grades 1–5. Causality categories are certainly/probably/possibly related or possibly/certainly unrelated. AESIs include sICH, ISTH major bleeding, ALT≥3×ULN with TBIL≥2×ULN, and creatinine ≥3× baseline or ≥4 mg/dL within 7 days. SITS-MOST and ECASS III define sICH; ISTH defines major, clinically relevant nonmajor, and mild bleeding. *(Source: Protocol V2.2 pages 159–164; SAP v1.0 pages 270–274)*

### 5.7 Software and References

- **Statistical Software:** SAS 9.4 or higher for randomization and data processing/summarization/analysis; final SAP v1.1 names SAS 9.4 for analysis. *(Source: Protocol V2.2 pages 137, 167; SAP v1.1 General Principles, page 284)*
- **Other Referenced Documents:** Protocol CRAD-001-03 V2.2 (17 Nov 2022); SAP v1.0 (7 Aug 2023); final academic SAP v1.1 (15 Aug 2023). The IDMC/DSMB charter, independent CEC charter, and separate TLF template are referenced but not included in this document. *(Source: Protocol V2.2 IDMC/CEC, page 114; SAP v1.0 pages 247–249, 275–276; SAP v1.1 pages 277–287)*

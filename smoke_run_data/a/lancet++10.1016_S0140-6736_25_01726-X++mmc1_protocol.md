# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale
POInT is a phase IIb primary-prevention trial in genetically at-risk infants. It tests whether sustained oral exposure to insulin during the usual period of initiation of beta-cell autoimmunity induces immune tolerance and reduces beta-cell autoimmunity and diabetes.

### 1.2 Objectives

**Primary Objectives**
- Determine whether daily oral insulin from age 4-7 months to age 3 years reduces cumulative incidence of beta-cell autoantibodies and diabetes in childhood.

**Secondary Objectives**
- Compare development of any persistent confirmed beta-cell autoantibody, persistent confirmed IAA, persistent confirmed GADA, and dysglycaemia or diabetes.

**Exploratory Objectives**
- Assess treatment effects in subgroups and in immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures; assess type 1 diabetes and progression from seroconversion to clinical type 1 diabetes.

## 2. Study Methods

### 2.1 Trial Design
- **Design Type:** Investigator-initiated, multicentre, multinational, randomized, double-blind, placebo-controlled, phase IIb primary-prevention study.
- **Allocation Ratio:** 1:1 oral insulin:placebo.
- **Intervention Summary:** Daily parent-administered oral capsule, preferably 07:00-10:00; treatment ends the day before the age-3 visit or with clinical diabetes.
  - Oral-insulin arm: 7.5 mg for 2 months, then 22.5 mg for 2 months, then 67.5 mg until age 3 years; human recombinant insulin crystals plus microcrystalline cellulose to total capsule weight 200 mg, in a 0.5-mL hard gelatin capsule.
  - Placebo arm: matching microcrystalline-cellulose capsule daily until age 3 years.

### 2.2 Randomization
- **Method:** Package-number randomization by the study-drug manufacturer; a separate randomization list assigns multiples to the same arm.
- **Stratification Factors:** Not reported in protocol.
- **Minimization or Blocking:** Not reported in protocol.

### 2.3 Sample Size
- **Planned Sample Size:** 1,050 infants allocated 1:1; the original design projected 1,040 and the completed enrollment was 1,050.
- **Outcome Used for Calculation:** Persistent confirmed multiple beta-cell autoantibodies or diabetes.
- **Outcome Type:** Time-to-event/hazard-rate outcome.
- **Assumed Control-Arm Value:** 7.5% event probability at 3.5 years, corresponding under an exponential distribution to hazard 0.02227; the later blinded re-estimate used placebo hazard 0.02456.
- **Assumed Treatment-Arm Value:** Hazard halved versus placebo (originally 0.011135; later scenario 0.01228).
- **Target Difference / Effect Size:** 50% risk reduction/hazard-rate reduction.
- **Variability Assumption:** Exponential time-to-event distribution.
- **Alpha (Significance Level):** Two-sided overall 0.05.
- **Power:** 80%; the October 2021 update projected 81.3% under the observed total hazard and halved treatment hazard.
- **Statistical Test Assumed:** Two-sided log-rank test of equal hazard rates.
- **Required Number of Events:** Not reported in protocol.
- **Non-Inferiority / Equivalence Margin:** Not applicable; superiority framework.
- **Dropout / Non-Adherence Inflation:** 20% anticipated dropout; October 2021 extrapolation was 12% (95% CI 8-15%).
- **Design Effect / Clustering:** Not applicable; individually randomized trial.
- **Basis for Assumptions:** Expected primary-outcome frequency, exponential hazard model, 3.5-year accrual and follow-up, and anticipated dropout; update used observed blinded dropout, accrual, and event-rate information.
- **Sample Size Re-Estimation / Amendments:** Blinded power calculation updated in October 2021; no power issue was judged to prevent trial end six months after last treatment.
- **Software Used for Calculation:** PROC POWER, SAS 9.4, based on the Lakatos formula for the updated calculation.
- **Sample Size Rationale:** The original calculation required 832 completely followed children, uniformly randomized over 3.5 years and followed another 3.5 years, for 80% power; 1,040 were to be randomized after 20% dropout. All randomized children, including those contributing observation time to dropout, contribute to the primary analysis. The completed accrual was 3.17 years with 3.25-year follow-up.

### 2.4 Hypothesis Framework
Primary and secondary endpoints are superiority endpoints. The primary null compares equal hazard rates; the primary confirmatory comparison is oral insulin versus placebo for persistent confirmed multiple beta-cell autoantibodies or diabetes.

### 2.5 Statistical Interim Analyses
- **Interim Analyses Planned:** No; the formerly planned interim analysis was cancelled. DSMB safety/efficacy reviews remain six-monthly.
- **Stopping Guidelines:** DSMB may recommend continuation, modification, suspension, or termination; guidelines include a significant >1.7-fold excess of multiple autoantibodies, >2-fold excess diabetes, statistically significant effect, or over-morbidity criteria.
- **Alpha Spending or Adjustment:** The amendment summary says the interim analysis was cancelled and SAP V1.0 says no multiplicity adjustment. Protocol V4 nevertheless retains legacy wording that the primary-analysis critical value and confidence intervals are determined by a group-sequential procedure; the supplied documents do not reconcile this versioned inconsistency.

### 2.6 Timing of Analyses
- **Final Analysis Timing:** After the observation period defined as six months after the last participant’s last treatment day (expected June 2024), final data export, and quality control; database lock was October 23, 2024.
- **Outcome Assessment Schedule:** Eight intervention visits from baseline through age 3 years and up to nine post-age-3 follow-up visits; blood for autoantibodies at every visit. Persistent-autoantibody-positive children undergo OGTTs from age 3 years at six-month intervals.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals
- **Alpha Level:** All testing is two-sided at 0.05.
- **Multiplicity Adjustment:** None; only primary-outcome testing is confirmatory and all other hypothesis testing is exploratory.
- **Confidence Intervals:** 95% confidence intervals; primary results include hazard ratios and cumulative incidences at years 1-7 with 95% confidence intervals. Protocol V4 retains wording that primary critical values and confidence intervals are determined by a group-sequential procedure, whereas the amendment cancelled interim analysis and SAP V1.0 specifies no multiplicity adjustment; the documents do not reconcile this versioned inconsistency.

### 3.2 Protocol Deviations
- **Adherence Definition:** Percentage adherence equals capsules taken divided by capsules expected, multiplied by 100; expected capsules use either pre-scheduled treatment duration (absolute) or actual treatment duration (relative).
- **Adherence Assessment:** Returned capsules are counted and checked against two records; adherence is summarized overall and by arm, including the proportion reaching 85%. Absolute and relative adherence for each participant are plotted by study arm.
- **Protocol Deviation Definition:** Minor and major deviations/violations are classified before unblinding; prespecified violations are missed visits, missing autoantibody blood samples, inclusion/exclusion errors, and expired IMP administration.
- **Protocol Deviation Reporting:** Numbers and percentages with minor/major deviations and each prespecified violation are reported by arm using the ITT denominator.

### 3.3 Analysis Populations
- **Intention-to-Treat:** All randomized children receiving at least one medication dose, analyzed as randomized. The primary full-analysis set is modified ITT excluding children multiple-autoantibody positive at baseline; those children enter primary ITT sensitivity analysis.
- **Per Protocol:** Randomized children administered at least 85% of expected capsules through age 3 years or, if primary outcome occurred before age 3, through the visit defining primary-outcome positivity.
- **Other Populations:** Safety population is all randomized children receiving at least one dose, analyzed as treated. For secondary outcomes, baseline-positive children are excluded for any-autoantibody and respective IAA/GADA analyses but included for dysglycaemia/type 1 diabetes.

## 4. Trial Population

### 4.1 Screening Data
Participants are recruited from GPPAD-02. The percentage of eligible children participating is assessed among children attending a consulting visit; sex and first-degree-family-history status are compared between participating and non-participating eligible children. Screening includes eligibility assessment, medical history restricted to conditions leading to medical consultation, and informed-consent process.

### 4.2 Eligibility Criteria Summary
Eligible infants are 4-7 months old, have >10% risk of developing multiple beta-cell autoantibodies by age 6 years, have introduced solid food, and have parental written consent. Without first-degree type 1 diabetes, eligibility requires DR3/DR4-DQ8 or DR4-DQ8/DR4-DQ8 plus genetic-risk score >14.4; with a first-degree history, it requires HLA DR4 and DQ8 without DRB1*1501 or DQB1*0503. Exclusions are interfering disease/treatment, a condition associated with poor compliance, unsafe medical condition, diabetes at recruitment, or another clinical trial.

### 4.3 Recruitment
Potential participants are identified through GPPAD-02 or similar infant type-1-diabetes-risk studies, with genetic screening from cord blood/newborn screening or a paediatric visit. Recruitment ran February 2018-March 2021 and enrolled 1,050 infants.

### 4.4 Withdrawal and Follow-up
- **Withdrawal Levels:** Treatment withdrawal for diabetes, moderate/severe treatment intolerance, incompatible intercurrent illness, or parental consent withdrawal; study withdrawal may occur for withdrawal of all future activities or loss to follow-up.
- **Withdrawal Data Collection:** Capture treatment discontinuation/withdrawal reason in the CRF, make every effort to follow enrolled children including non-completers, and document the primary study-withdrawal reason in the eCRF. After study end, contact participants regularly for up to 10 years for diabetes development and invite them, under separate consent outside POInT, to an available autoantibody follow-up study.
- **Reasons for Withdrawal:** Report consent withdrawals and losses to follow-up by arm with time points and reasons in a CONSORT 2010 flow diagram; collect information where possible.

### 4.5 Baseline Characteristics
- **Baseline Variables:** Sex; GRS; INS rs3842753 and rs1004446; HLA-DR4-DQ8/non-DR4-DQ8 and non-DR3, HLA-DR3/DR4-DQ8, and HLA-DR4-DQ8/DR4-DQ8; any first-degree family history, sibling with type 1 diabetes, mother with type 1 diabetes, father with type 1 diabetes; country; study site; age, age/sex-adjusted weight/height/BMI z-scores, and laboratory values.
- **Summary Methods:** Categorical variables as percent of ITT population; continuous variables as mean, SD, range or median, IQR, range.

## 5. Analysis

### 5.1 Primary Outcomes
**Outcome: Persistent confirmed multiple beta-cell autoantibodies or diabetes**
- **Definition:** Time from randomization to persistent confirmed IAA, GADA, IA-2A, or ZnT8A in two consecutive samples plus a confirmed second antibody in one sample, or diabetes, whichever first. Maternal GADA/IA-2A that become negative before age 3 are excluded; diabetes before a persistence sample fulfills the endpoint. Diabetes requires, on two occasions at least one day apart, symptoms plus casual plasma glucose >=200 mg/dL (>=11.1 mmol/L), fasting plasma glucose >=126 mg/dL (>=7 mmol/L), or 2-hour OGTT glucose >=200 mg/dL (>=11.1 mmol/L); diagnoses based on nonstandard criteria are adjudicated by the Endpoint Adjudication Committee.
- **Measurement Units:** Event time in days from randomization. IAA, GADA, IA-2A, and ZnT8A are tested at the central laboratory and positive samples are tested by the confirmatory laboratory; confirmed IAA/GADA/IA-2A require positivity in both, and confirmed ZnT8A requires ZnT8RA and/or ZnT8WA positivity in both. GADA also requires positive ELISA and RBA on at least one occasion.
- **Timing of Measurement:** Autoantibody blood is collected at every study visit; endpoint date is the defined persistent-confirmed-multiple-autoantibody date or diabetes diagnosis.
- **Transformations / Derived Variables:** Censor children without an outcome at their last tested autoantibody-negative blood sample. For maternal-antibody cases, apply the specified baseline classifications and date rules; conduct a sensitivity analysis including baseline multiple-autoantibody-positive children. Children reaching the multiple-autoantibody endpoint continue assigned treatment and follow-up for glucose tolerance, diabetes, and safety until diabetes or study completion.

### 5.2 Secondary Outcomes
**Outcome: Any persistent confirmed beta-cell autoantibody or diabetes**
- **Definition:** At least one persistent confirmed IAA, GADA, IA-2A, ZnT8A, or TS7A, or diabetes before collection of a persistence sample. Positivity cut-offs are defined in the Manual of Operation and eCRF.
- **Measurement Units:** Event time from randomization.
- **Timing of Measurement:** Each visit; TS7A is tested at study end in last-visit samples and, if positive, prior samples are assessed to define seroconversion.
- **Transformations / Derived Variables:** Exclude children single or multiple autoantibody positive at baseline; censor non-events at last tested negative blood sample.

**Outcome: Persistent confirmed IAA**
- **Definition:** IAA confirmed in two laboratories, positive in two consecutive samples and by RBA and LIPS, or one sample followed by diabetes before persistence assessment.
- **Measurement Units:** Event time from randomization.
- **Timing of Measurement:** Each blood-collection visit.
- **Transformations / Derived Variables:** Exclude baseline IAA-positive children and censor non-events at last tested negative sample.

**Outcome: Persistent confirmed GADA**
- **Definition:** GADA confirmed in the central and confirmatory laboratories and in two consecutive samples, or one sample followed by diabetes before persistence assessment.
- **Measurement Units:** Event time from randomization.
- **Timing of Measurement:** Each blood-collection visit.
- **Transformations / Derived Variables:** Exclude baseline GADA-positive children and censor non-events at last tested negative sample.

**Outcome: Persistent dysglycaemia or diabetes**
- **Definition:** Fasting glucose >=110 mg/dL (>=6.1 mmol/L), 2-hour glucose >=140 mg/dL (>=7.8 mmol/L), or 30/60/90-minute OGTT glucose >=200 mg/dL (>=11.1 mmol/L) at two consecutive occasions, or at one occasion followed by diabetes onset at the next sample; alternatively diabetes first.
- **Measurement Units:** Plasma glucose mg/dL and mmol/L; event time from randomization.
- **Timing of Measurement:** OGTT from age 3 years in persistent-confirmed-autoantibody-positive children, with 0/30/60/90/120-minute samples; then six-monthly.
- **Transformations / Derived Variables:** Date is first persistent dysglycaemia or diabetes, whichever first; baseline single/multiple autoantibody-positive children remain eligible for this analysis.

### 5.3 Analysis Methods
- **Primary Analysis Methods:** Estimate cumulative incidence by Kaplan-Meier function; compare arms with Cox regression including site as a covariate and Wald test at two-sided 0.05. The cumulative-incidence estimates and test adjust for periodic outcome-assessment visits. Report hazard ratios and cumulative incidences at years 1-7 with 95% CIs and curves.
- **Covariate Adjustment:** Primary protocol analysis includes site as a Cox-regression covariate. Exploratory Cox models evaluate covariate-by-treatment interactions; longitudinal models adjust for subject characteristics.
- **Assumption Checks:** Check proportional hazards visually using Schoenfeld residuals versus time and test a predictor-by-time interaction.
- **Alternative Methods if Assumptions Fail:** Examine source of non-proportional hazards; post-hoc frailty, parametric, interaction, or time-dependent-covariate models may be used.
- **Sensitivity Analyses:** Repeat primary outcome in ITT including children multiple-autoantibody positive at baseline; if maternal-antibody bias is found, analyze children autoantibody negative at baseline. Analyze outcomes during treatment versus non-treatment periods.
- **Subgroup Analyses:** Cox treatment-by-subgroup interactions for sex, race/ethnicity if appropriate, country/site, first-degree-relative status (none, mother, father, sibling), maternal antibodies, GRS tertiles, INS genotype, and HLA genotype. Evaluate quantitative baseline factors (weight, height, BMI z-scores and GRS) with treatment interactions; distinguish factors specified before unmasking from factors identified post-hoc. Analogous analyses apply to primary and secondary endpoints.

### 5.4 Missing Data
- **Missing Data Assumptions:** Not reported in protocol.
- **Handling Methods:** No imputation method is reported. Data acquired before termination are included unless consent is withdrawn; time-to-event non-events are censored at the last tested autoantibody-negative sample, while the added exploratory diabetes/progression analyses censor at last contact.

### 5.5 Additional Analyses
Secondary outcomes are compared with log-rank statistics. Exploratory analyses include longitudinal repeated-measures normal-error models, GEE for categorical measures (and quantitative measures if multivariate-normal errors fail), ANOVA/ANCOVA for suitable continuous measures, generalized linear models for categorical/dichotomous measures, and Cox models for risk-factor associations; exploratory longitudinal treatment-effect hypothesis testing will not be conducted. The amended exploratory clinical-type-1-diabetes and seroconversion-to-clinical-type-1-diabetes-progression analyses are outside the initial trial report.

### 5.6 Harms
- **Adverse Event Definitions:** An AE is any untoward medical occurrence irrespective of causal relationship; SAE includes death, life-threatening event, hospitalization/prolongation, disabling/incapacitating event, congenital anomaly, or important medical event. Diabetes/dysglycaemia hospitalization is not an AE/SAE. Presumed hypoglycaemia is compatible symptoms reversed by oral carbohydrate without contemporaneous glucose; definite hypoglycaemia is glucose <50 mg/dL (<2.8 mmol/L), with/without symptoms, or severe compatible symptoms reversed by intravenous glucose or subcutaneous glucagon.
- **Safety Analysis Methods:** Present number and percentage of all AEs by MedDRA and severity for each arm, with descriptive arm comparison and causality classification; compare 0/30/60/120-minute glucose values before/after study drug at visits 1-4 and height, weight, BMI z-scores during and after treatment.
- **Grading Scales and Causality:** Grade AEs by NCI-CTCAE v4.03 (grades 1-5); site investigator records NCI-CTCAE attribution unrelated, unlikely, possible, probable, or definite. AEs are collected during treatment and for 60 days afterward; potentially related post-study death/AEs are reported up to 3 months after study sign-out if known.

### 5.7 Software and References
- **Statistical Software:** SAP V1.0 commits to SAS, preferably the then-current version and at least SAS 9.4, for all analyses. Separately, Protocol V4 identifies PROC POWER in SAS 9.4 for the sample-size/power calculation.
- **Other Referenced Documents:** SAP V1.0 dated 22 January 2024 and SAP Amendment 1.0 dated 15 October 2024; protocol V4.0 dated 9 December 2021; autoantibody cut-offs are in the Manual of Operation and eCRF.

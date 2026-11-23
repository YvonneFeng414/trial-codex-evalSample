# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale
IgA nephropathy (IgAN) is a common glomerulonephritis; progressive renal failure occurs in a substantial proportion of clinically affected patients. STOP IgAN evaluates whether adding immunosuppression to optimized, comprehensive supportive care improves clinically important renal outcomes in patients at risk for progression.

### 1.2 Objectives

**Primary Objectives**

- Evaluate efficacy of immunosuppressive therapy added to comprehensive supportive therapy for inducing clinical remission in progressive IgAN.
- Compare treatments for the number of patients with GFR loss greater than or equal to 15 mL/min.

**Secondary Objectives**

Not reported as separately labelled objectives; the protocol specifies secondary efficacy endpoints.

**Exploratory Objectives**

No exploratory objectives are reported.

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Randomized, prospective, multicenter, open-label, two-arm parallel-group therapeutic trial, with a 6-month run-in phase and 36-month treatment/follow-up phase.
- **Allocation Ratio:** 1:1 (74 planned per treatment).
- **Intervention Summary:** All consented patients enter optimized supportive care during run-in: BP target below 125/75 mmHg; ACE inhibitor first line, with ARB if intolerant; statin therapy; low-sodium counseling and, if GFR <60 mL/min, protein intake 0.8 g/kg/day. Randomization requires proteinuria >0.75 g/d after run-in; if GFR at week -1 is <90 mL/min, run-in GFR loss must be <=30%, while any GFR loss is permitted if week--1 GFR is >=90 mL/min. The flow chart also identifies proteinuria >3.5 g/d as a run-in dropout condition.
  - Treatment S (supportive group): continue optimized supportive therapy.
  - Treatment I (immunosuppressive group): identical supportive care plus, for GFR >=60 mL/min, methylprednisolone 1 g IV daily for 3 days at months 1, 3, and 5 and prednisolone 0.5 mg/kg every 48 hours for 6 months; for GFR 30-60 mL/min, cyclophosphamide 1.5 mg/kg/day for 3 months with tapered prednisolone, then azathioprine 1.5 mg/kg/day plus prednisolone through 3 years. Vitamin D/calcium are recommended with corticosteroids; cotrimoxazole pneumocystis prophylaxis and Mesna prophylaxis are recommended with cyclophosphamide.

### 2.2 Randomization

- **Method:** Central, web-based randomization using a PHP 5.2 tool and PostgreSQL database; the allocation method is minimization.
- **Stratification Factors:** Baseline GFR and baseline proteinuria.
- **Minimization or Blocking:** Minimization is used; blocking is not reported.

### 2.3 Sample Size

- **Planned Sample Size:** 148 randomized patients: 74 per group.
- **Outcome Used for Calculation:** First hierarchically ordered primary endpoint, full clinical remission at 3 years.
- **Outcome Type:** Binary remission proportion.
- **Assumed Control-Arm Value:** Less than 5% full remission under standard/supportive therapy.
- **Assumed Treatment-Arm Value:** 25% full remission under combined/immunosuppressive therapy after 3 years.
- **Target Difference / Effect Size:** Difference in remission rates of 5% versus 25% (approximately 20 percentage points).
- **Variability Assumption:** Not applicable to the binary proportion calculation.
- **Alpha (Significance Level):** Two-sided 5%, adjusted for two interim looks by O'Brien-Fleming monitoring.
- **Power:** 80%.
- **Statistical Test Assumed:** Chi-square (F2) test with continuity correction; final analysis instead uses logistic regression because stratification-factor distributions were unavailable for the calculation.
- **Required Number of Events:** Not reported in protocol.
- **Non-Inferiority / Equivalence Margin:** Not applicable; this is superiority testing and the TSAP states non-inferiority/equivalence testing is not applicable.
- **Dropout / Non-Adherence Inflation:** 10%; increased from 60 to 74 patients per group (14 additional per group).
- **Design Effect / Clustering:** Not applicable; this is an individually randomized trial and center is not included as a stratification variable because of small per-center sample sizes.
- **Basis for Assumptions:** Experience with initial IgAN presentations over preceding years; Lachin is cited for dropout inflation.
- **Sample Size Re-Estimation / Amendments:** No sample-size re-estimation is reported. Recruitment duration was extended by one year to October 2014.
- **Software Used for Calculation:** Addplan 3.1.
- **Sample Size Rationale:** The unstratified calculation was considered conservative relative to the planned stratified logistic-regression analysis.

### 2.4 Hypothesis Framework
Two independent primary endpoints are tested hierarchically, first full clinical remission and then GFR loss >=15 mL/min only if the first endpoint is significant. For each endpoint, the null is equal treatment-group rates (or means for continuous secondary outcomes) versus a two-sided difference.

### 2.5 Statistical Interim Analyses

- **Interim Analyses Planned:** Two interim analyses at information rates 0.33 and 0.67; the third analysis at 1.00 is final. The safety committee evaluates both primary endpoints for possible consequences for trial continuation.
- **Stopping Guidelines:** At the first two stages: if remission fails, make no further evaluation and continue; if remission is significant but GFR loss fails, make no further evaluation, continue, and do not retest remission at the next stage; if both are significant, evaluate all secondary endpoints at that stage's significance level. At final analysis, test primary endpoints hierarchically; secondary endpoints are evaluated at 0.0451 as specified.
- **Alpha Spending or Adjustment:** O'Brien-Fleming, two-sided alpha 0.0005, 0.0141, and 0.0451 at information rates 0.33, 0.67, and 1.00, respectively.

### 2.6 Timing of Analyses

- **Final Analysis Timing:** The final efficacy analysis is at the third stage/information rate 1.00, after patients are evaluable at 36 months; the final report is to be submitted within one year after study end.
- **Outcome Assessment Schedule:** Run-in includes six visits over months -6 to -0.25. The study phase has 16 visits at months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36; urine and renal assessments are scheduled at baseline and selected follow-up visits, including month 36.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **Alpha Level:** Overall two-sided 5%, controlled with O'Brien-Fleming stage-specific levels.
- **Multiplicity Adjustment:** Hierarchical testing of the two primary endpoints plus O'Brien-Fleming interim monitoring; secondary endpoints are evaluated at the stage significance level only when the stated decision rules permit. The TSAP's separate “Multiplicity” heading says “Not applicable,” but its hierarchy and interim decision rules are the operative multiplicity strategy.
- **Confidence Intervals:** 95% confidence intervals are calculated except for the interim-stage significance levels; logistic models present odds ratios with 95% CIs.

### 3.2 Protocol Deviations

- **Adherence Definition:** Compliance variables include BP at every visit, total cholesterol at run-in and baseline, leukocytes/lymphocytes for corticosteroid recipients, and antihypertensive and statin medications at every visit.
- **Adherence Assessment:** Supportive therapy and medication names are documented at each visit; dietary restriction is verified by 24-hour urine sodium and urea excretion.
- **Protocol Deviation Definition:** Eligibility violations and lack of post-randomization data can exclude a randomized participant from the full analysis set; the listed major-entry criteria are age/biopsy-confirmed IgAN, 6-month run-in, proteinuria >750 and <=3500 mg/d, and run-in GFR loss <=30%. Such exclusion is unbiased only if the criterion was measured before randomization, detection is completely objective, all participants receive equal scrutiny, all detected violations of that criterion are excluded, and resulting potential bias is addressed.
- **Protocol Deviation Reporting:** Quality procedures include investigator training, monitoring, source-data verification, standardized terminology/procedures, double data entry and plausibility checks; incomplete/ambiguous documents prompt correction forms. Each data modification, transformation, description, and test is logged, and deviations from planned evaluation steps require steering committee and data safety monitoring committee approval.

### 3.3 Analysis Populations

- **Intention-to-Treat:** The full analysis set is the primary analysis population and seeks to include all randomized patients, preserving initial randomization, except objectively identified major eligibility violations or no post-randomization data.
- **Per Protocol:** The TSAP notes that ICH E9 distinguishes full-analysis and per-protocol sets, and the disposition graphic labels a per-protocol count; detailed membership criteria and analytic use are not reported.
- **Other Populations:** Safety and compliance variables are summarized by treatment group; no separately named safety population is defined.

## 4. Trial Population

### 4.1 Screening Data
Screening/run-in visits occur at months -6, -5, -4, -2, -1, and -0.25 and include history/questionnaire, BP and weight at each visit, physical examination at month -6, blood testing, pregnancy testing where applicable, hepatitis/HIV testing, and 24-hour urine sediment, creatinine clearance/excretion, protein, and sodium measures at specified visits. Study visits are months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36. Screening failures/nonrandomization categories include proteinuria <=0.75 g/d or >3.5 g/d, GFR loss >30%, creatinine clearance <30 mL/min, and other reasons.

### 4.2 Eligibility Criteria Summary
Eligible patients are men or women aged 18-70 years with nephropathologist-confirmed primary mesangioproliferative IgAN, proteinuria >0.75 g/d within 12 weeks before or at run-in start, and at least one additional ESRD risk factor: hypertension (ambulatory BP >140/90 mmHg or antihypertensive use) or impaired renal function (creatinine clearance or estimated GFR <90 mL/min). Exclusions are known study-drug allergy/intolerance (except ACE-inhibitor intolerance permitting ARB), pregnancy/breastfeeding/inadequate contraception, contraindication to immunosuppression (acute/chronic infection including hepatitis/HIV, malignancy, leukocytopenia/thrombocytopenia, prednisolone/azathioprine allergy, GI bleeding/ulcer, or need for permanent immunosuppression), prior immunosuppression, rapidly progressive/crescentic (>50% glomeruli) or minimal-change IgAN variants, secondary IgAN, another chronic renal disease, GPT >3-fold normal, mean of three creatinine-clearance measurements <30 mL/min, alcohol/drug abuse, mental incapacity, expected noncompliance, concurrent/recent trial participation, dependency, sponsor/investigator employment, or legal institutional commitment.

### 4.3 Recruitment
Multicenter recruitment is planned; all consenting patients enter the run-in phase, and only qualifying nonresponders are randomized. Recruitment was prolonged and the trial duration extended by one year, to October 2014.

### 4.4 Withdrawal and Follow-up

- **Withdrawal Levels:** Participants can withdraw at any time without giving a reason. The disposition plan separately captures nonrandomization, therapy not started, dropout before therapy, changes of therapy, loss to follow-up, death, and per-protocol status.
- **Withdrawal Data Collection:** Histories/questionnaires are scheduled at every study-phase visit; follow-up reminders are issued for missed documentation, and site records are checked for completeness/plausibility.
- **Reasons for Withdrawal:** The protocol does not provide an exhaustive coded reason list; the planned flow figure names patient refusal, practitioner decision, SAE, change of therapy, loss to follow-up, and death.

### 4.5 Baseline Characteristics

- **Baseline Variables:** The baseline-characteristics table records year of birth (year), sex, and height (cm) at month -6; and weight (kg), smoking, home systolic/diastolic BP (mmHg), proteinuria (mg/d), creatinine excretion (mg/d), serum creatinine (mg/dL), and creatinine clearance (mL/min) at month 0. BMI and CKD-EPI eGFR are derived/presented in later analysis tables.
- **Summary Methods:** Categorical variables: available N, n, and percentage by treatment group; continuous variables: N, mean, SD, and range by treatment group. Percentages are rounded to one decimal place and other results to one more decimal place than in the CRF.

## 5. Analysis

### 5.1 Primary Outcomes
**Outcome: Full clinical remission**
- **Definition:** Binary full remission requires proteinuria <0.2 g/g at 3 years and stable renal function, GFR loss <5 mL/min from baseline. Baseline eGFR is the mean of baseline and week -1; 36-month eGFR is the mean of the month-36 value and repeat laboratory testing within one week.
- **Measurement Units:** Proteinuria g/g from 24-hour collection; eGFR mL/min by CKD-EPI serum-creatinine formula.
- **Timing of Measurement:** End of the 36-month study period, with repeat laboratory test within one week.
- **Transformations / Derived Variables:** 24-hour proteinuria mg/d divided by 24-hour creatinine excretion mg/d produces g/g; CKD-EPI eGFR uses serum creatinine in mg/dL, age, and sex.

**Outcome: GFR loss >=15 mL/min**
- **Definition:** Binary event is eGFR decrease >=15 mL/min from baseline to 36 months, using the specified means of paired baseline/week -1 and month-36/repeat measurements.
- **Measurement Units:** eGFR mL/min estimated by CKD-EPI serum-creatinine formula.
- **Timing of Measurement:** Baseline/week -1 versus month 36/repeat within one week.
- **Transformations / Derived Variables:** Derived binary indicator from change in CKD-EPI eGFR.

### 5.2 Secondary Outcomes
**Outcome: Absolute GFR change**
- **Definition:** Difference between mean of two end-of-study GFR measurements and mean of two baseline GFR measurements.
- **Measurement Units:** mL/min eGFR by CKD-EPI.
- **Timing of Measurement:** Baseline and 36 months.
- **Transformations / Derived Variables:** End-of-study minus baseline eGFR.

**Outcome: GFR loss >=30 mL/min**
- **Definition:** Binary eGFR decrease >=30 mL/min from baseline at 36 months.
- **Measurement Units:** mL/min CKD-EPI eGFR.
- **Timing of Measurement:** Baseline/week -1 and month 36/repeat within one week.
- **Transformations / Derived Variables:** Derived binary indicator from CKD-EPI eGFR change.

**Outcome: Onset of end-stage renal disease**
- **Definition:** Start of chronic dialysis or renal transplantation during 3-year follow-up; chronic renal replacement need is persistent for >=4 weeks.
- **Measurement Units:** Binary event.
- **Timing of Measurement:** Any time during 36-month follow-up.
- **Transformations / Derived Variables:** Chronic dialysis or transplantation documented as an AE/SAE during follow-up is converted to an event indicator; a transient renal-replacement requirement alone does not meet the ESRD definition unless the requirement persists >=4 weeks.

**Outcome: Mean annual change in reciprocal serum creatinine**
- **Definition:** Individual slope from regression of time on reciprocal serum creatinine.
- **Measurement Units:** Reciprocal serum creatinine per year; serum creatinine is converted to mg/dL if recorded in mmol/L.
- **Timing of Measurement:** Baseline, 12, 24, and 36 months.
- **Transformations / Derived Variables:** Individual linear-regression slope of 1/serum creatinine versus time.

**Outcome: Proteinuria at 12 and 36 months**
- **Definition:** Absolute degree of proteinuria separately at months 12 and 36.
- **Measurement Units:** g/g protein/creatinine ratio from 24-hour urine collection.
- **Timing of Measurement:** Months 12 and 36.
- **Transformations / Derived Variables:** 24-hour proteinuria mg/d divided by 24-hour creatinine excretion mg/d.

**Outcome: Disappearance of microhematuria**
- **Definition:** Result showing disappearance by dipstick or urinary sediment at 36 months.
- **Measurement Units:** Binary categorical result.
- **Timing of Measurement:** End of study at 36 months.
- **Transformations / Derived Variables:** Derived binary endpoint from month-36 microhematuria assessment.

### 5.3 Analysis Methods

- **Primary Analysis Methods:** The primary-endpoint course applies at every interim stage: stratified logistic analysis first, then its sensitivity sequence. Full-analysis-set primary endpoints are analyzed with logistic regression including treatment, baseline GFR, and baseline proteinuria; report treatment odds ratio, 95% CI, and Wald p-value. Absolute GFR change uses repeated-measures mixed-model ANOVA with treatment, stratification factors, and time (compound-symmetry covariance); reciprocal-creatinine slopes and proteinuria use ANOVA/covariance models; binary secondary endpoints use logistic regression.
- **Covariate Adjustment:** Baseline GFR and baseline proteinuria are included in logistic, mixed, and ANOVA models; no center adjustment is performed because of small per-center samples.
- **Assumption Checks:** No statistical test for outliers or residuals is planned. For mixed models, residual analysis plus influence diagnostics assess fixed and random effect estimates; residual analysis is also specified for covariance/ANOVA models. Abnormalities and subsequent action will be described.
- **Alternative Methods if Assumptions Fail:** No prespecified alternative inferential method is reported; further proceeding is to be described if residual/influence abnormalities occur.
- **Sensitivity Analyses:** The prescribed “sensitive analysis” sequence for primary endpoints comprises stratified Fisher permutation testing, treatment-by-baseline-GFR interaction, treatment-by-baseline-proteinuria interaction, and an additional exploratory model including sex. The primary endpoint derivations are also re-evaluated with measured 24-hour creatinine clearance rather than CKD-EPI eGFR. Best- and worst-case analyses assess the conservative primary-endpoint missing-data substitutions.
- **Subgroup Analyses:** No subgroups are defined; sex is included only as an exploratory covariate analysis.

### 5.4 Missing Data

- **Missing Data Assumptions:** Baseline GFR and proteinuria should not be missing because central randomization requires them. For both primary endpoints, nonassessable treatment success is treatment failure; for remission, a dropout/missing 3-year GFR is “not in full clinical remission.” For GFR loss >=30 mL/min and ESRD, nonassessable cases are failures; for microhematuria, missing month-36 observation is failure. For reciprocal-creatinine slope, >2 missing measurements gives slope 0.
- **Handling Methods:** For full remission, a dropout/missing 3-year GFR is imputed as not in remission; for GFR loss >=15 mL/min, nonassessable treatment success is imputed as loss/failure. The same failure substitution applies to nonassessable GFR loss >=30 mL/min, ESRD, and month-36 microhematuria as stated above. The repeated-measures GFR-change model permits single missing observations, and best- and worst-case sensitivity analyses assess the two primary-endpoint substitutions. No generic imputation model is reported.

### 5.5 Additional Analyses
Supportive-care medication use is described as patient counts by treatment group and active-substance category: ACE inhibitors, angiotensin receptor blockers, renin antagonists, beta blockers, diuretics, aldosterone antagonists, dihydropyridine calcium blockers, non-dihydropyridine calcium blockers, and other. Statin use is summarized as patient counts by group. Longitudinal data are graphed as mean plus/minus confidence limits at each time point, and categorical variables as percentages.

### 5.6 Harms

- **Adverse Event Definitions:** Clinical safety variables include history/physical examination and systolic/diastolic BP; laboratory safety includes blood counts, glucose, liver and related tests. AE collection captures frequency, type, severity, and duration. Safety events include all AEs, treatment-attributed AEs, all SAEs, treatment-attributed SAEs, all SUSARs, transient renal replacement therapy, and cardiovascular/non-cardiovascular deaths.
- **Safety Analysis Methods:** Summarize AE/SAE counts by treatment group and prespecified system categories; also summarize patients with at least one SAE or SUSAR. Continuous safety laboratories are summarized by N, mean, SD, and range by group.
- **Grading Scales and Causality:** A severity grading scale is not reported, although severity and duration are collected; attribution to study treatment is captured and SUSARs are separately summarized. AE/SAE categories defined by project management are abdomen, central nervous system, circulatory system, dental system, electrolytes, endocrine system/metabolism, general condition, hematology, infection, musculoskeletal system, respiratory system, sensory system (ear/eye), skin, urogenital system, and other.

### 5.7 Software and References

- **Statistical Software:** Windows XP Professional is the stated operating system (with a future updated operating system to be used if installed); Addplan 3.1 is for sample-size calculation; PHP 5.2 and PostgreSQL 8.4/9 support the web randomization tool/database; PostgreSQL data are exported as SQL and imported to SAS via ODBC; SAS 9.2 (SAS Institute, Cary, NC) is used for statistical analysis. SAS macros/programs for transformation are tested using a test dataset, controlled using a four-eyes principle, commented, and logs/output stored.
- **Other Referenced Documents:** TSAP v1.0 (11 July 2012) is a technical extension of Protocol v4.1 (13 April 2012) for study design/objectives; it also references CRF v2.2 (2009) and Data Validation Plan v1.0 (5 July 2012) for variables, and was to be completed before the first interim analysis. Formats are deferred to the Data Validation Plan.

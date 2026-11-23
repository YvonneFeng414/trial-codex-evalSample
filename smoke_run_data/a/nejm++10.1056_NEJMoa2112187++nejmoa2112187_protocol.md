# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale
Patients with recurrent or metastatic cervical cancer progressing after platinum-based chemotherapy have poor outcomes and no widely accepted subsequent systemic standard. This pivotal phase 3 study compares cemiplimab with investigator’s-choice (IC) chemotherapy.

### 1.2 Objectives

**Primary Objectives**

- Compare overall survival (OS), first among patients with squamous cell carcinoma (SCC), then in the overall eligible population (SCC or adenocarcinoma/adenosquamous carcinoma), for cemiplimab versus IC chemotherapy.

**Secondary Objectives**

- Compare progression-free survival (PFS), objective response rate (ORR) by RECIST 1.1, duration of response (DoR), adverse-event profiles, and EORTC QLQ-C30 global-health-status/quality-of-life (GHS/QoL) and physical-functioning mean change from baseline, in SCC and overall populations.

**Exploratory Objectives**

- Characterize serum cemiplimab PK and immunogenicity; explore associations of efficacy with pretreatment-tumor molecular features and peripheral-blood pharmacodynamic activity.

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Open-label, randomized, multicentre phase 3 trial with screening, treatment, follow-up and subsequent survival follow-up; no treatment crossover.
- **Allocation Ratio:** 1:1 cemiplimab versus IC chemotherapy.
- **Intervention Summary:** Treatment is planned for up to 96 weeks.
  - Cemiplimab: 350 mg IV every 3 weeks.
  - IC chemotherapy: pemetrexed, topotecan, irinotecan, gemcitabine, or vinorelbine.

  - Pemetrexed: 500 mg/m² IV day 1 every 21 days, with folate/vitamin B12 support.
  - Topotecan: 1 mg/m² IV daily for 5 days every 21 days; may increase to 1.25 mg/m² after first course without significant toxicity.
  - Irinotecan: 100 mg/m² IV weekly for 4 doses, then 10–14 days' rest (≥14 days in Japan); may increase to 125 mg/m² after first course without significant toxicity.
  - Gemcitabine: 1000 mg/m² IV days 1 and 8 every 21 days.
  - Vinorelbine: 30 mg/m² IV days 1 and 8 every 21 days.

Cemiplimab and IC treatment continue to 96 weeks or RECIST 1.1 progression, unacceptable toxicity, death, or consent withdrawal. Cemiplimab may continue beyond RECIST progression only under protocol Section 8.6 criteria. In follow-up, a patient with PD may be retreated with the same originally assigned drug; IC selection and each drug’s dose/schedule are protocol specified.

### 2.2 Randomization
- **Method:** Interactive web response system (IWRS) treatment assignment after investigator deems eligibility.
- **Stratification Factors:** SCC analysis: geographic region (North America, Asia-Pacific, rest of world [ROW]). Overall analysis: region and histology (SCC versus adenocarcinoma; adenosquamous classified as adenocarcinoma).
- **Minimization or Blocking:** Not reported in protocol.

After Amendment 5, only SCC patients were randomized. Before Amendment 5, patients were stratified by SCC versus adenocarcinoma/adenosquamous histology; this historical distinction is retained in the overall-population analysis.

### 2.3 Sample Size
- **Planned Sample Size:** 460 randomized SCC patients; approximately 590 total patients projected.
- **Outcome Used for Calculation:** OS in SCC patients.
- **Outcome Type:** Time-to-event survival outcome.
- **Assumed Control-Arm Value:** Median OS 7 months for IC chemotherapy.
- **Assumed Treatment-Arm Value:** Median OS 10 months for cemiplimab.
- **Target Difference / Effect Size:** HR 0.70, corresponding to approximately 42.8% increase in median OS under exponential distributions.
- **Variability Assumption:** Exponential OS distributions in both groups.
- **Alpha (Significance Level):** Overall one-sided 0.025.
- **Power:** Approximately 90% for HR 0.70 with 340 SCC OS events.
- **Statistical Test Assumed:** Group-sequential, stratified log-rank OS test with Lan-DeMets (O’Brien-Fleming) alpha spending.
- **Required Number of Events:** 340 OS events in SCC patients.
- **Non-Inferiority / Equivalence Margin:** Not applicable; superiority hypothesis.
- **Dropout / Non-Adherence Inflation:** 10% dropout rate per year.
- **Design Effect / Clustering:** Not applicable; individually randomized trial.
- **Basis for Assumptions:** Phase 2 IC median OS reports (6.5–8.1 months) and enrollment assumptions of 2/month months 1–5, 9/month months 6–16, 20/month months 17–23, then 22/month.
- **Sample Size Re-Estimation / Amendments:** SAP v2.0 updated sample size, interim analysis, target population, and enrollment rate for protocol amendments through Amendment 6. A formal sample-size re-estimation procedure is not reported in protocol.
- **Software Used for Calculation:** East version 6.4.1.
- **Sample Size Rationale:** 460 SCC patients are expected to yield 340 events about 42 months after first SCC randomization; overall-population power is projected above 90% if HR=.70.

### 2.4 Hypothesis Framework
H0: cemiplimab and IC chemotherapy have the same OS survival curve; H1: cemiplimab is superior. OS is tested first in SCC and, only if significant, in the overall population.

### 2.5 Statistical Interim Analyses
- **Interim Analyses Planned:** Two SCC OS efficacy analyses at approximately 238 events (70%) and 289 events (85%).
- **Stopping Guidelines:** Efficacy boundaries use nominal one-sided alpha .0074 and .0129 at the first and second analyses. No futility boundary or futility stopping rule is identified; interim efficacy monitoring and safety/available-efficacy oversight are provided by an independent IDMC.
- **Alpha Spending or Adjustment:** Lan-DeMets O’Brien-Fleming spending; final nominal one-sided alpha .0202 at 340 events, based on actual event information.

### 2.6 Timing of Analyses
- **Final Analysis Timing:** Final OS cutoff is when 340 SCC OS events are observed; events through cutoff included and otherwise censor at earlier of last-known-alive date or cutoff.
- **Outcome Assessment Schedule:** Treatment starts within 5 days after randomization (within 10 days for pemetrexed) in 6-week cycles. CT/MRI is day 42 (±7 days) of cycles 1–4, 6, 8, 10, 12, 14, and 16; after treatment, imaging is every 90 days (±10) until PD for those without prior PD. QLQ-C30 is at screening and day 1 of treatment cycles (may be at another visit in the same cycle), before procedures; it is also at post-treatment follow-up visits 1 and 2. Follow-up visit 1 is ~30 days (±10) after last dose and visit 2 ~90 days (±10) later; survival ascertainment then occurs every 90 days (±10) until death or completion.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals
- **Alpha Level:** One-sided .025 for confirmatory hierarchy; specified effect estimates are accompanied by two-sided 95% CIs.
- **Multiplicity Adjustment:** Group-sequential alpha spending for SCC OS, plus the hierarchy: SCC OS; overall OS; SCC PFS; SCC GHS/QoL; SCC physical functioning; SCC ORR; overall PFS; overall ORR; then the specified SCC and overall cycle-2 and overall PRO endpoints. Later tests occur only after significant SCC OS.
- **Confidence Intervals:** Kaplan-Meier medians/rates, Cox HRs, and Clopper-Pearson ORR CIs are two-sided 95%.

### 3.2 Protocol Deviations
- **Adherence Definition:** Compliance = doses administered/planned doses ×100, ignoring temporary discontinuation.
- **Adherence Assessment:** Summarize percentages <60%, 60–80%, 80–100%, and >100% by group.
- **Protocol Deviation Definition:** Major deviations include inclusion/exclusion violations and post-enrollment deviations affecting efficacy or safety assessment.
- **Protocol Deviation Reporting:** Separate definition document/listing; determine major deviations before database lock and summarize by treatment.

### 3.3 Analysis Populations
- **Intention-to-Treat:** FAS: all randomized patients, analyzed as randomized; all efficacy endpoints.
- **Per Protocol:** Not reported in protocol.
- **Other Populations:** SAF: randomized patients receiving any study drug, as treated, for compliance/administration and all clinical safety variables. PKS: cemiplimab-treated patients with ≥1 nonmissing post-first-dose concentration. ADA: cemiplimab-treated patients with ≥1 nonmissing post-first-dose ADA result. NAb: cemiplimab-treated patients with ≥1 nonmissing assigned/assessed NAb result postdose, or ADA-negative status during study. BAS: treated patients with ≥1 assayed sample. The ORR-eligible restricted randomized set is a robustness population, not a per-protocol set.

## 4. Trial Population

### 4.1 Screening Data
Screening begins at informed consent and ends at confirmed eligibility/randomization or ineligibility/screen failure. It includes consent; inclusion/exclusion review; history/demographics; ECOG; tumor tissue/pathology; ECG; hematology, chemistry, coagulation, urinalysis and infection tests; pregnancy test where applicable; and baseline CT/MRI. Screening assessments have the protocol-specified timing windows.

### 4.2 Eligibility Criteria Summary
Eligible patients are women ≥18 years with recurrent/persistent/metastatic noncurable cervical SCC (adenocarcinoma/adenosquamous allowed before Amendment 5); progression after platinum specifically for recurrent/persistent/metastatic cancer (not curative chemoradiation); RECIST 1.1 measurable lesion ≥10 mm by CT/MRI/caliper or ≥20 mm chest radiograph (nodes >15 mm short axis); ECOG ≤1; bilirubin ≤1.5× ULN (≤3× with liver metastases), transaminases ≤3× (≤5× with liver metastases), alkaline phosphatase ≤2.5× (≤5× with liver/bone metastases), creatinine ≤1.5× ULN or clearance >45 mL/min, hemoglobin ≥9 g/dL, ANC ≥1.5×10⁹/L and platelets ≥75×10⁹/L; >12-week expectancy; ability to comply/complete questionnaires; consent; and required prior bevacizumab/paclitaxel status or exceptions. Exclusions include significant systemic-treatment autoimmune disease, prior PD-1/PD-L1 therapy, immune-modulator within 4 weeks or recent associated toxicity, active/unstable CNS metastasis, >10-mg prednisone-equivalent immunosuppression within 4 weeks, active serious infection/HIV/HBV/HCV, pneumonitis within 5 years, anticancer therapy within 30 days (radiation within 14 days), relevant allergy, concurrent/recent malignancy, transplant, pregnancy/breastfeeding, and failure to use required contraception.

### 4.3 Recruitment
Approximately 590 total patients (460 SCC) were projected, across approximately 100 US/global sites; planned enrollment rates are reported in Section 2.3.

### 4.4 Withdrawal and Follow-up
- **Withdrawal Levels:** Patient withdrawal, investigator/sponsor withdrawal, treatment discontinuation, end-of-treatment/follow-up, and study discontinuation are distinguished.
- **Withdrawal Data Collection:** Prematurely withdrawn patients are asked to complete end-of-treatment and follow-up assessments and consent to OS follow-up; document consent withdrawal and whether it covers treatment only or study procedures/follow-up in records/CRF. Follow-up visits include survival, limited examination, concomitant medication, vital signs, ECG, AEs, laboratory testing and QLQ-C30; survival contact may be clinic or telephone.
- **Reasons for Withdrawal:** Patient choice, investigator/sponsor judgment that continuation is not in patient interest or risks scientific outcome, toxicity, progression, death, consent withdrawal and treatment/study-discontinuation reasons are recorded; disposition listings report first/last treatment, end-of-treatment/end-of-study dates and reasons. Patients are not replaced.

### 4.5 Baseline Characteristics
- **Baseline Variables:** Age (continuous; <65/≥65), race (White, Black, Asian, American Indian/Alaska Native, Native Hawaiian/Other Pacific Islander, Other), ethnicity, North America/Asia/ROW, weight, height, BMI, SCC/adenocarcinoma/adenosquamous histology, ECOG 0/1; cancer diagnosis/history, prior systemic therapy, surgery, radiotherapy, and time from metastatic-setting platinum.
- **Summary Methods:** FAS treatment-group summaries: continuous n/mean/median/SD/min/max and quartiles; categorical frequencies/percentages. Baseline demographic measures are on/before randomization unless otherwise specified.

Safety baseline is latest valid value before first dose; QoL baseline is latest available before first dose.

## 5. Analysis

### 5.1 Primary Outcomes
**Outcome: Overall survival (OS)**
- **Definition:** Time from randomization to death; censor survivors at last-known-alive date, except the SAP's special convention censors patients lost to follow-up after randomization at randomization.
- **Measurement Units:** Time from randomization, reported in months/time-to-event summaries.
- **Timing of Measurement:** Continuous survival ascertainment; cutoff at 340 SCC events for final analysis.
- **Transformations / Derived Variables:** Kaplan-Meier OS distribution/median/rates and Cox HR; lost-to-follow-up patients censored at randomization.

### 5.2 Secondary Outcomes
**Outcome: Progression-free survival (PFS)**
- **Definition:** Randomization to first radiographic RECIST 1.1 progression or death; otherwise censor at last evaluable tumor assessment.
- **Measurement Units:** Time-to-event.
- **Timing of Measurement:** Scheduled imaging as in Section 2.6.
- **Transformations / Derived Variables:** Patients without postbaseline evaluable assessment and no death are censored at randomization.

**Outcome: Objective response rate (ORR)**
- **Definition:** Confirmed best overall CR or PR divided by FAS; BOR runs from randomization to first objective PD or subsequent anticancer therapy.
- **Measurement Units:** Proportion/percentage.
- **Timing of Measurement:** RECIST imaging schedule in Section 2.6; CR/PR confirmation at least 4 weeks apart.
- **Transformations / Derived Variables:** NE (including missing/unknown) is nonresponse; stable disease requires at least 4 weeks after first dose.

**Outcome: Duration of response (DoR)**
- **Definition:** For CR/PR patients, first CR/PR to radiographic PD or death; censor without progression at last valid tumor assessment.
- **Measurement Units:** Time-to-event.
- **Timing of Measurement:** Tumor-assessment schedule in Section 2.6.
- **Transformations / Derived Variables:** Descriptive median/range and Kaplan-Meier by treatment.

**Outcome: EORTC QLQ-C30 GHS/QoL and physical functioning**
- **Definition:** QLQ-C30 has five functional scales, eight symptom scales/items, GHS/QoL and a financial-impact scale; recall is past week. Items score 1–4 except GHS/QoL items, scored 1–7.
- **Measurement Units:** Each scale derived 0–100; higher symptom scores worse, higher GHS/function scores better.
- **Timing of Measurement:** Baseline and scheduled visits, including Cycle 2 analyses.
- **Transformations / Derived Variables:** Mean and change scores, longitudinal plots, adjusted overall and Cycle-2 mean changes.

### 5.3 Analysis Methods
- **Primary Analysis Methods:** FAS/as-randomized. SCC OS: region-stratified log-rank; stratified Cox treatment HR using Efron ties; Kaplan-Meier median and 6/12/18/24-month rates. Significant SCC OS permits corresponding overall analysis stratified by North America/Asia-Pacific/ROW and SCC versus adenocarcinoma (adenosquamous classified adenocarcinoma); after Amendment 5 only SCC was randomized, whereas pre-Amendment-5 patients were histology-stratified. PFS uses the same methods. ORR uses similarly stratified CMH and Clopper-Pearson 95% CI.
- **Covariate Adjustment:** Cox has treatment covariate and stated stratification; PRO MMRM fixed effects are treatment, visit, baseline PRO, region, histology in overall population, treatment×visit and baseline-score×visit.
- **Assumption Checks:** PRO MMRM convergence is assessed.
- **Alternative Methods if Assumptions Fail:** If unstructured MMRM covariance fails to converge, heterogeneous Toeplitz then AR(1) is tried; Kenward-Roger degrees of freedom. PRO disposition/completion rate is reported at each expected time point; all component means/changes are summarized and plotted, with overall adjusted estimates equally weighting visits. Pattern-mixture analyses are deferred to a separate SAP.
- **Sensitivity Analyses:** OS: (1) clinical-database histology stratification; (2) possible RPSFT for post-progression PD-1/PD-L1 treatment; (3) censor checkpoint-inhibitor recipients at start. PFS: (1) count new anticancer therapy as event only without radiographic PD/death on/before it; (2) count clinical progression similarly. ORR: repeat among randomized patients with baseline and valid postbaseline tumor evaluation.
- **Subgroup Analyses:** Descriptive stratified-Cox HR/95% CI forest plots by age, race, geographic regions, histology, prior bevacizumab, ECOG, IC choice, and prior-line count; not powered for hypothesis tests.

### 5.4 Missing Data
- **Missing Data Assumptions:** No endpoint-value imputation is planned unless specified. Missing categorical values are excluded from percentage calculations with counts presented where relevant.
- **Handling Methods:** QLQ-C30 partial missingness uses its scoring algorithm, with no additional imputation; last-known-alive partial dates use month=January 1 and day=first of month, but missing year is not imputed. Medication start/end dates are estimated earliest/latest for classification, but missing medication onset day is not imputed. First infusion is first nonmissing dosing date and a wholly missing last dose uses last visit. Scheduled and appropriate unscheduled assessments determine baseline/endpoint; extra safety assessments are listed. OS/PFS/ORR censoring/nonresponse rules are outcome-specific in Sections 5.1–5.2.

### 5.5 Additional Analyses
PK concentrations/variables are descriptively summarized by nominal time; ADA positivity is listed/summarized and assessed against PK and safety. Medical history, prior/concomitant medications, disposition, compliance, exposure (doses, total dose, duration, intensity), laboratory, vital-sign, ECG and physical-examination analyses are listed/summarized as specified. Biomarker analyses are exploratory and reported separately under a Biomarker Analytical Plan; further PRO pattern-mixture analyses are deferred to a separate SAP.

### 5.6 Harms
- **Adverse Event Definitions:** AE is any untoward occurrence. Pre-treatment is consent to first dose; treatment is first dose through 90 days after last dose or before new systemic anticancer therapy, whichever first; post-treatment begins next day. TEAEs develop/worsen in treatment; drug-related events anytime are TEAEs. SAEs are collected through end of study.
- **Safety Analysis Methods:** SAF/as-treated; treatment/overall summaries of TEAEs, related/serious events, discontinuations/deaths and AESIs using MedDRA SOC/PT. List/summarize laboratory results and baseline shifts/new-or-worsened CTCAE abnormalities, vital-sign baseline changes, ECG status shifts, and baseline/post-treatment physical examination findings.
- **Grading Scales and Causality:** CTCAE v4.03; non-CTCAE events use grades 1 mild through 5 death; investigator assesses relationship. Medically relevant symptomatic, corrective-therapy, discontinuation-causing or serious lab/vital/ECG abnormalities are AEs. AESIs include grade ≥2 infusion/allergic reactions, grade ≥3 irAEs, and any-grade irAE after PI3K inhibitor; assess suspected irAEs for neoplastic, infectious, metabolic, toxin or other causes and report AESIs within 24 hours.

### 5.7 Software and References
- **Statistical Software:** SAS version 9.4 or above for all statistical analyses; East version 6.4.1 for sample-size/power calculation.
- **Other Referenced Documents:** Current SAP v3.0, dated February 17, 2020; RECIST 1.1; EORTC QLQ-C30 and scoring manual; ICH E9; MedDRA; WHO Drug Dictionary; NCI-CTCAE; and the RPSFT reference. Separate protocol-deviation definition document, Biomarker Analytical Plan and additional PRO SAP are explicit referenced/deferred documents.

# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale

ING114467 is a Phase III study in antiretroviral therapy (ART)-naïve adults with HIV-1. It evaluates once-daily dolutegravir (DTG; GSK1349572) plus abacavir/lamivudine (ABC/3TC) versus the fixed-dose efavirenz/emtricitabine/tenofovir regimen Atripla, to establish non-inferior antiviral activity and characterize longer-term safety, tolerability, resistance, and health outcomes. DTG 50 mg once daily was selected from Phase 2b dose-ranging data.

### 1.2 Objectives

**Primary Objectives**

To demonstrate antiviral activity of DTG plus ABC/3TC FDC once daily versus Atripla over 48 weeks in HIV-1 infected, ART-naïve subjects.

**Secondary Objectives**

- Demonstrate antiviral activity through Week 96.
- Evaluate antiviral activity through Week 144.
- Compare tolerability, long-term safety, antiviral and immunologic activity over time.
- Assess development of viral resistance in subjects experiencing virologic failure.
- Assess change in symptom bother count.
- Evaluate incidence of HIV-associated conditions over time.
- Explore the impact of gender, race and/or HIV-1 subtype on response.
- Explore change in utility and health-related quality of life.

**Exploratory Objectives**

Not reported in protocol; the protocol lists all stated objectives as primary or secondary. Exploratory analyses are described as analyses rather than objectives.

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Phase III, multicentre, randomized, stratified, double-blind, double-dummy, active-controlled, parallel-group, fully powered non-inferiority study. The double-blind randomized phase runs from Day 1 through Week 96; Amendment 05 provides an open-label randomized phase through Week 144 and a DTG continuation phase thereafter.
- **Allocation Ratio:** 1:1; approximately 800 randomized subjects, approximately 400 per arm.
- **Intervention Summary:** Once daily, double-dummy, preferably fasting/at bedtime.
  - DTG + ABC/3TC: DTG 50 mg tablet plus ABC/3TC 600/300 mg tablet and Atripla placebo.
  - Atripla: EFV/FTC/TDF 600/200/300 mg tablet plus DTG and ABC/3TC placebos.

### 2.2 Randomization

- **Method:** Central computer-generated randomization after entry criteria confirmation; the GSK validated RANDALL/RandAll randomization software generates the schedule.
- **Stratification Factors:** Screening plasma HIV-1 RNA ≤100,000 versus >100,000 c/mL and screening CD4+ count ≤200 versus >200 cells/mm3, creating four strata.
- **Minimization or Blocking:** A fixed block size is used and remains confidential; minimization is not reported in protocol.

### 2.3 Sample Size

- **Planned Sample Size:** Approximately 800 randomized (~400/arm); 394 evaluable subjects/arm required.
- **Outcome Used for Calculation:** Proportion with plasma HIV-1 RNA <50 c/mL at Week 48.
- **Outcome Type:** Binary virologic response rate.
- **Assumed Control-Arm Value:** 75% Week-48 response in the Atripla (TDF/FTC/EFV) arm.
- **Assumed Treatment-Arm Value:** Same 75% response rate is the non-inferiority planning assumption; a distinct DTG value is not reported in protocol.
- **Target Difference / Effect Size:** Non-inferiority margin of −10 percentage points for DTG minus Atripla response rate.
- **Variability Assumption:** Binomial response-rate calculation; no separate variance assumption is reported in protocol.
- **Alpha (Significance Level):** One-sided 2.5%.
- **Power:** 90%.
- **Statistical Test Assumed:** Non-inferiority assessment of the difference in proportions using the lower bound of a two-sided 95% CI against −10%.
- **Required Number of Events:** Not applicable; this is powered on a binary response rate, not an event-driven time-to-event design.
- **Non-Inferiority / Equivalence Margin:** −10%.
- **Dropout / Non-Adherence Inflation:** No numerical inflation is specified. The 75% planning response incorporates historical approximately 15% drug-related and 14% non-drug-related failure context.
- **Design Effect / Clustering:** Not applicable; individual randomized parallel-group trial with no cluster design.
- **Basis for Assumptions:** Historical Atripla-controlled and GSK trials: approximate control response 71%, recent EFV-arm range 71%–82%, and anticipated better non-drug compliance.
- **Sample Size Re-Estimation / Amendments:** No sample-size re-estimation will be performed.
- **Software Used for Calculation:** Not reported in protocol.
- **Sample Size Rationale:** 394 evaluable per arm provides 90% power for 75% control response and a 10% NI margin at one-sided 2.5%; the recruitment target is approximately 800.

### 2.4 Hypothesis Framework

The primary hypotheses are H0: pDTG−pAtripla ≤−10% versus H1: pDTG−pAtripla >−10%. DTG is non-inferior if the lower bound of the two-sided 95% CI for the response-rate difference is greater than −10%. If ITT-E and PP analyses demonstrate NI, ITT-E superiority is tested two-sided at 5% and declared if the lower 95% CI bound exceeds 0. Conditional on NI, key secondary superiority tests are generalized Wilcoxon (time to suppression), repeated-measures mixed model (Week-48 CD4), and ANCOVA (Week-4 SDM bother), in the specified fallback sequence.

### 2.5 Statistical Interim Analyses

- **Interim Analyses Planned:** Week-48 primary analysis after all complete Week 48 and Week-96 secondary analysis after all complete Week 96; Amendment 05 adds Week-144 analysis. Further cuts may support submissions/publications. An external SDAC provides unblinded data to the IDMC for periodic high-viral-load efficacy and targeted safety review under its charter.
- **Stopping Guidelines:** IDMC operating details and any stopping guidance are in the IDMC charter; not included in this document.
- **Alpha Spending or Adjustment:** No adjustment for repeated Week-48/96 (and amended Week-144) evaluation because Week 96/144 analyses are secondary.

### 2.6 Timing of Analyses

- **Final Analysis Timing:** Final analysis occurs once all subjects have completed or discontinued; Week 48 is primary.
- **Outcome Assessment Schedule:** The final amended protocol schedules RNA at screening, Day 1, Weeks 2,4,8,12,16,24,32,40,48 and every 12 weeks thereafter through Week 144; CD4/CD8, SDM, EQ-5D and safety assessments follow Table 1. Amendment 05 documents the Week-144 open-label/continuation conduct; actual dates allocate analysis windows.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **Alpha Level:** The primary NI comparison is one-sided 2.5%; corresponding CIs are two-sided 95%. All CIs are two-sided.
- **Multiplicity Adjustment:** Gatekeeping permits superiority only after non-inferiority; no adjustment applies solely to secondary Week-96/144 repeated endpoint evaluation. The three key secondary tests use fallback alpha: time to suppression 1%, Week-48 CD4 change 3%, and Week-4 SDM bother change 1%. Rejection passes accumulated alpha forward; non-rejection burns it. Thus P1 rejection makes P2 4%; P1/P2 rejection makes P3 5%; if P1 fails, P2 is 3% and its rejection makes P3 4%; otherwise P3 remains 1%. The sequence controls overall type I error after primary NI.
- **Confidence Intervals:** Stratified CMH adjusted risk differences use Sato variance estimation and two-sided 95% CIs; unadjusted response differences also receive 95% CIs.

### 3.2 Protocol Deviations

- **Adherence Definition:** Compliance is evaluated by pill counts of unused investigational product at every visit through withdrawal or completion.
- **Adherence Assessment:** Pill-count data are recorded in the CRF; IP interruptions are recorded in the CRF.
- **Protocol Deviation Definition:** Deviations affecting the PP population directly affect HIV RNA efficacy or indirectly cause permanent IP discontinuation/withdrawal and missingness.
- **Protocol Deviation Reporting:** Summarize number/percentage with eligibility deviations and PP-exclusion deviations and list subjects/criteria. PP review occurs before database freeze/unblinding at Week-48 and Week-96 analyses.

### 3.3 Analysis Populations

- **Intention-to-Treat:** ITT-E comprises randomized subjects receiving at least one IP dose, analyzed by randomized treatment regardless of treatment received; it is primary for efficacy.
- **Per Protocol:** PP is ITT-E excluding prespecified efficacy-impacting deviations before the relevant timepoint; PP supports the primary endpoint. Deviations include eligibility departures, wrong IP >10% on-treatment, non-treatment-related interruption >10%, relevant prohibited medicines, and withdrawal for protocol deviation.
- **Other Populations:** Safety is exposed subjects analyzed by actual treatment (majority exposure if treatments differ) and is primary for safety. All Screened, Randomized, and PDVF genotype/phenotype populations are used as specified for listings, disposition, and resistance analyses.

## 4. Trial Population

### 4.1 Screening Data

Written consent precedes screening. The screening period is 21 days and may extend to 28; screen data include eligibility, full/targeted medical history, demographics, CDC class, prior ART, HIV risk/mode, concomitant medicines, plasma RNA/genotype, HLA-B*5701, laboratory safety assessments, hepatitis serologies and pregnancy testing. Screening failures and reasons are summarized/listed.

### 4.2 Eligibility Criteria Summary

Eligible subjects must be able to understand and comply, be expected to complete the study as planned, and be appropriate candidates for oral investigational therapy; they are HIV-1 infected adults ≥18 years, have screening RNA ≥1000 c/mL, are ART-naïve (≤10 prior ART days after diagnosis), HLA-B*5701 negative, and provide dated written consent. One re-screen (new number) and one repeat test per analyte/assessment are permitted; genotype retesting is not permitted.

Women must be non-child-bearing (post-menopausal: 12 months amenorrhea and ≥45 years; or documented sterilization) or have negative screening and Day-1 pregnancy tests and use protocol-specified abstinence, double barrier, qualifying IUD/other <1%-failure method, or hormonal contraception plus barrier method, consistently from two weeks before IP through two weeks after it. French enrollment also requires social-security affiliation/beneficiary status.

Exclusions retain the protocol’s numbered structure: breastfeeding; active CDC Category C disease except cutaneous Kaposi not needing systemic therapy (historical/current CD4 <200 is not exclusionary); hepatic impairment; HBsAg positivity or anticipated HCV therapy; recent GI bleed; allergy/intolerance to study drugs/class; recent/ongoing malignancy except specified skin/Kaposi exceptions; recent HIV immunotherapeutic vaccine, radiation, cytotoxic chemotherapy, immunomodulator, HIV-active agent, or experimental drug/vaccine (including France-specific restriction); primary resistance; verified Grade-4/acute disqualifying laboratory abnormality; ALT/bilirubin thresholds; and CrCl <50 mL/min by Cockcroft–Gault.

### 4.3 Recruitment

Sufficient subjects are screened to randomize approximately 800 (~400/arm); the protocol projects approximately 1150 screened. Subjects are recruited from multiple geographic regions.

### 4.4 Withdrawal and Follow-up

- **Withdrawal Levels:** Permanent randomized-treatment discontinuation before Week 96, or open-label discontinuation before commercial drug supply, is study withdrawal. Subjects may discontinue voluntarily; the investigator may discontinue at discretion; and withdrawal may occur for subject/investigator/sponsor request, noncompliance, prohibited therapy, confirmed virologic failure, pregnancy, required substitution/dose reduction, specified QTc/liver/renal toxicity, or causally related Grade 4 clinical AE.
- **Withdrawal Data Collection:** Perform and record Withdrawal and Follow-up procedures before discharge, record essential withdrawal evaluations and CRF reason, and make every effort to follow withdrawing subjects. Ongoing clinical/laboratory AEs trigger a medically appropriate follow-up visit approximately four weeks after last dose.
- **Reasons for Withdrawal:** Subjects need not state a reason; the investigator documents the stated reason or absence of reason in the Completion/Withdrawal CRF. Subjects are not replaced.

### 4.5 Baseline Characteristics

- **Baseline Variables:** Summarize gender, age, ethnicity/race, height, weight, hepatitis status, CDC HIV class, HIV risk/mode, current/past medical conditions, cardiovascular risk, screening/baseline RNA and CD4, and factors affecting completion. Baseline is the last pre-treatment value unless otherwise specified.
- **Summary Methods:** Present counts/percentages for categorical characteristics and descriptive summaries for continuous values by treatment; list subject-level data.

## 5. Analysis

### 5.1 Primary Outcomes

**Outcome: Proportion with plasma HIV-1 RNA <50 c/mL at Week 48**

- **Definition:** MSDF (FDA snapshot) response: last on-treatment RNA in the Week-48 window <50 c/mL; missing, switch, or discontinuation scenarios follow the specified virology-first algorithm.
- **Measurement Units:** Copies/mL, dichotomized at <50 c/mL.
- **Timing of Measurement:** Week 48 analysis window; actual dates, not nominal labels, allocate windows.
- **Transformations / Derived Variables:** Binary responder/nonresponder; continuous RNA summaries use log10 c/mL, with censored values replaced one unit beyond assay limits for summary statistics.

### 5.2 Secondary Outcomes

**Outcome: Time to viral suppression**

- **Definition:** Time to first viral load <50 c/mL.
- **Measurement Units:** Time from treatment initiation; viral RNA threshold in c/mL.
- **Timing of Measurement:** Scheduled RNA assessments through Week 96; subjects without suppression are censored at withdrawal/analysis as specified.
- **Transformations / Derived Variables:** Kaplan–Meier time-to-event endpoint.

**Outcome: Week-96 HIV-1 RNA response**

- **Definition:** Proportion with plasma HIV-1 RNA <50 c/mL using the Week-48 MSDF analysis repeated at Week 96.
- **Measurement Units:** Copies/mL, dichotomized at <50 c/mL.
- **Timing of Measurement:** Week 96; Amendment 05 also repeats analyses at Week 144.
- **Transformations / Derived Variables:** MSDF/snapshot binary response.

**Outcome: Change from baseline in CD4+ cells**

- **Definition:** Change in absolute CD4+ count from last pre-treatment baseline.
- **Measurement Units:** Cells/mm3.
- **Timing of Measurement:** Primary secondary timepoint Week 48; observed/change summaries and analyses at Weeks 48 and 96.
- **Transformations / Derived Variables:** Observed and change-from-baseline values, MMRM estimates, MI, LOCF and missing=baseline analyses.

The CD4 MMRM uses unstructured within-subject correlation, treatment-by-visit and baseline RNA/CD4-by-visit interactions; estimates and 95% CIs are produced by visit.

**Outcome: ACTG virologic failure**

- **Definition:** Confirmed RNA ≥1000 c/mL at/after Week 16 and before Week 24, or ≥200 c/mL at/after Week 24; protocol-defined failure is analyzed separately.
- **Measurement Units:** Copies/mL.
- **Timing of Measurement:** First of two qualifying samples; confirmation ideally 7–28 days later.
- **Transformations / Derived Variables:** Kaplan–Meier time to failure, by baseline RNA stratum and overall, with censoring rules and Pike-estimator odds ratio; repeat the analysis allowing Week-16 RNA ≥1000 c/mL without confirmation.

**Outcome: Symptom Distress Module (SDM) bother score**

- **Definition:** Change from baseline in overall symptom bother score; 20-item self-report, with each symptom scored 0–4.
- **Measurement Units:** Symptom count 0–20 and bother score 0–80.
- **Timing of Measurement:** Baseline, Weeks 4,24,48,96; Week-4 change is the main endpoint.
- **Transformations / Derived Variables:** Aggregate unweighted scores; missing-item rules and LOCF/OC datasets apply.

**Outcome: Longitudinal RNA, CD8+, and HIV disease progression**

- **Definition:** Longitudinal absolute/change RNA and CD4/CD8 and CDC-category progression or death.
- **Measurement Units:** RNA log10 c/mL and CD4/CD8 cells/mm3.
- **Timing of Measurement:** Per Table 1 and actual-date windows.
- **Transformations / Derived Variables:** RNA log10 and CDC progression definitions.

CDC progression is: Category A at baseline to B or C; Category B to C; Category C to a new Category C event; or Category A/B/C to death.

**Outcome: Safety endpoints (other endpoints, not secondary efficacy outcomes)**

- **Definition:** Incidence/severity of AEs and laboratory abnormalities, laboratory changes, AE-related treatment discontinuation, clinically significant ECG changes, and vital-sign change.
- **Measurement Units:** Event counts/percentages, laboratory units, milliseconds for ECG and blood pressure/pulse measures.
- **Timing of Measurement:** Per safety schedule and through follow-up.
- **Transformations / Derived Variables:** DAIDS grades, treatment-emergent shifts, post-baseline status and observed-case summaries.

**Outcome: Virology resistance (other endpoint)**

- **Definition:** Incidence of treatment-emergent genotypic and phenotypic resistance.
- **Measurement Units:** Mutation presence and phenotypic fold-change in IC50 versus wild type.
- **Timing of Measurement:** Baseline and suspected PDVF, with additional permitted timepoints.
- **Transformations / Derived Variables:** Treatment-emergent mutations are absent at baseline and present on treatment.

**Outcome: Health outcomes (other endpoints)**

- **Definition:** Change in utility/health-related QoL, symptom count and symptom bother count.
- **Measurement Units:** EQ-5D utility/VAS, symptom count 0–20, and bother 0–80.
- **Timing of Measurement:** EQ-5D at baseline/Weeks 24,48,96 and SDM at baseline/Weeks 4,24,48,96.
- **Transformations / Derived Variables:** UK EQ-5D tariff and SDM aggregate scoring rules.

### 5.3 Analysis Methods

- **Primary Analysis Methods:** In ITT-E, compare Week-48 MSDF response with a CMH stratified adjusted common risk difference across RNA/CD4 strata, Sato variance and two-sided 95% CI. NI is declared if lower CI >−10%.
- **Covariate Adjustment:** Primary CMH uses baseline RNA and CD4 strata. CD4 MMRM includes baseline RNA/CD4, visit and interactions; SDM/EQ-5D ANCOVA includes primary categorical covariates, gender, race, age and baseline score; bone/lipid models use stated baseline covariates.
- **Assumption Checks:** Test CMH homogeneity using Fleiss weighted least-squares chi-square at one-sided 10%. Assess ANCOVA normality/homoscedasticity by normal-probability and standardized-residual plots and assess influential observations.
- **Alternative Methods if Assumptions Fail:** Explore/report stratum-specific effects for material heterogeneity; combine sparse subgroups or remove baseline factors if logistic convergence fails; conduct additional health-outcome sensitivity analysis if model assumptions fail.
- **Sensitivity Analyses:** Repeat primary comparison in PP and with the alternate continuity-corrected CMH variance estimator; conduct TRDF and ERDF Kaplan–Meier sensitivity analyses; CD4 MI, LOCF and missing=baseline; SDM/EQ-5D OC; and lipid LOCF/OC where stated. TRDF/ERDF, subgroup and homogeneity analyses are supportive and have no multiplicity adjustment.
- **Subgroup Analyses:** Explore treatment effects using logistic regression with treatment-by-subgroup interactions; prespecified strata are baseline RNA and CD4, with gender, race, subtype and other listed descriptors. Interaction p-values use 5%; sparse groups can be combined.

### 5.4 Missing Data

- **Missing Data Assumptions:** MSDF is a virology-first algorithm rather than a stated MAR assumption. CD4 MMRM/MI uses MAR; a treatment-related withdrawal adjustment assumes 3 CD4 cells/week decline off treatment. No general assumption is reported for observed-case data.
- **Handling Methods:** MSDF classifies missing/switch/discontinuation at RNA endpoints; CD4 uses MMRM, 1000 MI, LOCF and missing=baseline; health outcomes use LOCF and OC; other laboratory, RNA continuous, CD8, vitals and ECG analyses use observed data without imputation. For SDM, fewer than 10% missing items (up to two) are treated as symptom absent; if >2 are missing, LOCF is applied at individual symptom level and OC aggregate scores are missing. Lipid LOCF excludes baseline lipid-lowering users, replaces later values after initiation with the last fasted on-treatment value before initiation, and does not impute other missing lipid values. Partial birth dates use day 15 or June 30 as specified; partial AE dates use first/last day of month.

### 5.5 Additional Analyses

Additional analyses include Kaplan–Meier time-to-suppression and ACTG failure; longitudinal snapshot response plots; CDC disease-progression and HIV-associated-condition summaries; resistance prevalence at PDVF; exploratory ANCOVA of bone biomarkers and lipids; ECG, Framingham-risk, hepatitis, PGx and detailed data listings.

### 5.6 Harms

- **Adverse Event Definitions:** An AE is any untoward medical occurrence temporally associated with a medicinal product, regardless of causality. SAE includes death, life-threatening event, hospitalization/prolongation, disability, congenital anomaly, medically important events, Hy’s Law events, and suspected ABC hypersensitivity.
- **Safety Analysis Methods:** Safety population; summarize exposure, post-baseline AEs by MedDRA SOC/preferred term/severity/relatedness/discontinuation/seriousness, labs/vitals/ECG by visit and treatment, and grade 2–4/grade 3–4 AEs. Safety uses observed-case data; data are summarized for randomized phase and specified long-term DTG outputs. Also list exposure duration and dose changes/interruptions; deaths, SAEs, neurologic/psychiatric AEs, pregnancies, suspected ABC hypersensitivity, and liver events. Summarize laboratory toxicity grades/ranges and shifts, NCEP lipid-category changes, ECG QTc categories (≤450, >450–≤480, >480–≤500, >500 msec) and change categories (≤30, >30–≤60, >60 msec), vital signs, and liver stopping-criterion/RUCAM follow-up information.
- **Grading Scales and Causality:** Investigators grade AEs using DAIDS Table for Grading the Severity of Adult and Pediatric AEs, Version 1.0 (December 2004), clarification August 2009; relationship is recorded and treatment-related categories are summarized. AEs are collected from first IP through follow-up; related SAEs from consent through follow-up.

### 5.7 Software and References

- **Statistical Software:** All data manipulation, tabulation and calculation use SAS Version 9.1 on UNIX; PROC MI/MIANALYZE serve CD4 multiple imputation and PROC MIXED health-outcome/adjusted estimates. Figures may use S-Plus or other clinical graphics software on that system. RANDALL/RandAll is validated randomization software.
- **Other Referenced Documents:** Protocol Amendment 05; embedded RAP effective 29-MAY-2012 (based on Amendment 03); RAP SOP_54838 (formerly SOP-WWD-4000) v04, effective 23-MAR-2011; GUI_137354 v01, effective 23-MAR-2011; IDMC charter; Study Procedures Manual; central laboratory manual; and CSR for RAP deviations.

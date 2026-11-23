# Statistical Analysis Plan

## 1. Introduction

### 1.1 Background and Rationale
ENSEMBLE (VAC31518COV3001) is a phase 3 study of Ad26.COV2.S, a recombinant replication-incompetent adenovirus type 26 vector encoding SARS-CoV-2 spike protein, to assess prevention of SARS-CoV-2-mediated COVID-19 in adults aged 18 years or older.

### 1.2 Objectives

**Primary Objectives**

- Demonstrate efficacy of Ad26.COV2.S versus placebo in preventing first molecularly confirmed moderate-to-severe/critical COVID-19 in SARS-CoV-2-seronegative adults, with onset at least Day 15 and, separately, at least Day 29.

**Secondary Objectives**

- Evaluate prevention of severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; burden of symptomatic disease; asymptomatic/undetected infection; and all SARS-CoV-2 infection.
- Evaluate SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, unsolicited AEs, and immunogenicity.

**Exploratory Objectives**

- Explore viral load, immune correlates, functional/molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.

## 2. Study Methods

### 2.1 Trial Design

- **Design Type:** Randomized, double-blind, placebo-controlled phase 3 study in adults aged ≥18 years.
- **Allocation Ratio:** 1:1 Ad26.COV2.S:placebo.
- **Intervention Summary:** One Day-1 0.5-mL injection.
  - Group 1: Ad26.COV2.S 5×10^10 viral particles, supplied at 1×10^11 vp/mL.
  - Group 2: 0.9% sodium chloride placebo.

### 2.2 Randomization

- **Method:** Central computer-generated randomization schedule prepared before study under sponsor supervision.
- **Stratification Factors:** Vaccination unit (site/mobile unit), age (≥18 to <60; ≥60 years), and absence/presence of comorbidities associated or potentially associated with progression to severe COVID-19.
- **Minimization or Blocking:** Randomly permuted blocks; no minimization reported.

### 2.3 Sample Size

- **Planned Sample Size:** Approximately 40,000 participants after Protocol Amendment 3; the previous maximum was approximately 60,000.
- **Outcome Used for Calculation:** First molecularly confirmed moderate-to-severe/critical COVID-19, separately onset ≥Day 15 and ≥Day 29, in PP participants.
- **Outcome Type:** Time-to-first-event/incident case endpoint.
- **Assumed Control-Arm Value:** Null VE 30%.
- **Assumed Treatment-Arm Value:** VE 60%.
- **Target Difference / Effect Size:** VE 60% versus null lower bound 30%.
- **Variability Assumption:** Not reported as a continuous-outcome variability parameter; event allocation uses an exact conditional binomial/SPRT framework.
- **Alpha (Significance Level):** One-sided 2.5%.
- **Power:** Approximately 90% planned; 86.22% with the truncated SPRT through 154 events at VE 60%.
- **Statistical Test Assumed:** Truncated sequential probability ratio test (conditional exact binomial framework), beginning at the 20th event.
- **Required Number of Events:** 154 total co-primary events.
- **Non-Inferiority / Equivalence Margin:** Not applicable; superiority hypotheses test VE >30% for co-primary endpoints.
- **Dropout / Non-Adherence Inflation:** No numerical inflation reported; epidemiologic uncertainty and potential dropouts informed maximum enrollment.
- **Design Effect / Clustering:** Not applicable; individually randomized trial.
- **Basis for Assumptions:** 1.4% moderate/severe incidence for first 3 months, 50% reduction in month 4, 62% reduction thereafter, and 10% seroprevalence; later epidemiologic modeling supported reduction to approximately 40,000.
- **Sample Size Re-Estimation / Amendments:** Amendment 3 reduced enrollment from approximately 60,000 to approximately 40,000 based on observed/modelled incidence.
- **Software Used for Calculation:** gsDesign version 3.1.1 is specified for SPRT boundary code; other sample-size software is not reported.
- **Sample Size Rationale:** The enrollment supports high probability of an efficacy signal within 8 months and sufficient likelihood of five placebo severe cases.

### 2.4 Hypothesis Framework
Co-primary hypotheses are H0: VE≤30% versus H1: VE>30%, each at one-sided 2.5%. Success requires both co-primary tests and, for each timing window, severe/critical VE point estimate ≥50% with at least five placebo severe/critical events. Conditional on primary success, confirmatory secondary tests use H0: VE≤0% versus H1: VE>0% under graphical multiple-testing control.

The graphical sequence evaluates the key confirmatory endpoints: BOD, medical intervention, all infection, and asymptomatic/undetected infection, subject to their endpoint/population windows. Secondary alpha is based on a single-interim Pocock/Wang–Tsiatis Δ=.5 information fraction derived from Day-29 primary events (154 target); the medical-intervention rationale uses 23 events, all-infection testing requires at least 15,000 available Day-71 samples, and asymptomatic testing requires all participants to have ≥6-month follow-up.

### 2.5 Statistical Interim Analyses

- **Interim Analyses Planned:** Continuous monitoring includes symptomatic-harm, severe-harm, non-efficacy, efficacy, and sample-size monitoring. The SSG monitors boundaries, promptly informs the DSMB Chair after a crossing, and the DSMB evaluates totality of data and recommends to the sponsor; the Clinical Severity Adjudication Committee supplies definitive severe/critical classifications.
- **Stopping Guidelines:** Efficacy begins only once ≥6 Day-29 cases aged ≥60, ≥42 Day-29 primary cases, and ≥5 severe/critical Day-29 cases are available; efficacy is checked at least weekly. Symptomatic harm starts at event 12 (exact one-sided binomial test, 5% overall); severe harm starts at event 5 and uses a daily exact one-sided binomial test at unadjusted 5% through primary analysis. Non-efficacy in baseline-seronegative FAS starts at event 20 after Day 15 and declares the boundary when the upper limit of exact 95% CI is <40% for H0 VE≥40% versus H1 VE<40%. Sample-size monitoring assesses whether event accrual supports the study objective.
- **Alpha Spending or Adjustment:** Primary fully sequential SPRT controls FWER at 2.5%; secondary alpha follows graphical gatekeeping and Pocock/Wang-Tsiatis Δ=.5. Harm monitoring is described separately at 5% one-sided.

### 2.6 Timing of Analyses

- **Final Analysis Timing:** Final analysis follows last participant’s month-12 visit or earlier discontinuation; end-of-study analysis follows all month-24 visits or earlier discontinuation.
- **Outcome Assessment Schedule:** eCOA symptom surveillance is at least twice weekly until the later of year 1 or primary analysis, then every 2 weeks; symptomatic episodes trigger serial testing/procedures. Immunogenicity sampling is baseline, Day 29, Day 71, month 6, year 1, month 18, and year 2 for the Immunogenicity Subset; asymptomatic-infection serology uses baseline, Day 71, month 6, and year 1. Co-primary efficacy windows are Day 15 and Day 29; a signal before 8-week median follow-up triggers an analysis at that median-follow-up timepoint.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **Alpha Level:** One-sided 2.5% for co-primary hypotheses, with primary sequential testing controlling family-wise error.
- **Multiplicity Adjustment:** Graphical approach for secondary endpoints, with alpha passed only after significant preceding tests and adjusted for interim stopping by Pocock/Wang-Tsiatis Δ=.5.
- **Confidence Intervals:** Primary VE has sequentially adjusted two-sided 100×(1−2α*)% CI; descriptive subgroups use unadjusted 95% CIs.

### 3.2 Protocol Deviations

- **Adherence Definition:** PP requires vaccine according to assignment and at least 80% of scheduled volume.
- **Adherence Assessment:** Administration log documents injection volume; blinded medical review assesses specified medical/medication deviations case by case.
- **Protocol Deviation Definition:** Major deviations are those judged potentially to affect efficacy or immunogenicity. Efficacy-relevant examples are prohibited medication/medical condition judged on blinded review, another SARS-CoV-2 vaccine, treatment-code awareness, wrong assigned treatment, inadequate (<80%) volume, baseline infection, and consent failure; PPI separately excludes deviations expected to affect immune outcomes and post-event/out-of-window samples.
- **Protocol Deviation Reporting:** Reasons for FAS-but-not-PP status are tabulated. The protocol-deviation appendix specifies categorization by treatment and analysis set, timing and handling before database lock, and treatment after a deviation.

  Major deviations are reviewed and categorized before confirmation/lock. For PP, efficacy data from the time of a prohibited medicine/condition, receipt of another SARS-CoV-2 vaccine, or treatment-code awareness onward are excluded (and the participant is excluded if all post-vaccination data are removed). For PPI, samples after molecularly confirmed infection and samples outside protocol windows are excluded, as are participants with a major deviation expected to affect immunogenicity; sensitivity FAS immune analyses can include excluded samples.

### 3.3 Analysis Populations

- **Intention-to-Treat:** No ITT set is defined; the FAS includes all randomized participants with documented study vaccination, irrespective of deviations and baseline serostatus, analyzed as treated.
- **Per Protocol:** PP efficacy set: FAS participants vaccinated, seronegative at vaccination, without major efficacy-impacting deviations; baseline PCR-positive participants are excluded, with missing serology/PCR treated as negative for analysis.
- **Other Populations:** Enrolled, randomized, FAS, PPI, Immunogenicity Subset (N=400), Safety Subset (approximately N=6,000), and correlates subset are defined.

## 4. Trial Population

### 4.1 Screening Data
Screened, screen-failed (with main reason), enrolled, randomized, vaccinated/not vaccinated, incorrect treatment, FAS, PP, FAS-not-PP, and discontinuation dispositions are summarized by group and overall.

### 4.2 Eligibility Criteria Summary
Participants are adults aged ≥18 years who provide informed consent and can comply with study procedures. Inclusion requires: stable/well-controlled illness and stable medication dose for ≥12 weeks where applicable; protocol-compliant contraception from consent through 3 months after vaccination for those of childbearing potential (hormonal contraception initiated ≥28 days before vaccination), negative highly sensitive urine pregnancy tests at screening and immediately before vaccination, no blood/bone-marrow donation through 3 months after vaccination, verifiable identity/contactability, and ability to complete eCOA questionnaires.

Exclusions are: acute clinically significant illness or temperature ≥38.0°C within 24 hours; serious vaccine/excipient allergy/anaphylaxis; immunologically relevant autoimmune disease/immunodeficiency, chronic/recurrent systemic corticosteroids, antineoplastic/immunomodulating therapy or radiotherapy; immunoglobulin within 3 months or blood products within 4 months; live vaccine within 28 days or non-live vaccine within 14 days; prior coronavirus vaccine; recent investigational drug/device/vaccine; pregnancy, breastfeeding, or pregnancy plan; condition compromising safety/assessments; contraindication to IM injection/blood draw; uncontrolled HIV; serious psychiatric illness/substance abuse; inability to communicate/adhere; and stage-specific high-risk comorbidities, recent malignancy, acute polyneuropathy, surgery, or active hepatitis. Ocular/topical/inhaled steroids and stable non-immunomodulator treatment may be permitted; smoking is not a comorbidity.

### 4.3 Recruitment
Participants are enrolled in staged age/comorbidity strata; randomization controls enrollment distribution to approximately 20% aged 18–<40, 50% aged 40–<60, and at least 30% aged ≥60.

### 4.4 Withdrawal and Follow-up

- **Withdrawal Levels:** Study vaccination may be discontinued while study follow-up continues; participant may discontinue/withdraw from study, withdraw research-sample use, or be lost to follow-up.
- **Withdrawal Data Collection:** Participants unblinded for another authorized/approved COVID-19 vaccine are asked to remain followed where permitted; later data are analyzed separately and efficacy analyses censor at unblinding.
- **Reasons for Withdrawal:** Discontinuation reasons are summarized by treatment group.

### 4.5 Baseline Characteristics

- **Baseline Variables:** Last available assessment before Day-1 vaccination is baseline; weight, height, BMI, demographic variables, comorbidities, serostatus, and frailty are included in planned descriptive/subgroup work.
- **Summary Methods:** Continuous data: n, mean, 95% CI, SD, median, quartiles, minimum, maximum; categorical data: frequencies and percentages.

## 5. Analysis

### 5.1 Primary Outcomes
**Outcome: Moderate-to-severe/critical COVID-19 with onset ≥Day 15**
- **Definition:** First molecularly confirmed symptomatic moderate-to-severe/critical COVID-19 in the PP seronegative population, onset on/after Day 15.
- **Measurement Units:** Incident first COVID-19 case; VE=100×(1−incidence ratio).
- **Timing of Measurement:** From Day 15 through the last available database timepoint; earlier events are excluded for this endpoint.
- **Transformations / Derived Variables:** Molecular confirmation requires positive PCR/molecular testing; moderate/severe category is derived from maximum episode severity.

  Episode onset is the first eCOA/CRF symptom day (first of consecutive at-least-mild days where applicable); when eCOA and eCRF conflict, a symptom is present if either source records it. Classification uses symptoms at any time during the episode, independent of duration; severity categories are mutually exclusive and highest severity prevails. Analysis-ready monitoring cases are centrally confirmed and cleaned by episode Day 15. Moderate disease requires respiratory rate ≥20/min, abnormal room-air SpO2 >93%, clinical/radiologic pneumonia, radiologic DVT, or shortness of breath; alternatively it requires at least two of fever ≥38°C, heart rate ≥90/min, chills/rigors, sore throat, cough, malaise, headache, myalgia, gastrointestinal symptoms, loss of smell/taste, or chilblains/pernio. Severe/critical disease includes respiratory rate ≥30/min, heart rate ≥125/min, SpO2 ≤93%, PaO2/FiO2 <300 mmHg, high-flow oxygen/non-invasive or mechanical ventilation/ECMO, shock (SBP <90, DBP <60, or vasopressors), acute renal/hepatic dysfunction, neurologic signs, ICU admission, or death. Potential severe cases and moderate cases with ≥3 signs/symptoms undergo blinded Clinical Severity Adjudication Committee review; adjudicated severe/critical classification is definitive, and internal review of PCR-positive SAE cases supports sensitivity analysis.

**Outcome: Moderate-to-severe/critical COVID-19 with onset ≥Day 29**
- **Definition:** First molecularly confirmed symptomatic moderate-to-severe/critical COVID-19 in the PP seronegative population, onset on/after Day 29.
- **Measurement Units:** Incident first COVID-19 case; VE=100×(1−incidence ratio).
- **Timing of Measurement:** From Day 29 through the last available database timepoint; earlier events are excluded for this endpoint.
- **Transformations / Derived Variables:** Molecular confirmation and severity derivation are as for the Day-15 co-primary endpoint.

  The same episode-onset, source-conflict, analysis-ready, mutually exclusive severity, threshold, and adjudication rules stated for the Day-15 endpoint apply.

### 5.2 Secondary Outcomes
**Outcome: Severe/critical COVID-19**
- **Definition:** First molecularly confirmed severe/critical case, onset ≥Day 15 and separately ≥Day 29; PP seronegative is confirmatory, with named FAS/PP supportive populations.
- **Measurement Units:** First incident case and VE.
- **Timing of Measurement:** ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** Severe/critical derivation and adjudication as specified for primary endpoints.

**Outcome: Moderate-to-severe/critical COVID-19 regardless of baseline serostatus**
- **Definition:** First molecularly confirmed moderate-to-severe/critical COVID-19 regardless of serostatus.
- **Measurement Units:** First incident case and VE.
- **Timing of Measurement:** Onset Day 2, separately ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** FAS and PP supportive analyses use the prespecified serostatus/population definitions.

**Outcome: BOD, medical intervention, mild/FDA-harmonized disease, asymptomatic/undetected infection, all infection, and viral RNA load**
- **Definition:** Medical intervention is hospitalization, ICU admission, mechanical ventilation, or ECMO linked to confirmed COVID-19; BOD scores mild/moderate=1, severe/critical=2, no symptomatic disease=0; asymptomatic infection is positive molecular test or N-protein serology without symptomatic case, with Day-71/month-6/month-12 conversion rules; all infection is first molecular/serologic infection ≥Day 29; viral load is quantitative RT-PCR AUC in log10 copies/mL. Mild and FDA-harmonized endpoints use their prespecified case definitions.
- **Measurement Units:** First incident case/event, categorical case severity, serial viral-load measures, serologic conversion/antibody titres, AE incidence and grading.
- **Timing of Measurement:** Severe, BOD, medical-intervention, mild, and FDA-harmonized endpoints use Day-15/Day-29 windows as applicable; all infection uses ≥Day 29; asymptomatic conversion uses Day 71/month 6/month 12 and requires completion of month 6 for testing; viral swabs occur at onset and every 2 days for 14 days or until two negative swabs, whichever is later.
- **Transformations / Derived Variables:** BOD and seroconversion are as above. Viral-load AUC uses all available timing and is tested by exact Wilcoxon rank-sum; VE uses geometric mean ratio. Immunogenicity GMT uses log10 transformation/back-transformation; response is baseline≤LLOQ/postbaseline>LLOQ or baseline>LLOQ with ≥4-fold increase.

**Outcome: Mild COVID-19**
- **Definition:** First molecularly confirmed mild COVID-19, defined by the prespecified mild case definition.
- **Measurement Units:** First incident case and VE.
- **Timing of Measurement:** Separately onset ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** VE and CI use Appendix-8 methodology.

**Outcome: Burden of disease (BOD)**
- **Definition:** First symptomatic molecularly confirmed case: mild/moderate score 1, severe/critical score 2, no symptomatic case score 0.
- **Measurement Units:** Severity-adjusted mean BOD score and VE.
- **Timing of Measurement:** PP-seronegative endpoints onset ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** VE is percent reduction in mean BOD score; severity-specific unadjusted CIs are also estimated.

**Outcome: COVID-19 requiring medical intervention**
- **Definition:** First confirmed COVID-19 episode with hospitalization, ICU admission, mechanical ventilation, or ECMO linked to objective clinical measures.
- **Measurement Units:** First event and VE with CI.
- **Timing of Measurement:** Separately onset ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** Follow-up is vaccination-to-first endpoint or cutoff/discontinuation for noncases.

**Outcome: Asymptomatic or undetected SARS-CoV-2 infection**
- **Definition:** No symptomatic case plus positive molecular test or positive non-S-protein serology; conversion is baseline/Day-29 negative and positive at Day 71, month 6, or month 12.
- **Measurement Units:** Seroconversion proportion and VE.
- **Timing of Measurement:** Confirmatory analysis is PP seronegative ≥Day 29 after all complete month 6; Day-1-to-Day-29 analysis is supportive.
- **Transformations / Derived Variables:** Missing Day-29 serology is treated as negative for this derivation.

**Outcome: Any SARS-CoV-2 infection**
- **Definition:** First serologically and/or molecularly confirmed SARS-CoV-2 infection.
- **Measurement Units:** First event and VE with CI.
- **Timing of Measurement:** PP-seronegative onset ≥Day 29; confirmatory testing requires ≥15,000 participants with Day-71 samples.
- **Transformations / Derived Variables:** Participants are categorized once by worst infection occurrence for specified tabulations.

**Outcome: SARS-CoV-2 viral RNA load**
- **Definition:** Viral-load AUC from quantitative RT-PCR nasal samples through episode resolution.
- **Measurement Units:** AUC in log10 copies/mL and geometric mean ratio.
- **Timing of Measurement:** Episode onset and every 2 days for 14 days or until two consecutive negative swabs, whichever is later.
- **Transformations / Derived Variables:** Exact Wilcoxon rank-sum comparison; preplanned 0 imputation and causal selection-bias sensitivity analysis.

**Outcome: FDA-harmonized COVID-19**
- **Definition:** First molecularly confirmed case meeting the US FDA harmonized symptom definition.
- **Measurement Units:** First incident case and VE.
- **Timing of Measurement:** Separately onset ≥Day 15 and ≥Day 29.
- **Transformations / Derived Variables:** It is independently classified alongside mild/moderate/severe severity.

**Outcome: Immunogenicity**
- **Definition:** Binding/neutralizing antibody and N-protein serology, with specified functional/molecular antibody and transcriptomic exploratory assays.
- **Measurement Units:** Titres, GMT, seropositivity/responder percentage, and 95% CI.
- **Timing of Measurement:** Baseline, Day 29, Day 71, and scheduled long-term timepoints; episode Day 3–5 and Day 29 assessments where applicable.
- **Transformations / Derived Variables:** log10 GMT calculation/back-transformation, LLOQ/ULOQ conventions, and protocol responder rule.

**Outcome: Safety and reactogenicity**
- **Definition:** Solicited local/systemic AEs, unsolicited AEs, SAEs, MAAEs, and discontinuation MAAEs.
- **Measurement Units:** Participant incidence, grade, relationship, onset and duration.
- **Timing of Measurement:** Solicited 7 days, unsolicited 28 days, MAAEs through 6 months, and SAEs/discontinuation MAAEs throughout study.
- **Transformations / Derived Variables:** Worst-grade and treatment-emergent phase allocation rules apply.

### 5.3 Analysis Methods

- **Primary Analysis Methods:** PP-seronegative co-primary VE is evaluated with truncated SPRT; cases are analysis-ready at database cut-off. At least weekly, the SSG evaluates available analysis-ready cases; overrun events extend the boundary while retaining overall one-sided α<2.5%. Supportive Cox proportional-hazards/Wald and negative-binomial analyses are specified. Repeated analyses include FAS-seronegative from Day 2, PP-seronegative Day-29 analysis excluding participants seropositive at/before Day 29 (missing data included), and analyses regardless of serostatus if >6 moderate/severe cases occur among baseline-seropositive participants.
- **Covariate Adjustment:** Primary analyses pool ages/comorbidity strata; Cox supportive analysis stratifies by age and comorbidity.
- **Assumption Checks:** No formal primary-model assumption-check procedure is reported.
- **Alternative Methods if Assumptions Fail:** Negative-binomial supportive model; further case-data handling may be specified blinded in DPS for unforeseen situations.
- **Sensitivity Analyses:** Cumulative-incidence VE for waning using Zeng method; causal TMLE sensitivity to differential major-deviation/loss-to-follow-up exclusion; sensitivity includes cases not analysis-ready at lock and alternative severe-case identification.
- **Subgroup Analyses:** Descriptive VE by age and comorbidity; selected analyses by sex, race, ethnicity, age categories, region, comorbidity, serostatus, and frailty; no subgroup hypothesis testing.

### 5.4 Missing Data

- **Missing Data Assumptions:** No MAR/MNAR assumption is reported. Baseline missing serology/PCR is treated as negative for PP determination; follow-up ends at last available measure/discontinuation; unblinding censors efficacy follow-up. Episode resolution uses two negative swabs and two symptom-free days; prespecified assumptions determine whether missing symptom days after symptom-free or symptomatic days are treated as symptom-free or symptomatic.
- **Handling Methods:** Immune-response missing data are not imputed; below-LLOQ values are LLOQ/2 for GMT and LLOQ for geometric mean increase, and above-ULOQ values are ULOQ. For viral-load AUC, below-LLOQ values and missing first/last post-infection observations are imputed as 0; no other viral-load values are imputed. Safety data are not imputed; absent event/medication reports count as no event/medication, and missing severity/relationship remains missing for those summaries. SIC part-1 score is missing when >75% of items are uncollected, except the stated all-yes exception; a missing severity after “yes” is imputed as 5, and a single missing fever day between fever days is interpolated for fever AUC.

### 5.5 Additional Analyses
Reactogenicity uses worst grade and daily maximum temperature/swelling. Immunogenicity uses PPI, scheduled assays including S-ELISA/VNA/N-ELISA and transcriptomics, GMT/95% CI and responder derivations; correlates are governed by a separate Correlates SAP. SIC includes daily symptom mean, duration, AUC, peak, fever and specific-symptom scores; continuous summaries and SE plots use the PP set. Disease resolution is summarized with Kaplan–Meier; proportional odds explores severity, medical intervention is summarized by intervention, and frailty is assessed longitudinally. Kaplan–Meier curves and forest plots display endpoint/subgroup VE.

### 5.6 Harms

- **Adverse Event Definitions:** Solicited AEs are predefined local/systemic events actively queried in diary; unsolicited AEs are not actively queried. Safety captures solicited events for 7 days in Safety Subset, unsolicited AEs for 28 days, SAEs and discontinuation MAAEs for the entire study, and MAAEs through 6 months.
- **Safety Analysis Methods:** FAS, as-treated, descriptive analyses by treatment, age, comorbidity, and serostatus; no formal safety hypothesis tests. Tabulations include numbers/percentages, exact 95% CI when appropriate, SOC/PT summaries, worst grade, relatedness, onset, and duration.
- **Grading Scales and Causality:** AEs are grade 1–4; solicited administration-site symptoms are related by definition; FDA toxicity scale is used if a solicited grade is unavailable.

### 5.7 Software and References

- **Statistical Software:** gsDesign version 3.1.1 for SPRT-boundary code; R code developed by P.N. Gilbert and R.J. Bosch for viral-load causal sensitivity analysis (version and bootstrap implementation details not reported).
- **Other Referenced Documents:** Approved final SAP dated 15 January 2021 (version-history changes through version 5); Protocol Amendment 3; Protocol; Data Presentation Specification; modeling/simulation report; separate sponsor unblinding strategy; DSMB Charter; separate Correlates SAP; Investigator’s Brochure; and FDA toxicity grading scale.

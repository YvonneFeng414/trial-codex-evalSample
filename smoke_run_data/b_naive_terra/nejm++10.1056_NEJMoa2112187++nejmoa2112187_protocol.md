# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Patients with recurrent or metastatic cervical cancer progressing after platinum-based chemotherapy have poor outcomes and no widely accepted subsequent systemic standard. This pivotal phase 3 study compares cemiplimab with investigator’s-choice (IC) chemotherapy.

### 1.2 Objectives

**[Provided]** The primary objective is to compare overall survival (OS) for cemiplimab versus IC chemotherapy, first in patients with squamous cell carcinoma (SCC), then in the overall eligible population, which includes SCC and adenocarcinoma/adenosquamous carcinoma.

**[Provided]** Secondary objectives in the SCC and overall populations are to compare progression-free survival (PFS), objective response rate (ORR) by RECIST 1.1, duration of response (DoR), adverse-event profiles, and EORTC QLQ-C30 global-health-status/quality-of-life (GHS/QoL) and physical-functioning mean change from baseline.

**[Provided]** Exploratory objectives are to characterize serum cemiplimab pharmacokinetics (PK) and immunogenicity and explore associations of efficacy with pretreatment-tumor molecular features and peripheral-blood pharmacodynamic activity.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is an open-label, randomized, multicentre phase 3 trial with screening, treatment, follow-up and subsequent survival follow-up. Allocation is 1:1 to cemiplimab or IC chemotherapy. Treatment crossover is not permitted.

**[Provided]** Treatment is planned for up to 96 weeks:

- **[Provided]** Cemiplimab: 350 mg intravenously every 3 weeks.
- **[Provided]** Pemetrexed: 500 mg/m² intravenously on day 1 every 21 days, with folate/vitamin B12 support.
- **[Provided]** Topotecan: 1 mg/m² intravenously daily for 5 days every 21 days; the dose may increase to 1.25 mg/m² after the first course without significant toxicity.
- **[Provided]** Irinotecan: 100 mg/m² intravenously weekly for 4 doses, followed by 10–14 days’ rest, or at least 14 days in Japan; the dose may increase to 125 mg/m² after the first course without significant toxicity.
- **[Provided]** Gemcitabine: 1000 mg/m² intravenously on days 1 and 8 every 21 days.
- **[Provided]** Vinorelbine: 30 mg/m² intravenously on days 1 and 8 every 21 days.

**[Provided]** Cemiplimab and IC treatment continue to 96 weeks or RECIST 1.1 progression, unacceptable toxicity, death, or consent withdrawal. Cemiplimab may continue beyond RECIST progression only under protocol criteria. During follow-up, a patient with progressive disease (PD) may be retreated with the same originally assigned drug; IC selection and each drug’s dose and schedule are protocol specified.

**[Clarification Required]** Specify the criteria for cemiplimab treatment beyond progression and for retreatment, including timing and duration. These decisions determine treatment eligibility and interpretation of post-progression outcomes.

### 2.2 Randomization

**[Provided]** The interactive web response system assigns treatment after the investigator deems the patient eligible.

**[Provided]** Stratification factors for the SCC analysis are geographic region: North America, Asia-Pacific, and rest of world. The overall analysis uses region and histology: SCC versus adenocarcinoma, with adenosquamous classified as adenocarcinoma.

**[Provided]** Before Amendment 5, patients were stratified by SCC versus adenocarcinoma/adenosquamous histology. After Amendment 5, only patients with SCC were randomized; the historical histology distinction is retained in the overall-population analysis.

**[Clarification Required]** Specify the allocation algorithm, including whether blocking or minimization was used, and how erroneous recorded stratification factors are handled. These details affect implementation and analysis reproducibility.

### 2.3 Sample Size

**[Provided]** Planned enrollment is 460 randomized patients with SCC, with approximately 590 patients projected overall. The calculation uses SCC OS, a time-to-event outcome.

**[Provided]** Assumed median OS is 7 months with IC chemotherapy and 10 months with cemiplimab. The target hazard ratio (HR) is 0.70, corresponding to an approximately 42.8% increase in median OS under exponential distributions.

**[Provided]** With an overall one-sided alpha of 0.025, approximately 90% power is planned for HR 0.70 with 340 SCC OS events, using a group-sequential stratified log-rank test and Lan-DeMets O’Brien-Fleming alpha spending. Annual dropout is assumed to be 10%. The trial is individually randomized; a clustering design effect is not applicable. No non-inferiority or equivalence margin applies.

**[Provided]** The assumptions draw on phase 2 reports of IC median OS of 6.5–8.1 months. Assumed enrollment is 2 patients per month during months 1–5, 9 per month during months 6–16, 20 per month during months 17–23, and 22 per month thereafter.

**[Provided]** The 460 SCC patients are expected to yield 340 events approximately 42 months after first SCC randomization. Overall-population power is projected above 90% if HR is 0.70. East version 6.4.1 was used for the calculation.

**[Provided]** SAP v2.0 updated sample size, interim analysis, target population and enrollment rate for protocol amendments through Amendment 6. A formal sample-size re-estimation procedure is not specified.

### 2.4 Hypothesis Framework

**[Provided]** The null hypothesis is that cemiplimab and IC chemotherapy have the same OS survival curve; the alternative is that cemiplimab is superior. OS is tested first in SCC and, only if significant, in the overall population.

**[Proposed]** Apply this directional superiority framework separately to the SCC and overall populations, with an HR below 1 favoring cemiplimab. This makes the comparison interpretable; it assumes the HR is an adequate summary of the survival difference.

**[Clarification Required]** Specify when a significant SCC result permits the overall-population test, including at interim looks. This is needed to implement the hierarchy without exceeding the intended type I error.

### 2.5 Statistical Interim Analyses

**[Provided]** The planned OS design is group sequential with Lan-DeMets O’Brien-Fleming alpha spending.

**[Clarification Required]** Specify the number and timing of interim looks, information fractions, efficacy boundaries, any futility rules, and the consequences of crossing a boundary, including any effect on the 340-event final cutoff. These decisions are necessary to calculate boundaries and interpret repeated testing.

**[Clarification Required]** Specify interim oversight, access to unblinded results and procedures for acting on recommendations. These decisions protect trial integrity and define authority for stopping or continuing.

### 2.6 Timing of Analyses

**[Provided]** The final OS cutoff occurs when 340 SCC OS events are observed. Events through cutoff are included; otherwise, OS is censored at the earlier of the last-known-alive date or cutoff.

**[Provided]** Treatment starts within 5 days after randomization, or within 10 days for pemetrexed, in 6-week cycles.

**[Provided]** CT/MRI is scheduled on day 42 ±7 days of cycles 1–4, 6, 8, 10, 12, 14 and 16. After treatment, imaging is every 90 ±10 days until PD for patients without prior PD.

**[Provided]** QLQ-C30 is assessed at screening and on day 1 of treatment cycles, potentially at another visit in the same cycle, before procedures; it is also assessed at post-treatment follow-up visits 1 and 2.

**[Provided]** Follow-up visit 1 is approximately 30 ±10 days after the last dose; visit 2 is approximately 90 ±10 days later. Survival ascertainment then occurs every 90 ±10 days until death or completion.

**[Clarification Required]** Specify database-lock and data-readiness requirements, including event verification and cutoff procedures. These are needed to determine when the analysis dataset is sufficiently complete.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The overall one-sided alpha is 0.025, with sequential alpha spending for OS and hierarchical testing of SCC before the overall population.

**[Proposed]** Report two-sided 95% confidence intervals for effect estimates, identifying intervals not adjusted for sequential monitoring or endpoint selection as nominal. This provides interpretable precision; it assumes nominal intervals are acceptable for estimation alongside the prespecified sequential tests.

**[Clarification Required]** Specify multiplicity control, if any, for secondary endpoints and whether adjusted confidence intervals are required for sequential or hierarchical inference. This determines which secondary claims are confirmatory and how interval coverage is interpreted.

### 3.2 Protocol Deviations

**[Proposed]** Document and summarize deviations by randomized group, identifying important deviations before unblinded analysis where practicable. This supports assessment of conduct; it assumes deviation classification can be applied consistently.

**[Clarification Required]** Define important deviations and their effect, if any, on analysis populations and sensitivity analyses. These decisions determine whether exclusions or alternative analyses are justified.

### 3.3 Analysis Populations

**[Proposed]** Use all randomized patients according to randomized assignment for the main efficacy analyses, with an SCC subset and an overall population. This preserves randomized comparisons; it assumes the intended efficacy population includes patients subsequently found ineligible or untreated.

**[Clarification Required]** Resolve how the stated overall *eligible* population relates to all randomized patients, and specify whether SCC membership and analysis strata use recorded or subsequently adjudicated information. These decisions can change denominators, strata and primary results.

**[Proposed]** Analyze safety in patients receiving at least one study-drug dose, grouped by treatment received. This describes exposure-related harms; it assumes actual treatment can be reliably identified.

**[Proposed]** Describe PK, immunogenicity and biomarker analyses using patients with relevant evaluable samples and measurements. This reflects data availability; it assumes assay-specific evaluability criteria will be defined before analysis.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Summarize numbers screened, randomized and not randomized, with available reasons for nonrandomization. This describes selection into the trial; it assumes sites collect these data consistently.

### 4.2 Eligibility Criteria Summary

**[Provided]** Inclusion criteria are:

- **[Provided]** Women aged at least 18 years with recurrent, persistent or metastatic noncurable cervical SCC; adenocarcinoma/adenosquamous carcinoma was allowed before Amendment 5.
- **[Provided]** Progression after platinum specifically for recurrent, persistent or metastatic cancer, not curative chemoradiation.
- **[Provided]** A RECIST 1.1 measurable lesion at least 10 mm by CT, MRI or caliper, or at least 20 mm by chest radiograph; nodes must be more than 15 mm in short axis.
- **[Provided]** ECOG performance status ≤1.
- **[Provided]** Bilirubin ≤1.5 × upper limit of normal (ULN), or ≤3 × ULN with liver metastases; transaminases ≤3 × ULN, or ≤5 × ULN with liver metastases; and alkaline phosphatase ≤2.5 × ULN, or ≤5 × ULN with liver or bone metastases.
- **[Provided]** Creatinine ≤1.5 × ULN or clearance >45 mL/min; hemoglobin ≥9 g/dL; absolute neutrophil count ≥1.5 × 10⁹/L; and platelets ≥75 × 10⁹/L.
- **[Provided]** Life expectancy >12 weeks, ability to comply and complete questionnaires, consent, and required prior bevacizumab/paclitaxel status or exceptions.

**[Provided]** Exclusion criteria are:

- **[Provided]** Significant systemic-treatment autoimmune disease; prior PD-1/PD-L1 therapy; an immune modulator within 4 weeks or recent associated toxicity; or >10 mg prednisone-equivalent immunosuppression within 4 weeks.
- **[Provided]** Active or unstable central nervous system metastasis; active serious infection/HIV/HBV/HCV; or pneumonitis within 5 years.
- **[Provided]** Anticancer therapy within 30 days or radiation within 14 days; relevant allergy; concurrent or recent malignancy; or transplant.
- **[Provided]** Pregnancy, breastfeeding, or failure to use required contraception.

**[Clarification Required]** Specify the prior bevacizumab/paclitaxel requirements and exceptions, and operational definitions or time windows not supplied for the summarized exclusions. These are needed for reproducible eligibility decisions.

### 4.3 Recruitment

**[Provided]** Approximately 590 total patients are projected, including 460 randomized patients with SCC; enrollment assumptions are given in Section 2.3.

**[Clarification Required]** Specify participating sites, recruitment dates and actual enrollment by population and amendment period. These are needed to describe trial conduct and generalizability.

### 4.4 Withdrawal and Follow-up

**[Provided]** Consent withdrawal is a treatment-stopping condition. Follow-up and survival-ascertainment schedules are given in Section 2.6.

**[Proposed]** Record reasons for treatment discontinuation, withdrawal from assessments and loss to follow-up separately, and continue permitted survival ascertainment where consent allows. This distinguishes treatment discontinuation from missing outcomes; it assumes patients have not withdrawn permission for the relevant follow-up.

**[Clarification Required]** Specify procedures and permissions after withdrawal, including use of already collected data. These determine what follow-up and analyses are permissible.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize demographics, region, histology, disease characteristics, prior therapies, ECOG status and relevant baseline laboratory and questionnaire measures by randomized group and analysis population. This describes balance and context; it assumes these variables are collected.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** OS is the primary outcome, compared first in SCC and then, only if significant, in the overall eligible population.

**[Proposed]** Define OS as time from randomization to death from any cause and apply the supplied cutoff and censoring rule. This aligns the endpoint with randomized comparison; it assumes randomization is the intended time origin.

**[Proposed]** Use the stratified log-rank test with the supplied analysis strata and sequential boundaries; estimate the treatment HR and confidence interval with a stratified Cox model and display Kaplan–Meier curves. This addresses the planned comparison; it assumes valid stratification data and that the HR is a useful summary.

### 5.2 Secondary Outcomes

**[Provided]** Secondary outcomes are PFS, ORR by RECIST 1.1, DoR, adverse-event profiles, and QLQ-C30 GHS/QoL and physical-functioning mean change from baseline, in SCC and overall populations.

**[Proposed]** Define PFS from randomization to first documented progression or death, whichever occurs first; define DoR from first documented response to progression or death. This supplies analyzable time-to-event definitions; it assumes these events and dates are collected consistently.

**[Proposed]** Define ORR as the proportion with complete or partial response under RECIST 1.1. This makes the response comparison operational; it assumes the response assessments are suitable for applying RECIST categories.

**[Clarification Required]** Specify the assessment source, response-confirmation requirements, endpoint-specific censoring rules and handling of subsequent anticancer treatment and missed assessments. These choices materially affect PFS, ORR and DoR estimates.

### 5.3 Analysis Methods

**[Proposed]** Analyze PFS using stratified log-rank and Cox methods and Kaplan–Meier estimates; report ORR by group with a between-group difference and confidence interval; summarize DoR among responders using Kaplan–Meier methods. This provides complementary effect summaries; it assumes adequate event and response data. DoR comparisons are descriptive because responders are post-randomization subsets.

**[Proposed]** For each QLQ-C30 domain, analyze change from screening baseline using a repeated-measures model with treatment, visit, treatment-by-visit interaction, baseline score and relevant stratification factors. Report estimated mean changes and between-group differences by visit. This uses longitudinal data; it assumes appropriate model specification and missing-at-random data among patients for whom the outcome is defined.

**[Proposed]** Use standard QLQ-C30 scoring, with higher GHS/QoL and physical-functioning scores indicating better status. This supports interpretation; it assumes the standard scoring rules are applicable to the collected questionnaire.

**[Clarification Required]** Specify the target QoL estimand, including the handling of treatment discontinuation, subsequent therapy and death. Scores after death are undefined, so the choice affects the population and meaning of the comparison.

### 5.4 Missing Data

**[Provided]** For OS, patients without an event through cutoff are censored at the earlier of last-known-alive date or cutoff.

**[Proposed]** Describe missingness and follow-up by treatment group and endpoint. Assess the influence of missing tumor assessments and questionnaire data in prespecified sensitivity analyses. This helps assess robustness; it assumes missingness patterns and assessment dates are available.

**[Proposed]** Consider a questionnaire sensitivity analysis under departures from missing at random, without imputing QoL scores after death. This tests a key modeling assumption while recognizing that post-death scores are undefined; it assumes a clinically interpretable sensitivity scenario can be specified.

**[Clarification Required]** Specify PFS censoring after missed assessments, the ORR treatment of unevaluable patients, and sensitivity-analysis scenarios. These decisions affect estimates and cannot be recovered from the supplied definitions.

### 5.5 Additional Analyses

**[Proposed]** Examine OS consistency across prespecified baseline subgroups and assess proportional-hazards plausibility using survival plots and model diagnostics. This helps interpret the overall HR; it assumes subgroup data and sufficient events are available. Treat subgroup findings as exploratory.

**[Provided]** Exploratory analyses characterize serum cemiplimab PK and immunogenicity and explore associations of efficacy with pretreatment-tumor molecular features and peripheral-blood pharmacodynamic activity.

**[Clarification Required]** Specify sample collection times, assays, evaluability criteria and planned PK, immunogenicity and biomarker analyses. These determine whether the exploratory objectives can be executed and interpreted.

### 5.6 Harms

**[Provided]** Adverse-event profiles are secondary outcomes in the SCC and overall populations. Unacceptable toxicity is a treatment-stopping condition.

**[Proposed]** Summarize adverse events, serious events, severity, deaths and events leading to treatment discontinuation by treatment received. This describes the safety profile; it assumes events and treatment exposure are collected consistently.

**[Clarification Required]** Specify the adverse-event coding and severity systems, treatment-emergent reporting window, causality rules and serious-event reporting procedures. These determine the safety denominators, classifications and reporting obligations.

### 5.7 Software and References

**[Provided]** East version 6.4.1 was used for the sample-size calculation.

**[Proposed]** Record the software and versions used for all analyses and validate the primary analysis programs. This supports reproducibility; it assumes analysis software and validation procedures will be selected before reporting.

**[Clarification Required]** Specify the software and versions for the planned analyses. These are needed to reproduce the statistical output.

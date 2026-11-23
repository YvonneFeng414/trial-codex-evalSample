# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Patients with recurrent or metastatic cervical cancer progressing after platinum-based chemotherapy have poor outcomes and no widely accepted subsequent systemic standard. This pivotal phase 3 study compares cemiplimab with investigator’s-choice (IC) chemotherapy.

### 1.2 Objectives

- **[Provided]** **Primary:** Compare overall survival (OS) between cemiplimab and IC chemotherapy, first among patients with squamous cell carcinoma (SCC), then in the overall eligible population comprising SCC or adenocarcinoma/adenosquamous carcinoma.
- **[Provided]** **Secondary:** Compare progression-free survival (PFS), objective response rate (ORR) by RECIST 1.1, duration of response (DoR), adverse-event profiles, and EORTC QLQ-C30 global-health-status/quality-of-life (GHS/QoL) and physical-functioning mean change from baseline, in SCC and overall populations.
- **[Provided]** **Exploratory:** Characterize serum cemiplimab pharmacokinetics (PK) and immunogenicity, and explore associations of efficacy with pretreatment-tumor molecular features and peripheral-blood pharmacodynamic activity.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is an open-label, randomized, multicentre phase 3 trial with screening, treatment, follow-up, and subsequent survival follow-up. Allocation is 1:1 to cemiplimab or IC chemotherapy, with no treatment crossover.

**[Provided]** Treatment is planned for up to 96 weeks. The assigned treatments are:

- **[Provided]** **Cemiplimab:** 350 mg intravenously every 3 weeks.
- **[Provided]** **IC chemotherapy:** Pemetrexed, topotecan, irinotecan, gemcitabine, or vinorelbine.
- **[Provided]** **Pemetrexed:** 500 mg/m² intravenously on day 1 every 21 days, with folate/vitamin B12 support.
- **[Provided]** **Topotecan:** 1 mg/m² intravenously daily for 5 days every 21 days; the dose may increase to 1.25 mg/m² after the first course without significant toxicity.
- **[Provided]** **Irinotecan:** 100 mg/m² intravenously weekly for 4 doses, followed by 10–14 days’ rest, or at least 14 days in Japan; the dose may increase to 125 mg/m² after the first course without significant toxicity.
- **[Provided]** **Gemcitabine:** 1000 mg/m² intravenously on days 1 and 8 every 21 days.
- **[Provided]** **Vinorelbine:** 30 mg/m² intravenously on days 1 and 8 every 21 days.

**[Provided]** Cemiplimab and IC chemotherapy continue until 96 weeks, RECIST 1.1 progression, unacceptable toxicity, death, or consent withdrawal. Cemiplimab may continue beyond RECIST progression only under protocol criteria. During follow-up, a patient with progressive disease may be retreated with the same originally assigned drug. IC selection and each drug’s dose/schedule are protocol specified.

**[Clarification Required]** The criteria for cemiplimab treatment beyond progression, retreatment eligibility and duration, the relationship of retreatment to the 96-week limit, and detailed dose-interruption/reduction rules are not supplied. These decisions are necessary for reproducible treatment delivery and exposure analysis.

**[Clarification Required]** Detailed IC selection criteria and the definition of “without significant toxicity” for topotecan and irinotecan escalation are unavailable. These affect regimen eligibility and safe dose escalation.

**[Proposed]** Require ethics approval, documented informed consent before study-specific procedures, confidentiality protections, and a documented safety-reporting pathway. Rationale: these provide essential participant protections. Assumption: applicable jurisdictional requirements will govern implementation.

### 2.2 Randomization

**[Provided]** Treatment assignment occurs through an interactive web response system (IWRS) after the investigator determines eligibility.

**[Provided]** The SCC analysis is stratified by geographic region: North America, Asia-Pacific, and rest of world (ROW). The overall analysis is stratified by region and histology: SCC versus adenocarcinoma, with adenosquamous carcinoma classified as adenocarcinoma.

**[Provided]** Before Amendment 5, patients were stratified by SCC versus adenocarcinoma/adenosquamous histology. After Amendment 5, only SCC patients were randomized. The historical histology distinction is retained in the overall-population analysis.

**[Clarification Required]** The allocation-sequence method, blocking or minimization, allocation-concealment safeguards within IWRS, and implementation of stratification across amendments are unspecified. These details are needed to document allocation integrity and reproduce randomization.

**[Proposed]** Record the intended IC regimen before treatment assignment. Rationale: prespecification reduces treatment-selection bias in an open-label trial. Assumption: prospective regimen selection is operationally feasible and consistent with the finalized protocol.

### 2.3 Sample Size

- **[Provided]** Planned enrollment is 460 randomized SCC patients, with approximately 590 total patients projected.
- **[Provided]** The calculation targets OS in SCC patients, assuming exponential OS distributions, median OS of 7 months with IC chemotherapy and 10 months with cemiplimab, and a target hazard ratio (HR) of 0.70, corresponding to approximately a 42.8% increase in median OS.
- **[Provided]** Approximately 90% power is expected with 340 SCC OS events, using an overall one-sided alpha of 0.025 and a group-sequential, stratified log-rank test with Lan–DeMets O’Brien–Fleming alpha spending.
- **[Provided]** The dropout assumption is 10% per year. No clustering design effect applies because patients are individually randomized. This is a superiority design; no non-inferiority or equivalence margin applies.
- **[Provided]** The control-survival assumption is based on phase 2 IC median OS reports of 6.5–8.1 months. Enrollment assumptions are 2 patients/month during months 1–5, 9/month during months 6–16, 20/month during months 17–23, and 22/month thereafter.
- **[Provided]** The 460 SCC patients are expected to yield 340 events approximately 42 months after first SCC randomization. Overall-population power is projected above 90% if HR = 0.70.
- **[Provided]** SAP version 2.0 updated sample size, interim analysis, target population, and enrollment rate for protocol amendments through Amendment 6. A formal sample-size re-estimation procedure is not specified.
- **[Provided]** Sample-size calculations used East version 6.4.1.

**[Clarification Required]** The operational meaning of the 10% annual dropout assumption and whether the enrollment-rate assumptions apply to SCC or total accrual are not specified. These distinctions matter for reproducing event-accrual projections.

### 2.4 Hypothesis Framework

**[Provided]** The null hypothesis is that cemiplimab and IC chemotherapy have the same OS survival curve. The alternative hypothesis is that cemiplimab is superior.

**[Provided]** OS is tested first in SCC patients and, only if significant, in the overall eligible population.

**[Derived]** Confirmatory overall-population OS superiority cannot be declared through this hierarchy if the SCC OS test does not meet its applicable significance criterion.

**[Proposed]** Express the treatment effect as the cemiplimab-to-IC death HR, with HR <1 favoring cemiplimab. Rationale: this aligns effect reporting with the design assumption. Assumption: a proportional-hazards summary is sufficiently informative; departures will be examined separately.

### 2.5 Statistical Interim Analyses

**[Provided]** The design uses a group-sequential, stratified log-rank OS test with Lan–DeMets O’Brien–Fleming alpha spending.

**[Clarification Required]** The number and timing of interim looks, information fractions, numerical efficacy boundaries, spending-function implementation, overrun handling, and any futility rule are not supplied. These are necessary to execute the sequential design without altering its type I error.

**[Clarification Required]** The rules for opening and repeatedly testing the overall-population OS hypothesis after SCC success are not specified. A joint sequential/gatekeeping procedure is needed to preserve the overall one-sided 0.025 error rate.

**[Clarification Required]** Interim-review membership, access to unblinded results, stopping recommendations, and decision authority are unspecified. These determine operational independence and confidentiality.

**[Proposed]** Finalize an interim-analysis charter before any unblinded efficacy review and use independent review of unblinded efficacy and safety data. Rationale: this limits operational bias and prevents data-driven boundary selection. Assumption: an appropriately independent review mechanism can be established.

### 2.6 Timing of Analyses

- **[Provided]** The final OS cutoff occurs when 340 SCC OS events are observed. Events through cutoff are included; otherwise, OS is censored at the earlier of last-known-alive date or cutoff.
- **[Provided]** Treatment starts within 5 days after randomization, or within 10 days for pemetrexed, in 6-week study cycles.
- **[Provided]** CT/MRI is performed on day 42, ±7 days, of cycles 1–4, 6, 8, 10, 12, 14, and 16.
- **[Provided]** After treatment, patients without prior progression undergo imaging every 90 days, ±10 days, until progressive disease.
- **[Provided]** QLQ-C30 is administered at screening and on day 1 of treatment cycles, or another visit within the same cycle, before procedures; it is also administered at post-treatment follow-up visits 1 and 2.
- **[Provided]** Follow-up visit 1 occurs approximately 30 days, ±10 days, after the last dose. Visit 2 occurs approximately 90 days, ±10 days, later. Survival ascertainment then occurs every 90 days, ±10 days, until death or study completion.

**[Clarification Required]** Database-lock requirements, data-readiness criteria, interim and secondary endpoint cutoffs, and whether all endpoints share the final OS cutoff are unspecified. These decisions determine which observations enter each analysis.

**[Proposed]** Before each analysis, reconcile deaths, treatment exposure, tumor assessments, and outstanding endpoint queries, then freeze the relevant data and analysis specifications. Rationale: consistent data maturity and traceability support reproducible inference. Assumption: this process does not change the prespecified event-triggered cutoff.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The overall primary-testing significance level is one-sided 0.025, with sequential alpha spending and SCC-before-overall testing.

**[Proposed]** Report treatment-effect estimates with two-sided 95% confidence intervals for descriptive interpretation; base confirmatory primary conclusions on the applicable sequential boundary rather than an unadjusted interval. Rationale: this separates estimation from sequential hypothesis testing. Assumption: the final SAP will additionally specify any sequentially adjusted intervals.

**[Clarification Required]** Confirmatory status, testing order, alpha allocation, and multiplicity adjustment for secondary outcomes, QoL domains, populations, and time points are not supplied. These decisions determine whether secondary findings can support controlled confirmatory claims.

**[Proposed]** Until a secondary multiplicity strategy is approved, present secondary and exploratory p-values and confidence intervals as nominal and avoid confirmatory claims. Rationale: this prevents unsupported interpretation of multiple comparisons. Assumption: no additional error-control procedure has been established.

### 3.2 Protocol Deviations

**[Proposed]** Prospectively classify important deviations, including eligibility violations, incorrect treatment, prohibited crossover, major dosing departures, and assessment failures that could affect endpoint interpretation. Retain patients in the primary randomized analysis regardless of these deviations. Rationale: classification supports transparent sensitivity analyses without compromising randomization. Assumption: categories and adjudication rules are finalized before unblinded outcome review.

**[Clarification Required]** The deviation taxonomy, adjudication process, thresholds for major deviations, and any per-protocol exclusions are unspecified. These are needed to prevent outcome-dependent exclusions and inconsistent reporting.

### 3.3 Analysis Populations

**[Clarification Required]** “Overall eligible population” is not operationally defined relative to all randomized patients, particularly those later found ineligible. This must be resolved because post-randomization exclusions can change the primary estimand and introduce bias.

**[Proposed]** Use all randomized patients, analyzed as assigned, for overall efficacy analyses; define the SCC efficacy subset using the prespecified histology classification at randomization. Rationale: this preserves the randomized comparison. Assumption: this intention-to-treat interpretation is approved as the operational meaning of the primary populations.

**[Proposed]** Define the safety population as all patients receiving at least one dose, analyzed according to treatment actually received. Rationale: safety attribution depends on exposure. Assumption: dosing records reliably establish actual treatment.

**[Proposed]** Define PK and immunogenicity evaluability using documented cemiplimab exposure and valid relevant samples; define QoL evaluability using valid baseline and postbaseline questionnaires, while reporting questionnaire availability for the full randomized populations. Rationale: these analyses require usable measurements. Assumption: assay and questionnaire validity rules are finalized before analysis.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Maintain a screening and disposition log showing patients screened, reasons for exclusion, randomized allocation, treatment receipt, discontinuation, follow-up status, and analysis-set membership. Rationale: participant flow is needed to assess selection and attrition. Assumption: screening information can be collected consistently while protecting confidentiality.

**[Clarification Required]** Actual screening counts, screen-failure reasons, and patient-flow data are not supplied. These must come from study records; no observed counts can be specified here.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Women aged ≥18 years with recurrent, persistent, or metastatic noncurable cervical SCC are eligible; adenocarcinoma/adenosquamous carcinoma was allowed before Amendment 5.
- **[Provided]** Progression must have occurred after platinum specifically for recurrent, persistent, or metastatic cancer, not after platinum given solely as curative chemoradiation.
- **[Provided]** Measurable disease must include a RECIST 1.1 lesion ≥10 mm by CT/MRI/caliper or ≥20 mm by chest radiograph; lymph nodes must be >15 mm in short axis.
- **[Provided]** ECOG performance status must be ≤1, and life expectancy must exceed 12 weeks.
- **[Provided]** Bilirubin must be ≤1.5× the upper limit of normal (ULN), or ≤3× ULN with liver metastases; transaminases must be ≤3× ULN, or ≤5× ULN with liver metastases.
- **[Provided]** Alkaline phosphatase must be ≤2.5× ULN, or ≤5× ULN with liver/bone metastases.
- **[Provided]** Creatinine must be ≤1.5× ULN or creatinine clearance >45 mL/min.
- **[Provided]** Hemoglobin must be ≥9 g/dL, absolute neutrophil count ≥1.5×10⁹/L, and platelets ≥75×10⁹/L.
- **[Provided]** Patients must be able to comply with study procedures and complete questionnaires, provide consent, and satisfy the required prior bevacizumab/paclitaxel status or applicable exceptions.

**[Clarification Required]** The required prior bevacizumab/paclitaxel exposure and permitted exceptions are not detailed. These requirements must be specified to determine eligibility consistently.

- **[Provided]** Exclusions include significant systemic-treatment autoimmune disease, prior PD-1/PD-L1 therapy, immune-modulator use within 4 weeks or recent associated toxicity, and >10-mg prednisone-equivalent immunosuppression within 4 weeks.
- **[Provided]** Other exclusions include active/unstable CNS metastasis; active serious infection/HIV/HBV/HCV; and pneumonitis within 5 years.
- **[Provided]** Anticancer therapy within 30 days or radiation within 14 days is exclusionary.
- **[Provided]** Relevant allergy, concurrent/recent malignancy, transplant, pregnancy/breastfeeding, and failure to use required contraception are exclusionary.

**[Clarification Required]** Operational definitions and exceptions for autoimmune disease, recent immune toxicity, CNS stability, infection/viral status, relevant allergy, concurrent/recent malignancy, transplantation, contraception, and eligibility-assessment windows are not supplied. These determine consistent screening and patient safety.

### 4.3 Recruitment

**[Provided]** Recruitment is multicentre. After Amendment 5, only SCC patients are randomized.

**[Clarification Required]** Actual recruitment dates, participating sites, amendment implementation dates, and achieved accrual are unavailable. These are needed to describe recruitment and distinguish historical enrollment cohorts.

**[Proposed]** Monitor accrual by treatment-independent characteristics, including histology, region, and amendment period, without changing eligibility or allocation rules. Rationale: this identifies operational shortfalls and documents population shifts. Assumption: monitoring uses aggregate information that does not reveal comparative efficacy.

### 4.4 Withdrawal and Follow-up

**[Provided]** Treatment can stop for progression, unacceptable toxicity, death, consent withdrawal, or completion of 96 weeks. Post-treatment follow-up includes the specified visits, imaging where applicable, and subsequent survival ascertainment.

**[Proposed]** Distinguish treatment discontinuation from withdrawal of consent for assessments or survival follow-up, and continue permitted endpoint follow-up after treatment cessation. Rationale: treatment discontinuation need not imply loss of outcome data. Assumption: continued contact is authorized by consent and applicable requirements.

**[Clarification Required]** Procedures for loss to follow-up, permitted survival-data sources, partial consent withdrawal, and use of previously collected data after withdrawal are unspecified. These affect both participant rights and completeness of OS ascertainment.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize age, region, histology, ECOG status, disease distribution, prior anticancer treatment including platinum, bevacizumab and paclitaxel status, baseline laboratory values, and baseline QoL by assigned treatment in SCC and overall populations. Use descriptive summaries rather than significance tests of randomized baseline balance. Rationale: these variables characterize prognosis and applicability. Assumption: they are captured in study records.

**[Clarification Required]** The final baseline-variable inventory, categorization rules, and observed values are not supplied. These must be established from the case-report forms and collected data before tables are finalized.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary outcome is OS for cemiplimab versus IC chemotherapy, tested first in SCC patients and then, conditional on SCC significance, in the overall eligible population.

**[Proposed]** Define OS as time from randomization to death from any cause. Estimate the effect of randomized assignment regardless of treatment discontinuation, subsequent anticancer treatment, or permitted retreatment. Rationale: this captures the survival effect of the assigned treatment strategy and preserves randomization. Assumption: this time origin and treatment-policy estimand are approved.

**[Provided]** Include deaths through the analysis cutoff. For patients without an observed death through cutoff, censor at the earlier of last-known-alive date or cutoff.

### 5.2 Secondary Outcomes

**[Provided]** Secondary efficacy, safety, and patient-reported outcomes comprise PFS, RECIST 1.1 ORR, DoR, adverse-event profiles, and mean change from baseline in QLQ-C30 GHS/QoL and physical functioning, in SCC and overall populations.

**[Proposed]** Define PFS as time from randomization to first RECIST 1.1 progression or death from any cause, whichever occurs first. Rationale: this measures disease control while recognizing death as failure. Assumption: this composite definition and time origin are approved.

**[Proposed]** Define ORR as the proportion of the relevant randomized population with a best overall RECIST 1.1 response of complete or partial response. Define DoR among responders from first qualifying response to progression or death. Rationale: these distinguish response frequency from persistence. Assumption: response qualification and confirmation rules are finalized consistently across arms.

**[Clarification Required]** The tumor-assessment reader, any independent review, response-confirmation requirements, progression adjudication, handling of assessments after new anticancer therapy, and detailed response-evaluability rules are unspecified. These decisions directly affect PFS, ORR, and DoR.

**[Proposed]** Use the valid screening QLQ-C30 assessment as baseline and calculate each postbaseline domain score minus baseline using the instrument’s scoring rules. Rationale: screening precedes treatment and provides a common reference. Assumption: a valid pretreatment screening assessment is available.

**[Clarification Required]** QoL scoring-version requirements, visit windows, duplicate-assessment selection, target follow-up horizon, and the principal mean-change contrast are not supplied. These are needed to define a reproducible longitudinal endpoint.

**[Provided]** Exploratory outcomes include serum cemiplimab PK and immunogenicity, and efficacy associations with pretreatment-tumor molecular features and peripheral-blood pharmacodynamic activity.

**[Clarification Required]** PK, immunogenicity, tumor, and blood sampling schedules; assay specifications; biomarker definitions; and laboratory evaluability rules are unavailable. These determine which exploratory quantities can validly be estimated.

### 5.3 Analysis Methods

**[Provided]** Primary OS testing uses a stratified log-rank test within the specified sequential design. SCC analyses use geographic-region strata; overall analyses use region and histology strata, with adenosquamous carcinoma classified as adenocarcinoma.

**[Proposed]** Present Kaplan–Meier OS curves, numbers at risk, median OS with confidence intervals when estimable, and a stratified Cox-model HR with confidence interval. Rationale: these provide complementary absolute and relative survival summaries. Assumption: the model uses the prespecified analysis strata and adequate event information is available.

**[Proposed]** Examine proportional-hazards adequacy using graphical and residual-based diagnostics, without changing the prespecified primary test retrospectively. Rationale: an HR can obscure time-varying effects. Assumption: diagnostics are supportive rather than a data-dependent mechanism for selecting the primary analysis.

**[Proposed]** Analyze PFS using Kaplan–Meier summaries and stratified log-rank/Cox methods analogous to OS, with nominal inference unless a confirmatory multiplicity plan is established. Rationale: PFS is also a time-to-event endpoint. Assumption: its finalized event and censoring rules are applied consistently.

**[Proposed]** Report ORR by arm with binomial confidence intervals, the between-arm response difference, and a stratified comparison using the relevant analysis strata. Rationale: both absolute response frequency and treatment contrast are clinically interpretable. Assumption: sparse-stratum handling is prespecified rather than selected from observed results.

**[Proposed]** Summarize DoR by treatment among responders using Kaplan–Meier methods; treat between-arm comparisons as descriptive. Rationale: responder-only groups are selected after randomization and are not a randomized comparison. Assumption: response and censoring definitions are harmonized between arms.

**[Proposed]** Analyze longitudinal QoL change using a repeated-measures model with treatment, categorical visit, treatment-by-visit interaction, baseline domain score, and the applicable stratification factors. Report estimated mean changes and between-arm differences at prespecified visits. Rationale: this uses repeated observations while adjusting for baseline. Assumption: the model and covariance structure are estimable, and missingness is conditionally at random.

**[Proposed]** Summarize measured cemiplimab concentrations by sampling time and report baseline and postbaseline immunogenicity findings with evaluable denominators. Rationale: descriptive analyses do not require an unsupported structural PK model. Assumption: validated assays, sample timing, and drug-exposure records are available.

### 5.4 Missing Data

**[Proposed]** Report the amount, timing, and reasons for missing survival contacts, imaging, questionnaires, and exploratory samples by treatment and population. Rationale: missingness patterns inform the credibility of endpoint analyses. Assumption: reasons for missing assessments are recorded where obtainable.

**[Proposed]** Do not impute unobserved OS deaths; apply the specified last-known-alive/cutoff censoring rule. Rationale: inventing death dates would alter the event process. Assumption: censoring is sufficiently independent for the primary survival analysis.

**[Proposed]** For a treatment-policy PFS/DoR analysis, retain observed qualifying events after treatment discontinuation or subsequent therapy; absent an event, censor at the last adequate tumor assessment on or before cutoff. For PFS without an adequate postbaseline assessment, censor at randomization unless death is observed through cutoff. Rationale: these rules distinguish missing assessment from treatment failure and avoid automatically censoring at treatment changes. Assumption: continued imaging is feasible and these rules are approved.

**[Clarification Required]** The final PFS/DoR policy for prolonged assessment gaps, late deaths, new therapy, absent postresponse assessments, and interval timing remains unspecified. These choices can materially change event classification and must be reconciled with the proposed treatment-policy approach before analysis.

**[Proposed]** Count patients without a qualifying documented response as nonresponders in the primary ORR denominator, and supplement with missing-response sensitivity analyses where warranted. Rationale: this avoids restricting response estimates to assessable survivors. Assumption: response ascertainment and sensitivity scenarios are prespecified.

**[Proposed]** Use likelihood-based QoL analysis under conditional missing-at-random assumptions, without last-observation-carried-forward, and assess departures using prespecified pattern-mixture or delta-adjustment scenarios. Rationale: dropout may relate to worsening health and can bias observed-case means. Assumption: sensitivity scenarios are clinically justified before comparative results are reviewed.

**[Proposed]** Where vital-status loss is substantial, examine sensitivity to informative censoring using prespecified scenarios or weighting if adequate predictors exist. Rationale: independent censoring may be questionable. Assumption: available covariates can support the chosen analysis.

**[Clarification Required]** Partial-date conventions, invalid-assessment rules, questionnaire item-level missingness rules, and numerical sensitivity-analysis assumptions are not supplied. These affect reproducibility and must be finalized before database lock.

### 5.5 Additional Analyses

**[Proposed]** Explore treatment-effect consistency by region and histology, and describe outcomes by amendment period. Use interaction estimates rather than separate subgroup significance claims. Rationale: these analyses assess heterogeneity and consequences of the enrollment change. Assumption: subgroup definitions are fixed in advance and results are considered exploratory.

**[Proposed]** Conduct a supportive per-protocol analysis only after prospective definition of important exclusions; retain randomized assignment and report exclusions by arm. Rationale: this can assess robustness but cannot replace the primary randomized analysis. Assumption: exclusions are determined without reference to comparative outcomes.

**[Proposed]** Explore associations between efficacy and pretreatment-tumor features or blood pharmacodynamic measures using endpoint-appropriate regression, with effect estimates, uncertainty, and the number of comparisons disclosed. Rationale: this supports hypothesis generation without implying validated predictive biomarkers. Assumption: assay quality and sample size support the selected models.

**[Clarification Required]** Specific molecular features, pharmacodynamic measures, transformations, covariates, interaction hypotheses, and any exploratory multiplicity procedure are unspecified. These must be prespecified sufficiently to distinguish planned analyses from post hoc exploration.

**[Proposed]** Describe subsequent anticancer treatment, treatment beyond progression, and retreatment by arm, without censoring primary OS at their initiation. Rationale: these events help interpret the assigned-strategy survival effect. Assumption: their dates and treatment details are collected reliably.

### 5.6 Harms

**[Provided]** Comparing adverse-event profiles between cemiplimab and IC chemotherapy is a secondary objective in SCC and overall populations.

**[Proposed]** Summarize adverse events by actual treatment, system organ class/preferred term, severity, seriousness, relationship, and consequences such as interruption or discontinuation; separately summarize fatal events and clinically important prespecified event categories. Rationale: frequency alone does not capture clinical impact. Assumption: standardized coding and grading are available.

**[Proposed]** Present treatment exposure, duration, dose modifications, and patient-level adverse-event proportions; supplement selected events with exposure-adjusted rates where useful. Rationale: differing exposure durations can affect crude event frequencies. Assumption: exposure dates are accurate, and adjusted rates are not interpreted as removing all follow-up-related bias.

**[Clarification Required]** Adverse-event definitions, treatment-emergent and post-treatment collection windows, grading and coding versions, seriousness/causality procedures, special-interest categories, retreatment reporting rules, and expedited-reporting requirements are unspecified. These decisions are necessary for consistent ascertainment and interpretation.

### 5.7 Software and References

**[Provided]** East version 6.4.1 was used for sample-size calculations.

**[Clarification Required]** Software and versions for final efficacy, safety, QoL, PK, immunogenicity, and biomarker analyses are not specified. These must be recorded to support reproducibility.

**[Proposed]** Use validated statistical software, version-controlled programs, independent checks of primary results, and archived analysis datasets and outputs. Rationale: these support computational accuracy and auditability. Assumption: appropriate validation and secure archiving resources are available.

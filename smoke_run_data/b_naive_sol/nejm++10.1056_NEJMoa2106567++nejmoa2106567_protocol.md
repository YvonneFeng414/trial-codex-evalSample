# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** This study evaluates subcutaneous dupilumab in children aged 6 to <12 years with uncontrolled persistent asthma receiving background controller therapy.

**[Proposed]** Efficacy assessment should distinguish prevention of severe exacerbations from effects on lung function, asthma control, and patient-reported health. Rationale: these outcomes describe complementary treatment effects. Assumption: their definitions and measurement procedures will be finalized before unblinding.

### 1.2 Objectives

- **[Provided]** **P1—Primary:** Evaluate the efficacy of dupilumab in children aged 6 to <12 years with uncontrolled persistent asthma. The objective-level outcome is efficacy.
- **[Provided]** **S1—Secondary:** Assess safety and tolerability; patient-reported outcomes (PROs), including health-related quality of life (HRQoL); systemic exposure; anti-drug antibodies; and the association of treatment with pediatric immune responses to tetanus, diphtheria, pertussis and/or seasonal trivalent/quadrivalent influenza vaccination.
- **[Provided]** **S2—Exploratory:** Explore biomarker prediction of and association with treatment response and optional genetic profiles; evaluate inhaled corticosteroid (ICS)/second-controller step-up and additional PROs.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a multinational, multicenter, randomized, double-blind, placebo-controlled, parallel-group study. Screening lasts 4±1 weeks, treatment lasts up to 52 weeks, and participants not entering the one-year extension have a 12-week post-treatment period.

**[Provided]** Participants are allocated to dupilumab or matching placebo in a 2:1 ratio. Treatment is administered subcutaneously every two weeks (Q2W), according to baseline weight.

| Evidence | Baseline weight | Dupilumab assignment | Matching-placebo assignment |
|---|---|---|---|
| **[Provided]** | ≤30 kg | 100 mg Q2W; 0.67 mL | Matching placebo Q2W; 0.67 mL |
| **[Provided]** | >30 kg | 200 mg Q2W; 1.14 mL | Matching placebo Q2W; 1.14 mL |

**[Provided]** Background treatment consists of medium-dose ICS plus a second controller, or high-dose ICS alone or with a second controller. Background controllers continue during the study.

**[Provided]** Temporary ICS increases of up to fourfold for ≤10 days are permitted. Permanent controller step-up may follow at least two severe exacerbations.

**[Provided]** Investigators and patients are unblinded to dose level because injection volumes differ.

**[Derived]** Weight-based dose levels are not separately randomized treatment arms. Awareness of dose level is distinct from knowledge of dupilumab versus placebo assignment.

**[Clarification Required]** The operational rules for permanent controller step-up, any permitted subsequent dose modifications, and prohibited concomitant treatments must be specified. These rules affect treatment consistency, intercurrent-event handling, and deviation classification.

### 2.2 Randomization

**[Provided]** Central interactive voice/web response system (IVRS/IWRS) permuted-block randomization occurs after screening.

**[Provided]** Randomization is stratified by screening ICS dose, screening eosinophils, and region.

| Evidence | Stratification factor | Categories |
|---|---|---|
| **[Provided]** | Screening ICS dose | Medium; high |
| **[Provided]** | Screening eosinophils | <0.3; ≥0.3 Giga/L |
| **[Provided]** | Latin America | Argentina, Brazil, Colombia, Chile, Mexico |
| **[Provided]** | Eastern Europe | Poland, Hungary, Romania, Lithuania, Russia, Ukraine, Turkey |
| **[Provided]** | Western Countries | Australia, Canada, Italy, South Africa, Spain, USA |

**[Provided]** These randomization regions are distinct from pooled-country regional analysis. Minimization is not specified.

**[Proposed]** Allocation should remain concealed until central assignment, with access to treatment codes restricted by role. Rationale: concealment protects against selection bias and unauthorized unblinding. Assumption: IVRS/IWRS can implement these controls.

**[Clarification Required]** Block sizes, sequence-generation responsibility, allocation-access permissions, emergency unblinding procedures, and the pooled-country analysis-region definitions are not supplied. These details are needed to implement allocation and distinguish randomization strata from analysis groupings.

### 2.3 Sample Size

**[Provided]** The planned overall sample size is at least 402 participants: 268 assigned to dupilumab and 134 to placebo. The three powered biomarker-defined populations are retained separately.

| Evidence | Powered population | Total; dupilumab/placebo | Placebo rate | Dupilumab rate | Relative-risk reduction | Power |
|---|---|---:|---:|---:|---:|---:|
| **[Provided]** | Type 2 inflammatory phenotype: eosinophils ≥0.15 Giga/L or FeNO ≥20 ppb | Approximately 345; 230/115 | 0.7/year | 0.322/year | 54% | 94% |
| **[Provided]** | Eosinophils ≥0.15 Giga/L | 327; 218/109 | 0.7/year | 0.322/year | 54% | 93% |
| **[Provided]** | Eosinophils ≥0.3 Giga/L | 255; 170/85 | 0.8/year | 0.32/year | 60% | 96% |

**[Provided]** Calculations concern the annualized rate of severe exacerbations during 52 weeks, using a negative-binomial count/rate comparison between dupilumab and placebo.

**[Provided]** Calculation assumptions are dispersion parameter 1.5, 2:1 allocation, two-sided alpha 0.05, linear discontinuation of 20% at one year, and average exposure of 0.9 year.

**[Provided]** Projected prevalences are 86% for the Type 2 population, 81% for eosinophils ≥0.15 Giga/L, and 64% for eosinophils ≥0.3 Giga/L. Relative-risk-reduction assumptions were based on prior Phase 3 results.

**[Derived]** Linear loss of 20% of participants over one year produces average exposure of \(1-0.20/2=0.90\) year under that discontinuation assumption.

**[Provided]** Sizing was intended to assure target power across all three biomarker-defined populations under 2:1 allocation. A required event count and calculation software are not specified. Non-inferiority/equivalence margins and a clustering design effect are not applicable because this is an individually randomized superiority trial.

**[Provided]** Amendment 2 increased the planned sample size from 294 to 471. Amendment 3 revised the primary populations and final calculation to 402.

**[Clarification Required]** The negative-binomial dispersion parameterization and detailed computational implementation must be documented to reproduce the stated powers. A dispersion value of 1.5 cannot be implemented reliably without knowing its parameterization.

### 2.4 Hypothesis Framework

**[Provided]** Superiority hypotheses compare dupilumab with placebo for severe-exacerbation rate and sequentially tested efficacy endpoints. The final statistical analysis plan (SAP) uses regional hierarchical sequences to control two-sided Type I error at 5%.

**[Provided]** The US/reference hierarchy prioritizes eosinophils ≥0.3 Giga/L, then ≥0.15 Giga/L, then Type 2 within the initial severe-exacerbation, FEV1, and ACQ-7 endpoint groups. The EU/reference hierarchy instead prioritizes Type 2, then ≥0.15 Giga/L, then ≥0.3 Giga/L, retaining that population order for the high-ICS and FeNO groups.

**[Derived]** Expanding the supplied endpoint groups gives the following 24 ordered tests in each hierarchy.

| Evidence | Order | Endpoint | US/reference population | EU/reference population |
|---|---:|---|---|---|
| **[Derived]** | 1 | Severe-exacerbation rate | Eosinophils ≥0.3 Giga/L | Type 2 |
| **[Derived]** | 2 | Severe-exacerbation rate | Eosinophils ≥0.15 Giga/L | Eosinophils ≥0.15 Giga/L |
| **[Derived]** | 3 | Severe-exacerbation rate | Type 2 | Eosinophils ≥0.3 Giga/L |
| **[Derived]** | 4 | Week-12 pre-bronchodilator FEV1 | Eosinophils ≥0.3 Giga/L | Type 2 |
| **[Derived]** | 5 | Week-12 pre-bronchodilator FEV1 | Eosinophils ≥0.15 Giga/L | Eosinophils ≥0.15 Giga/L |
| **[Derived]** | 6 | Week-12 pre-bronchodilator FEV1 | Type 2 | Eosinophils ≥0.3 Giga/L |
| **[Derived]** | 7 | Week-24 ACQ-7 | Eosinophils ≥0.3 Giga/L | Type 2 |
| **[Derived]** | 8 | Week-24 ACQ-7 | Eosinophils ≥0.15 Giga/L | Eosinophils ≥0.15 Giga/L |
| **[Derived]** | 9 | Week-24 ACQ-7 | Type 2 | Eosinophils ≥0.3 Giga/L |
| **[Derived]** | 10 | Severe-exacerbation rate | FeNO ≥20 ppb | FeNO ≥20 ppb |
| **[Derived]** | 11 | Week-12 pre-bronchodilator FEV1 | FeNO ≥20 ppb | FeNO ≥20 ppb |
| **[Derived]** | 12 | Week-24 ACQ-7 | FeNO ≥20 ppb | FeNO ≥20 ppb |
| **[Derived]** | 13 | Severe-exacerbation rate | Full ITT | Full ITT |
| **[Derived]** | 14 | Week-12 pre-bronchodilator FEV1 | Full ITT | Full ITT |
| **[Derived]** | 15 | Severe-exacerbation rate | High-ICS, eosinophils ≥0.3 Giga/L | High-ICS, Type 2 |
| **[Derived]** | 16 | Severe-exacerbation rate | High-ICS, eosinophils ≥0.15 Giga/L | High-ICS, eosinophils ≥0.15 Giga/L |
| **[Derived]** | 17 | Severe-exacerbation rate | High-ICS, Type 2 | High-ICS, eosinophils ≥0.3 Giga/L |
| **[Derived]** | 18 | Severe-exacerbation rate | High-ICS, FeNO ≥20 ppb | High-ICS, FeNO ≥20 ppb |
| **[Derived]** | 19 | Severe-exacerbation rate | High-ICS, full ITT | High-ICS, full ITT |
| **[Derived]** | 20 | Week-12 FeNO | Eosinophils ≥0.3 Giga/L | Type 2 |
| **[Derived]** | 21 | Week-12 FeNO | Eosinophils ≥0.15 Giga/L | Eosinophils ≥0.15 Giga/L |
| **[Derived]** | 22 | Week-12 FeNO | Type 2 | Eosinophils ≥0.3 Giga/L |
| **[Derived]** | 23 | Week-12 FeNO | FeNO ≥20 ppb | FeNO ≥20 ppb |
| **[Derived]** | 24 | Week-12 FeNO | Full ITT | Full ITT |

**[Proposed]** For the severe-exacerbation comparison, test the equality null \(H_0:RR=1\) against \(H_1:RR\ne1\), with superiority concluded only for a statistically significant result favoring dupilumab, \(RR<1\). Rationale: this formalization accommodates the supplied two-sided significance level. Assumption: the rate ratio is the primary treatment-effect measure.

**[Proposed]** Implement each applicable hierarchy as a fixed sequence: test at two-sided 0.05 and stop confirmatory testing after the first non-rejection; later results remain descriptive or nominal. Rationale: fixed-sequence testing controls familywise error without dividing alpha among sequential tests. Assumption: no alternative gatekeeping or alpha-recycling algorithm supersedes this proposal.

**[Clarification Required]** Confirm the exact sequential rejection rule, which regional hierarchy governs each reporting context, and how claims from the two hierarchies will be presented. This prevents treating the two sequences as independent opportunities for the same confirmatory claim.

### 2.5 Statistical Interim Analyses

**[Clarification Required]** Interim efficacy or futility analyses, information fractions, alpha spending, monitoring-committee arrangements, and statistical stopping boundaries are not supplied. Their presence or absence must be established before unblinded review because they can affect Type I error and study conduct.

**[Proposed]** Routine operational monitoring should use blinded recruitment, data-completeness, adherence, and pooled safety summaries, with any unblinded review governed by an approved access and analysis plan. Rationale: this limits operational bias. Assumption: appropriate independent access can be arranged when safety oversight requires it.

### 2.6 Timing of Analyses

**[Provided]** Final database lock occurs after every randomized participant completes Week 52 or discontinues earlier. Analyses through that lock are final clinical study report (CSR) analyses.

**[Provided]** Two originally planned database locks were integrated into one final lock. Treatment of post-lock data is determined for the CSR/addendum. A calendar date is not specified.

**[Provided]** The primary severe-exacerbation rate is assessed through Week 52. The key FEV1 assessment is at Week 12. Spirometry occurs at screening, randomization, and subsequent visits.

**[Provided]** Post-bronchodilator assessments include Weeks 2, 4, 8, 12, 24, 36, 52, and 64.

**[Provided]** Scheduled visits use a ±5-day window. Exceptions apply to early-treatment-discontinuation/end-of-treatment (ETD/EOT) assessments and telephone follow-up.

**[Derived]** The final-lock trigger does not require every participant to complete the 12-week post-treatment period. Consequently, the lock rule alone does not assure complete Week-64 data.

**[Clarification Required]** The complete schedule of assessments, ETD/EOT and telephone exceptions, visit-assignment rules, and schedules for PROs, biomarkers, exposure, antibodies, and vaccination responses are missing. These decisions determine endpoint availability and analysis windows.

**[Clarification Required]** Specify how follow-up data received after lock will enter the CSR or an addendum, including Week-64 safety and spirometry data. Otherwise, different outputs could use inconsistent follow-up cutoffs.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The superiority framework uses a two-sided 5% Type I error level controlled through regional hierarchical sequences.

**[Proposed]** Report treatment-effect estimates with two-sided 95% confidence intervals and exact p-values where estimable. Rationale: estimates and uncertainty complement hypothesis tests. Assumption: the selected models provide valid interval estimates.

**[Proposed]** Identify ordinary confidence intervals and p-values as nominal unless they support a claim permitted by the applicable hierarchy; do not describe all displayed intervals as simultaneously multiplicity-adjusted. Rationale: presentation should not imply stronger familywise coverage than the testing procedure provides. Assumption: no separate simultaneous-interval procedure is adopted.

**[Proposed]** For continuous outcomes, use equality-null two-sided tests and prespecify the favorable direction: higher FEV1, lower ACQ-7, and lower FeNO. Rationale: this prevents interpreting a significant unfavorable difference as benefit. Assumption: these directions are appropriate for the finalized endpoint scales.

### 3.2 Protocol Deviations

**[Proposed]** Record deviations involving eligibility, randomization, dosing, background-controller use, prohibited medications, adherence, blinding, assessment timing, and missing outcome ascertainment. Classify major deviations using rules finalized before treatment-code release. Rationale: prospective classification reduces outcome-driven exclusions. Assumption: source records permit reliable adjudication.

**[Proposed]** Retain randomized participants in the primary intention-to-treat analysis despite deviations, while describing deviations by assigned group. Rationale: retaining assignment preserves the randomized comparison. Assumption: continued data use is legally and ethically permissible.

**[Clarification Required]** Major-deviation definitions, treatment-adherence thresholds during follow-up, and consequences of prohibited treatment are not supplied. These decisions affect supportive populations and interpretation; the screening adherence exclusion must not automatically become a treatment-period exclusion.

### 3.3 Analysis Populations

**[Provided]** The three separately powered populations are Type 2 inflammatory phenotype, eosinophils ≥0.15 Giga/L, and eosinophils ≥0.3 Giga/L. The hierarchy also includes FeNO ≥20 ppb, full ITT, and specified high-ICS subsets.

**[Derived]** These biomarker populations are overlapping rather than mutually exclusive groups; their sample sizes must not be added to obtain overall enrollment.

**[Proposed]** Define full intention-to-treat (ITT) as all randomized participants analyzed according to assigned treatment, regardless of dosing, adherence, or subsequent treatment changes. Apply each biomarker or high-ICS restriction within ITT. Rationale: this preserves randomization within the prespecified populations. Assumption: valid subgroup-classification data are available.

**[Proposed]** Define the safety population as participants receiving at least one dose, analyzed according to treatment actually received. Rationale: exposure-based grouping is appropriate for treatment-emergent harms. Assumption: actual dosing is reliably recorded.

**[Proposed]** Define a supportive per-protocol population using prospectively specified major-deviation exclusions, without replacing ITT. Rationale: this assesses sensitivity to substantial departures from intended treatment. Assumption: exclusions are determined without knowledge of comparative outcomes.

**[Proposed]** Define exposure and anti-drug-antibody evaluable sets according to available valid samples and the relevant assay requirements, documenting exclusions separately. Rationale: assay validity and sampling determine interpretability. Assumption: laboratory validity criteria can be finalized before analysis.

**[Clarification Required]** Specify the biomarker sampling time, repeat-value algorithm, assay rules, handling of discordant measurements, and handling of missing eosinophils or FeNO. Screening eosinophils are supplied for randomization, but the analytic population-classification algorithm is not.

**[Clarification Required]** Specify the analytic definition and assessment time for high-ICS status, as well as rules for participants exposed to both study treatments. These choices affect subgroup membership and safety attribution.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Maintain a coded screening log documenting screening, eligibility, consent/assent, randomization, and reasons for non-randomization; present participant disposition by treatment after randomization. Rationale: this permits transparent accounting of selection and retention. Assumption: collection complies with applicable privacy requirements.

**[Clarification Required]** Actual screening counts, screen-failure reasons, recruitment dates, and site-level enrollment are not supplied. They must be populated from study records rather than inferred from the planned sample size.

### 4.2 Eligibility Criteria Summary

#### Inclusion Criteria

- **[Provided]** Age 6 to <12 years.
- **[Provided]** Physician-diagnosed persistent asthma for ≥12 months and uncontrolled persistent asthma.
- **[Provided]** Medium-dose ICS plus one controller, or high-dose ICS alone or with a second controller, for ≥3 months, with a stable dose for ≥1 month before screening; a third controller is not permitted.
- **[Provided]** Pre-bronchodilator FEV1 ≤95% predicted or FEV1/FVC <0.85 at screening/baseline.
- **[Provided]** Bronchodilator reversibility ≥10%, with stated alternatives.
- **[Provided]** A prior-year systemic-corticosteroid-treated exacerbation or hospital/emergency care.
- **[Provided]** Screening evidence of uncontrolled asthma through ACQ-5 ≥1.5, reliever use, sleep awakening, or symptoms.
- **[Provided]** Ability to comply, caregiver comprehension, required assent/consent, and questionnaire completion.

#### Exclusion Criteria

- **[Provided]** Age <6 or ≥12 years, or weight <16 kg.
- **[Provided]** Chronic lung disease or life-threatening asthma.
- **[Provided]** Interfering disease, malignancy, or inability to follow study procedures.
- **[Provided]** Timing-restricted omalizumab or other biologic/immunosuppressant use, allergen immunotherapy, investigational medicines, or prohibited concomitant treatments.
- **[Provided]** Prior participation in a dupilumab study or a site-staff relationship.
- **[Provided]** <80% diary-recorded adherence to background treatment.
- **[Provided]** Specified corticosteroid exposure, including prohibited systemic or topical corticosteroid use.
- **[Provided]** Clinically significant illness, including stated tuberculosis provisions, or major medical disease.
- **[Provided]** Pregnancy/contraception restrictions.
- **[Provided]** Parasite, HIV, infection, immunosuppression, autoimmune disease, biologic hypersensitivity, or viral-hepatitis risk.
- **[Provided]** Liver injury or specified liver/laboratory abnormalities, including creatine phosphokinase, platelet, eosinophil, and creatinine thresholds; numerical thresholds are not specified.
- **[Provided]** Consent withdrawal or study-level enrollment cessation.

**[Clarification Required]** Eligibility implementation requires the unspecified reversibility alternatives; reliever, awakening, and symptom thresholds; ICS dose classifications; and interpretation of “screening/baseline.” These omissions can change who qualifies.

**[Clarification Required]** Exact medication washouts, corticosteroid restrictions, tuberculosis provisions, pregnancy/contraception requirements, infection and disease definitions, and laboratory thresholds are missing. These details are necessary for consistent and safe screening and must not be replaced with assumed numerical limits.

### 4.3 Recruitment

**[Provided]** Recruitment is multinational and multicenter, with countries grouped into the specified randomization regions.

**[Clarification Required]** Site counts, recruitment duration, country/site targets, referral methods, and any enrollment controls beyond the supplied cessation criterion are not specified. These decisions affect feasibility and representativeness.

**[Proposed]** Obtain applicable ethics approvals and caregiver consent and child assent before study-specific procedures, using age-appropriate materials. Rationale: the population is pediatric and participation requires informed authorization. Assumption: local requirements determine the precise consent and assent process.

**[Proposed]** Treat genetic participation as a separate optional decision without making refusal a reason to exclude a participant from the main trial. Rationale: this preserves the stated optional nature of genetic profiling. Assumption: no additional genetic eligibility requirement is intended.

### 4.4 Withdrawal and Follow-up

**[Provided]** A 12-week post-treatment period applies to participants who do not enter the one-year extension.

**[Proposed]** Distinguish discontinuation of study treatment, withdrawal from assessments, withdrawal of consent, and loss to follow-up. Record dates and reasons separately. Rationale: these events have different implications for exposure, endpoint observation, and permitted data use. Assumption: participants can discontinue treatment without necessarily withdrawing all follow-up.

**[Proposed]** Seek scheduled efficacy and safety follow-up after treatment discontinuation when consent permits, without overriding the supplied database-lock trigger. Rationale: off-treatment observations support an assignment-based treatment-policy analysis. Assumption: follow-up is operationally feasible; unavailable periods require explicit missing-data handling.

**[Clarification Required]** Specify mandatory ETD/EOT procedures, telephone follow-up, extension-entry rules, permitted follow-up after withdrawal, and retention of previously collected data. These decisions govern completeness and participant rights.

**[Clarification Required]** Clarify how consent withdrawal or study-level enrollment cessation operates after randomization. Listing these as exclusions must not automatically remove randomized participants from analysis, because that could compromise the randomized comparison.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize age, weight, available demographic characteristics, country/region, asthma history, prior-year exacerbation burden, controller regimen and ICS dose, diary adherence, lung function, asthma-control scores, eosinophils, and FeNO by assigned treatment and relevant analysis population. Rationale: these describe disease severity, allocation balance, and subgroup composition. Assumption: these variables are collected.

**[Proposed]** Use counts and percentages for categorical variables and suitable distribution summaries for continuous variables; do not use baseline significance tests to select covariates. Rationale: descriptive summaries are sufficient for randomized-group characterization and avoid data-driven model selection. Assumption: prespecified models will be used.

**[Clarification Required]** Define baseline selection for each variable, including handling of repeated screening/randomization measurements and measurements after first dose. These rules affect baseline adjustment and change calculations.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary outcome is the annualized rate of severe asthma exacerbations during the 52-week treatment period, evaluated in the three separately powered biomarker-defined populations.

**[Clarification Required]** The operational definition of a severe exacerbation is missing, including qualifying treatment or healthcare use, episode separation, overlapping events, and event dating. These rules determine the primary event count and must be fixed before analysis.

**[Clarification Required]** Finalize the primary estimand: the outcome observation period after treatment discontinuation, treatment switching, controller step-up, and other rescue treatment, together with the treatment of death if it occurs. These choices determine what the treatment contrast means.

**[Proposed]** Target the effect of randomized assignment on severe-exacerbation rate through Week 52, retaining observed events after treatment discontinuation and permitted controller changes rather than censoring automatically at those changes. Rationale: this treatment-policy approach reflects assignment under the permitted care strategy. Assumption: post-change ascertainment is available or its absence can be addressed credibly in sensitivity analyses.

**[Proposed]** Report adjusted annualized rates, the dupilumab/placebo rate ratio, and relative rate reduction \(100(1-RR)\%\). Rationale: these provide absolute and relative interpretations aligned with the sizing assumptions. Assumption: the rate model and observation-time definition are appropriate.

### 5.2 Secondary Outcomes

- **[Provided]** Hierarchically tested efficacy endpoints include Week-12 pre-bronchodilator FEV1, Week-24 ACQ-7, and Week-12 FeNO in the populations specified in Section 2.4.
- **[Provided]** Other secondary objectives cover safety/tolerability, PROs including HRQoL, systemic exposure, anti-drug antibodies, and treatment association with immune responses to tetanus, diphthertheria, pertussis and/or seasonal trivalent/quadrivalent influenza vaccination.
- **[Provided]** Exploratory objectives include biomarker prediction/association with response, optional genetic profiles, ICS/second-controller step-up, and additional PROs.

**[Clarification Required]** For FEV1, ACQ-7, and FeNO, specify whether the endpoint is the observed value, absolute change, percentage change, or another contrast; specify FEV1 units and reference equations. These decisions change the estimand, model scale, and interpretation.

**[Clarification Required]** Identify HRQoL and additional PRO instruments, scoring and responder rules, assessment times, and proxy-versus-child reporting. Without these details, their endpoints cannot be derived reproducibly.

**[Clarification Required]** Exposure sampling, assay characteristics, antibody positivity and treatment-emergence rules, vaccine eligibility and administration schedules, immune-response measurements, and response thresholds are not supplied. These determine evaluability and prevent unsupported endpoint definitions.

### 5.3 Analysis Methods

#### Severe-Exacerbation Rate

**[Provided]** The sample-size framework assumes a negative-binomial severe-exacerbation count/rate comparison.

**[Proposed]** Fit a negative-binomial model with log link and log observed ascertainment time in years as an offset: \(\log E(N_i)=\log(T_i)+\beta_0+\beta_T Z_i+\boldsymbol{\beta}^{\mathsf T}\boldsymbol{X}_i\). Estimate the treatment rate ratio as \(\exp(\beta_T)\). Rationale: this models recurrent counts while allowing unequal observed time and overdispersion. Assumption: the mean structure and conditional rate assumptions are adequate.

**[Proposed]** Include assigned treatment and the randomization factors—screening ICS dose, screening eosinophil stratum, and randomization region—omitting a factor when it is constant within the analyzed population. Rationale: this respects the stratified design without fitting non-estimable terms. Assumption: sample sizes support these adjustments.

**[Proposed]** Estimate analysis dispersion from observed data rather than fixing it to the sizing value of 1.5. Rationale: a planning assumption need not equal the realized dispersion. Assumption: the negative-binomial model is estimable.

**[Proposed]** Examine convergence, influential observations, mean–variance fit, and sparse population-by-region cells. Report observed event totals and ascertainment time alongside modeled rates. Rationale: diagnostics and raw summaries make model dependence visible. Assumption: event dates and observation periods are complete enough to construct these summaries.

**[Clarification Required]** Define ascertainment start/end dates, time during gaps in event surveillance, and fallback analysis rules for nonconvergence or sparse events. An offset cannot correct periods during which events were not reliably observed.

#### Lung Function, Asthma Control, and FeNO

**[Proposed]** For FEV1 and ACQ-7 at their target visits, use baseline-adjusted analysis of covariance with treatment and nonconstant randomization factors, reporting adjusted treatment differences and 95% confidence intervals. Rationale: baseline adjustment generally improves precision for continuous outcomes. Assumption: the finalized scale supports this model and valid baseline measurements exist.

**[Proposed]** Analyze FeNO using log-scale baseline-adjusted analysis of covariance and report a back-transformed treatment ratio. Rationale: a log scale can accommodate positive, right-skewed measurements and relative effects. Assumption: FeNO values are positive and this scale is approved before unblinding; it remains subject to final endpoint clarification.

**[Proposed]** Use repeated-measures models as supportive analyses when multiple comparable post-baseline measurements are available, estimating contrasts at the prespecified target weeks. Rationale: longitudinal information can assess consistency and sensitivity to incomplete visits. Assumption: visit definitions and covariance modeling can be prespecified from the actual assessment schedule.

#### Exposure, Immunogenicity, Vaccination, and Other PROs

**[Proposed]** Describe systemic exposure by dose level and sampling time, and summarize anti-drug-antibody incidence and available assay categories using evaluable denominators. Rationale: these characterize pharmacologic exposure and immunogenicity without inventing efficacy hypotheses. Assumption: valid samples and assay classifications are available.

**[Proposed]** Analyze vaccine responses separately by vaccine or antigen, adjusting for pre-vaccination response where an appropriate measure exists. Rationale: different antigens and prior immunity are not interchangeable. Assumption: vaccine identity, timing, and baseline response are recorded.

**[Proposed]** Interpret vaccine findings as treatment-associated rather than as effects of randomized vaccination. Rationale: vaccination assignment is not specified as randomized. Assumption: vaccination uptake and timing may differ between participants.

**[Proposed]** Analyze other PROs using methods appropriate to their finalized scoring scales, separating continuous-score comparisons from any prespecified responder analysis. Rationale: scale properties determine valid analysis. Assumption: validated scoring and missing-item rules are available.

### 5.4 Missing Data

**[Proposed]** Summarize missingness by treatment, visit, endpoint, reason, and relation to treatment discontinuation or controller changes. Rationale: missing-data patterns inform the plausibility of analysis assumptions. Assumption: reasons can be obtained without inventing outcomes.

**[Proposed]** Distinguish a confirmed event-free interval from an interval with unknown exacerbation status; do not code unknown intervals as zero events. Rationale: absence of observation is not evidence of absence of exacerbation. Assumption: surveillance coverage can be reconstructed.

**[Proposed]** For incomplete exacerbation follow-up, supplement the observed-time rate analysis with model-based imputation of missing-period counts under a missing-at-random assumption conditional on treatment, baseline factors, and observed exacerbation history. Rationale: observed-time analysis alone may be biased by informative discontinuation. Assumption: these observed variables sufficiently explain missingness for the principal imputation scenario.

**[Proposed]** Assess departures from missing at random by varying assumed missing-period exacerbation rates, including less favorable assumptions for dupilumab. Rationale: unobserved event rates are not identifiable from observed data. Assumption: a clinically interpretable sensitivity range can be prespecified.

**[Proposed]** For continuous target-visit outcomes, use multiple imputation incorporating treatment, baseline value, randomization factors, and available longitudinal measurements, followed by the prespecified endpoint model and standard pooling of estimates. Rationale: this permits an explicit missing-at-random analysis rather than implicit complete-case selection. Assumption: the imputation and analysis models are compatible.

**[Proposed]** Include controlled departures from missing at random for continuous outcomes and avoid last-observation-carried-forward as the principal method. Rationale: carrying observations forward imposes an unsupported no-change assumption. Assumption: clinically meaningful departure scenarios can be specified.

**[Clarification Required]** Prespecify imputation implementation, sensitivity parameters and ranges, handling of missing subgroup-defining biomarkers, and handling of terminal events. These decisions materially affect population membership and robustness claims.

### 5.5 Additional Analyses

**[Proposed]** Treat analyses outside the applicable hierarchy as exploratory, with effect estimates and clearly nominal uncertainty measures. Rationale: additional analyses should not create unplanned confirmatory claims. Assumption: no additional multiplicity-controlled family is approved.

**[Proposed]** Explore treatment-effect modification by supplied biomarker measures, screening ICS dose, region, and baseline weight/dose level using treatment-by-factor interactions rather than comparing within-subgroup significance labels. Rationale: interaction tests address heterogeneity directly. Assumption: subgroup sizes and measurement quality are adequate.

**[Derived]** Because dose level is determined by baseline weight, comparisons between the 100-mg and 200-mg groups do not isolate a randomized dose effect.

**[Proposed]** Distinguish biomarker prognostic association from treatment-response prediction, using treatment-by-biomarker interactions for the latter. Rationale: association with outcome alone does not demonstrate differential treatment benefit. Assumption: biomarker models and functional forms are prespecified.

**[Proposed]** Summarize permanent ICS/second-controller step-up by treatment, including frequency and timing, while distinguishing permitted temporary ICS increases. Rationale: temporary rescue adjustment and permanent escalation represent different treatment changes. Assumption: dates and reasons for changes are recorded.

**[Proposed]** Analyze optional genetic profiles only among appropriately consented participants and characterize selection into that subset. Rationale: optional participation can produce a nonrepresentative sample. Assumption: consent and suitable genetic data are available.

**[Clarification Required]** Genetic hypotheses, biomarker functional forms, step-up endpoint definitions, and any high-dimensional multiplicity strategy are unspecified. These must be finalized to prevent selective reporting and uninterpretable exploratory findings.

### 5.6 Harms

**[Provided]** Safety and tolerability are secondary objectives, and participants not entering the extension have a 12-week post-treatment period.

**[Proposed]** Summarize adverse events, serious adverse events, deaths, adverse events leading to treatment discontinuation, and available laboratory and clinical safety measurements by actual treatment received. Rationale: these provide complementary descriptions of tolerability and clinically important harm. Assumption: standardized safety collection is implemented.

**[Proposed]** Present participant incidence with explicit denominators, severity and investigator-assessed relatedness where collected, and exposure duration; use exposure-adjusted summaries when materially unequal follow-up makes them informative. Rationale: denominators and observation time are essential for interpreting event frequencies. Assumption: exposure and event dates are available.

**[Proposed]** Present post-treatment safety observations separately when their ascertainment differs from treatment-period observations. Rationale: separating periods avoids obscuring changes in risk windows or follow-up completeness. Assumption: events can be dated relative to the final dose.

**[Clarification Required]** Specify adverse-event definitions, coding system/version, severity and causality rules, treatment-emergent risk window, events of special interest, serious-event reporting procedures, laboratory alert rules, and safety stopping criteria. These details are necessary for consistent monitoring and analysis.

**[Proposed]** Avoid interpreting nonsignificant safety comparisons as evidence of equivalent safety. Rationale: the supplied sample size is powered for efficacy rather than exclusion of clinically important harm differences. Assumption: no separate safety-equivalence design exists.

### 5.7 Software and References

**[Provided]** Sample-size calculation software is not specified.

**[Clarification Required]** Select and document analysis software, versions, packages/procedures, random-number seeds where relevant, and the software used to reproduce sample-size calculations. These details are necessary for reproducibility and validation.

**[Proposed]** Use a validated, version-controlled analysis environment with archived derivation specifications, executable programs, model diagnostics, and independent checks of primary results and hierarchy decisions. Rationale: reproducible programming and verification reduce implementation errors. Assumption: qualified statistical and programming resources are available.

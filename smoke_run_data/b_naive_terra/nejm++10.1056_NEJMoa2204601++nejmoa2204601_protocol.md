# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Pediatric type 2 diabetes mellitus (T2DM) has limited glucose-lowering options. This study evaluates once-weekly dulaglutide added to diet and exercise, with or without metformin and/or basal insulin, versus placebo.

**[Provided]** HbA1c was selected as an accepted endpoint for pediatric T2DM glycemic trials.

### 1.2 Objectives

**[Provided]** P1: Test superiority of pooled dulaglutide 0.75 mg and 1.5 mg versus placebo for change in central-laboratory HbA1c from baseline to Week 26.

**[Provided]** S1: Compare individual doses and, where specified, pooled dulaglutide with placebo for individual-dose HbA1c change, fasting blood glucose (FBG) change, HbA1c <7.0%, and body mass index (BMI) change at Week 26. Assess HbA1c, FBG, and BMI changes and HbA1c <7.0% at Week 52.

**[Provided]** S2: Assess safety at Week 26 versus placebo and at Week 52 within dulaglutide groups, and characterize pharmacokinetics (PK) and exposure relationships with safety and efficacy.

**[Provided]** S3: Assess the exploratory glycemic, growth, developmental, laboratory, quality-of-life, and insulin-dose outcomes specified in Section 5.2.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a Phase 3, multicenter, randomized, double-blind, placebo-controlled, parallel-arm superiority trial, followed by a 26-week open-label extension and approximately 30 days of safety follow-up.

**[Provided]** At baseline, participants are allocated 1:1:1 to weekly subcutaneous dulaglutide 0.75 mg, dulaglutide 1.5 mg, or placebo. The respective open-label sequences are 0.75/0.75 mg, 1.5/1.5 mg, and placebo/0.75 mg.

**[Provided]** Week-26 labels are All Dula, Dula 1.5, Dula 0.75, and Placebo; All Dula pools the two dulaglutide doses and placebo is the reference. Post-Week-26 labels are All Dula, Dula 1.5/1.5, Dula 0.75/0.75, and Placebo/Dula 0.75; All Dula pools the two continuous-dulaglutide sequences. No between-group inference is made after Week 26.

**[Clarification Required]** Study-treatment volumes and adjuvant content are not specified. They are needed for complete preparation and administration instructions.

### 2.2 Randomization

**[Provided]** A computer-generated random sequence is implemented through an interactive web response system (IWRS) after eligibility confirmation at Visit 2. Stratification factors are screening HbA1c <8.0% or ≥8.0%, metformin use yes/no, and insulin use yes/no.

**[Clarification Required]** Blocking or minimization is not specified. The allocation-generation and concealment procedures need confirmation for implementation and auditability.

**[Proposed]** Restrict access to treatment codes until the relevant unblinding and maintain an access log. Rationale: protect allocation concealment and trial integrity. Assumption: the IWRS supports controlled access.

### 2.3 Sample Size

**[Provided]** The initial plan was approximately 150 enrolled, 50 per arm, to obtain 120 Week-26 completers. Approximately 750 would be screened, assuming an 80% screen-failure rate and 20% dropout.

**[Provided]** The calculation used the continuous percentage-point change in HbA1c from baseline to Week 26 for pooled dulaglutide versus placebo. The initial assumed difference was −0.65%, the standard deviation (SD) was 1.0%, and two-sided alpha was 0.05. Initial power was at least 90% for the pooled comparison and 80% for each dose.

**[Provided]** In a sample-size re-estimation (SSR) scenario with SD 1.3%, up to 189 enrolled, 63 per arm, would give at least 80% pooled power and 69% power for each dose. SSR did not require an alpha adjustment.

**[Provided]** The statistical analysis committee (SAC) could recommend a variability-only SSR after approximately 100 enrolled, bounded at 150–189; Lilly would decide whether to implement it. The blinded Week-26 SD was estimated by restricted maximum likelihood (REML) using an MMRM containing baseline HbA1c, insulin and metformin use, treatment, visit, and treatment-by-visit.

**[Provided]** The 2019 SSR used the SAC-estimated HbA1c SD of 1.4%, an assumed difference of −0.8%, and 10% Week-26 HbA1c missingness; it confirmed a sample size of approximately 150.

**[Provided]** The assumptions reflected limited pediatric GLP-1 receptor agonist experience, broad baseline HbA1c values, and inclusion of metformin and/or basal-insulin users. The rationale was to preserve power while limiting placebo exposure and accommodating uncertainty in pediatric variability.

**[Provided]** Absolute arm-specific HbA1c values and sample-size software are not specified. An event count and non-inferiority or equivalence margin are not applicable to this continuous-endpoint superiority calculation; no clustering is described.

### 2.4 Hypothesis Framework

**[Provided]** Two primary estimands compare pooled dulaglutide with placebo for Week-26 HbA1c change: an ITT efficacy estimand censoring post-rescue data, and an ITT treatment-regimen estimand regardless of rescue or adherence. Each has full two-sided 0.05 significance level.

**[Provided]** After success for H1, pooled HbA1c, a graphical procedure transfers alpha among H2–H3, individual-dose HbA1c; H4–H6, HbA1c <7%; H7–H9, FBG; and H10–H12, BMI. The latter three families cover pooled, 1.5-mg, and 0.75-mg comparisons with placebo.

**[Provided]** The graph is run separately for treatment-regimen washout multiple imputation (MI), efficacy, and EMA-restricted efficacy populations. It may be revised using blinded Week-26 correlations before database lock.

**[Clarification Required]** The graph’s initial weights, directed transfer weights, exact mapping of H2–H12 to comparisons, and success criteria across the two primary estimands are not specified. These decisions determine which claims are multiplicity-controlled and at what local alpha.

### 2.5 Statistical Interim Analyses

**[Provided]** The SAC’s blinded variability assessment and possible SSR are described in Section 2.3. The sponsor unblinds after the primary database lock to analyze and report primary data.

**[Clarification Required]** Any additional interim efficacy or futility analyses, stopping rules, and access restrictions are not specified. Confirmation matters for operational control of type I error and confidentiality.

**[Proposed]** Document the blinded SSR recommendation and implementation decision separately from efficacy results. Rationale: preserve the distinction between variability-based planning and treatment-effect assessment. Assumption: personnel performing the SSR remain appropriately blinded.

### 2.6 Timing of Analyses

**[Provided]** The primary database lock occurs after all randomized patients complete Week 26/Visit 9; the sponsor then unblinds for primary reporting. The final lock occurs after all complete the 4-week safety follow-up/Visit 801.

**[Provided]** Baseline is Visit 2. Week 13 is fasting, with pre-dose and 1-to-12-hour post-dose PK. Week 26 is fasting, with pre-dose PK, central laboratories, ECG, and EQ-5D-Y; its window is ±6 days.

**[Provided]** Week-39 PK is permitted within 2 days postdose. Week 52 is fasting, with PK, ECG, and EQ-5D-Y; its window is ±7 days. Visit 801/Week 56 is approximately 30 days later, with safety follow-up and PK. EQ-5D-Y is scheduled at baseline, Weeks 26 and 52, or early termination.

**[Clarification Required]** The lock criteria for participants who withdraw or miss a scheduled visit are not specified. A completion and data-reconciliation rule is needed to operationalize both locks without assuming every participant attends every visit.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** Each primary estimand has full two-sided alpha 0.05. Multiplicity for specified secondary hypotheses follows the graphical procedure in Section 2.4.

**[Proposed]** Report two-sided 95% confidence intervals alongside estimates; identify intervals that are not multiplicity-adjusted as descriptive. Rationale: show precision without overstating adjusted inference. Assumption: the applicable estimation method supports the interval.

**[Proposed]** For the primary superiority test, compare pooled dulaglutide minus placebo using a two-sided test at 0.05 and require an estimated difference below zero for a superiority conclusion. Rationale: align the decision with the stated superiority objective. Assumption: the approved estimand-specific analysis and any required joint decision rule are used.

### 3.2 Protocol Deviations

**[Proposed]** Record, classify, and review deviations before unblinding, including eligibility, treatment, rescue, and assessment deviations; summarize them by randomized group. Rationale: support interpretation and reproducible population assignment. Assumption: deviations are captured sufficiently for review.

**[Clarification Required]** The material deviation definitions and their consequences for any restricted analysis population are not specified. They affect population membership and interpretability.

### 3.3 Analysis Populations

**[Provided]** Both primary estimands use an ITT approach. The graph is also run in an EMA-restricted efficacy population.

**[Proposed]** Analyze efficacy participants according to randomized assignment and summarize safety by treatment received, documenting discrepancies. Rationale: preserve randomized comparisons while describing actual exposure. Assumption: randomized assignment and administered treatment are available.

**[Clarification Required]** The exact ITT, safety, PK, and EMA-restricted efficacy population rules, including treatment of participants without post-baseline data or study treatment, are not specified. They determine denominators and eligibility for each analysis.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Summarize numbers screened, screening failures and their reasons, enrolled, randomized, treated, and completing each period, with missing status identified. Rationale: describe participant flow and selection. Assumption: screening and disposition records are available.

### 4.2 Eligibility Criteria Summary

**[Provided]** Eligible participants are male or female, aged 10 to <18 years, with IDF-ISPAD T2DM; BMI >85th percentile; weight ≥50 kg; and assent and parent consent.

**[Provided]** Lifestyle measures, metformin, and basal insulin must have been stable for at least 8 weeks before screening. Metformin must be at least 1000 mg/day or the highest tolerated or locally approved dose.

**[Provided]** Screening HbA1c must be >6.5% to ≤11.0%, or ≤9.0% if newly diagnosed or lifestyle only.

**[Provided]** Exclusions include T1DM or antibodies; ketoacidosis or hyperosmolar syndrome; gastrointestinal, pancreatic, thyroid, renal, or cardiovascular risks; Hb variants; pregnancy, breastfeeding, or ineffective contraception; unstable psychiatric treatment; and prohibited medicines or other trials.

**[Provided]** Other antihyperglycemics require at least a 3-month washout. Bolus insulin requires at least a 6-week washout, except for up to 14 days of acute-condition rescue.

**[Clarification Required]** Operational definitions for the listed risk exclusions, antibody and diagnostic criteria, BMI percentile reference, contraception requirements, and permissible concomitant medicines are not specified. These are needed for consistent eligibility decisions.

### 4.3 Recruitment

**[Provided]** Approximately 750 participants were expected to be screened to enroll approximately 150, based on an estimated 80% screen-failure rate.

**[Clarification Required]** Recruitment locations, number of sites, recruitment period, and methods are not specified. They are needed for an operational recruitment plan.

### 4.4 Withdrawal and Follow-up

**[Provided]** The design includes a 26-week open-label extension and approximately 30-day safety follow-up.

**[Proposed]** Record reasons and dates for treatment discontinuation, study withdrawal, loss to follow-up, rescue, and missed visits separately; seek outcome and safety data where consent permits. Rationale: distinguish intercurrent events from missing data. Assumption: continued data collection is permitted and feasible.

**[Clarification Required]** Rescue criteria and procedures, withdrawal rules, and follow-up after discontinuation or withdrawal are not specified. These decisions affect participant safety, estimand implementation, and missing-data interpretation.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize demographics, disease and treatment history, baseline HbA1c, FBG, BMI and other available baseline outcomes, and randomization strata by randomized group. Rationale: characterize the trial population and contextualize results. Assumption: these data are collected.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary outcome is central-laboratory HbA1c change from baseline to Week 26, comparing pooled dulaglutide 0.75 mg and 1.5 mg with placebo.

**[Derived]** The treatment contrast is dulaglutide minus placebo in percentage-point HbA1c change; a negative difference favors dulaglutide.

**[Provided]** For the efficacy estimand, post-rescue data are censored. For the treatment-regimen estimand, outcomes are considered regardless of rescue or adherence.

**[Clarification Required]** The precise rescue-censoring boundary, handling of other intercurrent events for the efficacy estimand, and Week-26 assessment selection when multiple values occur are not specified. These determine which observations contribute to each estimand.

### 5.2 Secondary Outcomes

**[Provided]** Week-26 secondary efficacy outcomes are individual-dose HbA1c change, FBG change, HbA1c <7.0%, and BMI change versus placebo, including pooled dulaglutide where specified. HbA1c, FBG, and BMI changes and HbA1c <7.0% are also assessed at Week 52.

**[Provided]** Safety outcomes include self-reported hypoglycemia and rescue; adjudicated pancreatitis and pancreatic enzymes; thyroid treatment-emergent adverse events and calcitonin; antidrug antibodies, allergic or hypersensitivity reactions, and injection-site reactions. Safety is assessed at Week 26 versus placebo and at Week 52 within dulaglutide groups.

**[Provided]** Exploratory outcomes at Weeks 26 and 52 include HbA1c ≤6.5%; HbA1c <7.0% and HbA1c ≤6.5% without severe, documented symptomatic hypoglycemia <70 mg/dL, or probable hypoglycemia; weight, BMI standard deviation score (SDS), height and height SDS, waist, lipids, Tanner stage, EQ-5D-Y visual analogue scale and domain levels, and basal-insulin-dose change.

**[Provided]** Exploratory morning laboratory outcomes at Weeks 26 and 52 include prolactin, IGF-1, estradiol, testosterone in males, LH, and cortisol. HbA1c change is assessed at Week 13; insulin resistance, beta-cell function, and adiponectin are assessed at Weeks 13 and 26.

**[Clarification Required]** The specified pooled comparisons for each secondary endpoint, definitions and assessment windows for hypoglycemia-free composites, and methods for insulin resistance and beta-cell function are not fully specified. These are needed to construct and analyze the outcomes consistently.

### 5.3 Analysis Methods

**[Proposed]** For the efficacy estimand, fit an MMRM to available pre-rescue HbA1c changes with randomized treatment, visit, treatment-by-visit, baseline HbA1c, and insulin and metformin use. Estimate the Week-26 pooled contrast as the equally weighted mean of the two dose effects minus placebo. Rationale: use repeated observations while respecting the 1:1:1 allocation and rescue censoring. Assumption: relevant repeated measurements are available and missing outcomes are adequately modeled under a missing-at-random assumption conditional on included data.

**[Proposed]** Use an unstructured within-participant covariance when estimable and a prespecified simpler covariance if it is not; report estimates, standard errors, confidence intervals, and tests. Rationale: accommodate repeated-measure correlation and convergence. Assumption: the selected covariance adequately represents the observed data.

**[Provided]** Treatment-regimen washout MI is one of the analyses for which the graphical procedure is run.

**[Clarification Required]** The washout-MI algorithm, its reference distribution and timing, and its relationship to outcomes after rescue or nonadherence are not specified. These must be defined to determine whether the imputation assumptions target the stated treatment-regimen estimand.

**[Proposed]** For other Week-26 continuous endpoints, use an appropriate baseline-adjusted repeated-measures or visit-specific model; for binary endpoints, estimate group proportions and treatment contrasts using a suitable regression model. Rationale: account for baseline values and outcome type. Assumption: sufficient data and model fit are available.

**[Proposed]** Describe Week-52 outcomes within treatment sequences, including the placebo-to-dulaglutide sequence, without between-group inference. Rationale: respect the post-Week-26 design and reporting rule. Assumption: sequence and assessment data are available.

**[Proposed]** Summarize PK concentrations by dose, visit, and sampling time and explore exposure–efficacy and exposure–safety relationships using suitable descriptive or model-based methods. Rationale: address S2 while respecting the sampling schedule. Assumption: dosing, sampling times, concentrations, and relevant outcomes are usable.

**[Clarification Required]** Exact models, covariates, pooling rules, and estimable exposure metrics for secondary and PK/PD analyses require confirmation. They affect reproducibility and interpretation.

### 5.4 Missing Data

**[Provided]** The efficacy estimand censors post-rescue data; the treatment-regimen estimand is regardless of rescue or adherence.

**[Proposed]** Tabulate missingness by treatment, visit, reason, rescue, and treatment status; distinguish unobserved values from observed post-rescue values censored for the efficacy estimand. Rationale: make missing-data patterns and estimand implementation transparent. Assumption: reasons and event dates are recorded.

**[Proposed]** Conduct prespecified sensitivity analyses varying assumptions about unobserved Week-26 outcomes, separately for each estimand. Rationale: assess robustness to departures from the primary missing-data assumptions. Assumption: plausible alternative distributions can be specified before unblinding.

**[Clarification Required]** Imputation models, number of imputations, sensitivity scenarios, and handling of missing binary and composite components are not specified. These choices can materially change estimates and conclusions.

### 5.5 Additional Analyses

**[Proposed]** Summarize exploratory outcomes by treatment at Week 26 and by sequence at Week 52; identify these analyses as exploratory. Rationale: address S3 without implying unprovided confirmatory claims. Assumption: outcome-specific measurements are available.

**[Proposed]** Examine primary-effect consistency across the randomization strata descriptively, with interaction estimates where data permit. Rationale: investigate heterogeneity relevant to stratification. Assumption: subgroup sizes support estimation; these analyses are not assumed to be powered.

**[Clarification Required]** Any additional prespecified subgroups, per-protocol analyses, and their decision roles are not specified. They are needed before confirmatory interpretation.

### 5.6 Harms

**[Proposed]** Summarize exposure, treatment-emergent adverse events, serious adverse events, discontinuations due to adverse events, and the specified safety outcomes by group through Week 26 and by sequence thereafter. Rationale: provide a structured safety profile. Assumption: event dates, severity, and treatment exposure are collected.

**[Proposed]** Present hypoglycemia and rescue counts and participant incidence, laboratory values and changes, and adjudicated pancreatitis separately; describe post-Week-26 results without between-group inference. Rationale: address the specified safety objectives and extension design. Assumption: adjudication and event-level data are available.

**[Clarification Required]** Adverse-event coding, treatment-emergent windows, severe and probable hypoglycemia definitions, adjudication procedures, and safety reporting rules are not specified. These govern classification and denominators.

### 5.7 Software and References

**[Provided]** Sample-size software is not specified.

**[Clarification Required]** Analysis software, versions, validated implementation, and any protocol-specific reference materials are not specified. They are needed for reproducibility and final study documentation.

# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** This phase IIb primary-prevention trial evaluates genetically at-risk infants. It tests whether sustained oral exposure to insulin during the usual period of initiation of beta-cell autoimmunity induces immune tolerance and reduces beta-cell autoimmunity and diabetes.

### 1.2 Objectives

- **[Provided]** **P1—Primary:** Determine whether daily oral insulin from age 4–7 months to age 3 years reduces the cumulative incidence of beta-cell autoantibodies and diabetes in childhood. The objective-level outcome is cumulative incidence of beta-cell autoantibodies and diabetes in childhood.
- **[Provided]** **S1—Secondary:** Compare development of any persistent confirmed beta-cell autoantibody, persistent confirmed insulin autoantibodies (IAA), persistent confirmed glutamic acid decarboxylase autoantibodies (GADA), and dysglycaemia or diabetes.
- **[Provided]** **S2—Exploratory:** Assess treatment effects in subgroups and in immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures; assess type 1 diabetes and progression from seroconversion to clinical type 1 diabetes.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** The study is investigator-initiated, multicentre, multinational, randomized, double-blind, placebo-controlled, and phase IIb, with a primary-prevention design. Allocation is 1:1 oral insulin to placebo.

**[Provided]** Treatment consists of a daily parent-administered oral capsule, preferably administered between 07:00 and 10:00. Treatment ends the day before the age-3 visit or upon development of clinical diabetes.

- **[Provided]** **Oral insulin:** 7.5 mg daily for 2 months, then 22.5 mg daily for 2 months, then 67.5 mg daily until age 3 years. Each capsule contains human recombinant insulin crystals plus microcrystalline cellulose to a total capsule weight of 200 mg, in a 0.5-mL hard gelatin capsule.
- **[Provided]** **Placebo:** A matching microcrystalline-cellulose capsule administered daily until age 3 years.

**[Clarification Required]** The preparation and feeding instructions for administering capsule contents to infants, management of missed or vomited doses, permitted dose interruptions, and adherence assessment are not supplied. These decisions are necessary for safe, reproducible administration and interpretation of actual exposure.

### 2.2 Randomization

**[Provided]** The study-drug manufacturer performs package-number randomization. A separate randomization list assigns multiples to the same treatment arm.

**[Clarification Required]** Stratification factors and any blocking or minimization are not specified. The allocation algorithm and any factors requiring inclusion in the analysis must be confirmed.

**[Clarification Required]** Allocation-concealment procedures, the personnel covered by blinding, code custody, and emergency-unblinding procedures are not specified. These details are necessary to assess protection against selection and ascertainment bias.

**[Proposed]** Maintain restricted access to treatment codes, document emergency unblinding, and keep endpoint review blinded where feasible. Rationale: these measures protect the randomized comparison. Assumption: treatment-code management can be separated from routine clinical care and outcome review.

### 2.3 Sample Size

**[Provided]** The planned sample size is 1,050 infants allocated 1:1; the original design projected 1,040 infants, and completed enrollment was 1,050.

**[Provided]** The original calculation used persistent confirmed multiple beta-cell autoantibodies or diabetes as a time-to-event/hazard-rate outcome. The control event probability was 7.5% at 3.5 years, corresponding under an exponential distribution to a hazard of 0.02227. The assumed treatment hazard was halved to 0.011135, representing a target 50% risk reduction/hazard-rate reduction.

**[Provided]** The original calculation assumed an exponential time-to-event distribution, two-sided overall significance level 0.05, 80% power, and a two-sided log-rank test of equal hazard rates. It required complete follow-up of 832 children, uniformly randomized over 3.5 years and followed for another 3.5 years. A 20% dropout allowance increased the required randomized sample to 1,040.

**[Provided]** The calculation was based on the expected primary-outcome frequency, exponential hazard model, accrual and follow-up assumptions, and anticipated dropout. All randomized children, including those contributing observation time before dropout, contribute to the primary analysis.

**[Provided]** An October 2021 blinded update used observed blinded dropout, accrual, and event-rate information. The re-estimation scenario used a placebo hazard of 0.02456 and a halved treatment hazard of 0.01228. Projected power was 81.3% under the observed total hazard and halved treatment-hazard scenario.

**[Provided]** The blinded update extrapolated dropout of 12% with a 95% confidence interval of 8–15%. Completed accrual was 3.17 years, with 3.25-year follow-up. The calculation used PROC POWER in SAS 9.4, based on the Lakatos formula. No power issue was judged to prevent trial end six months after the last treatment.

**[Provided]** A non-inferiority or equivalence margin is not applicable because this is a superiority study. A sample-size design effect for clustering was not applicable to the individually randomized design.

**[Clarification Required]** A required event count is not specified. Confirm whether an event target was documented for planning or monitoring; no additional event-driven stopping requirement should be inferred from the supplied calendar-based timing.

### 2.4 Hypothesis Framework

**[Provided]** Primary and secondary endpoints are superiority endpoints. The primary null hypothesis compares equal hazard rates, and the primary confirmatory comparison is oral insulin versus placebo for persistent confirmed multiple beta-cell autoantibodies or diabetes.

**[Proposed]** Express the primary null as \(H_0:\lambda_I(t)=\lambda_P(t)\), assessed against a two-sided alternative. Declare evidence of oral-insulin superiority only when the primary test is significant and the estimated treatment effect favors oral insulin. Rationale: this preserves the supplied two-sided superiority framework. Assumption: the primary test and its significance threshold are finalized consistently with any previous efficacy analyses.

**[Clarification Required]** Whether secondary superiority endpoints have a confirmatory testing hierarchy or multiplicity allocation is not specified. This decision determines whether secondary findings can support confirmatory claims.

### 2.5 Statistical Interim Analyses

**[Provided]** A blinded sample-size and power reassessment was performed in October 2021 using dropout, accrual, and event-rate information.

**[Clarification Required]** No efficacy or futility interim-analysis schedule, statistical stopping boundaries, alpha-spending rule, or independent monitoring arrangements are supplied. Confirm whether treatment-comparative analyses occurred, because they may affect final inference.

**[Proposed]** Treat the documented update as a blinded design reassessment rather than an efficacy test, with no alpha expenditure attributable to that reassessment alone. Rationale: reassessing nuisance parameters need not constitute testing a treatment effect. Assumption: no unblinded treatment comparison or efficacy-based decision was incorporated.

### 2.6 Timing of Analyses

**[Provided]** Final analysis follows the observation period ending six months after the last participant’s last treatment day, expected in June 2024, together with final data export and quality control. Database lock was October 23, 2024.

**[Provided]** Assessments comprise eight intervention visits from baseline through age 3 years and up to nine post-age-3 follow-up visits. Blood is collected for autoantibodies at every visit. Persistent-autoantibody-positive children undergo oral glucose tolerance tests (OGTTs) from age 3 years at six-month intervals.

**[Clarification Required]** Exact visit ages, allowable visit windows, the actual observation cutoff, and final export and quality-control completion dates are not supplied. These are needed to define administratively complete follow-up and distinguish an expected date from an actual analysis cutoff.

**[Proposed]** Finalize endpoint derivations, deviation classifications, and analysis code before treatment-code access wherever feasible, and identify any decisions made afterward. Rationale: transparent timing limits outcome-driven analytical choices. Assumption: access histories and versioned analysis documents are available.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The original design specifies a two-sided overall significance level of 0.05.

**[Proposed]** Use a two-sided 0.05 threshold for the single primary confirmatory test and report treatment-effect estimates with two-sided 95% confidence intervals. Rationale: this aligns estimation with the supplied design level. Assumption: no prior efficacy testing requires adjustment of the final threshold.

**[Proposed]** In the absence of a documented confirmatory secondary-testing procedure, report secondary superiority comparisons with nominal p-values and 95% confidence intervals, explicitly identifying them as not multiplicity-controlled. Treat exploratory analyses as hypothesis-generating. Rationale: this avoids unsupported family-wise error claims. Assumption: no previously specified testing hierarchy supersedes this approach.

### 3.2 Protocol Deviations

**[Proposed]** Classify deviations before treatment-code access where feasible, including eligibility errors, incorrect dose escalation, substantial treatment interruptions, nonadherence, prohibited concurrent trial participation, missed endpoint assessments, and inappropriate unblinding. Rationale: consistent classification supports interpretation and sensitivity analyses. Assumption: source records permit reliable classification.

**[Proposed]** Summarize deviations by randomized group without automatically excluding affected participants from the primary analysis. Rationale: retaining randomized allocation limits post-randomization selection bias. Assumption: legally usable follow-up remains available.

**[Clarification Required]** Quantitative adherence thresholds, visit-window limits, prohibited treatments, and criteria for major versus minor deviations are not supplied. These are needed before defining any per-protocol population.

### 3.3 Analysis Populations

**[Provided]** All randomized children contribute to the primary analysis, including observation time contributed before dropout.

**[Proposed]** Define the primary intention-to-treat population as all randomized children, analyzed according to assigned treatment regardless of adherence, dose interruption, or treatment cessation. Rationale: this estimates the effect of assignment and preserves randomization. Assumption: continued outcome ascertainment is permissible after treatment discontinuation.

**[Proposed]** Define a safety population comprising children receiving at least one dose, summarized according to treatment actually received, with treatment discrepancies reported separately. Rationale: exposure-based summaries aid attribution of harms. Assumption: dosing records identify actual exposure.

**[Proposed]** Use any per-protocol analysis only as supportive and define eligibility prospectively through the finalized deviation rules. Rationale: adherence-related exclusions can introduce bias. Assumption: adherence and deviation data are sufficiently complete.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Report available numbers screened, genetically eligible, consented, excluded, randomized, treated, and followed, with reasons for exclusion and nonparticipation where recorded. Rationale: a participant-flow summary supports assessment of selection and retention. Assumption: screening records can be used within applicable consent restrictions.

**[Clarification Required]** Screening denominators and screening procedures beyond the supplied eligibility criteria are not specified. Their availability determines which recruitment and screening proportions can be estimated.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion requires age 4–7 months.
- **[Provided]** Inclusion requires greater than 10% risk of developing multiple beta-cell autoantibodies by age 6 years.
- **[Provided]** Solid food must have been introduced, and parental written consent is required.
- **[Provided]** Without first-degree type 1 diabetes, genetic eligibility requires DR3/DR4-DQ8 or DR4-DQ8/DR4-DQ8, together with a genetic-risk score greater than 14.4.
- **[Provided]** With a first-degree history of type 1 diabetes, genetic eligibility requires HLA DR4 and DQ8 without DRB1*1501 or DQB1*0503.
- **[Provided]** Exclusion criteria are interfering disease or treatment, a condition associated with poor compliance, an unsafe medical condition, diabetes at recruitment, or participation in another clinical trial.

**[Clarification Required]** The genetic-risk calculation and operational definitions of interfering disease/treatment, poor compliance, and unsafe medical conditions are not supplied. These definitions are needed for reproducible screening decisions.

**[Clarification Required]** Baseline autoantibody negativity is not stated as an eligibility criterion. Confirm how baseline-positive children are classified and handled, because this affects incident endpoint ascertainment and the time origin for progression analyses.

### 4.3 Recruitment

**[Provided]** Recruitment was multicentre and multinational, and completed enrollment comprised 1,050 infants. The blinded update reported completed accrual over 3.17 years.

**[Clarification Required]** Participating countries and centres, recruitment sources, and calendar dates of recruitment are not supplied. These details are needed to describe the recruitment setting and assess applicability.

**[Proposed]** Summarize recruitment and retention by centre or country where disclosure is appropriate, without treating centre-specific differences as efficacy findings. Rationale: this documents operational variation. Assumption: centre and country identifiers are available.

### 4.4 Withdrawal and Follow-up

**[Provided]** Treatment ends the day before the age-3 visit or upon clinical diabetes. Follow-up includes post-age-3 assessments within the supplied observation period.

**[Proposed]** Distinguish treatment discontinuation, withdrawal from visits, withdrawal of permission for further data collection, and loss to follow-up. Continue permitted endpoint follow-up after treatment discontinuation. Rationale: treatment cessation does not itself eliminate the relevance of subsequent outcomes. Assumption: consent permits continued contact or use of subsequent clinical information.

**[Proposed]** Record the date and reason for each discontinuation or withdrawal, the last adequate outcome assessment, and available vital status. Rationale: these data support censoring and missing-data assessment. Assumption: collection remains ethically and legally permissible.

**[Clarification Required]** Withdrawal procedures, permitted data use after consent withdrawal, retention measures, and clinical follow-up after diabetes diagnosis are not specified. These decisions affect participant protection and completeness of outcome ascertainment.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize available baseline age, sex, family history, genetic eligibility category, genetic-risk score, centre/country, autoantibody status, and relevant clinical and metabolic measurements by randomized group. Use suitable descriptive statistics without significance tests of baseline balance. Rationale: this characterizes the population without testing differences generated by randomization. Assumption: the listed variables were collected.

**[Clarification Required]** The definitive baseline dataset, measurement units, and rules for selecting pre-randomization values are not supplied. These are needed for reproducible summaries and any adjusted analysis.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary confirmatory endpoint is persistent confirmed multiple beta-cell autoantibodies or diabetes. The primary objective concerns cumulative incidence of beta-cell autoantibodies and diabetes in childhood.

**[Proposed]** Analyze the primary endpoint as time from randomization to the first qualifying composite event, and summarize its components separately. Rationale: this follows the supplied time-to-event design while showing which events contribute to the composite. Assumption: the endpoint charter resolves qualifying events, baseline status, and event dates.

**[Clarification Required]** The qualifying autoantibody panel, assay thresholds, persistence requirements, confirmation method, required sampling intervals, and definition of multiple positivity are not supplied. These decisions are necessary to construct the primary endpoint.

**[Clarification Required]** Diabetes diagnostic criteria and whether primary-endpoint diabetes includes only type 1 diabetes are not supplied. Clarification matters because diabetes is part of the primary composite, whereas type 1 diabetes is separately identified as exploratory.

**[Clarification Required]** The event date could be the first qualifying positive sample, the confirming sample, or another adjudicated date. The chosen rule, including handling of confirmation after the observation cutoff, materially affects event timing and classification.

### 5.2 Secondary Outcomes

- **[Provided]** Secondary outcomes are development of any persistent confirmed beta-cell autoantibody, persistent confirmed IAA, persistent confirmed GADA, and dysglycaemia or diabetes.
- **[Provided]** Exploratory outcomes include immunologic, transcriptomic, metabolic, and viral-antibody longitudinal measures; type 1 diabetes; and progression from seroconversion to clinical type 1 diabetes.
- **[Provided]** Exploratory objectives also include assessing treatment effects in subgroups.

**[Clarification Required]** Secondary endpoint definitions require the same unresolved assay and persistence rules as the primary endpoint. Dysglycaemia thresholds, diabetes criteria, seroconversion definition, and the exact longitudinal markers and measurement schedules also require specification because they determine reproducible outcome derivations.

### 5.3 Analysis Methods

**[Proposed]** Use an unadjusted two-sided log-rank test for the primary treatment comparison. Rationale: it matches the test used in the original sample-size calculation. Assumption: the finalized randomization scheme does not require a stratified primary test, and the approach remains suitable after review of follow-up and event ascertainment.

**[Proposed]** Estimate the oral-insulin versus placebo hazard ratio and 95% confidence interval using a Cox model with treatment as the explanatory variable. Report events, participants at risk, person-time, and event curves by randomized group. Rationale: these summaries convey both relative effect and observed follow-up. Assumption: the hazard ratio is an appropriate summary; proportional-hazards adequacy will be assessed.

**[Proposed]** Censor event-free participants at the earlier of their last adequate endpoint assessment and the administrative observation cutoff, rather than at treatment discontinuation alone. Rationale: censoring should reflect outcome ascertainment rather than adherence. Assumption: censoring is noninformative conditional on information used in the analysis.

**[Proposed]** If deaths occur before the primary endpoint, treat death as a competing event for absolute cumulative-incidence estimation and report it separately. Use Aalen–Johansen estimates; without competing deaths these reduce to one minus Kaplan–Meier survival. Rationale: death precludes subsequent endpoint occurrence. Assumption: event and death dates are adequately ascertained.

**[Proposed]** For the hazard-based primary comparison, remove participants from the risk set at a competing death and interpret the resulting treatment estimate as cause-specific. Rationale: this distinguishes the supplied hazard comparison from absolute cumulative incidence. Assumption: the cause-specific estimand is accepted in the finalized analysis plan.

**[Proposed]** Examine proportional hazards graphically and using model diagnostics. If materially violated, supplement—not replace—the primary analysis with time-varying effects or restricted mean event-free time over a prespecified common horizon. Rationale: a single hazard ratio may obscure changing treatment effects. Assumption: the supplementary horizon is chosen without treatment-effect-driven selection.

**[Proposed]** Analyze secondary time-to-event endpoints analogously, with endpoint-specific event dates and risk sets. Rationale: consistent methods facilitate interpretation across superiority endpoints. Assumption: their finalized definitions support time-to-event analysis.

**[Proposed]** Analyze longitudinal outcomes with models appropriate to their distributions, accounting for within-child correlation and including treatment, visit time, and treatment-by-time interaction. Rationale: repeated-measures models use longitudinal information without treating observations as independent. Assumption: the mean structure, distribution, and missing-data assumptions are adequate for each measure.

### 5.4 Missing Data

**[Proposed]** Summarize missing visits, unavailable samples, unsuccessful assays, incomplete confirmations, and loss to follow-up by treatment group and reason. Do not classify an unmeasured or unconfirmed endpoint as negative. Rationale: distinct missingness mechanisms can affect endpoint ascertainment differently. Assumption: reasons for missingness are recorded.

**[Proposed]** Do not impute primary events in the main time-to-event analysis; use observed qualifying events and the prespecified censoring rules. Retain randomized children with no post-randomization assessment in accounting, showing their lack of informative follow-up rather than assigning event-free time. Rationale: this avoids inventing outcomes or follow-up. Assumption: an appropriate last-known assessment can be identified where follow-up exists.

**[Proposed]** Assess sensitivity to informative dropout using approaches such as inverse-probability-of-censoring weighting and prespecified departures from noninformative censoring. Rationale: the main analysis may be biased if dropout depends on unobserved disease risk. Assumption: weighting models have adequate predictors and positivity; departures represent explicitly stated sensitivity assumptions.

**[Proposed]** For longitudinal models, use likelihood-based inference under a missing-at-random assumption and supplement important findings with plausible missing-not-at-random sensitivity analyses. Rationale: available repeated observations can contribute without single-value imputation. Assumption: each model and sensitivity scenario is scientifically defensible.

**[Clarification Required]** Rules for incomplete confirmatory sampling and missed OGTTs are not supplied. These rules determine whether an endpoint is established, unresolved, or censored and must be fixed before final derivation.

### 5.5 Additional Analyses

**[Proposed]** Conduct supportive adjusted analyses using a limited, prespecified set of prognostic baseline variables, including any confirmed randomization stratification factors. Rationale: adjustment may improve precision without replacing the primary randomized comparison. Assumption: variables are measured before treatment and the event count supports model complexity.

**[Proposed]** Consider exploratory subgroup analyses by first-degree family history, genetic eligibility category, and baseline age, using treatment-by-subgroup interactions rather than comparing within-subgroup significance. Rationale: these characteristics relate to the supplied eligibility framework. Assumption: subgroup definitions are fixed without reference to treatment effects and sample sizes permit meaningful estimation.

**[Clarification Required]** The intended subgroup list, categorization rules, and any priority ordering are not supplied. These decisions matter because unrestricted subgroup exploration increases false-positive findings.

**[Proposed]** Assess progression from seroconversion using seroconversion as the analysis time origin, reporting treatment-group comparisons as exploratory and conditional on entering that state. Rationale: this addresses the specified progression objective. Assumption: seroconversion dates and subsequent diabetes ascertainment are available; conditioning on a post-randomization event limits causal interpretation.

**[Proposed]** For high-dimensional exploratory measures, define analysis families and apply a stated false-discovery-rate procedure, alongside effect sizes and uncertainty. Rationale: large numbers of comparisons require multiplicity-aware interpretation. Assumption: assay processing, normalization, filtering, and the procedure’s dependence assumptions are appropriate.

**[Proposed]** If sufficient multiple-birth families are represented, perform a supportive analysis accounting for within-family dependence. Rationale: assigning multiples to the same arm can produce correlated outcomes despite the individually randomized design. Assumption: family identifiers and enough independent families are available for reliable inference.

**[Proposed]** Where autoantibody onset is known only between visits, consider an interval-censored sensitivity analysis. Rationale: visit-based detection does not establish the biological onset date precisely. Assumption: assessment intervals and the relationship between initial positivity and confirmation can be reconstructed.

### 5.6 Harms

**[Proposed]** Summarize adverse events, serious adverse events, deaths, treatment discontinuations due to adverse events, and available clinically relevant laboratory abnormalities by safety population and treatment received. Present participant counts and event counts separately. Rationale: these describe both the proportion affected and recurrent harms. Assumption: systematic safety data were collected.

**[Proposed]** Separate harms occurring during treatment from those observed after treatment, using actual exposure dates. Rationale: temporal context supports interpretation without implying causality. Assumption: event onset and exposure dates are available.

**[Clarification Required]** Adverse-event definitions, collection windows, severity grading, attribution procedures, expedited reporting requirements, safety oversight, and individual or trial stopping rules are not supplied. These are necessary for participant protection and reproducible safety reporting.

**[Clarification Required]** Management pathways for abnormal glucose findings, dysglycaemia, suspected diabetes, and other urgent findings are not supplied. These decisions matter because endpoint surveillance can identify conditions requiring prompt clinical assessment.

### 5.7 Software and References

**[Provided]** The October 2021 blinded power update used PROC POWER in SAS 9.4, based on the Lakatos formula.

**[Proposed]** Use validated statistical software for final analyses, recording software versions, procedures, options, seeds where relevant, and all endpoint-derivation code. Independently verify the primary endpoint and primary analysis. Rationale: reproducibility and verification reduce programming errors. Assumption: analysis datasets and controlled code storage are available.

**[Clarification Required]** Software and versions for the final efficacy, longitudinal, exploratory, and safety analyses are not specified. These must be documented to make the final analyses reproducible.

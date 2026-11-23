# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Noninfectious intermediate-, posterior-, and pan-uveitis may threaten vision, while sustained corticosteroid exposure has ocular and systemic risks. This final analysis specification evaluates steroid-sparing maintenance adalimumab against placebo in active disease.

### 1.2 Objectives

- **[Provided]** **P1:** Evaluate the efficacy and safety of adalimumab, administered as 80 mg subcutaneously at Baseline followed by 40 mg subcutaneously every other week from Week 1, versus placebo as maintenance therapy in subjects requiring high-dose corticosteroids for active noninfectious intermediate-, posterior-, or pan-uveitis.
- **[Provided]** **P1 outcome:** Efficacy and safety of adalimumab versus placebo as maintenance therapy.
- **[Provided]** Secondary objectives are not separately labeled; ranked secondary efficacy endpoints and their confirmatory testing sequence are defined.
- **[Provided]** Exploratory objectives are not separately labeled; other efficacy, sensitivity, and subgroup analyses are designated exploratory.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a Phase 3, randomized, double-masked, placebo-controlled, multicenter parent study. Analyses cover the non-Japan parent study, with a separate Japan sub-study.
- **[Provided]** Treatment allocation is 1:1.
- **[Provided]** The adalimumab arm receives an 80-mg subcutaneous loading dose at Baseline, followed by 40 mg subcutaneously every other week beginning at Week 1.
- **[Provided]** The placebo arm receives matching placebo loading and every-other-week doses.
- **[Provided]** All continuing subjects receive a standardized prednisone burst of 60 mg/day at entry, with mandatory taper and discontinuation by Week 15. Topical corticosteroids are tapered per protocol.
- **[Clarification Required]** The prednisone taper steps, topical corticosteroid taper, permitted concomitant treatments, rescue-treatment rules, and study-treatment stopping criteria are not supplied. These details determine treatment adherence, protocol deviations, and interpretation of maintenance efficacy.
- **[Clarification Required]** The duration of randomized treatment, masking responsibilities, emergency-unmasking procedures, and operational relationship between the parent study and Japan sub-study require specification to implement treatment and masking consistently.

### 2.2 Randomization

- **[Provided]** Eligible subjects are randomized through IVRS/IWRS. The AbbVie Deutschland Statistics Department prepared the randomization schedule.
- **[Provided]** Randomization is stratified by baseline immunosuppressant (IMM) usage. Japanese subjects are randomized in a separate stratum without IMM stratification.
- **[Provided]** Randomization is not stratified by site, and an adequate block size is used.
- **[Clarification Required]** The numerical block size, any block-size variation, and access restrictions for the allocation schedule are not supplied. These details are needed for randomization documentation and evaluation of allocation concealment.

### 2.3 Sample Size

- **[Provided]** Approximately 234 patients are planned to obtain 138 treatment-failure events.
- **[Provided]** The calculation uses time to treatment failure at 6 months, assuming treatment-failure rates of 70% with placebo and 50% with adalimumab: an absolute difference of 20 percentage points.
- **[Provided]** Failures are conservatively assumed to begin after 2 months, as prednisone reaches lower doses.
- **[Provided]** The planned log-rank comparison uses a two-sided significance level of 5% and 90% power.
- **[Provided]** The calculation incorporates pooled dropout of 35% over 12 months and average accrual of 4 subjects/month for the first 30 months, followed by 7 subjects/month.
- **[Provided]** Calculations across sample sizes using these event, recruitment, and dropout assumptions indicate approximately 234 patients are needed to achieve 138 events.
- **[Provided]** This is a superiority comparison; a non-inferiority or equivalence margin is not applicable. A clustering design effect is not applicable to the individually randomized sample-size calculation.
- **[Provided]** Sample-size calculations used East5 Version 5.2.0.0.
- **[Clarification Required]** Whether the approximately 234 patients include Japan sub-study participants is not explicit. This affects reconciliation of planned enrollment with the non-Japan primary analysis population.
- **[Clarification Required]** Sample-size re-estimation and amendments are not specified. Any such changes and their timing relative to treatment unmasking must be documented to assess operating characteristics and interpretation.

### 2.4 Hypothesis Framework

- **[Provided]** Primary time-to-treatment-failure and ranked secondary endpoints are tested two-sided at 0.05.
- **[Provided]** Ranked-secondary testing begins only if the primary endpoint is significant. Testing proceeds in the specified hierarchy, and every preceding endpoint must be significant before the next is tested, controlling the two-sided 5% multiple significance level.
- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.
- **[Proposed]** For the primary comparison, express the null hypothesis as equal treatment-failure time distributions between randomized groups, against a two-sided alternative. Rationale: this is consistent with the supplied superiority framework and log-rank sample-size method. Assumption: the final endpoint definition and analysis population are established before analysis.
- **[Clarification Required]** The ranked secondary endpoint names, order, definitions, and endpoint-specific hypotheses are not supplied. They are essential to execute the confirmatory testing sequence without data-driven selection.
- **[Clarification Required]** No separate confirmatory safety hypothesis or safety multiplicity procedure is supplied. Whether any safety comparison is intended to support formal inference must be resolved before assigning confirmatory status.

### 2.5 Statistical Interim Analyses

- **[Clarification Required]** Planned or conducted interim efficacy analyses, futility rules, stopping boundaries, alpha spending, and independent monitoring arrangements are not specified. These decisions matter because prior unblinded testing or stopping decisions may affect final inference.
- **[Proposed]** Reconcile all documented interim data reviews before final testing and distinguish blinded operational reviews from unblinded treatment comparisons. Rationale: this establishes whether the stated final significance framework remains applicable. Assumption: review records are available.

### 2.6 Timing of Analyses

- **[Provided]** Analyses occur after parent-study termination.
- **[Provided]** The final efficacy value is obtained at the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure occurs.
- **[Provided]** Assessments are scheduled at Baseline, Week 1, Week 4, and every 4 weeks thereafter, with Week 27 replacing Week 28. Treatment failure is assessed at Week 6 and later visits.
- **[Provided]** Analysis windows extend through Week 80 using Rx day. The assessment closest to the nominal day is selected; ties are resolved using the latest assessment.
- **[Clarification Required]** The Rx-day origin, window boundaries, handling of unscheduled visits, and placement of the Week 6 failure assessment within the visit schedule are not supplied. These details affect visit assignment and endpoint derivation.
- **[Clarification Required]** The data cutoff, database-lock criteria, data-readiness requirements, and relationship between study termination and the 138-event target are not specified. They determine which observations and events enter the final analysis.
- **[Proposed]** Finalize endpoint derivations, analysis populations, and unresolved data queries before database lock and treatment-code release. Rationale: this limits outcome-informed analytical changes. Assumption: final unmasked comparative analyses have not already occurred.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The primary and eligible ranked-secondary tests use two-sided 0.05 significance, subject to the hierarchical gatekeeping procedure.
- **[Proposed]** Report treatment-effect estimates with two-sided 95% confidence intervals. Label exploratory intervals as nominal and distinguish them from multiplicity-controlled hypothesis tests. Rationale: estimates and uncertainty complement significance testing. Assumption: an appropriate interval method can be specified for each finalized endpoint.
- **[Proposed]** Report exact calculated p-values where practical and interpret statistically significant findings in conjunction with effect direction and clinical magnitude. Rationale: statistical significance alone does not establish benefit. Assumption: endpoint directionality is defined before analysis.

### 3.2 Protocol Deviations

- **[Proposed]** Before unmasking, classify deviations using predefined categories covering eligibility, randomized treatment, corticosteroid taper, prohibited medication, assessments, and masking. Summarize subjects with deviations by randomized group. Rationale: consistent classification supports transparent interpretation. Assumption: sufficient protocol and monitoring records exist.
- **[Proposed]** Retain subjects with deviations in the proposed intention-to-treat analysis rather than excluding them retrospectively. Rationale: this preserves the randomized comparison. Assumption: the primary analysis population is approved as proposed.
- **[Clarification Required]** Definitions of important deviations and any deviation-based exclusions are not supplied. They must be finalized before defining a per-protocol analysis to prevent selective exclusions.

### 3.3 Analysis Populations

- **[Proposed]** Use all randomized non-Japan parent-study subjects, analyzed according to assigned treatment, as the primary efficacy population. Rationale: this preserves randomization while respecting the stated parent-study scope. Assumption: no different prespecified primary population governs the final analysis.
- **[Proposed]** Define the safety population as subjects receiving at least one study-treatment dose, summarized by treatment actually received. Rationale: safety summaries should reflect exposure. Assumption: dosing records identify actual treatment.
- **[Clarification Required]** The formal efficacy and safety population definitions, handling of randomized-but-untreated subjects, and assignment of subjects receiving both treatments are not supplied. These decisions determine denominators and treatment attribution.
- **[Clarification Required]** The Japan sub-study analysis population and whether any combined analysis is intended require specification. Pooling without a defined plan could obscure the separate randomization structure.
- **[Proposed]** Restrict any per-protocol population to a supportive sensitivity analysis using prospectively finalized exclusions. Rationale: exclusion-based analyses can compromise randomized comparability. Assumption: deviation criteria can be determined without reference to outcomes.

## 4. Trial Population

### 4.1 Screening Data

- **[Provided]** Screening includes medical history, laboratory profile, physical examination, chest radiograph, and ECG.
- **[Proposed]** Summarize numbers screened, eligible, randomized, treated, and included in each analysis population, with screening-failure reasons where recorded. Rationale: participant accounting supports assessment of selection and attrition. Assumption: screening and disposition records are available.
- **[Clarification Required]** Screening duration, repeat-screening rules, and handling of subjects with multiple screening records are not supplied. These decisions affect eligibility verification and screening denominators.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion requires age ≥18 years and noninfectious intermediate-, posterior-, or pan-uveitis.
- **[Provided]** Active disease must be present in either eye despite ≥2 weeks of stable prednisone ≥10 mg/day, or equivalent. Active disease is defined by an active chorioretinal/retinal vascular lesion, OCT macular edema with intraocular inflammation, anterior chamber (AC) cells ≥2+, or vitreous haze ≥2+.
- **[Provided]** Inclusion also requires appropriate contraception and negative pregnancy tests; the screening health evaluation; injection capability; consent and compliance; and satisfaction of TB testing/therapy conditions.
- **[Provided]** Exclusions include isolated anterior or infectious uveitis and inadequate response or intolerance to high-dose corticosteroids.
- **[Provided]** Ocular exclusions include POHS, ocular masquerade/serpiginous disease, pupil-dilation limitation, fundus-obscuring opacity or cataract need, and specified glaucoma, BCVA, demyelination, retinopathy, macular disease, vitreoretinal-interface, or recent/planned eye-surgery conditions.
- **[Provided]** Treatment-related exclusions include prior anti-TNF/biologic, cyclophosphamide/chlorambucil, or steroid implant exposure; unstable, multiple, prohibited, or excessive immunosuppression; local steroids within 90 days; and recent investigational drugs.
- **[Provided]** Infection-related exclusions include prohibited infections, TB, hepatitis B, HIV, immunodeficiency or anti-infective treatment, and positive syphilis/Lyme tests.
- **[Provided]** Other exclusions include selected cardiovascular/neurologic history, hypersensitivity, pregnancy/breastfeeding, malignancy, drug/alcohol abuse, significant screening laboratory abnormalities, and investigator unsuitability.
- **[Clarification Required]** Detailed definitions, thresholds, medication limits, look-back periods, contraception requirements, and TB testing/therapy conditions underlying these summarized criteria are not supplied. They are necessary for reproducible eligibility adjudication; unspecified numerical limits cannot be inferred.

### 4.3 Recruitment

- **[Provided]** Recruitment is multicenter, with individually randomized treatment assignment.
- **[Provided]** Sample-size planning assumes accrual averaging 4 subjects/month for the first 30 months and 7 subjects/month thereafter.
- **[Clarification Required]** Actual recruitment dates, site counts, geographic distribution, and achieved accrual are not supplied. These are needed to describe the enrolled population and distinguish planning assumptions from study conduct.
- **[Proposed]** Describe actual enrollment over calendar time and by region or site where disclosure is appropriate. Rationale: this documents recruitment performance and population distribution. Assumption: recruitment dates and location identifiers are available.

### 4.4 Withdrawal and Follow-up

- **[Provided]** The final efficacy assessment is linked to the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure occurs.
- **[Clarification Required]** Rules for treatment discontinuation, withdrawal of consent, loss to follow-up, post-discontinuation assessments, rescue treatment, and subsequent therapy are not supplied. These rules affect the estimand, censoring, and completeness of safety follow-up.
- **[Proposed]** Distinguish treatment discontinuation from withdrawal from study follow-up and summarize timing and reasons separately by randomized group. Rationale: stopping treatment does not necessarily terminate outcome ascertainment. Assumption: these events are separately recorded.
- **[Proposed]** Use valid outcome observations collected after treatment discontinuation in the primary randomized-group analysis unless the finalized endpoint or estimand requires otherwise. Rationale: this reduces exclusion of post-randomization information. Assumption: continued collection is permitted and such observations are available.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize available demographics, uveitis subtype and laterality, disease activity, ocular measurements, prednisone exposure, and baseline IMM usage by randomized group. Rationale: these characteristics describe disease severity and treatment context. Assumption: the variables were collected consistently.
- **[Proposed]** Use counts and percentages for categorical variables and suitable measures of location and dispersion for continuous variables, with missing-value counts. Avoid baseline significance tests. Rationale: descriptive summaries characterize randomized groups without testing chance imbalance. Assumption: variable scales and distributions are available.
- **[Clarification Required]** The baseline assessment rule and units, scales, and eye-selection conventions are not supplied. These definitions are necessary for reproducible baseline summaries and change-from-baseline analyses.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary efficacy endpoint is time to treatment failure, assessed at Week 6 and later visits.
- **[Provided]** The sample-size calculation uses treatment failure at 6 months and targets 138 treatment-failure events.
- **[Derived]** The assumption that failures begin after 2 months is a sample-size planning assumption, not a replacement for the specified Week 6-and-later assessment rule.
- **[Clarification Required]** The treatment-failure components, thresholds, confirmation requirements, eye-level aggregation, and event-date rules are not supplied. Without these definitions, the primary endpoint cannot be derived reproducibly.
- **[Clarification Required]** The time origin, treatment of events before Week 6, and handling of death, rescue therapy, treatment changes, and early termination are not specified. These choices determine the primary estimand and event/censoring classification.
- **[Clarification Required]** Specific primary safety outcomes are not supplied beyond the efficacy-and-safety objective. Safety endpoint definitions and assessment windows are needed to operationalize that objective.

### 5.2 Secondary Outcomes

- **[Provided]** Ranked secondary efficacy endpoints are subject to sequential confirmatory testing after a significant primary result.
- **[Clarification Required]** The actual ranked endpoint list and order are absent. Each endpoint requires its outcome definition, measurement scale, assessment time, eye-selection rule, analysis population, missing-data method, and statistical test before confirmatory analysis is possible.
- **[Proposed]** Report estimates for ranked endpoints even when gatekeeping prevents further confirmatory testing, clearly marking subsequent results as nonconfirmatory. Rationale: this preserves descriptive completeness without extending the stated error-control procedure. Assumption: the endpoint hierarchy is finalized independently of results.

### 5.3 Analysis Methods

- **[Provided]** The sample-size calculation assumes a log-rank test.
- **[Proposed]** Use a two-sided log-rank test stratified by baseline IMM usage for the primary non-Japan treatment comparison. Rationale: this aligns with the planning test and randomization stratification. Assumptions: the IMM strata are correctly recorded and censoring is conditionally independent of failure.
- **[Proposed]** Present Kaplan–Meier failure-free survival curves, numbers at risk, event and censoring counts, and estimable median failure-free times. Rationale: these describe the timing and extent of treatment failure. Assumption: event times and censoring rules are finalized.
- **[Proposed]** Estimate an adalimumab-versus-placebo hazard ratio and 95% confidence interval using a Cox model stratified by baseline IMM usage. Rationale: this complements the log-rank test with an effect estimate. Assumption: proportional hazards is adequate for interpretation as a common hazard ratio.
- **[Proposed]** Examine proportional-hazards adequacy using graphical and residual-based diagnostics; interpret any resulting alternative summaries as exploratory. Rationale: a single hazard ratio may inadequately describe time-varying effects. Assumption: event numbers support meaningful diagnostics.
- **[Proposed]** Summarize 6-month treatment-failure probability from the survival analysis, with uncertainty estimates. Rationale: this connects observed results to the planning assumptions without replacing the time-to-event primary comparison. Assumption: follow-up supports estimation at 6 months.
- **[Clarification Required]** Exact censoring rules, treatment of tied event times, and endpoint-specific methods for secondary outcomes require finalization. These choices affect numerical results and reproducibility.
- **[Proposed]** Keep the Japan sub-study separate from the primary non-Japan analysis unless a combined analysis is explicitly approved and labeled. Rationale: the supplied design distinguishes the two components and their stratification. Assumption: participant membership is identifiable.

### 5.4 Missing Data

- **[Proposed]** Summarize missing assessments, incomplete follow-up, and reasons for missingness by group and visit. Rationale: missingness patterns inform interpretation of potential bias. Assumption: reasons and assessment dates are recorded.
- **[Proposed]** For subjects without documented failure, use the last evaluable failure assessment as the candidate censoring date, subject to the finalized administrative cutoff and intercurrent-event rules. Rationale: this avoids counting unobserved time as confirmed failure-free follow-up. Assumption: censoring is sufficiently independent for the primary survival analysis.
- **[Proposed]** Do not automatically classify every missing assessment or treatment discontinuation as treatment failure. Rationale: failure should follow its predefined clinical criteria rather than an unsupported missingness rule. Assumption: the final endpoint definition does not explicitly classify such events as failures.
- **[Clarification Required]** Missing component assessments, intermittent gaps, partial dates, and missing ranked-secondary outcomes require endpoint-specific rules. These decisions can change event ascertainment and hierarchical conclusions.
- **[Proposed]** Assess sensitivity to potentially informative censoring using clinically justified alternative assumptions fixed before comparative results are reviewed. Rationale: dropout may be related to disease activity or treatment response. Assumption: adequate information exists to specify plausible alternatives.

### 5.5 Additional Analyses

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.
- **[Clarification Required]** The specified exploratory endpoints, sensitivity analyses, and subgroup definitions are not supplied. Their exact scope must be recovered or finalized to avoid presenting newly selected analyses as prespecified.
- **[Proposed]** Include an unstratified primary-endpoint comparison as a sensitivity analysis. Rationale: this assesses dependence on stratification. Assumption: the primary analysis uses the proposed IMM-stratified approach.
- **[Proposed]** Explore treatment-effect consistency by baseline IMM usage using an interaction model and subgroup estimates with confidence intervals. Rationale: IMM usage is a supplied randomization factor. Assumptions: subgroup data and event counts permit estimation; interaction findings remain exploratory.
- **[Proposed]** Describe corticosteroid exposure and adherence to the required taper if dosing data are available. Rationale: these contextualize the steroid-sparing maintenance objective without creating a new confirmatory endpoint. Assumption: sufficiently detailed dose records exist.

### 5.6 Harms

- **[Provided]** Safety is part of the primary objective comparing adalimumab with placebo.
- **[Clarification Required]** Adverse-event definitions, collection periods, treatment-emergent windows, severity and relatedness classifications, serious-event criteria, and laboratory toxicity thresholds are not supplied. These are required for consistent safety ascertainment and attribution.
- **[Proposed]** Summarize adverse events, serious adverse events, deaths, events leading to treatment discontinuation, and available laboratory abnormalities by safety-analysis group. Rationale: these provide a broad descriptive safety assessment. Assumption: corresponding data were collected and definitions are finalized.
- **[Proposed]** Present subject-level event incidence with explicit denominators and summarize treatment exposure; add exposure-adjusted rates where exposure differs materially. Rationale: unequal observation or treatment duration can complicate crude comparisons. Assumption: reliable treatment and event dates are available.
- **[Proposed]** Provide clinical summaries of deaths and serious events without implying causation from temporal association alone. Rationale: clinically important harms require contextual interpretation. Assumption: sufficient event narratives or source summaries are available.
- **[Clarification Required]** Safety follow-up after treatment cessation, adverse events of special interest, coding conventions, and attribution after switching treatments require specification. These decisions affect event inclusion and interpretation.

### 5.7 Software and References

- **[Provided]** Sample-size calculations used East5 Version 5.2.0.0.
- **[Clarification Required]** Software and versions for final analyses, statistical procedures, and adverse-event coding dictionaries are not supplied. These details are necessary for reproducibility.
- **[Proposed]** Use version-controlled analysis programs, documented derivation specifications, and independent verification of primary endpoint derivations and confirmatory results. Rationale: these controls support reproducibility and reduce programming error. Assumption: analysis datasets, programming resources, and verification access are available.

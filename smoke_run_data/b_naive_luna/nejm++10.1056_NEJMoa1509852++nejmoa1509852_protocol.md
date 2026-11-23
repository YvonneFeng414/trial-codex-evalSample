# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

- **[Provided]** Noninfectious intermediate-, posterior-, and pan-uveitis may threaten vision, while sustained corticosteroid exposure has ocular and systemic risks. This final analysis specification evaluates steroid-sparing maintenance adalimumab against placebo in active disease.

### 1.2 Objectives

- **[Provided]** **Primary objective (P1):** Evaluate the efficacy and safety of adalimumab (80 mg SC at Baseline, then 40 mg SC every other week from Week 1) versus placebo as maintenance therapy in subjects requiring high-dose corticosteroids for active noninfectious intermediate-, posterior-, or pan-uveitis. The stated P1 outcome is the efficacy and safety of adalimumab versus placebo as maintenance therapy.

- **[Provided]** The protocol does not separately label secondary objectives; it defines ranked secondary efficacy endpoints and their confirmatory testing sequence.

- **[Provided]** The protocol does not separately label exploratory objectives; other efficacy, sensitivity, and subgroup analyses are specified as exploratory analyses.

- **[Clarification Required]** The specific ranked secondary endpoints and their order are not supplied. They are needed to implement the confirmatory testing hierarchy.

## 2\. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a Phase 3, randomized, double-masked, placebo-controlled, multicenter parent study. Analyses cover the non-Japan parent study, with a separate Japan sub-study. Allocation is 1:1.

- **[Provided]** All continuing subjects received a standardized 60-mg/day prednisone burst at entry, with mandatory taper and discontinuation by Week 15. Topical corticosteroids were tapered per protocol.

- **[Provided]** Arm 1 received adalimumab 80 mg SC as a Baseline loading dose, then 40 mg SC every other week beginning Week 1. Arm 2 received matching placebo loading and every-other-week doses.

- **[Clarification Required]** The operational definition of “continuing subjects” and the detailed prednisone and topical corticosteroid taper schedules are not supplied. These details matter for defining the treated population and assessing adherence to concomitant-treatment requirements.

### 2.2 Randomization

- **[Provided]** Eligible subjects were randomized by IVRS/IWRS; the AbbVie Deutschland Statistics Department prepared the randomization schedule.

- **[Provided]** Randomization was stratified by Baseline immunosuppressant (IMM) usage. Japanese subjects were randomized in a separate stratum without IMM stratification. Randomization was not stratified by site; an adequate block size was used.

- **[Clarification Required]** The block size and the categories used for Baseline IMM usage are not supplied. These details matter for reproducing the allocation scheme and any stratified analysis.

### 2.3 Sample Size

- **[Provided]** Approximately 234 patients were planned to obtain 138 treatment-failure events. The sample-size outcome was time to treatment failure at 6 months.

- **[Provided]** The assumed 6-month treatment-failure rates were 70% in the placebo arm and 50% in the adalimumab arm, an absolute difference of 20 percentage points. Failures were conservatively assumed to begin after 2 months as prednisone reached lower doses.

- **[Provided]** The calculation used a two-sided 5% alpha, 90% power, and the log-rank test. The comparison was for superiority; a non-inferiority or equivalence margin was not applicable.

- **[Provided]** The planned dropout assumption was a pooled 35% over 12 months. The accrual assumptions were an average of 4 subjects/month for the first 30 months, then 7/month. Design effect or clustering was not applicable to the individually randomized sample-size calculation.

- **[Provided]** Calculations across sample sizes using the stated assumptions indicated that approximately 234 patients would achieve 138 events. East5 Version 5.2.0.0 was used for the sample-size calculation.

- **[Clarification Required]** Sample-size re-estimation and amendments are not specified. Whether either occurred matters for documenting the final design and interpreting the planned event target and error rates.

### 2.4 Hypothesis Framework

- **[Provided]** The primary time-to-treatment-failure endpoint and ranked secondary endpoints are tested two-sided at 0.05. Ranked-secondary testing begins only if the primary endpoint is significant and proceeds in the specified hierarchy: each preceding endpoint must be significant to test the next, controlling the two-sided 5% multiple significance level.

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.

- **[Clarification Required]** The ranked secondary endpoint definitions and order are not supplied. Without them, the confirmatory sequence cannot be applied.

- **[Proposed]** For the primary efficacy comparison, test the null hypothesis of no treatment difference against a two-sided alternative using the prespecified 0.05 significance level. **Rationale:** This expresses the supplied two-sided superiority framework in testable terms. **Assumption:** The primary test compares the randomized treatment groups in the non-Japan parent study.

### 2.5 Statistical Interim Analyses

- **[Clarification Required]** Whether interim analyses were planned or conducted, their timing, the data reviewed, and any decision or alpha-spending rules are not specified. These decisions matter for interpreting the final significance level and determining whether the final analysis requires adjustment.

### 2.6 Timing of Analyses

- **[Provided]** The final efficacy value is the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure has occurred. Analyses occur after parent-study termination.

- **[Provided]** Outcome assessments are scheduled at Baseline, Week 1, Week 4, and then every 4 weeks, with Week 27 replacing Week 28. Treatment failure is assessed at Week 6 and later visits.

- **[Provided]** Analysis windows run through Week 80 by Rx day. The assessment closest to the nominal day is used; ties are resolved using the latest assessment.

- **[Clarification Required]** The data cutoff, database-lock requirements, and criteria for data readiness are not specified. These are needed to establish the analysis population’s data snapshot and the timing at which the final analysis can be conducted.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The primary time-to-treatment-failure and ranked secondary endpoints use two-sided testing at 0.05. The ranked secondary sequence controls the two-sided 5% multiple significance level as described above.

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.

- **[Proposed]** Report treatment-effect estimates with two-sided 95% confidence intervals alongside p-values. **Rationale:** These intervals are consistent with the stated two-sided 0.05 testing level and convey estimate precision. **Assumption:** Confidence intervals are descriptive for exploratory analyses and do not create additional confirmatory claims.

### 3.2 Protocol Deviations

- **[Clarification Required]** Definitions of important or major protocol deviations, the process and timing for classifying them, and their impact on analysis populations are not supplied. These decisions matter for reproducible population assignment and sensitivity analyses.

- **[Proposed]** Classify deviations using prespecified criteria before treatment-group unmasking, document the reason for each classification, and summarize deviations by randomized group. **Rationale:** Prespecification and blinded classification reduce the risk of outcome- or treatment-informed population decisions. **Assumption:** Treatment assignments can remain masked during deviation review.

### 3.3 Analysis Populations

- **[Proposed]** Use a primary efficacy population comprising all randomized non-Japan parent-study subjects, analyzed according to randomized assignment. **Rationale:** This preserves the randomized comparison and aligns with the stated non-Japan parent-study analysis scope. **Assumption:** “Analyses cover the non-Japan parent study” means Japan-sub-study subjects are not included in the parent-study primary analysis.

- **[Proposed]** Analyze the Japan sub-study separately, using randomized assignment for efficacy summaries and actual treatment received for safety summaries. **Rationale:** Separate reporting respects the stated separate Japan sub-study and its different randomization stratum. **Assumption:** No pooled Japan/non-Japan confirmatory analysis is intended.

- **[Proposed]** Define a safety population as all subjects who received at least one dose of study treatment, analyzed according to treatment received. **Rationale:** This links safety summaries to actual exposure. **Assumption:** Dose administration data are available and a subject is considered exposed after any study-treatment dose.

- **[Clarification Required]** The study-specific population definitions, including whether a per-protocol population is required and whether any Japan data enter pooled analyses, are not supplied. These decisions matter for the analysis denominator and interpretation of treatment effects.

## 4\. Trial Population

### 4.1 Screening Data

- **[Provided]** Screening health evaluation included medical history, laboratory profile, physical examination, chest radiograph, and ECG. Eligibility also required specified TB testing and therapy conditions.

- **[Proposed]** Summarize the number of subjects screened, eligible, randomized, and not randomized, with reasons for non-enrollment when available. **Rationale:** A screening disposition summary describes how the enrolled population arose. **Assumption:** Screening and disposition records are available.

- **[Clarification Required]** The screening period, screening failure categories, and required reporting detail are not supplied. These affect how screening disposition and eligibility are summarized.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion criteria were age ≥18 years; noninfectious intermediate-, posterior-, or pan-uveitis; and active disease in either eye despite at least 2 weeks of stable prednisone ≥10 mg/day (or equivalent). Active disease was defined by an active chorioretinal/retinal vascular lesion, OCT macular edema with intraocular inflammation, anterior chamber (AC) cells ≥2+, or vitreous haze ≥2+.

- **[Provided]** Other inclusion requirements were appropriate contraception and negative pregnancy tests; screening health evaluation; injection capability; consent and compliance; and TB testing/therapy conditions.

- **[Provided]** Exclusion criteria included isolated anterior or infectious uveitis, and inadequate response or intolerance to high-dose steroids.

- **[Provided]** Ocular exclusions included POHS; ocular masquerade or serpiginous disease; pupil-dilation limitation; fundus-obscuring opacity or need for cataract surgery; specified glaucoma or BCVA conditions; demyelination; retinopathy; macular disease or vitreoretinal-interface conditions; and specified recent or planned eye-surgery conditions.

- **[Provided]** Treatment-related exclusions included prior anti-TNF/biologic, cyclophosphamide or chlorambucil, or steroid implant exposure; unstable, multiple, prohibited, or excessive immunosuppression; local steroids within 90 days; and recent investigational drugs.

- **[Provided]** Other exclusions included prohibited infections, TB, hepatitis B, HIV, immunodeficiency or anti-infective treatment; positive syphilis or Lyme tests; selected cardiovascular or neurologic history; hypersensitivity; pregnancy or breastfeeding; malignancy; drug or alcohol abuse; significant screening laboratory abnormalities; and investigator-determined unsuitability.

- **[Clarification Required]** Exact operational definitions and thresholds are not supplied for several summarized exclusions, including specified glaucoma/BCVA, eye-surgery, infection, cardiovascular, neurologic, laboratory, and investigator-unsuitability criteria. These details matter for consistent eligibility determination and interpretation of generalizability.

### 4.3 Recruitment

- **[Provided]** The study was multicenter. For sample-size planning, accrual was assumed to average 4 subjects/month for the first 30 months and 7 subjects/month thereafter.

- **[Clarification Required]** Recruitment methods, participating-site counts, and actual enrollment dates or accrual are not supplied. These details matter for describing recruitment and evaluating whether planning assumptions were met.

### 4.4 Withdrawal and Follow-up

- **[Provided]** The final efficacy value is the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure has occurred. The assessment schedule extends through Week 80.

- **[Clarification Required]** Withdrawal criteria, follow-up after treatment discontinuation, handling of withdrawal of consent, and rules for continued outcome collection are not supplied. These decisions matter for follow-up completeness and time-to-event censoring.

- **[Proposed]** Where permitted by consent and applicable study procedures, continue outcome follow-up after study-treatment discontinuation through Week 80. **Rationale:** Continued outcome ascertainment can preserve information for the treatment-failure analysis despite treatment discontinuation. **Assumption:** Follow-up after treatment discontinuation is allowed and does not conflict with the study’s consent or procedures.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize Baseline demographic and clinical characteristics by randomized group using descriptive statistics, without significance tests for between-group differences. Include Baseline IMM usage because it was a randomization stratification factor. **Rationale:** Descriptive summaries characterize the randomized groups without treating chance Baseline differences as confirmatory tests. **Assumption:** The relevant Baseline data were collected.

- **[Clarification Required]** The full set of Baseline variables to be reported is not supplied. The variable list matters for standardized reporting and any adjusted analyses.

## 5\. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary objective concerns efficacy and safety of adalimumab versus placebo as maintenance therapy. The primary time-to-treatment-failure endpoint is subject to two-sided 0.05 testing.

- **[Provided]** Time to treatment failure at 6 months was the outcome used for sample-size planning. The final efficacy value is the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure has occurred.

- **[Clarification Required]** The exact treatment-failure criteria, event-date assignment, and handling of multiple or indeterminate failure criteria are not supplied. These definitions are essential to derive the primary endpoint consistently.

- **[Clarification Required]** No specific primary safety endpoint is defined, despite the primary objective’s inclusion of safety. The safety endpoint definition and assessment period matter for determining whether safety is confirmatory or descriptive.

### 5.2 Secondary Outcomes

- **[Provided]** Ranked secondary efficacy endpoints are tested only after a significant primary endpoint, in the specified hierarchy, with each preceding endpoint required to be significant before testing the next.

- **[Clarification Required]** The secondary endpoint names, definitions, assessment times, and hierarchy order are not supplied. These are necessary to conduct and report the planned confirmatory testing.

### 5.3 Analysis Methods

- **[Provided]** The log-rank test was assumed for the sample-size calculation. The primary time-to-treatment-failure and ranked secondary endpoints are tested two-sided at 0.05.

- **[Proposed]** For the primary time-to-treatment-failure analysis, estimate the time-to-event distribution by randomized group using Kaplan–Meier methods and compare groups using a log-rank test. Report estimated survival probabilities at relevant times, including 6 months, with confidence intervals. **Rationale:** These methods align with the time-to-event endpoint and the log-rank sample-size assumption. **Assumption:** The event and censoring rules are finalized before analysis, and the 6-month estimate is interpretable under the selected analysis population.

- **[Proposed]** Report a Cox-model treatment-effect estimate with a two-sided 95% confidence interval as a supporting summary. **Rationale:** A hazard ratio provides a compact relative-effect estimate alongside the time-to-event curves. **Assumption:** The proportional-hazards model is suitable; evaluate this assumption and interpret the hazard ratio cautiously if it is not supported.

- **[Clarification Required]** Whether the log-rank test is the prespecified final primary test, which randomization strata should be included in the primary analysis, and whether the primary comparison is adjusted are not specified. These decisions affect the test implementation and the relationship between the analysis and randomization.

- **[Proposed]** Use a stratified primary test by Baseline IMM usage for the non-Japan parent-study analysis if that factor matches the randomization strata used for those subjects. **Rationale:** Stratification can respect the stated randomization design. **Assumption:** The IMM strata are defined consistently and have adequate data for the planned test.

- **[Clarification Required]** The endpoint definitions and analysis methods for ranked secondary outcomes are not supplied. They must be specified before the hierarchy can be executed; no endpoint-specific method is assumed here.

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.

### 5.4 Missing Data

- **[Clarification Required]** The protocol’s rules for missing endpoint assessments, missed visits, withdrawal, treatment discontinuation, and incomplete safety data are not supplied. These rules matter for event ascertainment, censoring, and interpretation of the analyses.

- **[Proposed]** For the primary time-to-event analysis, censor subjects without a documented treatment-failure event at the last evaluable disease assessment, subject to any study-specific censoring rules. **Rationale:** This is a transparent time-to-event approach when no failure is observed. **Assumption:** The last evaluable assessment provides a defensible censoring time and censoring is not materially informative after accounting for the analysis design.

- **[Clarification Required]** Whether withdrawal, loss to follow-up, prohibited medication, or other intercurrent events count as treatment failure or as censoring is not specified. The decision matters because it can change event counts, event times, and the treatment comparison.

- **[Proposed]** For secondary outcomes, use the endpoint-appropriate missing-data method only after the endpoint definitions and estimands are confirmed; report the extent and pattern of missingness by group. **Rationale:** Missing-data methods depend on outcome type and estimand. **Assumption:** The missing-data pattern can be described from collected study data.

### 5.5 Additional Analyses

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.

- **[Proposed]** Conduct sensitivity analyses for the primary time-to-treatment-failure result using reasonable alternative censoring rules once the study-specific event and censoring definitions are confirmed. **Rationale:** Alternative rules can show whether conclusions depend on censoring choices. **Assumption:** Sufficient data are available to implement the alternatives.

- **[Clarification Required]** The planned sensitivity analyses, subgroup factors, and subgroup definitions are not supplied. These details matter for reproducibility and for distinguishing prespecified exploratory analyses from post hoc analyses.

### 5.6 Harms

- **[Provided]** Safety is included in the primary objective. Adalimumab and placebo regimens, the prednisone burst and taper, and protocol-directed topical corticosteroid taper are specified.

- **[Proposed]** Summarize available safety data descriptively by treatment group, including subject counts and proportions for collected adverse events, serious adverse events, events leading to discontinuation, deaths, and clinically relevant laboratory or examination findings. **Rationale:** Grouped descriptive summaries support the stated safety objective without implying an unprovided confirmatory safety hypothesis. **Assumption:** These safety data were collected and their study-specific definitions are available.

- **[Clarification Required]** Adverse-event definitions, severity and relatedness grading, coding conventions, safety follow-up period, and specific safety variables are not supplied. These decisions matter for consistent safety tabulation and interpretation.

### 5.7 Software and References

- **[Provided]** East5 Version 5.2.0.0 was used for the sample-size calculation.

- **[Clarification Required]** The statistical software and version used for the final analyses are not specified. This information is needed for reproducibility.

- **[Proposed]** Use validated statistical software for final analyses and document the software name, version, and relevant procedures in the final analysis records. **Rationale:** Documented, validated software supports reproducibility and quality control. **Assumption:** The analysis environment is subject to appropriate validation procedures.

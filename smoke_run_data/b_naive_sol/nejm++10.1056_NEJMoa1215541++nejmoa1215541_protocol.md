# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

**[Provided]** This Phase III study evaluates once-daily dolutegravir (DTG; GSK1349572) plus fixed-dose abacavir/lamivudine (ABC/3TC) versus fixed-dose efavirenz/emtricitabine/tenofovir (Atripla) in antiretroviral therapy (ART)-naïve adults with HIV-1. It aims to establish non-inferior antiviral activity and characterize longer-term safety, tolerability, resistance, and health outcomes.

**[Provided]** DTG 50 mg once daily was selected from Phase 2b dose-ranging data.

### 1.2 Objectives

- **[Provided]** **P1—Primary:** Demonstrate antiviral activity of DTG plus ABC/3TC fixed-dose combination once daily versus Atripla over 48 weeks. The corresponding outcome is comparative antiviral activity over 48 weeks.
- **[Provided]** **S1—Secondary:** Demonstrate antiviral activity through Week 96. The corresponding outcome is antiviral activity through Week 96.
- **[Provided]** **S2—Secondary:** Evaluate antiviral activity through Week 144. The corresponding outcome is antiviral activity through Week 144.
- **[Provided]** **S3—Secondary:** Compare tolerability, long-term safety, antiviral activity, and immunologic activity over time. The corresponding outcomes are these measures over time.
- **[Provided]** **S4—Secondary:** Assess development of viral resistance in subjects experiencing virologic failure. The corresponding outcome is development of viral resistance in these subjects.
- **[Provided]** **S5—Secondary:** Assess change in symptom bother count. The corresponding outcome is change in symptom bother count.
- **[Provided]** **S6—Secondary:** Evaluate incidence of HIV-associated conditions over time. The corresponding outcome is incidence of these conditions over time.
- **[Provided]** **S7—Secondary:** Explore the impact of gender, race, and/or HIV-1 subtype on response. The corresponding outcome is response within these groups.
- **[Provided]** **S8—Secondary:** Explore change in utility and health-related quality of life. The corresponding outcomes are changes in utility and health-related quality of life.

**[Provided]** All stated objectives are designated primary or secondary. Exploratory objectives are not separately reported; exploratory work is described as analyses rather than additional objectives.

## 2\. Study Methods

### 2.1 Trial Design

**[Provided]** The study is Phase III, multicentre, randomized, stratified, double-blind, double-dummy, active-controlled, parallel-group, and fully powered for non-inferiority.

**[Provided]** Allocation is 1:1, with approximately 800 randomized subjects and approximately 400 subjects per arm. The double-blind randomized phase runs from Day 1 through Week 96. Amendment 05 provides an open-label randomized phase through Week 144 and a DTG continuation phase thereafter.

- **[Provided]** **DTG plus ABC/3TC arm:** Once-daily DTG 50 mg tablet plus ABC/3TC 600/300 mg tablet and Atripla placebo.
- **[Provided]** **Atripla arm:** Once-daily EFV/FTC/TDF 600/200/300 mg tablet plus DTG and ABC/3TC placebos.

**[Provided]** Double-dummy treatment is preferably administered fasting/at bedtime.

**[Clarification Required]** Treatment arrangements during the open-label and DTG continuation phases—including continued comparator access, permitted switching, continuation eligibility, and continuation duration—are not specified. These decisions determine exposure attribution and interpretation beyond Week 96.

### 2.2 Randomization

**[Provided]** Central computer-generated randomization occurs after confirmation of entry criteria. The allocation schedule is generated using GSK-validated RANDALL/RandAll software.

**[Provided]** Randomization is stratified by screening plasma HIV-1 RNA ≤100,000 versus >100,000 c/mL and screening CD4+ count ≤200 versus >200 cells/mm³, creating four strata. A fixed block size is used and remains confidential.

**[Clarification Required]** No minimization procedure is specified. The randomization specification should confirm whether the supplied stratified fixed-block procedure constitutes the complete allocation algorithm, because additional allocation restrictions would affect implementation.

**[Proposed]** Restrict allocation-schedule access to authorized personnel independent of blinded assessment, and maintain an auditable treatment-assignment record. Rationale: this protects allocation concealment and blinding; it assumes suitable central randomization and drug-supply systems are available.

### 2.3 Sample Size

**[Provided]** The recruitment target is approximately 800 randomized subjects, approximately 400 per arm. The required evaluable sample is 394 subjects per arm.

**[Derived]** The required evaluable total is 788 subjects. The approximate recruitment target therefore exceeds this total by approximately 12 subjects; this difference does not establish a specified dropout-inflation percentage.

**[Provided]** Sample size is based on the binary proportion with plasma HIV-1 RNA <50 c/mL at Week 48. Planning assumes a 75% response rate in the Atripla arm and the same 75% response rate in the DTG arm; no distinct DTG planning rate is specified.

**[Provided]** The calculation uses a −10-percentage-point non-inferiority margin for DTG minus Atripla, one-sided significance level of 2.5%, and 90% power. The assumed assessment compares the lower bound of a two-sided 95% confidence interval for the response-rate difference with −10%.

**[Provided]** The stated rationale is that 394 evaluable subjects per arm provides 90% power under these assumptions. The calculation is binomial; no separate variance assumption is specified. Required event counts and cluster-design effects are not applicable because this is an individually randomized binary-response design rather than an event-driven or cluster-randomized design.

**[Provided]** No numerical dropout/non-adherence inflation is specified. The 75% planning response incorporates historical context of approximately 15% drug-related and 14% non-drug-related failure. Supporting assumptions include an approximate historical control response of 71%, a recent EFV-arm range of 71%–82%, and anticipated better non-drug compliance.

**[Provided]** No sample-size re-estimation will be performed.

**[Clarification Required]** The operational meaning of “evaluable” for sample-size purposes and the calculation software are unspecified. These details are needed to reconcile recruitment targets with analysis-population membership and reproduce the calculation.

### 2.4 Hypothesis Framework

**[Provided]** Let \(p_{\mathrm{DTG}}\) and \(p_{\mathrm{Atripla}}\) denote Week-48 response probabilities. The non-inferiority hypotheses are \(H_0: p_{\mathrm{DTG}}-p_{\mathrm{Atripla}}\leq-0.10\) versus \(H_1: p_{\mathrm{DTG}}-p_{\mathrm{Atripla}}>-0.10\).

**[Provided]** DTG is non-inferior if the lower bound of the two-sided 95% confidence interval for the response-rate difference is greater than −10 percentage points.

**[Provided]** If both ITT-E and PP analyses demonstrate non-inferiority, ITT-E superiority is tested two-sided at 5%. Superiority is declared if the lower 95% confidence bound exceeds zero.

**[Provided]** Conditional on non-inferiority, the key secondary superiority tests are generalized Wilcoxon for time to suppression, a repeated-measures mixed model for Week-48 CD4, and ANCOVA for Week-4 SDM bother, within the specified fallback sequence.

**[Derived]** A lower confidence bound exactly equal to −10 percentage points does not establish non-inferiority. A lower bound exactly equal to zero does not establish superiority.

**[Clarification Required]** The full fallback algorithm—including local significance levels, allocation or recycling of alpha, and its relationship to the ITT-E superiority test—is not supplied. These decisions are necessary for reproducible familywise-error control.

### 2.5 Statistical Interim Analyses

**[Clarification Required]** The presence, timing, purpose, and decision boundaries of any interim efficacy or futility analyses are unspecified. These details matter because repeated confirmatory testing can alter the overall type I error rate.

**[Clarification Required]** Independent monitoring arrangements, access to unblinded safety data, and statistical or clinical stopping rules are unspecified. They are needed to define oversight responsibilities without compromising blinded conduct.

**[Proposed]** Do not introduce an unplanned confirmatory interim efficacy test without a prospective amendment defining its error-control consequences. Rationale: this preserves the stated significance framework; it assumes no already-approved interim testing plan exists outside the supplied information.

### 2.6 Timing of Analyses

**[Provided]** Week 48 is the primary analysis time point. The final analysis occurs once all subjects have completed or discontinued.

**[Provided]** Plasma HIV-1 RNA assessments in the final amended protocol occur at screening, Day 1, Weeks 2, 4, 8, 12, 16, 24, 32, 40, and 48, and every 12 weeks thereafter through Week 144.

**[Provided]** Amendment 05 documents Week-144 open-label/continuation conduct. Actual assessment dates determine allocation to analysis windows.

**[Clarification Required]** The relationship between the Week-48 primary analysis, Week-96 and Week-144 analyses, and the final analysis after completion or discontinuation is unspecified. The endpoint of the post-Week-144 continuation phase must also be defined to establish when final follow-up is complete.

**[Clarification Required]** Assessment schedules for CD4/CD8, SDM, EQ-5D, and safety are not supplied. Visit-window boundaries, data cutoffs, database-lock requirements, and data-readiness criteria are also unspecified; these determine which observations enter each analysis.

**[Proposed]** Finalize analysis specifications, visit-window rules, endpoint derivations, and data-review requirements before access to treatment-comparative results for the relevant analysis. Rationale: prospective specification limits result-driven choices; it assumes these decisions remain available for prospective finalization.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** Primary non-inferiority testing uses one-sided 2.5% significance, implemented through the lower bound of a two-sided 95% confidence interval. Eligible ITT-E superiority testing uses two-sided 5% significance and the stated positive lower-confidence-bound rule.

**[Proposed]** Report treatment effects with two-sided 95% confidence intervals, denominators, and exact reported p-values where applicable. Treat secondary comparisons outside an approved multiplicity procedure as descriptive. Rationale: this distinguishes estimation from confirmatory claims; it assumes no additional multiplicity specification is available.

**[Proposed]** Express binary treatment differences as DTG minus Atripla in percentage points throughout. Rationale: this maintains consistency with the non-inferiority hypotheses; it assumes the same direction is used in all displays.

### 3.2 Protocol Deviations

**[Proposed]** Prospectively classify deviations affecting eligibility, randomized treatment, prohibited therapy, adherence, endpoint assessment, and blinding, with major/minor status assigned without knowledge of comparative outcomes. Rationale: consistent classification protects the integrity of PP analyses; it assumes adequate source documentation.

**[Clarification Required]** Major-deviation definitions, adherence thresholds, prohibited concomitant therapies, and PP exclusion rules are unspecified. These decisions can materially change the non-inferiority result and must not be selected after reviewing treatment effects.

**[Proposed]** Summarize deviations by randomized arm and category, retaining subjects in the principal randomized comparison unless its prespecified population definition requires otherwise. Rationale: this makes exclusions transparent and limits selective removal; it assumes deviations can be adjudicated consistently.

### 3.3 Analysis Populations

**[Provided]** ITT-E and PP analyses are required for the stated non-inferiority-to-superiority sequence.

**[Clarification Required]** Formal definitions of ITT-E, PP, and safety populations, including treatment attribution, are not supplied. The designated primary non-inferiority population and whether both populations are required for the non-inferiority claim itself must be confirmed; both are explicitly required before superiority testing.

**[Proposed]** Define ITT-E as all randomized subjects receiving at least one dose, analyzed by randomized assignment. Rationale: this provides an explicit exposed-randomized population consistent with the population name; it assumes exposure is the intended meaning of “E.”

**[Proposed]** Define PP as the ITT-E subset without prospectively adjudicated major deviations that compromise interpretation of assigned-treatment efficacy. Do not exclude subjects solely because an outcome is missing unless explicitly justified in the approved rules. Rationale: this supports a credible non-inferiority sensitivity analysis; it assumes exclusion criteria are finalized without comparative outcome knowledge.

**[Proposed]** Define the safety population as all subjects receiving at least one dose, analyzed according to treatment actually received, with exposure periods distinguished after switching. Rationale: harms are attributable to exposure; it assumes treatment administration dates are available.

**[Proposed]** Include an all-randomized sensitivity analysis if any randomized subjects are excluded from ITT-E. Rationale: this assesses the consequence of post-randomization exclusions; it assumes allocation records are available for every randomized subject.

## 4\. Trial Population

### 4.1 Screening Data

**[Provided]** One re-screen with a new screening number and one repeat test per analyte/assessment are permitted. Genotype retesting is not permitted.

**[Proposed]** Maintain linked screening and re-screening records and summarize unique individuals screened, screening attempts, eligibility outcomes, reasons for exclusion, and randomization. Rationale: linkage prevents double-counting while retaining the required new number; it assumes a secure subject-linkage mechanism.

**[Clarification Required]** Screening counts, screening dates, and the rules identifying which permitted repeat result determines eligibility are unspecified. These are needed for participant flow and reproducible eligibility assessment.

### 4.2 Eligibility Criteria Summary

#### Inclusion Criteria

- **[Provided]** Subjects must understand and comply with study requirements, be expected to complete the study as planned, and be appropriate candidates for oral investigational therapy.
- **[Provided]** Subjects must be HIV-1 infected adults aged ≥18 years, with screening HIV-1 RNA ≥1,000 c/mL.
- **[Provided]** ART-naïve status is defined as ≤10 prior ART days after diagnosis.
- **[Provided]** Subjects must be HLA-B*5701 negative and provide dated written informed consent.
- **[Provided]** Women must be non-child-bearing—post-menopausal with 12 months of amenorrhea and age ≥45 years, or documented sterilization—or have negative screening and Day-1 pregnancy tests and consistently use protocol-specified contraception from two weeks before investigational product through two weeks afterward.
- **[Provided]** Permitted contraceptive methods include abstinence, double barrier, a qualifying IUD or another method with <1% failure, or hormonal contraception plus a barrier method.
- **[Provided]** Enrollment in France additionally requires social-security affiliation or beneficiary status.

#### Exclusion Criteria

- **[Provided]** Breastfeeding.
- **[Provided]** Active CDC Category C disease, except cutaneous Kaposi not requiring systemic therapy. Historical or current CD4 <200 cells/mm³ is not exclusionary.
- **[Provided]** Hepatic impairment; HBsAg positivity; or anticipated HCV therapy.
- **[Provided]** Recent gastrointestinal bleeding or allergy/intolerance to study drugs or their class.
- **[Provided]** Recent or ongoing malignancy, except specified skin/Kaposi exceptions.
- **[Provided]** Recent HIV immunotherapeutic vaccine, radiation, cytotoxic chemotherapy, immunomodulator, HIV-active agent, or experimental drug/vaccine, including an additional France-specific restriction.
- **[Provided]** Primary resistance.
- **[Provided]** Verified Grade-4/acute disqualifying laboratory abnormality, or meeting the specified ALT/bilirubin exclusion thresholds.
- **[Provided]** Creatinine clearance <50 mL/min by Cockcroft–Gault.

**[Clarification Required]** Numerical ALT/bilirubin thresholds, hepatic-impairment criteria, “recent” exposure intervals, malignancy exceptions, primary-resistance criteria, acute laboratory exclusions, and the additional France-specific restriction are not fully specified. These details are necessary for consistent eligibility decisions and must not be inferred.

**[Clarification Required]** Detailed qualifying contraception requirements and any exceptions to the summarized reproductive criteria are not supplied. These affect eligibility and reproductive safety procedures.

### 4.3 Recruitment

**[Provided]** Recruitment is multicentre and targets approximately 800 randomized subjects.

**[Clarification Required]** Participating countries and sites, recruitment dates, site targets, and recruitment procedures are unspecified. These determine operational feasibility and the setting to which results apply.

**[Proposed]** Monitor recruitment, screening exclusions, and the distribution of the four randomization strata without examining treatment effects. Rationale: this supports accrual oversight without outcome-driven enrollment; it assumes blinded operational summaries are available.

### 4.4 Withdrawal and Follow-up

**[Clarification Required]** Treatment-discontinuation criteria, withdrawal procedures, follow-up after stopping therapy, loss-to-follow-up procedures, and post-treatment safety windows are unspecified. These decisions determine intercurrent-event handling, outcome completeness, and safety ascertainment.

**[Proposed]** Distinguish permanent treatment discontinuation from withdrawal from study follow-up, and continue scheduled outcome collection after treatment discontinuation when consent permits. Rationale: continued observation reduces avoidable missingness; it assumes consent and local requirements permit follow-up.

**[Proposed]** Record discontinuation dates and reasons, subsequent ART, consent withdrawal, loss to follow-up, and death separately. Rationale: these events have different clinical and statistical implications; it assumes the data collection system can capture them distinctly.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize age, gender, race, HIV-1 subtype, HIV-1 RNA, CD4/CD8 measures, relevant HIV history, and available baseline safety and health-outcome measures by randomized arm. Rationale: these describe the population and support prespecified analyses; it assumes the relevant variables are collected.

**[Proposed]** Present continuous variables using sample size, mean, standard deviation, median, and range, and categorical variables using counts and percentages with missing categories identified. Avoid significance tests of randomized baseline differences. Rationale: descriptive summaries characterize balance without treating chance imbalance as a selection criterion; it assumes appropriate variable-level reporting.

**[Clarification Required]** The baseline-selection hierarchy is unspecified, particularly where screening and Day-1 values differ. This matters because screening values define randomization strata, whereas analysis covariates may require a separate pre-dose baseline definition.

## 5\. Analysis

### 5.1 Primary Outcomes

**[Provided]** The Week-48 primary binary response measure is the proportion with plasma HIV-1 RNA <50 c/mL, comparing DTG plus ABC/3TC with Atripla.

**[Proposed]** Operationalize the principal binary comparison as response while maintaining the assigned regimen: a qualifying Week-48 RNA result <50 c/mL constitutes response, while death, permanent assigned-regimen discontinuation, disqualifying treatment switch, or absence of a qualifying measurement constitutes nonresponse. Rationale: this combines antiviral activity with maintenance of assigned therapy; it assumes a composite strategy is intended and requires approval before implementation.

**[Clarification Required]** The intended estimand and response-classification algorithm are not supplied. In particular, the treatment of temporary interruptions, permitted substitutions, rescue therapy, discontinuation with documented suppression, and results obtained after switching must be confirmed because they can change response rates and the non-inferiority conclusion.

**[Clarification Required]** Week-48 window limits, selection among multiple results, assay reporting conventions, and handling of values reported only as below quantification are unspecified. These determine whether a subject meets the strict <50 c/mL threshold.

**[Proposed]** Report arm-specific responder counts and proportions, the DTG-minus-Atripla difference, its two-sided 95% confidence interval, and the non-inferiority decision in ITT-E and PP. Rationale: these outputs directly implement the supplied hypotheses and superiority gate; it assumes the population and endpoint rules have been finalized.

### 5.2 Secondary Outcomes

**[Provided]** Secondary outcomes comprise antiviral activity through Weeks 96 and 144; tolerability, long-term safety, antiviral and immunologic activity over time; resistance in virologic failure; change in symptom bother count; incidence of HIV-associated conditions; response by gender, race, and/or HIV-1 subtype; and change in utility and health-related quality of life.

**[Provided]** Named key secondary comparisons are time to suppression, Week-48 CD4, and Week-4 SDM bother.

**[Clarification Required]** Time-to-suppression definitions—including threshold, confirmation requirements, time origin, and censoring—are unspecified. The virologic-failure definition, confirmation schedule, resistance-testing triggers, and resistance interpretation rules are also missing; these determine event ascertainment and denominators.

**[Clarification Required]** SDM scoring, symptom-count derivation, CD4/CD8 endpoint definitions, EQ-5D version and scoring/value set, and HIV-associated-condition definitions are unspecified. These decisions are necessary to construct valid outcomes and interpret changes.

**[Proposed]** Apply the finalized Week-48 binary-response framework consistently at Weeks 96 and 144, while identifying blinded and open-label periods in reporting. Rationale: consistent rules facilitate longitudinal interpretation; it assumes the same response construct remains appropriate after unblinding.

### 5.3 Analysis Methods

**[Proposed]** Estimate the primary risk difference by standardizing stratum-specific DTG-minus-Atripla differences across the four screening strata, using pooled stratum proportions within the analysis population as weights. Calculate a two-sided 95% normal-approximation interval using the sum of squared weights multiplied by the within-stratum binomial variances. Rationale: this respects the stratified design and estimates the supplied absolute difference; it assumes adequate stratum sizes for the approximation.

**[Clarification Required]** The definitive confidence-interval method and sparse-stratum handling are not specified. These must be frozen before comparative analysis because alternative valid methods can yield different conclusions near the −10-percentage-point boundary.

**[Proposed]** Use the same approved risk-difference estimator and confidence-interval construction for the corresponding non-inferiority and gated ITT-E superiority decisions. Rationale: this avoids method-dependent switching between claims; it assumes the selected method is appropriate for both comparisons.

**[Provided]** The specified test for the key secondary time-to-suppression comparison is generalized Wilcoxon.

**[Proposed]** Accompany the generalized Wilcoxon comparison with time-to-suppression curves and clinically interpretable time summaries under the finalized event and censoring rules. Rationale: the test alone does not quantify the response pattern; it assumes censoring assumptions are defensible and explicitly assessed.

**[Provided]** The specified analysis for the key Week-48 CD4 comparison is a repeated-measures mixed model.

**[Proposed]** Model post-baseline CD4 measurements using treatment, categorical visit, treatment-by-visit interaction, baseline CD4, and screening RNA stratum, with the Week-48 treatment contrast extracted from the longitudinal model. Use an unstructured within-subject covariance where estimable, with a prospectively specified convergence fallback. Rationale: this uses repeated observations while adjusting for baseline prognostic information; it assumes the model and missing-at-random assumption are adequate.

**[Clarification Required]** Whether the CD4 estimand is an adjusted Week-48 level or change from baseline, the full fixed-effect specification, and covariance fallback order are unspecified. These details are needed to finalize the model and its interpretation.

**[Provided]** The specified analysis for the key Week-4 SDM bother comparison is ANCOVA.

**[Proposed]** Analyze Week-4 change in the finalized SDM bother measure using treatment, baseline score, and randomization strata as covariates. Rationale: baseline adjustment improves precision for a change outcome; it assumes the scoring scale and residual behavior support ANCOVA.

**[Proposed]** Summarize resistance among subjects meeting the finalized virologic-failure definition, distinguishing eligible subjects, tested subjects, assay failures, and detected resistance. Rationale: explicit denominators prevent missing tests from being interpreted as absence of resistance; it assumes baseline and failure samples can be linked.

**[Proposed]** Summarize HIV-associated conditions using subject counts, event counts, and exposure-adjusted incidence rates; add time-to-first-event analyses if events and follow-up support them. Rationale: these capture both occurrence and unequal observation time; it assumes condition definitions and exposure dates are standardized.

**[Proposed]** Analyze other longitudinal symptom, utility, and quality-of-life outcomes using models appropriate to their finalized scales, with treatment-by-visit contrasts and baseline adjustment. Rationale: repeated-measures methods support change-over-time objectives; it assumes scoring rules and model diagnostics are established before analysis.

### 5.4 Missing Data

**[Proposed]** Summarize missing assessments and their reasons by treatment and visit, distinguishing unavailable measurements from observed outcomes classified as nonresponse because of an intercurrent event. Rationale: missingness and composite endpoint failure are not interchangeable; it assumes reasons are captured reliably.

**[Proposed]** Under the proposed principal binary-response algorithm, do not impute an unobserved RNA concentration; classify absence of a qualifying assessment as nonresponse. Rationale: this implements the proposed operational endpoint; it assumes that endpoint strategy is approved.

**[Proposed]** Assess binary-response sensitivity using opposing extreme allocations of missing outcomes and a treatment-specific tipping-point analysis. Include the unfavorable-to-DTG allocation in which missing DTG outcomes are failures and missing Atripla outcomes are successes. Rationale: equal missing-as-failure rules are not necessarily conservative for non-inferiority; it assumes missing observations can be separated from observed protocol-defined failures.

**[Proposed]** For continuous longitudinal outcomes, use the specified likelihood-based models under missing at random, supplemented by multiple-imputation or pattern-mixture sensitivity analyses allowing less favorable unobserved outcomes after dropout. Rationale: observed-data models do not resolve informative missingness; it assumes sufficient predictors and plausible departure scenarios can be prespecified.

**[Clarification Required]** Imputation models, departure parameters, minimum questionnaire-completion rules, and handling of partially missing dates are unspecified. These decisions affect reproducibility and must be finalized before implementation.

### 5.5 Additional Analyses

**[Provided]** Analyses will explore the impact of gender, race, and/or HIV-1 subtype on response. These remain analyses supporting secondary objectives rather than separately designated exploratory objectives.

**[Proposed]** Present response estimates and treatment-by-subgroup interaction analyses for gender, race, HIV-1 subtype, and the screening RNA and CD4 strata. Treat subgroup findings as descriptive unless a separate multiplicity procedure is approved. Rationale: interaction analyses address heterogeneity more directly than separate within-group significance tests; it assumes adequate subgroup sizes.

**[Proposed]** Include unadjusted risk differences and analyses assessing the influence of major deviations, adherence, and post-randomization treatment changes. Rationale: these evaluate robustness of the principal non-inferiority result; it assumes definitions are prospective and such analyses do not replace randomized comparisons.

**[Proposed]** Report longer-term outcomes by the original randomized groups, clearly separating double-blind follow-up through Week 96, open-label follow-up through Week 144, and DTG continuation thereafter. Rationale: unblinding and selective continuation can change interpretation; it assumes original assignment and phase-specific exposure remain traceable.

**[Clarification Required]** Subgroup category definitions, handling of unknown or mixed HIV-1 subtype, and continuation-phase comparison populations are unspecified. These affect estimability and whether longer-term comparisons retain a randomized interpretation.

### 5.6 Harms

**[Provided]** Tolerability and long-term safety are secondary objectives. Eligibility restrictions include HLA-B*5701 negativity, exclusion of relevant allergy/intolerance, hepatic and laboratory exclusions, and creatinine clearance ≥50 mL/min by Cockcroft–Gault.

**[Proposed]** Summarize adverse events, serious adverse events, deaths, discontinuations due to adverse events, clinically important laboratory abnormalities, and treatment interruptions by actual treatment exposure and study phase. Rationale: these distinguish event burden from treatment-limiting toxicity; it assumes standardized event and exposure records.

**[Proposed]** Present the number and percentage of subjects affected, severity, investigator-assessed relationship, and exposure-adjusted rates where follow-up differs materially. Rationale: raw proportions alone can mislead during unequal long-term exposure; it assumes a common coding and severity framework.

**[Clarification Required]** Adverse-event definitions, coding dictionary, severity scale, treatment-emergent window, post-treatment reporting period, pregnancy reporting, and expedited-reporting procedures are unspecified. These are required for consistent safety classification and reporting.

**[Clarification Required]** Drug-specific interruption/discontinuation criteria, urgent unblinding procedures, and management of clinically significant laboratory findings are not supplied. These decisions are necessary for safe operational conduct and must not be inferred from eligibility exclusions.

**[Proposed]** Route urgent clinical safety findings for prompt investigator assessment and record resulting treatment actions separately from statistical endpoint classification. Rationale: clinical care must not depend on analysis conventions; it assumes an approved clinical safety-management process is established before enrollment.

### 5.7 Software and References

**[Provided]** RANDALL/RandAll is the specified validated software for randomization-schedule generation.

**[Clarification Required]** Statistical analysis software, versions, packages, and sample-size calculation software are not specified. These details are required to reproduce numerical results and verify implementation of confidence intervals and fallback testing.

**[Proposed]** Use validated statistical software with version-controlled programs, fixed random seeds for stochastic procedures, independently checked endpoint derivations, and archived analysis specifications and outputs. Rationale: this supports reproducibility and auditability; it assumes access to an approved computing environment.

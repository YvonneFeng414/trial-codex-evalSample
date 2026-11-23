# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

[Provided] Selexipag (ACT-293987) is a non-prostanoid IP-receptor agonist being evaluated against placebo in pulmonary arterial hypertension (PAH), with assessments of morbidity/mortality, exercise capacity, safety, and tolerability.

### 1.2 Objectives

- [Provided] **P1:** Demonstrate the effect of selexipag versus placebo on time to first CEC-confirmed morbidity/mortality event in PAH.
- [Provided] **S1:** Evaluate selexipag versus placebo for exercise capacity and other secondary/exploratory efficacy endpoints in PAH.
- [Provided] **S2:** Evaluate the safety and tolerability of selexipag in PAH in the randomized study and the open-label extension.
- [Provided] Exploratory objectives are not separately labelled. Enumerated exploratory analysis areas include efficacy, dose-response, pharmacoeconomics, pharmacokinetics (PK), and safety.
- [Clarification Required] The complete secondary and exploratory endpoint inventory and its mapping to these objectives must be supplied; the broad objective descriptions do not establish operational endpoint definitions.

## 2. Study Methods

### 2.1 Trial Design

- [Provided] The randomized study is prospective, multicenter, double-blind, placebo-controlled, parallel-group, Phase 3, and event-driven.
- [Provided] A separate open-label, uncontrolled extension evaluates long-term safety and tolerability.
- [Provided] The planned allocation is placebo:selexipag 1:1, with 1,150 randomized patients and 575 planned patients per group.
- [Provided] Treatment starts with the Day-1 evening administration of the 200-µg twice-daily selexipag regimen or matching placebo.
- [Provided] Selexipag is increased weekly in 200-µg twice-daily increments to the individual maximum tolerated dose, not exceeding 1,600 µg twice daily. Dose reductions are permitted for tolerability.
- [Provided] Placebo is matching ACT-293987 placebo administered twice daily under the same titration schedule.
- [Provided] From Week 12, the dose is held through Week 26. Later increases are permitted at scheduled visits.
- [Provided] Treatment continues until 331 CEC-confirmed events, with a maximum duration of 4.3 years.
- [Provided] The randomized study also has a Treatment Extension period running from EOS to EOTE after unblinding.
- [Clarification Required] The relationship between the randomized-study Treatment Extension and the separate open-label extension must be specified, including transition eligibility, dosing, participant overlap, and data ownership; these decisions determine exposure attribution and prevent duplicate safety reporting.
- [Clarification Required] Operational titration rules, management between Weeks 8 and 12, dose-interruption/restart rules, and tolerability criteria must be supplied; the stated schedule does not fully define individual dose management.
- [Clarification Required] The scope of the 4.3-year maximum and the operational treatment-stop trigger require confirmation, including whether the trigger uses confirmed events available in real time; these details determine treatment duration and closure procedures.

### 2.2 Randomization

- [Provided] An independent centralized IWRS/IVRS assigns each patient a unique randomization number. The randomization code remains confidential until unblinding.
- [Provided] Randomization is stratified by site.
- [Clarification Required] Blocking or minimization methods, any block sizes, and allocation-list generation procedures are unspecified; these are needed to document implementation and assess allocation concealment.
- [Proposed] Restrict allocation-code access and document any emergency unblinding with its reason, timing, and recipients. Rationale: this protects masking and permits assessment of potential bias. Assumption: controlled code access and emergency unblinding functionality are available.

### 2.3 Sample Size

- [Provided] The final Version-7 specifications are 1,150 planned randomized patients, 575 per group, and 331 first CEC-confirmed morbidity/mortality events.
- [Provided] The calculation concerns a time-to-event outcome and assumes constant annual event hazards of 0.2231 in the control group and 0.145 in the selexipag group, with a target hazard ratio of 0.65.
- [Provided] The calculation uses variance under the alternative hypothesis and a constant annual dropout hazard of 0.051 in both groups. No separate numerical sample-size inflation is reported.
- [Provided] The assumed test is a one-sided, unstratified log-rank test within a group-sequential design, with overall α = 0.005 and 90% power to reject the null hypothesis.
- [Provided] Under the stated assumptions, 331 events achieve the planned 90% power; recruitment of up to 1,150 patients randomized 1:1 was expected to yield that event count.
- [Provided] The calculation used EAST 5.3 with its variance-under-alternative option.
- [Provided] No non-inferiority or equivalence margin applies. The study is individually randomized and non-clustered, so no clustering design effect applies.
- [Provided] Earlier Version 1 allowed a blinded sample-size adaptation up to 1,150 patients. The statistical analysis framework uses the final Version-7 specifications.
- [Clarification Required] Whether a blinded adaptation was actually performed, and any associated review dates and decisions, must be documented; permission to adapt does not establish that adaptation occurred.

### 2.4 Hypothesis Framework

- [Provided] The primary comparison is superiority. The one-sided null hypothesis states that survival free of a first CEC-confirmed morbidity/mortality event with selexipag is no greater than with placebo at all times.
- [Provided] The alternative states that event-free survival with selexipag is no worse at all times and is greater at some time.
- [Derived] The target hazard ratio of 0.65 is a planning assumption, not a non-inferiority margin or a required observed treatment effect.
- [Proposed] Use the randomized treatment contrast as the primary efficacy comparison rather than comparing achieved dose groups. Rationale: this preserves the randomized comparison. Assumption: randomized allocation records are reliable.

### 2.5 Statistical Interim Analyses

- [Provided] The design is group-sequential, with an overall one-sided α of 0.005.
- [Provided] The planned probability of rejecting the null hypothesis at interim was approximately 19%. Under HR = 1, the probability described as accepting the null hypothesis at interim was approximately 50%.
- [Clarification Required] The number and timing of interim looks, information fractions, efficacy boundaries, futility boundaries, spending functions, and binding or nonbinding status of futility rules must be supplied; the operating probabilities alone cannot reconstruct valid stopping rules.
- [Clarification Required] The meaning and operational consequence of “accepting the null” must be established; an interim futility decision is not necessarily evidence that the treatments are equivalent.
- [Clarification Required] Interim oversight membership, access to unblinded results, recommendation procedures, and any interim analyses actually performed must be documented; these affect confidentiality and final sequential inference.
- [Proposed] Do not substitute ad hoc stopping thresholds for the missing sequential rules. Rationale: unplanned thresholds can invalidate type I error control. Assumption: the original design specifications or equivalent validated records can be obtained.

### 2.6 Timing of Analyses

- [Provided] The randomized-study final analysis includes Treatment and post-treatment observation data, excludes Treatment Extension data, and uses a cutoff of 27-Apr-2014.
- [Provided] Open-label-extension safety data through 10-Mar-2014 are included.
- [Provided] Screening occurs no more than 28 days before Day 1. Baseline and randomization occur on Day 1.
- [Provided] The assessment schedule includes titration through Week 8; visits at Weeks 12, 16, and 26; visits every 6 months thereafter; EOS; and safety follow-up.
- [Provided] Study closure prompts EOS or PTOCV within four weeks.
- [Provided] Six-minute walk test (6MWT) and Borg assessments occur at baseline and scheduled follow-ups. Week-26 endpoint assessments occur before the morning dose, at trough.
- [Clarification Required] Visit windows, endpoint-specific assessment schedules, safety follow-up duration, and the operational definitions of EOS, PTOCV, and EOTE must be supplied; these determine analysis windows and completeness assessments.
- [Clarification Required] Database-lock and data-readiness requirements are unspecified; the required status of event adjudication, outstanding queries, reconciliation, and late-arriving data must be defined before final datasets are established.
- [Proposed] Reconcile treatment exposure, vital status, suspected events, and adjudication decisions before freezing analysis datasets, retaining an audit trail for subsequent corrections. Rationale: this reduces inconsistent outcome and exposure classification. Assumption: source records and adjudication records are accessible.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- [Provided] The primary design uses an overall one-sided significance level of 0.005.
- [Clarification Required] The final nominal significance threshold cannot be specified without the sequential design and interim history; applying 0.005 directly at every analysis would not establish overall error control.
- [Proposed] Report the primary treatment-effect estimate with confidence bounds calibrated to the prespecified sequential design. Rationale: estimation and hypothesis testing should use compatible error control. Assumption: the sequential rules and analysis history are recoverable.
- [Clarification Required] The confirmatory status, ordering, and multiplicity strategy for secondary endpoints must be specified; no secondary confirmatory claim is supported by the supplied primary α alone.
- [Proposed] Until a secondary testing strategy is established, present secondary and exploratory estimates with nominal two-sided 95% confidence intervals and explicitly descriptive interpretation. Rationale: this communicates precision without implying familywise error control. Assumption: these summaries are not used for confirmatory decisions.

### 3.2 Protocol Deviations

- [Proposed] Maintain a deviation listing covering eligibility errors, incorrect treatment, prohibited medications, titration departures, unblinding, and missed outcome ascertainment, with predefined severity classifications. Rationale: consistent classification supports interpretation and sensitivity analyses. Assumption: deviations can be identified from auditable records.
- [Proposed] Review and classify deviations without comparative outcome knowledge where feasible, and retain randomized participants in the primary analysis population despite deviations. Rationale: this limits outcome-driven exclusions and preserves randomization. Assumption: treatment allocation and outcome records can be separated during classification.
- [Clarification Required] The final major-deviation criteria and any per-protocol exclusion rules require approval; otherwise per-protocol membership could be determined inconsistently.

### 3.3 Analysis Populations

- [Proposed] Define the primary intention-to-treat population as all randomized patients, analyzed by assigned treatment. Rationale: this preserves the randomized treatment contrast. Assumption: all randomizations can be accounted for.
- [Proposed] Define the randomized-study safety population as all patients receiving at least one dose, summarized by treatment actually received. Rationale: safety attribution should reflect exposure. Assumption: dosing records identify actual treatment.
- [Proposed] Define the open-label-extension safety population separately as all extension participants receiving at least one extension dose. Rationale: this distinguishes uncontrolled long-term exposure from randomized exposure. Assumption: extension enrollment and dosing records are available.
- [Proposed] Use any per-protocol population only for sensitivity analysis. Rationale: exclusions after randomization may introduce selection bias. Assumption: exclusion criteria are finalized without outcome-driven selection.
- [Clarification Required] Rules for never-treated patients, incorrect-treatment exposure, treatment switching, and overlapping extension participation must be specified; these determine denominators and exposure attribution.
- [Clarification Required] Inclusion of post-discontinuation observations in the primary endpoint requires a separate endpoint-window decision; inclusion of post-treatment data in the database does not establish their eligibility for every efficacy analysis.

## 4. Trial Population

### 4.1 Screening Data

- [Proposed] Summarize numbers screened, eligible, ineligible, randomized, and treated, with screen-failure reasons and reconciliation of duplicate screening records. Rationale: this documents participant selection and disposition. Assumption: screening logs are available.
- [Proposed] Summarize screening-to-randomization timing and completeness of eligibility assessments. Rationale: this identifies departures from the screening window and incomplete qualification. Assumption: dated screening records are retained.
- [Clarification Required] Screening counts and actual exclusion frequencies are not supplied; these must come from study records rather than planned enrollment.

### 4.2 Eligibility Criteria Summary

- [Provided] Eligible patients are aged 18–75 years and have symptomatic Group-1 idiopathic, heritable, drug/toxin-induced, connective-tissue-disease-associated, repaired-shunt congenital-heart-disease-associated, or HIV-associated PAH.
- [Provided] Documented right-heart catheterization must show mPAP ≥25 mmHg, PVR ≥400 dyn·s·cm−5, and PCWP/LVEDP ≤15 mmHg.
- [Provided] Screening six-minute walk distance (6MWD) must be 50–450 m.
- [Provided] Women of childbearing potential require contraception with a failure rate <1% per year through one month after the final dose.
- [Provided] Endothelin receptor antagonists and PDE5 inhibitors are permitted if stable for at least three months before baseline and through Week 26.
- [Provided] Exclusions include pulmonary hypertension Groups 2–5.
- [Provided] Prostacyclin or analogue treatment within one month, or planned during the trial, is excluded, except for a single administration for acute vasodilator testing.
- [Provided] Obstructive disease is excluded when FEV1/FVC <70% and FEV1 <65% predicted. Restrictive disease is excluded when TLC <70% predicted.
- [Provided] Additional exclusions are Child-Pugh B/C impairment, LVEF <45%, severe renal dysfunction, and BMI <18.5.
- [Provided] Additional exclusions are recent investigational drug use; inability to comply or perform the 6MWT; rehabilitation completed less than eight weeks before screening or planned rehabilitation; impaired consent/adherence capacity; life expectancy <12 months; and pregnancy or lactation.
- [Provided] Prostacyclin/analogues and investigational drugs are prohibited.
- [Clarification Required] “Severe renal dysfunction,” “recent investigational drug,” and acceptable documentation timing require operational definitions; otherwise eligibility cannot be applied reproducibly.
- [Clarification Required] Any additional requirements for repaired shunts, reproductive testing, and permitted contraceptive methods must be supplied; these cannot be inferred from the summarized criteria.
- [Clarification Required] Procedures for medically necessary prohibited therapy and its consequences for treatment continuation and endpoint handling must be defined; prohibition alone does not specify rescue care or analysis consequences.

### 4.3 Recruitment

- [Provided] Recruitment is multicenter, with up to 1,150 randomized patients planned.
- [Clarification Required] Participating sites, recruitment dates, recruitment duration, site targets, and recruitment procedures are unspecified; these are needed for operational planning and assessment of recruitment feasibility.
- [Proposed] Obtain documented informed consent before study-specific procedures and retain screening logs. Rationale: this supports participant protection and traceable recruitment. Assumption: approved consent procedures and appropriate oversight are in place.

### 4.4 Withdrawal and Follow-up

- [Proposed] Distinguish study-drug discontinuation, withdrawal from assessments, withdrawal of consent, and loss to follow-up in disposition records. Rationale: these events have different implications for exposure and missing outcomes. Assumption: participant permissions can be documented accurately.
- [Proposed] Continue permitted event and vital-status ascertainment after treatment discontinuation when consent and applicable requirements allow. Rationale: this reduces avoidable loss of outcome information. Assumption: follow-up can be conducted without requiring continued treatment.
- [Clarification Required] Withdrawal criteria, contact procedures, permissible record-based follow-up, and safety follow-up timing must be defined; they determine ascertainment completeness and participant obligations.
- [Clarification Required] The effect of discontinuation, rescue treatment, and extension entry on primary efficacy follow-up must be specified; continued data collection does not by itself resolve the primary estimand.

### 4.5 Baseline Characteristics

- [Proposed] Summarize available age, sex, PAH etiology, hemodynamics, screening/baseline 6MWD, Borg assessments, and background PAH therapy by randomized group. Rationale: these characterize the enrolled population and potential prognostic imbalance. Assumption: the listed variables were collected with usable definitions.
- [Proposed] Use counts and percentages for categorical variables and appropriate location and dispersion summaries for continuous variables, reporting missing denominators explicitly. Rationale: these summaries support transparent description. Assumption: measurement scales and units are verified.
- [Proposed] Avoid significance testing of baseline differences. Rationale: descriptive assessment is more appropriate for interpreting chance imbalance after randomization. Assumption: randomization was implemented as intended.
- [Clarification Required] Baseline selection rules, especially for repeated screening and predose measurements, must be specified; inconsistent selection could affect covariate adjustment and change-from-baseline analyses.

## 5. Analysis

### 5.1 Primary Outcomes

- [Provided] The primary outcome is time to first CEC-confirmed morbidity/mortality event in PAH, comparing selexipag with placebo.
- [Derived] Only the first qualifying confirmed event contributes to a participant’s primary event count; later events do not add primary first events.
- [Clarification Required] The morbidity/mortality composite components, qualifying criteria, event-date conventions, and handling of simultaneous components must be supplied; the composite cannot be implemented from its name alone.
- [Clarification Required] The CEC charter, masking arrangements, adjudication status categories, and treatment of unresolved or unconfirmed suspected events must be specified; these determine which events qualify.
- [Clarification Required] The time origin, endpoint observation period, censoring rules, treatment of post-discontinuation events, and handling of deaths require specification; they materially define the primary estimand.
- [Clarification Required] The actual confirmed-event total and its relationship to the 331-event target and final cutoff must be established from study records; a target is not an observed result.
- [Proposed] Report event counts, observed follow-up, event-free survival curves, and the treatment-effect estimate alongside the primary test. Rationale: these describe both relative effect and observed outcome experience. Assumption: validated event and censoring records are available.

### 5.2 Secondary Outcomes

- [Provided] Secondary efficacy evaluation includes exercise capacity and other secondary/exploratory endpoints.
- [Provided] 6MWT and Borg assessments are scheduled at baseline and follow-up, with Week-26 endpoint assessments obtained before the morning dose.
- [Clarification Required] The exact exercise-capacity endpoint, other secondary endpoints, analysis visits, measurement units, favorable directions, and endpoint hierarchy must be specified; assessment names alone do not define statistical outcomes.
- [Proposed] Consider change in 6MWD from baseline to Week 26 as a candidate exercise-capacity endpoint, subject to confirmation. Rationale: this gives an interpretable functional contrast at a specified assessment time. Assumption: baseline and Week-26 distance measurements are intended for this comparison.
- [Clarification Required] The Borg scale version and whether its endpoint is a value, change, or categorical response must be confirmed; scale properties determine appropriate analysis.
- [Clarification Required] Rules for death, clinical deterioration, inability to walk, rescue therapy, and missing Week-26 assessments must be specified; these outcomes are not interchangeable with ordinary missed visits.

### 5.3 Analysis Methods

- [Proposed] Use an unstratified one-sided log-rank test for the primary randomized comparison, subject to confirmation of the sequential testing implementation. Rationale: this aligns the analysis with the sample-size test. Assumption: no superseding primary-test specification exists.
- [Proposed] Estimate the selexipag-to-placebo hazard ratio using a Cox model containing randomized treatment as the explanatory variable. Rationale: this provides a treatment-effect estimate on the planning scale. Assumption: proportional hazards is sufficiently reasonable for a single hazard-ratio summary.
- [Proposed] Present Kaplan–Meier curves with numbers at risk and appropriate censoring indicators; report median event-free survival only when estimable. Rationale: these show the observed time course without requiring proportional hazards. Assumption: censoring is sufficiently noninformative for these estimates.
- [Proposed] Assess proportional hazards using graphical diagnostics and treatment-related residual diagnostics. Rationale: marked time variation can make a single hazard ratio incomplete. Assumption: sufficient events and follow-up are available.
- [Proposed] If proportional hazards is questionable, supplement rather than replace the primary analysis with clearly exploratory time-varying treatment-effect summaries. Rationale: this characterizes nonproportional effects without silently changing the confirmatory test. Assumption: the supplementary model can be specified transparently.
- [Proposed] Use site-stratified survival analysis as a sensitivity analysis where estimable. Rationale: this examines sensitivity to the randomization stratification factor. Assumption: site-level event information supports estimation.
- [Clarification Required] Sparse-site handling, Cox tie handling, and any additional covariate adjustment require specification; these choices affect reproducibility and model stability.
- [Proposed] If Week-26 change in 6MWD is confirmed as an endpoint, analyze Week-26 distance with treatment and baseline distance in an ANCOVA model, expressing the treatment contrast as a baseline-adjusted difference. Rationale: baseline adjustment can improve precision. Assumption: the endpoint strategy and model residual behavior support a continuous-outcome analysis.
- [Clarification Required] Methods for remaining secondary endpoints cannot be finalized until their scales, timing, intercurrent-event strategies, and hierarchy are supplied; one generic model would not be appropriate for all possible endpoints.

### 5.4 Missing Data

- [Proposed] Report missingness by treatment, visit, endpoint, and reason, distinguishing death and inability to assess from administrative omissions. Rationale: different missingness mechanisms require different interpretation. Assumption: reasons are recorded or can be reconciled.
- [Proposed] For time-to-event analysis, use right-censoring at the last verified event-free time within the finalized endpoint observation period when subsequent status is unavailable. Rationale: this uses verified follow-up without inventing event times. Assumption: the censoring convention is compatible with the finalized estimand and is sufficiently noninformative.
- [Clarification Required] Specific censoring dates for withdrawal, loss to follow-up, treatment discontinuation, extension entry, and administrative cutoff must be defined; generic right-censoring principles do not determine these dates.
- [Proposed] Investigate sensitivity to informative loss to follow-up using alternative event-risk assumptions or inverse-probability-of-censoring methods when supported by the data. Rationale: the primary analysis may be sensitive to prognosis-related censoring. Assumption: sensitivity assumptions and required predictors can be specified credibly.
- [Proposed] For a confirmed continuous Week-26 endpoint, consider multiple imputation for ordinary missing measurements using randomized treatment, baseline outcome, and available earlier measurements. Rationale: this can incorporate observed predictors of missing outcomes. Assumption: missing at random is plausible conditional on included information.
- [Clarification Required] Death and other intercurrent events require an explicit endpoint strategy before imputation; imputing them as ordinary missing continuous measurements could change the clinical question.
- [Proposed] Add missing-not-at-random sensitivity analyses for continuous endpoints using prespecified departures from the primary imputation assumptions. Rationale: the missing-at-random assumption is not empirically verifiable. Assumption: clinically defensible departure ranges can be agreed.
- [Clarification Required] Imputation specifications, departure ranges, and sensitivity decision criteria must be finalized; otherwise these analyses would be vulnerable to outcome-driven selection.

### 5.5 Additional Analyses

- [Provided] Exploratory analysis areas include dose-response, pharmacoeconomics, PK, exploratory efficacy, and safety.
- [Clarification Required] Dose categories, exposure metrics, pharmacoeconomic instruments and perspectives, PK sampling and parameters, and exploratory efficacy definitions are not supplied; these analyses cannot be operationalized without them.
- [Proposed] Treat achieved-dose analyses as exploratory associations rather than randomized dose comparisons. Rationale: tolerated dose may reflect patient characteristics and treatment experience. Assumption: dose selection was not independently randomized.
- [Proposed] Present any subgroup analyses using treatment-by-subgroup interaction estimates and confidence intervals, without interpreting separate within-subgroup significance as evidence of heterogeneity. Rationale: interaction estimates address differences in treatment effect directly. Assumption: subgroups are defined before comparative analysis and contain adequate information.
- [Clarification Required] Subgroup variables, cut points, and their prespecified status must be supplied; post hoc selection can exaggerate apparent heterogeneity.
- [Proposed] Clearly distinguish prespecified analyses, sensitivity analyses, and post hoc analyses in reporting. Rationale: this supports appropriate interpretation of exploratory findings. Assumption: dated analysis specifications and amendment records are available.

### 5.6 Harms

- [Provided] Safety and tolerability are evaluated in both the randomized study and the open-label extension.
- [Provided] The open-label extension is uncontrolled.
- [Derived] The open-label extension alone cannot provide a randomized selexipag-versus-placebo safety comparison.
- [Proposed] Summarize adverse events, serious adverse events, deaths, and discontinuations attributed to adverse events by randomized-study exposure group, with separate extension summaries. Rationale: this distinguishes comparative safety from uncontrolled long-term experience. Assumption: event records and exposure attribution are available.
- [Proposed] Include event counts, numbers and percentages of affected patients, treatment duration, and exposure-adjusted rates where informative. Rationale: unequal exposure can affect crude event proportions. Assumption: exposure dates and event timing are sufficiently complete.
- [Proposed] Summarize dose reductions and interruptions associated with tolerability, and laboratory or vital-sign changes if collected. Rationale: these characterize tolerability beyond event incidence alone. Assumption: these assessments and reasons for dose changes are recorded.
- [Clarification Required] Adverse-event definitions, seriousness criteria, coding dictionary and version, severity and causality scales, treatment-emergent windows, and laboratory thresholds must be supplied; these determine classification and comparability.
- [Clarification Required] Safety follow-up rules and handling of events spanning randomized treatment, post-treatment observation, Treatment Extension, and open-label extension require specification; overlapping periods could otherwise cause omission or double counting.
- [Proposed] Interpret safety comparisons descriptively unless a separate inferential strategy is specified. Rationale: multiple event categories and potentially unequal exposure complicate unadjusted significance testing. Assumption: no confirmatory safety-testing plan has been established.

### 5.7 Software and References

- [Provided] Sample-size calculations used EAST 5.3 with the variance-under-alternative option.
- [Clarification Required] Statistical analysis software, versions, packages, and the implementation of sequential testing and confidence intervals are unspecified; these are required for reproducibility.
- [Proposed] Use validated analysis programs with independent checks of population counts, endpoint derivations, event totals, and primary results, retaining code, software versions, and random seeds where applicable. Rationale: this supports reproducibility and reduces programming error. Assumption: analysis datasets and execution environments can be archived.
- [Proposed] Maintain a controlled specification of endpoint derivations, censoring rules, model settings, and dataset versions alongside the final outputs. Rationale: this makes the analytical framework auditable. Assumption: specification and version-control procedures are available.

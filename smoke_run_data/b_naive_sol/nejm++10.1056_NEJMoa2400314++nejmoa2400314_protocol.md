# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** Acute ischemic stroke (AIS) produces neurologic impairment, disability, and mortality. This phase III study evaluates reteplase, a genetically engineered recombinant human tissue-type plasminogen activator derivative administered by bolus injection, against alteplase for AIS treated within 4.5 hours of symptom onset.

**[Provided]** The study evaluates noninferiority for excellent functional outcome while also assessing functional, neurologic, and safety outcomes.

### 1.2 Objectives

- **[Provided]** **P1—Primary objective:** Evaluate reteplase versus alteplase effectiveness for AIS within 4.5 hours, operationalized as the between-group difference in the proportion with modified Rankin Scale (mRS) 0–1 at day 90.
- **[Provided]** **P1 outcome:** Difference in the day-90 mRS 0–1 proportions between reteplase and alteplase.
- **[Provided]** **S1—Secondary objective:** Evaluate safety and secondary functional and neurologic outcomes, including favorable function, mRS distribution, National Institutes of Health Stroke Scale (NIHSS) improvement, Barthel Index, hemorrhage, adverse events (AEs), serious adverse events (SAEs), and death.
- **[Provided]** Exploratory objectives were not reported as a separately labelled objective.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a multicenter, prospective, randomized, open-label, blinded-endpoint-assessment, positive active-controlled, parallel-group phase III noninferiority trial in Chinese patients with AIS within 4.5 hours of onset. Allocation is 1:1 reteplase:alteplase.

**[Provided]** Thrombolysis must begin within 4.5 hours of last known well.

- **[Provided]** **Reteplase:** An 18 mg intravenous bolus followed by a second 18 mg intravenous bolus 30±5 minutes after completion of the first injection. Each injection lasts at least 2 minutes.
- **[Provided]** **Alteplase:** 0.9 mg/kg intravenously, maximum 90 mg; 10% is administered as a bolus within 1 minute, and the remainder is infused over 60 minutes.

**[Proposed]** Separate treatment-delivery personnel from endpoint assessors, restrict assessors’ access to treatment records, and document accidental disclosure. Rationale: preserve blinded endpoint assessment despite visibly different administration regimens. Assumption: operational separation is feasible.

**[Clarification Required]** Specify permitted and prohibited concomitant treatments, rescue-treatment rules, and routine post-thrombolysis management. These decisions affect participant safety, treatment comparability, and protocol-deviation classification.

### 2.2 Randomization

**[Provided]** An independent statistician generates random numbers using SAS 9.4 or higher. After eligibility is established, the investigator obtains allocation through an interactive web response system (IWRS).

**[Provided]** Random numbers assigned to withdrawn participants are retained and cannot be replaced or reused. Initial random-number seed parameters are retained.

**[Provided]** SAP v1.0 describes simple stratified randomization without naming factors. Final Protocol V2.2 specifies variable-block 1:1 randomization without describing stratification. No individual stratification factor is reported.

**[Clarification Required]** Reconcile the randomization descriptions and confirm the implemented algorithm, whether stratification was used, any factors and levels, and the block-size specification. This determines allocation-system validation and whether design factors require analytical adjustment.

**[Proposed]** Maintain allocation concealment until IWRS assignment and restrict access to block sizes, seeds, and the allocation list. Rationale: reduce allocation predictability. Assumption: IWRS permissions and audit trails support these controls.

### 2.3 Sample Size

**[Provided]** Planned enrollment is **1,412 participants**, comprising **706 per group**. The calculation targets the binary proportion with mRS 0–1 at day 90.

**[Provided]** Assumptions are an alteplase excellent-outcome proportion of **62.5%**, a true reteplase:alteplase efficacy risk ratio (RR) of **1.05**, a noninferiority margin of **0.93**, and one-sided alpha **0.025**. The assumed test demonstrates noninferiority when the lower RR confidence bound exceeds 0.93.

**[Derived]** These efficacy assumptions imply a reteplase excellent-outcome proportion of 65.625% and an absolute reteplase-minus-alteplase difference of 3.125 percentage points.

**[Provided]** The margin of 0.93 is based on a historical alteplase-versus-placebo lower 95% confidence limit for RR of 1.15, using a preservation factor of \(f=0.5\).

**[Provided]** Protocol V2.2 and SAP v1.0 specify **80% power** and approximately **15% dropout/non-adherence inflation**. SAP v1.1 instead specifies **85% power** and **3% dropout/non-adherence inflation**.

**[Clarification Required]** Reconcile the power and inflation assumptions and reproduce the calculation supporting 706 participants per group. Without this reconciliation, a single definitive sample-size justification cannot be established.

**[Provided]** No separate variability assumption or design-effect/clustering adjustment applies to the stated binary proportion/RR calculation. There is no event-count requirement for the primary endpoint.

**[Provided]** The safety rationale assumes symptomatic intracranial hemorrhage (sICH) at **1%** and death at **5%**, with **>99% probability** of observing at least one death or sICH. The 1:1 sample therefore targets efficacy noninferiority while providing substantial probability of observing key safety events.

**[Provided]** Original Protocol V1.0 planned Mehta–Pocock sample-size re-estimation conditional on interim efficacy of **50%–80%**. Protocol V2.2 does not retain that procedure, and SAP v1.0/v1.1 state that no interim efficacy analysis is planned.

### 2.4 Hypothesis Framework

**[Provided]** Let RR denote the day-90 mRS 0–1 rate in the reteplase group divided by that in the alteplase group. The primary hypotheses are \(H_0:RR\leq0.93\) versus \(H_1:RR>0.93\).

**[Provided]** Noninferiority is concluded at one-sided \(P<0.025\), or when the lower bound of the RR 95% confidence interval exceeds 0.93. Superiority is subsequently concluded if that lower confidence bound exceeds 1.

**[Derived]** The absolute difference specified in P1 and the RR used for hypothesis testing are distinct summaries of the same binary endpoint: \(RD=p_R-p_A\) and \(RR=p_R/p_A\), where \(p_R\) and \(p_A\) are the respective excellent-outcome probabilities.

**[Proposed]** Report both RR and absolute risk difference, while applying the supplied noninferiority and subsequent superiority rules to RR. Rationale: retain the objective’s absolute comparison without changing its specified inferential framework. Assumption: RR remains the governing hypothesis-test scale.

### 2.5 Statistical Interim Analyses

**[Provided]** The version-specific interim-analysis descriptions conflict: Protocol V1.0 contains the re-estimation procedure, Protocol V2.2 omits it, and both SAP versions specify no interim efficacy analysis.

**[Clarification Required]** Establish the controlling document and settle the interim-analysis policy before execution. If re-estimation is retained, define the meaning of “interim efficacy 50%–80%,” analysis timing, adaptation algorithm, sample-size limits, independent access arrangements, and type I error protection.

**[Proposed]** Pending reconciliation, do not perform an unplanned interim efficacy analysis or outcome-driven sample-size modification. Rationale: prevent an incompletely specified adaptation from compromising inference. Assumption: the later no-interim approach is intended unless formally amended.

**[Clarification Required]** Specify safety-monitoring responsibilities, access to comparative safety data, and any stopping or escalation rules. These are necessary for participant protection and cannot be inferred from the absence of efficacy interim analyses.

### 2.6 Timing of Analyses

**[Provided]** Final analysis occurs after the end of the entire trial and after database lock, protocol-violation identification, and treatment unblinding.

**[Provided]** Scheduled assessments are Screening/D1; 24 hours±2 hours; 72 hours±6 hours; D8±1 day; D31±3 days; and D91±7 days.

**[Provided]** NIHSS is assessed at baseline, 24 hours, and D8. mRS and Barthel Index are assessed at D31 and D91, with blinded endpoint evaluation at follow-up.

**[Clarification Required]** Confirm the time origin and how the nominal day-90 endpoint maps to the D91±7-day visit, including handling of multiple and out-of-window assessments. This is necessary for reproducible endpoint selection.

**[Clarification Required]** Define “treatment unblinding” in this open-label trial, including which endpoint and analysis personnel remain blinded and when their access changes. This matters for endpoint integrity and prospective analysis decisions.

**[Proposed]** Finalize the SAP, endpoint-selection rules, population definitions, and deviation classifications before comparative outcome review or release of treatment codes to blinded analysts. Rationale: limit outcome-dependent analytical choices. Assumption: an appropriate restricted-access review process is available.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The primary noninferiority significance level is one-sided 0.025, with the supplied decision rule expressed using the lower bound of a 95% RR confidence interval. Superiority follows successful noninferiority and requires that lower bound to exceed 1.

**[Proposed]** Generate the primary P value and confidence interval using the same estimation framework, including compatible pooling rules if imputation is used. Rationale: make the supplied P-value and confidence-bound criteria concordant. Assumption: the chosen implementation supports compatible tests and intervals.

**[Proposed]** Report secondary and exploratory comparisons with two-sided nominal 95% confidence intervals and clearly identify them as nonconfirmatory. Rationale: communicate uncertainty without implying unsupported study-wide error control. Assumption: no additional confirmatory testing hierarchy is approved.

**[Clarification Required]** Determine whether any secondary endpoint supports a confirmatory claim and, if so, specify its hierarchy and multiplicity adjustment. This affects the interpretation of secondary P values.

### 3.2 Protocol Deviations

**[Proposed]** Record deviations involving eligibility, treatment initiation, dose, injection/infusion timing, prohibited treatment, endpoint assessment, and assessor blinding. Classify their importance before comparative outcome review. Rationale: support transparent conduct assessment and reproducible sensitivity populations. Assumption: source records permit objective classification.

**[Clarification Required]** Approve the exact major-deviation definitions and per-protocol exclusions, including the handling of missed second reteplase doses, crossovers, and treatment-window violations. These decisions can materially affect a noninferiority conclusion.

**[Proposed]** Retain randomized participants in the intention-to-treat analysis despite deviations and provide deviation summaries by assigned treatment. Rationale: preserve the randomized comparison. Assumption: consent and applicable data-retention requirements permit analysis.

### 3.3 Analysis Populations

**[Clarification Required]** Confirm the governing primary analysis population and whether agreement between intention-to-treat and per-protocol results is required for noninferiority. Neither population definitions nor a concordance rule are supplied, and exclusions can change the estimated treatment effect.

**[Proposed]** Use all randomized participants, analyzed as assigned, as the primary intention-to-treat population. Rationale: preserve randomization and estimate the effect of treatment assignment. Assumption: randomized participants’ data may lawfully be retained and used.

**[Proposed]** Define a supportive per-protocol population using prospectively approved, clinically important deviations without selecting participants according to outcomes. Rationale: assess robustness to non-adherence in a noninferiority setting. Assumption: exclusions can be determined independently of comparative outcomes.

**[Proposed]** Define the safety population as participants receiving any study treatment, grouped by the initial study drug actually received, with mixed exposure explicitly flagged. Rationale: relate harms to exposure while maintaining interpretable denominators. Assumption: administration records identify initial and subsequent exposure.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Maintain a screening log with numbers assessed, eligible, consented, randomized, and not randomized, together with reasons for exclusion or nonparticipation. Rationale: describe selection and participant flow. Assumption: screening information can be collected under applicable privacy requirements.

**[Clarification Required]** Establish the available screening dataset and reporting period. Actual screening counts and exclusion frequencies are not supplied and must not be inferred.

### 4.2 Eligibility Criteria Summary

**[Provided]** Inclusion requires age **18–80 years**; WHO-defined AIS within **4.5 hours of last known well**; NIHSS **4–25 before thrombolysis**; agreement to contraception where applicable; ability to comply; and participant or guardian consent.

**[Provided]** Exclusions include non-ascertainable onset; weight **<45 or >120 kg**; pre-stroke **mRS≥2**; and NIHSS consciousness item **1a≥2**.

**[Provided]** Additional exclusions are hemorrhage/imaging/anticoagulation risks; uncontrolled blood pressure; out-of-range glucose; large infarction; important hepatic or other comorbidity; planned or received endovascular treatment; interfering treatments; recent trial participation; pregnancy/lactation; and investigator-determined barriers to compliance.

**[Clarification Required]** Supply operational definitions for hemorrhage and imaging risks, anticoagulation restrictions, blood-pressure and glucose limits, large infarction, hepatic and other comorbidities, interfering treatments, recent-trial lookback periods, and contraception requirements. These unspecified thresholds and durations are necessary for consistent eligibility decisions.

### 4.3 Recruitment

**[Provided]** Recruitment concerns Chinese patients with AIS in a multicenter study.

**[Clarification Required]** Specify participating centers, recruitment dates, site activation requirements, and ethics/consent oversight arrangements. These determine where and when enrollment may proceed and how recruitment performance will be assessed.

**[Proposed]** Monitor enrollment against the overall randomized target without replacing or reusing withdrawn participants’ random numbers. Rationale: distinguish enrollment accounting from retention while respecting allocation integrity. Assumption: IWRS and recruitment records can be reconciled.

### 4.4 Withdrawal and Follow-up

**[Proposed]** Distinguish treatment discontinuation, withdrawal from assessments, withdrawal of permission for further contact, and loss to follow-up. Continue scheduled assessments after treatment discontinuation when permission remains. Rationale: reduce avoidable outcome loss and distinguish its causes. Assumption: continued contact is consented and clinically feasible.

**[Proposed]** Record withdrawal dates, reasons, treatment exposure, last contact, and available vital status; use documented contact attempts for missed visits. Rationale: support participant-flow reporting and missing-data assessment. Assumption: authorized contact methods are available.

**[Clarification Required]** Define withdrawal procedures, permitted use of previously collected data, vital-status ascertainment permissions, and acceptable remote follow-up methods. These affect both participant rights and endpoint completeness.

### 4.5 Baseline Characteristics

**[Provided]** Baseline NIHSS is scheduled, and eligibility uses age, weight, pre-stroke mRS, consciousness assessment, and time from last known well.

**[Proposed]** Summarize available demographics, baseline NIHSS, pre-stroke function, weight, onset-to-treatment timing, relevant medical history, medications, and eligibility-related measurements by randomized group. Use counts/percentages and appropriate continuous summaries without baseline significance tests. Rationale: describe clinical comparability without testing chance imbalances. Assumption: these variables are collected reliably.

**[Clarification Required]** Finalize the baseline variable list, measurement definitions, and reference times. These are needed for consistent tables, covariate adjustment, and imputation.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The primary outcome is excellent functional outcome, defined as **mRS 0–1 at day 90**. P1 specifies the difference in its proportion between reteplase and alteplase; the governing noninferiority hypothesis uses their RR.

**[Proposed]** Define the primary estimand as the effect of randomized assignment on the probability of excellent function at the target follow-up, regardless of subsequent treatment discontinuation, crossover, or rescue treatment. Rationale: align the primary analysis with randomized assignment. Assumption: a treatment-policy approach is approved.

**[Proposed]** Classify verified death before the target assessment as failure to achieve excellent function rather than as a missing functional outcome. Rationale: death cannot represent mRS 0–1 under standard mRS interpretation. Assumption: death timing is verified and standard mRS scoring is adopted.

**[Clarification Required]** Approve endpoint ascertainment procedures, evaluator qualifications, visit-selection rules, and treatment of unavailable or invalid assessments. These determine the primary outcome assigned to each participant.

### 5.2 Secondary Outcomes

**[Provided]** Secondary outcomes comprise favorable function, mRS distribution, NIHSS improvement, Barthel Index, hemorrhage, AE/SAE outcomes, and death.

**[Provided]** Available assessment timing is NIHSS at baseline, 24 hours, and D8, and mRS/Barthel Index at D31 and D91.

**[Clarification Required]** Define favorable function, NIHSS improvement thresholds or change-score definitions, Barthel endpoints, and the exact timepoint associated with each secondary comparison. These are necessary to avoid introducing unprovided endpoint definitions.

**[Clarification Required]** Specify hemorrhage classifications, the sICH definition, safety observation windows, mortality horizons, and handling of death in non-mRS functional outcomes. These decisions determine safety event counts and the interpretation of survivor-based assessments.

### 5.3 Analysis Methods

**[Proposed]** Estimate the primary RR using an unadjusted modified Poisson model with log link, treatment indicator, and robust standard errors. Report the RR with a two-sided 95% confidence interval and the compatible one-sided test against RR=0.93. Rationale: estimate the required risk ratio directly rather than an odds ratio. Assumption: independent participant-level observations and adequate large-sample performance.

**[Proposed]** Report group-specific excellent-outcome proportions and the reteplase-minus-alteplase absolute risk difference with a 95% confidence interval. Rationale: quantify the absolute effect specified in P1. Assumption: the same population and missing-data strategy are used for both effect scales.

**[Proposed]** Prespecify handling of nonestimable or boundary estimates and validate the implementation before database lock; do not introduce automatic continuity corrections after examining results. Rationale: prevent data-dependent method selection. Assumption: boundary-capable alternative calculations can be specified if needed.

**[Proposed]** Analyze binary secondary endpoints using risks, risk differences, and RRs at their approved timepoints. Analyze the ordered mRS distribution using a proportional-odds model oriented so that the effect direction is explicit, and always display category frequencies. Rationale: match analyses to outcome scale. Assumption: proportional odds is reasonable for a common ordinal effect; otherwise that summary is interpreted cautiously.

**[Proposed]** For approved continuous NIHSS or Barthel comparisons, summarize their distributions and estimate between-group differences with robust uncertainty estimates, adjusting for baseline NIHSS and age where appropriate. Rationale: describe magnitude while accounting for baseline prognosis. Assumption: the approved endpoint definition supports continuous analysis and the adjustment variables are available.

**[Clarification Required]** Confirm whether implemented randomization factors must enter the primary model and finalize any adjustment specification before lock. Unresolved stratification prevents a definitive design-adjusted analysis specification.

### 5.4 Missing Data

**[Proposed]** Report missingness by treatment, endpoint, visit, and reason, distinguishing death from unavailable assessment. Rationale: identify differential ascertainment and inform sensitivity analyses. Assumption: missingness reasons and vital status are recorded.

**[Proposed]** For the proposed intention-to-treat primary analysis, multiply impute missing excellent-outcome status among participants not known to have died, using treatment, age, baseline NIHSS, and available earlier functional assessments. Use at least 100 imputations and pool log-RR estimates and variances using Rubin’s rules, with matching confidence intervals and tests. Rationale: retain randomized participants and reflect imputation uncertainty. Assumption: missingness is conditionally at random and the imputation model is adequately specified.

**[Proposed]** Conduct arm-specific tipping-point analyses, including missing reteplase outcomes assigned failure and missing alteplase outcomes assigned success, and the reverse configuration; also report observed-case results. Rationale: assess sensitivity to departures from the missing-at-random assumption, particularly for noninferiority. Assumption: these scenarios are stress tests rather than claims about the true missing outcomes.

**[Clarification Required]** Specify handling of missing baseline covariates, partially observed scales, secondary outcomes after death, and unavailable vital status. These situations require endpoint-specific rules and cannot safely be treated as interchangeable missing values.

### 5.5 Additional Analyses

**[Proposed]** Repeat the primary comparison in the approved per-protocol population and provide supportive covariate-adjusted estimates using baseline age, NIHSS, and confirmed design factors. Standardize adjusted risks to the randomized cohort when reporting adjusted RRs and risk differences. Rationale: assess robustness to adherence and prognostic imbalance. Assumption: covariates are available and models are adequately specified.

**[Proposed]** Evaluate exploratory treatment interactions with prespecified baseline age, NIHSS, and onset-to-treatment time, preferably retaining continuous information rather than selecting outcome-driven cutpoints. Rationale: explore heterogeneity without arbitrary subgroup construction. Assumption: sufficient data and variation are available; results are not confirmatory.

**[Proposed]** Examine center-related robustness only after reviewing center sizes and the implemented randomization structure. Rationale: assess whether pooling across centers obscures material variation. Assumption: a feasible prespecified model can be supported without excessive sparse-center parameters.

### 5.6 Harms

**[Provided]** Safety outcomes include hemorrhage, AEs, SAEs, and death. The sample-size safety assumptions are sICH at 1% and death at 5%.

**[Proposed]** Summarize participants with at least one event, total event counts, severity, seriousness, assessed relatedness, treatment discontinuations, and deaths by actual-treatment safety group. Present absolute risks and comparative risk estimates where estimable. Rationale: distinguish affected participants from recurrent events and quantify uncertainty. Assumption: event-level data and exposure are available.

**[Proposed]** Obtain timely clinical evaluation of suspected major bleeding or neurologic deterioration, and use blinded hemorrhage/death adjudication where feasible. Rationale: support participant protection and consistent event classification. Assumption: emergency care and appropriately independent reviewers are available.

**[Clarification Required]** Establish AE/SAE definitions, collection periods, coding dictionary/version, causality and severity rules, expedited reporting deadlines, imaging requirements, adjudication procedures, and safety escalation responsibilities. These are essential for consistent safety capture and reporting.

### 5.7 Software and References

**[Provided]** Random-number generation uses SAS 9.4 or higher.

**[Clarification Required]** Specify sample-size calculation software, the final analysis software and versions, procedures/packages, and any random seeds used for imputation or resampling. These details are required for reproducibility and reconciliation of the sample-size discrepancies.

**[Proposed]** Validate analysis datasets, endpoint derivations, population flags, and key inferential outputs through independent programming or equivalent documented quality control; archive executable code and software settings. Rationale: make the final results auditable and reproducible. Assumption: appropriate programming and review resources are available.

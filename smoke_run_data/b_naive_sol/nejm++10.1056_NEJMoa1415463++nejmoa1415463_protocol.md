# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

**[Provided]** IgA nephropathy (IgAN) is a common glomerulonephritis, and progressive renal failure occurs in a substantial proportion of clinically affected patients. This study evaluates whether adding immunosuppression to optimized, comprehensive supportive care improves clinically important renal outcomes in patients at risk for progression.

### 1.2 Objectives

- **[Provided]** **P1:** Evaluate the efficacy of immunosuppressive therapy added to comprehensive supportive therapy for inducing clinical remission in progressive IgAN. The corresponding outcome is clinical remission.
- **[Provided]** **P2:** Compare treatments for the number of patients experiencing GFR loss ≥15 mL/min.
- **[Provided]** Secondary objectives are not separately labelled, although secondary efficacy endpoints are referenced. No exploratory objectives are reported.
- **[Clarification Required]** The secondary efficacy endpoints are not enumerated. Their definitions, assessment times, and intended interpretations are needed before a complete endpoint-specific analysis plan can be finalized.

## 2\. Study Methods

### 2.1 Trial Design

**[Provided]** This is a randomized, prospective, multicenter, open-label, two-arm, parallel-group therapeutic trial with a 6-month run-in phase followed by a 36-month treatment/follow-up phase. Allocation is 1:1, with 74 patients planned per treatment group.

**[Provided]** All consented patients enter optimized supportive care during run-in:

- **[Provided]** Blood pressure target: <125/75 mmHg.
- **[Provided]** An ACE inhibitor is first-line treatment; an ARB is used if the ACE inhibitor is not tolerated.
- **[Provided]** Statin therapy is included.
- **[Provided]** Low-sodium counseling is provided. Patients with GFR <60 mL/min receive a protein-intake target of 0.8 g/kg/day.

**[Provided]** Randomization requires proteinuria >0.75 g/d after run-in. Proteinuria >3.5 g/d is identified as a run-in dropout condition.

**[Provided]** If GFR at week −1 is <90 mL/min, GFR loss during run-in must be ≤30%. Any run-in GFR loss is permitted if week −1 GFR is ≥90 mL/min.

- **[Provided]** **Treatment S:** Continue optimized supportive therapy.
- **[Provided]** **Treatment I:** Continue identical supportive care and add the GFR-dependent immunosuppressive regimen below.
- **[Provided]** **GFR ≥60 mL/min:** Methylprednisolone 1 g intravenously daily for 3 days at months 1, 3, and 5, plus prednisolone 0.5 mg/kg every 48 hours for 6 months.
- **[Provided]** **GFR 30–60 mL/min:** Cyclophosphamide 1.5 mg/kg/day for 3 months with tapered prednisolone, followed by azathioprine 1.5 mg/kg/day plus prednisolone through 3 years.
- **[Provided]** Vitamin D/calcium are recommended with corticosteroids. Cotrimoxazole pneumocystis prophylaxis and Mesna prophylaxis are recommended with cyclophosphamide.

**[Clarification Required]** The two immunosuppression ranges overlap at GFR exactly 60 mL/min. The assigned regimen at this boundary, the GFR measurement used for assignment, and whether subsequent GFR changes alter treatment must be specified to ensure reproducible treatment allocation.

**[Clarification Required]** The prednisolone starting dose, taper, maintenance schedule in the lower-GFR regimen, and treatment dose-adjustment or interruption rules are unspecified. These decisions are necessary for safe and consistent administration.

**[Clarification Required]** The reference measurements and calculation used to determine percentage GFR loss during run-in are unspecified. They are needed to apply the ≤30% eligibility rule consistently.

### 2.2 Randomization

**[Provided]** Randomization is central and web-based, using a PHP 5.2 tool and PostgreSQL database with minimization. The allocation ratio is 1:1, and the stratification factors are baseline GFR and baseline proteinuria.

**[Provided]** Blocking is not specified. Center is not a stratification variable because of small per-center sample sizes.

**[Clarification Required]** The minimization categories, factor weights, initial allocation procedure, tie-breaking rules, and any random component are unspecified. These details are needed to reproduce allocation and determine whether additional design-specific statistical considerations are required.

**[Proposed]** Release allocation only after eligibility confirmation and irrevocable registration, with an auditable allocation record. Rationale: this limits selection bias despite the open-label design. Assumption: the central system can enforce these controls.

### 2.3 Sample Size

- **[Provided]** Planned randomized enrollment is 148 patients: 74 per group.
- **[Provided]** The calculation concerns the first hierarchically ordered primary endpoint: full clinical remission at 3 years, analyzed as a binary proportion.
- **[Provided]** Remission under supportive therapy is assumed to be <5%; the numerical comparison used for planning is 5% versus 25% under combined treatment, an approximately 20-percentage-point difference.
- **[Provided]** Power is 80%, with a two-sided 5% significance level adjusted for two interim looks using O’Brien–Fleming monitoring.
- **[Provided]** The calculation uses a chi-square (F2) test with continuity correction. Stratification-factor distributions were unavailable; the unstratified calculation was considered conservative relative to the planned stratified logistic-regression analysis.
- **[Provided]** Dropout/non-adherence inflation is reported as 10%, increasing the sample from 60 to 74 patients per group, or 14 additional patients per group.
- **[Provided]** No required event count is specified. A separate variability assumption is not applicable to the binary-proportion calculation. No non-inferiority/equivalence margin or clustering design effect applies.
- **[Provided]** The assumptions are based on experience with initial IgAN presentations over preceding years. Calculation software is Addplan 3.1.
- **[Provided]** Sample-size re-estimation is not specified.

**[Derived]** Increasing 60 to 74 patients per group is a 23.3% increase over 60. A simple allowance for 10% loss from 60 evaluable patients would require approximately 67 randomized patients per group, not 74.

**[Clarification Required]** The relationship between the stated 10% allowance and the increase from 60 to 74 per group must be reconciled. The underlying calculation output is needed to distinguish attrition inflation from any additional sequential-design adjustment without changing the stated enrollment target.

### 2.4 Hypothesis Framework

**[Provided]** The two primary endpoints are described as independent and are tested hierarchically: first full clinical remission, then GFR loss ≥15 mL/min only if the first endpoint is significant.

**[Provided]** For each binary endpoint, the null hypothesis is equality of treatment-group rates versus a two-sided difference. For continuous secondary outcomes, the null hypothesis is equality of treatment-group means versus a two-sided difference.

**[Derived]** If the first primary endpoint is not significant under its applicable monitoring rule, the second primary endpoint cannot support a confirmatory conclusion within the stated hierarchy.

**[Clarification Required]** The meaning of “independent” is unspecified. It must be established whether this describes separate clinical endpoints or assumes statistical independence; that distinction matters for interpreting and implementing the monitoring framework.

### 2.5 Statistical Interim Analyses

**[Provided]** Two interim looks are incorporated using O’Brien–Fleming monitoring. The final analysis is the third stage, at information rate 1.00.

**[Clarification Required]** Interim information fractions, information definitions, numerical boundaries, and the exact O’Brien–Fleming implementation are unspecified. They are necessary to reproduce the intended overall two-sided 5% error control.

**[Clarification Required]** The interaction between interim testing and the endpoint hierarchy is unspecified, including when the second endpoint may be tested and whether it receives repeated testing opportunities. This must be resolved to avoid an unintended increase in false-positive probability.

**[Clarification Required]** Futility rules, safety stopping rules, authority to stop recruitment or treatment, and handling of data accrued after a stopping boundary are unspecified. These decisions affect trial conduct and final estimation.

**[Proposed]** Use an independent monitoring body to review unblinded interim efficacy and safety results, with access restricted to designated personnel. Rationale: this limits operational bias in an open-label trial. Assumption: an independent review structure can be established.

### 2.6 Timing of Analyses

**[Provided]** Final efficacy analysis occurs at the third stage/information rate 1.00 after patients are evaluable at 36 months. The final report is to be submitted within one year after study end.

**[Provided]** Six run-in visits occur over months −6 to −0.25.

**[Provided]** Sixteen study-phase visits occur at months 0, 0.5, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36. Urine and renal assessments are scheduled at baseline and selected follow-up visits, including month 36.

**[Clarification Required]** Data-cutoff rules, database-lock requirements, visit windows, and selection of measurements when multiple assessments fall within a window are unspecified. These determine which observations enter each analysis.

**[Clarification Required]** The full urine/renal assessment schedule and arrangements for the month-5 steroid administration are needed because month 5 is not among the sixteen listed study-phase visits.

**[Proposed]** Finalize the analysis plan and resolve endpoint definitions before reviewing comparative outcome results; lock the analysis database after eligibility, endpoint, and safety queries are resolved. Rationale: this reduces outcome-driven decisions. Assumption: unresolved specifications can be settled without access to comparative results.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** Confirmatory testing is two-sided at an overall 5% significance level, with O’Brien–Fleming adjustment for two interim looks and hierarchical ordering of the primary endpoints.

**[Proposed]** Report confirmatory treatment-effect confidence intervals using a method compatible with the finalized sequential testing procedure, alongside clearly identified descriptive estimates. Rationale: ordinary fixed-sample intervals alone do not reflect repeated testing. Assumption: the complete monitoring procedure is specified before implementation.

**[Proposed]** Treat secondary and additional analyses as supportive unless a separate multiplicity strategy is prospectively established. Rationale: no confirmatory secondary-endpoint testing family is specified. Assumption: confirmatory claims remain confined to the supplied primary hierarchy.

### 3.2 Protocol Deviations

**[Clarification Required]** Major-deviation definitions and adherence thresholds are unspecified. They are needed to classify eligibility violations, treatment departures, prohibited medication use, and missed assessments consistently.

**[Proposed]** Record deviations by type, timing, treatment group, and potential effect on treatment delivery or endpoint ascertainment; classify them before comparative outcome review. Rationale: prospective classification reduces selective exclusions. Assumption: sufficient source documentation is available.

**[Proposed]** Do not exclude randomized participants from the primary analysis solely because of a protocol deviation. Rationale: retaining assignment preserves the randomized comparison. Assumption: an intention-to-treat treatment-policy approach is adopted.

### 3.3 Analysis Populations

**[Proposed]** Define the primary intention-to-treat population as all randomized participants, analyzed according to assigned treatment. Rationale: this estimates the effect of assignment while preserving randomization. Assumption: follow-up is sought regardless of treatment adherence or discontinuation.

**[Proposed]** Define a supportive per-protocol population using prospectively specified eligibility and adherence criteria. Rationale: it can assess robustness to important treatment departures but does not replace the randomized comparison. Assumption: criteria can be defined without reviewing treatment effects.

**[Proposed]** Summarize safety both by randomized assignment and by actual immunosuppressive exposure. Rationale: assignment supports comparison, whereas exposure helps describe treatment-associated harms. Assumption: treatment receipt, crossover, and exposure dates are recorded accurately.

**[Clarification Required]** The handling of participants randomized in error and participants with no post-randomization measurements requires specification. These cases affect analysis denominators and missing-data procedures.

## 4\. Trial Population

### 4.1 Screening Data

**[Proposed]** Maintain a screening and participant-flow log showing screening, consent, run-in entry, run-in completion, randomization, treatment receipt, follow-up completion, and reasons for nonprogression. Rationale: run-in selection is important to interpreting the randomized population. Assumption: screening information can be collected under applicable consent and privacy arrangements.

**[Proposed]** Distinguish failure of run-in eligibility from withdrawal, treatment discontinuation, and loss to follow-up. Rationale: these events have different implications for recruitment and analysis. Assumption: their dates and reasons are available.

### 4.2 Eligibility Criteria Summary

**[Provided]** Inclusion criteria are:

- **[Provided]** Men or women aged 18–70 years.
- **[Provided]** Nephropathologist-confirmed primary mesangioproliferative IgAN.
- **[Provided]** Proteinuria >0.75 g/d within 12 weeks before or at run-in start.
- **[Provided]** At least one additional ESRD risk factor: hypertension, defined as ambulatory blood pressure >140/90 mmHg or antihypertensive use; or impaired renal function, defined as creatinine clearance or estimated GFR <90 mL/min.

**[Provided]** Exclusion criteria are:

- **[Provided]** Known study-drug allergy or intolerance, except ACE-inhibitor intolerance permitting ARB use.
- **[Provided]** Pregnancy, breastfeeding, or inadequate contraception.
- **[Provided]** Contraindication to immunosuppression: acute or chronic infection, including hepatitis/HIV; malignancy; leukocytopenia/thrombocytopenia; prednisolone/azathioprine allergy; gastrointestinal bleeding/ulcer; or need for permanent immunosuppression.
- **[Provided]** Prior immunosuppression.
- **[Provided]** Rapidly progressive/crescentic IgAN involving >50% of glomeruli, or minimal-change IgAN variants.
- **[Provided]** Secondary IgAN or another chronic renal disease.
- **[Provided]** GPT >3-fold normal.
- **[Provided]** Mean of three creatinine-clearance measurements <30 mL/min.
- **[Provided]** Alcohol/drug abuse.
- **[Provided]** Mental incapacity or expected noncompliance.
- **[Provided]** Concurrent/recent trial participation.
- **[Provided]** Dependency.
- **[Provided]** Sponsor/investigator employment.
- **[Provided]** Legal institutional commitment.

**[Derived]** Combining the supplied post-run-in proteinuria rules gives a randomization-compatible range of >0.75 to ≤3.5 g/d, subject to the other requirements.

**[Clarification Required]** Operational definitions are needed for recent trial participation, dependency, adequate contraception, relevant laboratory cytopenia thresholds, and the timing of eligibility measurements. These definitions affect consistent eligibility decisions across centers.

### 4.3 Recruitment

**[Provided]** Recruitment duration was extended by one year to October 2014.

**[Clarification Required]** Recruitment start, participating-center details, expected screening/run-in attrition, and recruitment procedures are unspecified. They are needed for an operational recruitment plan; no total screening target can be inferred from 148 randomized participants.

**[Proposed]** Obtain required ethics approvals and written informed consent before study-specific procedures. Rationale: prospective interventional research requires participant protection and authorization. Assumption: these procedures will be implemented locally.

### 4.4 Withdrawal and Follow-up

**[Provided]** Proteinuria >3.5 g/d is a run-in dropout condition.

**[Clarification Required]** The consequences of run-in dropout for subsequent clinical follow-up and data collection are unspecified. “Dropout” must be distinguished from loss to follow-up and consent withdrawal.

**[Proposed]** After randomization, continue scheduled outcome follow-up after treatment discontinuation or crossover unless the participant withdraws permission. Rationale: continued ascertainment supports the proposed intention-to-treat analysis. Assumption: follow-up without assigned treatment is acceptable to participants and centers.

**[Proposed]** Record treatment discontinuation, study withdrawal, consent restrictions, loss to follow-up, and their reasons separately. Rationale: each has different analytical implications. Assumption: documentation remains permissible after the event.

### 4.5 Baseline Characteristics

**[Provided]** Baseline GFR and baseline proteinuria are randomization stratification factors.

**[Clarification Required]** The precise definition of randomized baseline, including selection among run-in and week −1 measurements, is unspecified. This affects covariate adjustment and calculation of subsequent GFR loss.

**[Proposed]** Describe randomized groups using available demographic, renal, blood-pressure, and treatment characteristics, including age, sex, GFR, proteinuria, and supportive therapies. Rationale: these characterize the study population and clinical comparability. Assumption: these variables are collected.

**[Proposed]** Report continuous variables using distribution-appropriate summaries and categorical variables as counts and percentages, without baseline significance tests. Rationale: descriptive summaries characterize chance imbalance without implying a test of successful randomization. Assumption: no outcome-driven selection of baseline variables occurs.

## 5\. Analysis

### 5.1 Primary Outcomes

**[Provided]** **P1:** Full clinical remission at 3 years, represented as a binary remission outcome.

**[Clarification Required]** The clinical and laboratory criteria for full remission, required duration or confirmation, and acceptable assessment window are unspecified. Without them, remission cannot be classified reproducibly.

**[Provided]** **P2:** Number of patients with GFR loss ≥15 mL/min, compared between treatments.

**[Clarification Required]** The GFR measurement method, reference assessment, endpoint time window, confirmation requirements, and treatment of transient losses are unspecified. These decisions determine the binary P2 classification.

**[Proposed]** Assess P2 as loss from randomized baseline to the 36-month assessment, subject to an agreed measurement window. Rationale: this aligns the endpoint with the supplied follow-up horizon. Assumption: the intended endpoint is final change rather than time to any threshold crossing.

**[Clarification Required]** Death, kidney replacement therapy, transplantation, rescue immunosuppression, and treatment discontinuation require endpoint-specific handling rules. These events may prevent measurement or change its clinical meaning and cannot automatically be treated as ordinary missing observations.

### 5.2 Secondary Outcomes

**[Provided]** Secondary efficacy endpoints are referenced, but their names, definitions, and assessment times are not supplied.

**[Clarification Required]** The complete secondary endpoint list, measurement scales, timepoints, and any ordering must be specified. Endpoint-specific hypotheses, models, and missing-data rules cannot otherwise be finalized.

**[Proposed]** Prepare an endpoint specification for each secondary outcome covering its clinical meaning, calculation, units, assessment window, analysis population, and model. Rationale: this prevents inconsistent post hoc definitions. Assumption: the intended endpoint list can be recovered or prospectively agreed.

### 5.3 Analysis Methods

**[Provided]** The planned stratified analysis underlying the remission sample-size rationale is logistic regression.

**[Proposed]** Fit a logistic-regression model for remission with assigned treatment and the baseline GFR and proteinuria stratification factors. Rationale: this implements the stated analysis approach while accounting for allocation factors. Assumption: their coding is specified before comparative analysis.

**[Clarification Required]** The functional forms and category boundaries for baseline GFR and proteinuria are unspecified. They affect model specification and must be aligned with, or explicitly distinguished from, the minimization scheme.

**[Proposed]** Report each group’s remission count, denominator, and proportion, together with the adjusted treatment odds ratio and a model-standardized absolute risk difference. Rationale: relative and absolute effects provide complementary clinical interpretation. Assumption: the fitted model supports stable estimation.

**[Proposed]** Analyze the GFR-loss binary endpoint using the same adjustment factors and analogous summaries, applying the supplied hierarchical gate. Rationale: a consistent binary-outcome framework facilitates interpretation. Assumption: P2 is defined as a participant-level binary outcome at the agreed assessment time.

**[Proposed]** Prespecify a penalized logistic-regression fallback for separation or nonconvergence and establish its compatibility with sequential testing before use. Rationale: sparse remission counts may destabilize ordinary logistic regression. Assumption: an appropriate implementation and monitoring calibration are available.

**[Proposed]** For any confirmed continuous secondary endpoint, consider baseline-adjusted linear regression with treatment and randomization factors; use a longitudinal model when repeated measurements are the intended target. Rationale: model choice should match the endpoint and account for prognostic baseline measurements. Assumption: the relevant measurements exist and model diagnostics are acceptable.

**[Proposed]** Check model convergence, influential observations, functional forms, and relevant distributional assumptions, documenting any prespecified corrective analysis. Rationale: model-based estimates require adequate fit. Assumption: diagnostics are interpreted without changing the endpoint or confirmatory hierarchy.

### 5.4 Missing Data

**[Clarification Required]** No missing-outcome strategy or primary estimand is fully specified. The protocol must distinguish unavailable measurements from outcomes affected by death or renal replacement therapy before selecting an analysis method.

**[Proposed]** Summarize missingness by treatment, endpoint, visit, and documented reason, separately identifying intercurrent events. Rationale: the amount and pattern of missingness inform interpretation and sensitivity analyses. Assumption: reasons are recorded reliably.

**[Proposed]** For missing measurements not assigned an outcome by an agreed intercurrent-event rule, use multiple imputation incorporating treatment, baseline GFR, baseline proteinuria, and available longitudinal renal measurements. Rationale: this uses observed predictors rather than discarding incomplete cases. Assumption: missingness is conditionally at random given the imputation variables and the imputation model is compatible with endpoint definitions.

**[Proposed]** Conduct missing-not-at-random sensitivity analyses using clinically interpretable departures from the imputation assumptions, including tipping-point assessment where feasible. Rationale: the primary missingness assumption is not empirically verifiable. Assumption: clinically plausible departures can be specified before treatment-effect review.

**[Proposed]** Present complete-case analyses as supportive rather than automatically definitive. Rationale: complete-case results can be biased when observation depends on prognosis. Assumption: sufficient observed outcomes remain for meaningful comparison.

### 5.5 Additional Analyses

**[Provided]** No exploratory objectives are reported.

**[Proposed]** If undertaken, label per-protocol, alternative endpoint-window, and alternative missing-data analyses as sensitivity analyses rather than new confirmatory tests. Rationale: these assess robustness without expanding the primary claims. Assumption: their specifications are fixed before comparative results are reviewed.

**[Proposed]** If clinically justified, explore treatment-effect heterogeneity by baseline GFR and proteinuria using treatment-by-factor interactions rather than separate within-subgroup significance claims. Rationale: these factors influence allocation and renal prognosis. Assumption: categories are prespecified and the limited sample size is acknowledged; findings remain exploratory.

**[Clarification Required]** No center-effect model is supplied. Any center-adjusted sensitivity analysis requires center-size information and a prespecified approach, particularly because small per-center samples motivated omission of center from stratification.

### 5.6 Harms

**[Provided]** Corticosteroid-associated vitamin D/calcium and cyclophosphamide-associated cotrimoxazole and Mesna prophylaxis are recommended.

**[Clarification Required]** Adverse-event definitions, grading, collection windows, expedited reporting procedures, monitoring frequency, and treatment-specific safety stopping thresholds are unspecified. These are necessary for a complete safety plan.

**[Proposed]** Collect adverse events and serious adverse events with onset, duration, severity, seriousness, relationship assessment, action taken, and outcome, covering run-in and randomized follow-up. Rationale: this supports assessment of both supportive-care and immunosuppressive harms. Assumption: the final reporting windows and collection procedures are approved.

**[Proposed]** Include targeted surveillance for infection, hematologic and hepatic abnormalities, and corticosteroid-related complications. Rationale: these are clinically relevant to the administered drug classes. Assumption: appropriate clinical and laboratory monitoring can be implemented; exact schedules remain to be specified.

**[Proposed]** Summarize participants affected and event counts by treatment and seriousness, alongside exposure duration, discontinuations due to adverse events, and deaths. Rationale: participant-level risk and recurrent-event burden provide different safety information. Assumption: event and exposure records are sufficiently complete.

### 5.7 Software and References

**[Provided]** Sample-size calculations use Addplan 3.1. Central randomization uses a PHP 5.2 tool with a PostgreSQL database.

**[Clarification Required]** Final analysis software, versions, packages, and the implementation used for sequential boundaries and adjusted inference are unspecified. These details are needed for reproducibility.

**[Proposed]** Use validated statistical software with version-controlled programs, reproducible analysis datasets, and independent checks of primary endpoint derivation and confirmatory analyses. Rationale: these controls reduce programming and implementation errors. Assumption: the necessary technical resources are available.

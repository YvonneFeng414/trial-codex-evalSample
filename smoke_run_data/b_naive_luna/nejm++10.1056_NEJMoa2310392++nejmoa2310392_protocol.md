# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

- [Provided] The trial evaluates whether IV tenecteplase improves clinical outcomes versus placebo in imaging-selected acute ischemic stroke (AIS) presenting 4.5–24 hours after last-known-well time.
- [Provided] The rationale is to achieve earlier reperfusion in patients with salvageable tissue and ICA/MCA occlusion, including patients needing transfer for endovascular therapy (EVT).

### 1.2 Objectives

- [Provided] **Primary objective (P1):** Compare tenecteplase with placebo using ordinal Day-90 modified Rankin Scale (mRS). The primary outcome is ordinal Day-90 mRS.
- [Provided] **Secondary objective (S1):** Evaluate efficacy using Day-90 functional independence, angiographic reperfusion, NIHSS, Barthel Index (BI), Glasgow Outcome Scale (GOS), 24-hour reperfusion and 24-hour recanalization; evaluate safety using symptomatic intracranial hemorrhage (sICH), adverse events, mortality, and PH2.
- [Provided] **Exploratory objective (S2):** Evaluate final infarct volume/growth, mRS subgroups, outcomes when thrombectomy is not performed, 30-day readmission, one-pass EVT, Neuro-QoL, and Day-90 survival.

## 2\. Study Methods

### 2.1 Trial Design

- [Provided] This is a Phase III, prospective, double-blind, randomized, placebo-controlled trial in imaging-eligible patients with AIS presenting 4.5–24 hours after last-known-well time and ICA or MCA (M1/M2) occlusion.
- [Provided] Patients are allocated 1:1 to tenecteplase or placebo.
- [Provided] Both groups receive guideline-based standard care. ICA/M1 patients may receive adjuvant EVT if guideline criteria are met.
- [Provided] Tenecteplase is administered as 0.25 mg/kg IV, maximum 25 mg, in one bolus over 5 seconds.
- [Provided] Placebo is administered as one bolus injection over 5 seconds.
- [Clarification Required] The specific standard-care guidelines and EVT eligibility criteria are not identified; specifying them matters for consistent treatment and interpretation of outcomes.

### 2.2 Randomization

- [Provided] IWRS assigns a treatment kit and randomizes eligible, consented patients; treatment is to be given as soon as possible.
- [Provided] Randomization is 1:1 using permuted blocks to provide approximately 1:1 balance within each stratum.
- [Provided] Stratification factors are age ≤70/>70 years; occlusion ICA/M1 versus M2; baseline NIHSS ≤15/>15; and ECC versus nECC.
- [Clarification Required] ECC and nECC are not defined; their meanings and assignment rules are needed to implement stratification consistently.
- [Clarification Required] Details of who is blinded, how blinding is maintained, and procedures for emergency unblinding are not supplied; these matter for operational conduct and bias control.

### 2.3 Sample Size

- [Provided] Planned enrollment is 456 patients, approximately 228 per group; 432 evaluable patients are stated after 5% dropout.
- [Provided] The sample-size outcome is Day-90 ordinal mRS with seven levels (0–6).
- [Provided] Assumed control-arm mRS 0–6 distribution: 13%, 13%, 12%, 14%, 18%, 12%, 18%.
- [Provided] Assumed treatment-arm mRS 0–6 distribution: 17%, 20%, 16%, 15%, 13%, 7%, 12%.
- [Provided] The target effect is a common odds ratio of at least 1.76 for tenecteplase versus placebo.
- [Provided] The variability assumption is based on the assumed ordinal mRS distributions; alternative historical scenarios gave >99% and >88% power.
- [Provided] The significance level is two-sided 0.049 after adjustment for one efficacy interim analysis, and power is at least 90%.
- [Provided] The sample-size calculation assumed a Wilcoxon–Mann–Whitney test.
- [Provided] The design is not event-driven; a required number of events is not applicable.
- [Provided] The design is for superiority; a non-inferiority/equivalence margin is not applicable.
- [Provided] Dropout inflation is 5%; a design effect/clustering adjustment is not applicable because this is an individually randomized trial with no cluster design.
- [Provided] The mRS distribution assumptions and alternative scenarios were derived from prior stroke studies.
- [Provided] Sample-size re-estimation or amendments are not specified.
- [Provided] The sample-size software is EAST 6.4.1.
- [Provided] The stated rationale is that 456 patients provide 90% power to detect the specified mRS distribution difference after 5% dropout.
- [Derived] Exactly 5% dropout from 456 corresponds to 433.2 expected evaluable patients, whereas 432 evaluable patients would represent approximately 5.3% fewer than 456.
- [Clarification Required] Confirm whether 432 is the intended evaluable target or whether the 5% dropout assumption should determine that target; the distinction affects the enrollment and power assumptions.

### 2.4 Hypothesis Framework

- [Provided] All efficacy endpoints are assessed for superiority.
- [Provided] For the primary endpoint, the null hypothesis is common odds ratio = 1 versus a two-sided alternative of common odds ratio not equal to 1.
- [Provided] The odds ratio represents the odds of lower (better) mRS for tenecteplase versus placebo.
- [Clarification Required] The supplied primary hypothesis specifies a common odds ratio, while the sample-size calculation assumes a Wilcoxon–Mann–Whitney test; confirm the primary test/model and how it will align with the hypothesis and calculation.

### 2.5 Statistical Interim Analyses

- [Provided] One efficacy interim analysis is included in the adjustment underlying the two-sided significance level of 0.049.
- [Clarification Required] The interim timing, data cutoff, analysis population, stopping boundaries, decision rules, and oversight arrangements are not specified; these are needed to control type I error and govern trial conduct.
- [Proposed] Prespecify an interim monitoring plan, including the analysis timing, boundary or alpha-spending method, and any stopping rules, before access to interim efficacy results. Rationale: a prespecified plan supports error control and consistent decisions. Assumption: the stated 0.049 level is intended to account for the interim analysis.

### 2.6 Timing of Analyses

- [Provided] Final analysis is planned after all patients complete or discontinue, all data are in the database, and the database is locked.
- [Provided] 24-hour imaging and NIHSS assessments are scheduled at 18–30 hours.
- [Provided] 72–96-hour NIHSS assessments are scheduled at 60–96 hours; imaging is scheduled at 60–120 hours.
- [Provided] Day 5 mRS/GOS/BI assessments are scheduled at 4–6 days.
- [Provided] Day 30 clinical outcomes are scheduled at 15–60 days.
- [Provided] Day 90 clinical outcomes are scheduled at 61–120 days.
- [Clarification Required] The exact timing and visit windows for each individual secondary and exploratory outcome are not fully specified; confirming them is necessary for consistent endpoint ascertainment.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

- [Provided] The primary sample-size calculation uses a two-sided significance level of 0.049 after adjustment for one efficacy interim analysis.
- [Provided] The primary hypothesis is two-sided, and efficacy endpoints are assessed for superiority.
- [Proposed] Report effect estimates with confidence intervals and p-values, with inferential decisions using the prespecified interim-adjusted procedure. Rationale: this communicates both magnitude and uncertainty while respecting the stated alpha adjustment. Assumption: the final testing procedure will be defined in the interim analysis plan.
- [Clarification Required] The confidence-interval level and the exact relationship between interim monitoring and the final significance threshold are not specified; these are needed for interpretable, error-controlled inference.

### 3.2 Protocol Deviations

- [Clarification Required] Criteria for major and minor protocol deviations and the rules for excluding patients from any analysis population are not supplied; they matter for reproducible population definitions and interpretation.
- [Proposed] Record deviations prospectively and classify their importance using prespecified rules before treatment-group results are reviewed. Rationale: this reduces outcome-informed classification. Assumption: deviation review can be conducted without knowledge of comparative outcomes.

### 3.3 Analysis Populations

- [Clarification Required] The analysis populations are not specified; their definitions affect which patients contribute to efficacy and safety conclusions.
- [Proposed] Define the primary efficacy population as all randomized patients analyzed according to randomized assignment. Rationale: this preserves the randomized comparison. Assumption: the primary estimand is the effect of assignment to tenecteplase versus placebo.
- [Proposed] Define a safety population as randomized patients who receive any amount of study bolus, analyzed according to treatment received. Rationale: safety summaries should reflect exposure. Assumption: study-bolus receipt can be reliably documented.
- [Proposed] Define any per-protocol population and its exclusions prospectively, and use it only for supportive analyses. Rationale: prespecification limits post hoc selection. Assumption: a per-protocol analysis is considered useful in addition to the randomized comparison.

## 4\. Trial Population

### 4.1 Screening Data

- [Clarification Required] Screening variables, reasons for screen failure, and the intended screening denominator are not specified; these are needed to describe recruitment and assess how the randomized population arose.
- [Proposed] Maintain a screening record with eligibility disposition and a categorized reason for non-enrollment. Rationale: this supports transparent reporting of participant flow. Assumption: screening information may be collected for all screened patients under applicable consent and privacy procedures.

### 4.2 Eligibility Criteria Summary

- [Provided] The trial population is imaging-eligible AIS presenting 4.5–24 hours after last-known-well time with ICA or MCA (M1/M2) occlusion.
- [Provided] Inclusion criteria are pre-stroke mRS 0–2; NIHSS ≥5 both at baseline and immediately pre-randomization; qualifying CTA/MRA plus CTP/MRP target mismatch with core <70 mL, ratio ≥1.8, and mismatch ≥15 mL; and capacity to comply.
- [Provided] Exclusion criteria are bleeding/coagulopathy/anticoagulants; prior thrombolysis; relevant intracranial pathology; uncontrolled hypertension; glucose extremes; prior recent stroke/surgery; pregnancy; and prohibitive imaging findings.
- [Clarification Required] Specific definitions and thresholds for the listed exclusion categories, including uncontrolled hypertension, glucose extremes, recent stroke/surgery, and prohibitive imaging findings, are not supplied; they are needed for consistent eligibility decisions.
- [Clarification Required] Imaging acquisition, mismatch calculation, image-reading procedures, and the meaning of “qualifying” CTA/MRA and CTP/MRP are not specified; these determine whether the stated imaging thresholds are applied consistently.
- [Clarification Required] No age eligibility limit is supplied; the age strata alone do not establish whether any ages are excluded.
- [Clarification Required] The inclusion criteria refer to capacity to comply but do not specify how that capacity is assessed; a consistent assessment rule is needed.

### 4.3 Recruitment

- [Clarification Required] Recruitment sites, geography, recruitment dates, and recruitment procedures are not supplied; these affect operational planning and the population to which results may apply.
- [Proposed] Track enrollment against the planned total of 456 and report participant disposition by randomized group. Rationale: this supports monitoring of recruitment and clear accounting of participants. Assumption: the planned total remains unchanged.

### 4.4 Withdrawal and Follow-up

- [Provided] Final analysis is to occur after all patients complete or discontinue.
- [Clarification Required] Withdrawal criteria, withdrawal procedures, follow-up after treatment discontinuation, and whether replacement enrollment is permitted are not specified; these decisions affect follow-up completeness and analysis populations.
- [Proposed] Seek outcome follow-up after study-treatment discontinuation when permitted by the participant’s consent and applicable procedures. Rationale: retaining outcome data can reduce missing endpoint information. Assumption: continued follow-up is permissible and consistent with participant consent.

### 4.5 Baseline Characteristics

- [Provided] Randomization stratification uses age ≤70/>70 years, occlusion ICA/M1 versus M2, baseline NIHSS ≤15/>15, and ECC versus nECC.
- [Clarification Required] The baseline assessment schedule and full set of baseline variables to be collected are not specified; this matters for describing the enrolled population and planning adjusted analyses.
- [Proposed] Summarize baseline characteristics by randomized group using descriptive statistics, without using baseline significance tests to determine the primary model. Rationale: descriptive summaries characterize group comparability without conditioning the analysis on chance imbalances. Assumption: baseline measurements are available for the variables selected for collection.

## 5\. Analysis

### 5.1 Primary Outcomes

- [Provided] The primary outcome is ordinal Day-90 mRS, comparing tenecteplase with placebo; the scale has seven levels (0–6) for the sample-size calculation.
- [Provided] Day-90 clinical outcomes are assessed at 61–120 days.
- [Provided] The primary hypothesis concerns the common odds of lower (better) mRS for tenecteplase versus placebo.
- [Clarification Required] The exact endpoint ascertainment method, assessor procedures, and handling of assessments outside the Day-90 window are not supplied; these affect outcome comparability and analysis.

### 5.2 Secondary Outcomes

- [Provided] Secondary outcomes are Day-90 functional independence, angiographic reperfusion, NIHSS, BI, GOS, 24-hour reperfusion, 24-hour recanalization, sICH, adverse events, mortality, and PH2.
- [Provided] Exploratory outcomes are final infarct volume/growth, mRS subgroups, outcomes when thrombectomy is not performed, 30-day readmission, one-pass EVT, Neuro-QoL, and Day-90 survival.
- [Clarification Required] Definitions, scales, event windows, analysis denominators, and ascertainment methods for these outcomes are not fully specified; they are needed to make endpoint analyses reproducible.
- [Clarification Required] The cutoffs defining functional independence and mRS subgroups, and the definition of one-pass EVT, are not supplied; these choices determine endpoint classification.
- [Clarification Required] The criteria and analysis population for outcomes when thrombectomy is not performed are not specified; these are necessary because that subgroup may be defined after randomization.
- [Clarification Required] The assessment timing for Neuro-QoL, final infarct volume/growth, and 30-day readmission is not specified; timing determines which observations contribute to these outcomes.

### 5.3 Analysis Methods

- [Proposed] Analyze the primary ordinal mRS outcome using a proportional-odds ordinal logistic model that estimates the common odds ratio for lower (better) mRS with tenecteplase versus placebo. Rationale: this directly represents the stated common-odds-ratio hypothesis. Assumption: the proportional-odds model is appropriate for the outcome.
- [Proposed] Include randomized treatment and the randomization stratification factors in the primary model, using the prespecified categories. Rationale: this accounts for the design stratification. Assumption: ECC/nECC and all stratum assignments are defined and available for analysis.
- [Proposed] Evaluate the proportional-odds assumption and prespecify a suitable alternative if it is not tenable. Rationale: violation could make a single common odds ratio misleading. Assumption: model diagnostics and an alternative analysis can be specified before unblinding.
- [Proposed] Use a two-sided test of the primary null hypothesis at the interim-adjusted significance level, with an estimated odds ratio greater than 1 indicating odds favoring lower mRS for tenecteplase. Rationale: this follows the stated hypothesis and direction of benefit. Assumption: the final alpha allocation is confirmed in the interim analysis plan.
- [Proposed] Report the Wilcoxon–Mann–Whitney analysis as a supportive analysis of ordinal mRS. Rationale: it is the test assumed for the sample-size calculation. Assumption: its role is supportive unless the primary test is clarified otherwise.
- [Proposed] Analyze binary outcomes with an appropriate regression model and report group-specific estimates and between-group contrasts; analyze continuous outcomes with a model appropriate to their distribution and report treatment contrasts. Rationale: these methods match common endpoint data types. Assumption: endpoint definitions, scales, and distributions will support the selected models.
- [Proposed] Summarize safety outcomes by randomized group using counts and proportions, with suitable comparative estimates and confidence intervals where data permit. Rationale: this describes the frequency and uncertainty of harms. Assumption: safety event definitions and observation periods are prespecified.
- [Clarification Required] The multiplicity procedure for secondary efficacy endpoints is not specified; it matters for the interpretation of multiple superiority tests and type I error.
- [Proposed] Treat secondary and exploratory results as supportive or exploratory unless a multiplicity-controlled testing strategy is prespecified. Rationale: this avoids implying confirmatory evidence from multiple unadjusted tests. Assumption: no secondary-endpoint testing hierarchy has already been established.
- [Clarification Required] The treatment-effect estimand and handling of EVT, treatment discontinuation, and other post-randomization events are not specified; these decisions affect what treatment effect the analyses estimate.
- [Proposed] Use a treatment-policy approach for the primary randomized comparison, retaining outcomes regardless of subsequent EVT or study-treatment discontinuation. Rationale: this preserves the randomized comparison and includes downstream care in the treatment effect. Assumption: the intended primary question concerns assignment to treatment under the trial’s standard-care context.

### 5.4 Missing Data

- [Provided] The sample-size plan includes 5% dropout inflation.
- [Clarification Required] The definition of dropout, expected missingness by endpoint, and primary missing-data method are not specified; these affect the number of analyzable participants and potential bias.
- [Proposed] Describe missingness by randomized group and endpoint, including reasons when available. Rationale: the pattern and reasons for missing data inform interpretation. Assumption: reasons for missingness are collected.
- [Proposed] For the primary ordinal outcome, use multiple imputation under a missing-at-random assumption as a proposed primary missing-data approach, with sensitivity analyses addressing departures from that assumption. Rationale: this uses available participant information without treating missing outcomes as known. Assumption: relevant predictors of outcome and missingness are measured and can be included in the imputation model.
- [Clarification Required] Confirm the primary missing-data assumption and sensitivity-analysis strategy; the choice matters because missing Day-90 mRS may affect the treatment-effect estimate.

### 5.5 Additional Analyses

- [Provided] The exploratory objective includes final infarct volume/growth, mRS subgroups, outcomes when thrombectomy is not performed, 30-day readmission, one-pass EVT, Neuro-QoL, and Day-90 survival.
- [Clarification Required] No additional subgroup definitions, covariates, or sensitivity analyses are specified; prespecification matters to distinguish planned analyses from post hoc findings.
- [Proposed] Present exploratory analyses with their denominators, effect estimates, and uncertainty, and identify analyses not prespecified as exploratory. Rationale: this supports transparent interpretation. Assumption: the relevant outcome data and subgroup definitions are available.

### 5.6 Harms

- [Provided] Safety outcomes include sICH, adverse events, mortality, and PH2.
- [Clarification Required] Definitions, grading, collection periods, seriousness criteria, and analysis windows for harms are not specified; these are necessary for consistent safety reporting.
- [Proposed] Summarize harms by randomized group, including the number and proportion of patients affected and, where relevant, the number of events. Rationale: both patient-level frequency and recurrent events may be informative. Assumption: event-level data are collected and defined consistently.

### 5.7 Software and References

- [Provided] EAST 6.4.1 was used for the sample-size calculation.
- [Clarification Required] Statistical analysis software and version are not specified; documenting them supports reproducibility.
- [Clarification Required] No bibliographic details for the prior stroke studies underlying the sample-size assumptions are supplied; these are needed if those assumptions are to be documented with references.

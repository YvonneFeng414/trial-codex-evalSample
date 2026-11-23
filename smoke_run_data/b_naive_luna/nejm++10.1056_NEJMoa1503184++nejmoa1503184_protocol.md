# Clinical Study Protocol and Statistical Analysis Framework

## 1\. Introduction

### 1.1 Background and Rationale

- **[Provided]** GRIPHON evaluates selexipag (ACT-293987), a non-prostanoid IP-receptor agonist, in pulmonary arterial hypertension (PAH), with morbidity/mortality, exercise capacity, and safety evaluated against placebo.

### 1.2 Objectives

- **[Provided]** **Primary objective (P1):** Demonstrate the effect of selexipag versus placebo on time to first CEC-confirmed morbidity/mortality event in PAH. The objective-level outcome is time to first CEC-confirmed morbidity/mortality event in PAH, comparing selexipag versus placebo.
- **[Provided]** **Secondary/exploratory objective (S1):** Evaluate selexipag versus placebo for exercise capacity and other secondary/exploratory efficacy endpoints in PAH. The objective-level outcome is exercise capacity and other secondary/exploratory efficacy endpoints in PAH, comparing selexipag versus placebo.
- **[Provided]** **Secondary/exploratory objective (S2):** Evaluate safety and tolerability of selexipag in PAH (AC-065A302 and AC-065A303). The objective-level outcome is safety and tolerability of selexipag in PAH.
- **[Provided]** Exploratory objectives are not reported as separately labelled objectives. Exploratory efficacy endpoints and exploratory dose-response, pharmacoeconomic, PK, and safety analyses are enumerated.

## 2\. Study Methods

### 2.1 Trial Design

- **[Provided]** AC-065A302/GRIPHON is a prospective, multicenter, double-blind, randomized, placebo-controlled, parallel-group Phase 3, event-driven study. The allocation ratio is placebo:selexipag 1:1, with 1,150 planned randomized patients (575 per group).
- **[Provided]** Selexipag starts at 200 µg twice daily, with the Day-1 dose given in the evening. Weekly increments of 200 µg twice daily are used to reach an individual maximum tolerated dose, up to 1,600 µg twice daily; dose reductions are allowed for tolerability.
- **[Provided]** Matching ACT-293987 placebo is administered twice daily under the same titration schedule.
- **[Provided]** From Week 12, the dose is held through Week 26; later dose increases are allowed at scheduled visits. Treatment continues until 331 CEC-confirmed events, with a maximum duration of 4.3 years.
- **[Provided]** AC-065A303 is an open-label, uncontrolled extension for long-term safety and tolerability.
- **[Clarification Required]** The protocol does not specify the treatment or follow-up disposition for participants still on study when the 4.3-year maximum is reached without 331 events. This decision affects treatment exposure and endpoint follow-up.

### 2.2 Randomization

- **[Provided]** An independent centralized IWRS/IVRS assigns a unique randomization number; the code remains confidential until unblinding. Randomization is stratified by site.
- **[Provided]** Minimization or blocking is not specified.
- **[Clarification Required]** The allocation sequence’s blocking or other implementation details, if any, are not specified. This matters for describing and auditing randomization procedures, but no such method should be presumed.

### 2.3 Sample Size

- **[Provided]** The Version 7 plan is to randomize 1,150 patients, 575 per group. The calculation outcome is time to first CEC-confirmed morbidity/mortality event, analyzed as a time-to-event outcome.
- **[Provided]** Sample-size assumptions are a control-arm constant event hazard of 0.2231/year, a treatment-arm constant event hazard of 0.145/year, target hazard ratio (HR) 0.65, and constant dropout hazard of 0.051/year in both arms. No separate numerical sample-size inflation for dropout is reported.
- **[Provided]** The design assumes variance under the alternative hypothesis, a one-sided overall α=0.005 group-sequential design, and 90% power to reject the null. The assumed test is a one-sided, unstratified log-rank test in a group-sequential setting.
- **[Provided]** The required number of first CEC-confirmed events is 331. The comparison is for superiority; a non-inferiority/equivalence margin is not applicable. Design effect/clustering is not applicable to this individually randomized, non-clustered trial.
- **[Provided]** The stated basis for assumptions includes event and dropout hazards, target HR, group-sequential design, and variance under the alternative. Under the stated hazards, 331 events achieve 90% power; recruitment of up to 1,150 randomized patients was expected to yield the target.
- **[Provided]** The sample-size calculation used EAST 5.3 with its variance-under-alternative option. Planned interim operating characteristics were an approximately 19% probability of rejecting the null at interim and, under HR=1, an approximately 50% probability of accepting the null at interim.
- **[Provided]** An earlier Version 1 allowed a blinded sample-size adaptation up to 1,150 patients. The SAP uses the final Version 7 specifications of 1,150 planned patients and 331 events.

### 2.4 Hypothesis Framework

- **[Provided]** For the primary endpoint, the one-sided null hypothesis is that selexipag survival for remaining free of a first CEC-confirmed event is no greater than placebo at all times. The alternative is that survival is no worse at all times and greater at some time. The primary comparison is superiority.
- **[Clarification Required]** The precise mathematical convention for the survival comparison and handling of possible crossing curves is not further specified. This matters for interpreting the stated hypotheses and the primary test if survival curves do not maintain the assumed ordering.

### 2.5 Statistical Interim Analyses

- **[Provided]** The design is group-sequential, with one-sided overall α=0.005; the stated interim operating characteristics are approximately 19% probability of rejecting the null at interim and approximately 50% probability of accepting the null at interim under HR=1.
- **[Clarification Required]** Interim-analysis timing, event information fractions, stopping boundaries, decision rules, and the meaning of “accepting the null” are not specified. These are necessary to reproduce interim decisions and to interpret the group-sequential error control.
- **[Clarification Required]** The procedures for maintaining confidentiality and access to interim results beyond the stated randomization-code confidentiality are not specified. This matters for preserving trial blinding and preventing operational bias.

### 2.6 Timing of Analyses

- **[Provided]** The final AC-065A302 analysis includes Treatment and post-treatment observation data but excludes Treatment Extension data; its cutoff is 27-Apr-2014. AC-065A303 safety data through 10-Mar-2014 are included.
- **[Provided]** Screening occurs no more than 28 days before Day 1; baseline and randomization occur on Day 1. Titration continues through Week 8, with visits at Week 12, Week 16, Week 26, and then every 6 months, followed by EOS and safety follow-up.
- **[Provided]** Study closure prompts EOS or PTOCV within four weeks. Treatment Extension runs from EOS to EOTE after unblinding.
- **[Provided]** 6MWT and Borg assessments occur at baseline and scheduled follow-ups. Week-26 endpoint assessments occur before the morning dose (trough).
- **[Clarification Required]** Database-lock timing and data-readiness requirements are not specified. These are needed to define the operational trigger for final analysis and ensure the data are sufficiently complete and validated.

## 3\. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** The primary superiority design uses a one-sided overall α=0.005 in a group-sequential setting.
- **[Proposed]** Report treatment-effect estimates with confidence intervals alongside test results, and distinguish nominal intervals from intervals adjusted for the group-sequential design. **Rationale:** Estimates and uncertainty aid interpretation beyond a hypothesis-test result. **Assumption:** The final group-sequential boundaries and adjustment method will be supplied before analysis.
- **[Clarification Required]** The confidence level, sidedness, and group-sequential adjustment for confidence intervals are not specified. These choices affect interpretation and consistency between intervals and the primary test.
- **[Clarification Required]** Multiplicity control for secondary and exploratory efficacy analyses is not specified. This matters when interpreting multiple endpoint tests and any confirmatory claims.

### 3.2 Protocol Deviations

- **[Proposed]** Document deviations, their timing, and their potential effect on eligibility, treatment assignment, endpoint ascertainment, and analysis inclusion; finalize a blinded classification before database lock where feasible. **Rationale:** Consistent documentation supports transparent interpretation. **Assumption:** Deviation records can be reviewed before treatment-code disclosure.
- **[Clarification Required]** Criteria for classifying major deviations and the process for adjudicating them are not supplied. These decisions affect analysis-population membership and should be prespecified to avoid outcome-informed exclusions.

### 3.3 Analysis Populations

- **[Proposed]** Use all randomized participants in the group to which they were assigned for the primary efficacy analysis, regardless of treatment received. **Rationale:** This preserves the randomized comparison. **Assumption:** Randomization and endpoint data are available for all randomized participants.
- **[Proposed]** Define a safety population as randomized participants who received at least one dose, analyzed according to treatment received; describe any participants not fitting that rule separately. **Rationale:** Safety summaries should reflect actual exposure. **Assumption:** Dose administration data are available and the rule is acceptable for the final SAP.
- **[Proposed]** Use a per-protocol population only as a supportive analysis if its membership criteria are prespecified before unblinding. **Rationale:** A supportive analysis can assess robustness without replacing the randomized comparison. **Assumption:** Protocol deviations can be assessed without knowledge of comparative outcomes.
- **[Clarification Required]** The named analysis populations and their exact inclusion rules are not specified. These rules affect which participants contribute to each analysis and should be finalized before database lock.

## 4\. Trial Population

### 4.1 Screening Data

- **[Proposed]** Summarize the number screened, eligible, randomized, and not randomized, with reasons for non-randomization where recorded. **Rationale:** This describes participant flow and screening outcomes. **Assumption:** Screening and disposition records are collected for all screened individuals.
- **[Provided]** Screening is scheduled no more than 28 days before Day 1.

### 4.2 Eligibility Criteria Summary

- **[Provided]** **Inclusion criteria:** Age 18–75 years; symptomatic Group-1 idiopathic, heritable, drug/toxin-induced, connective-tissue-disease-associated, repaired-shunt congenital-heart-disease-associated, or HIV-associated PAH.
- **[Provided]** **Inclusion criteria:** Documented right-heart catheterization (RHC) with mPAP ≥25 mmHg, PVR ≥400 dyn·s·cm−5, and PCWP/LVEDP ≤15 mmHg; screening 6MWD 50–450 m.
- **[Provided]** **Inclusion criteria:** Women of childbearing potential require contraception with a failure rate <1%/year through one month after the final dose. ERAs/PDE5 inhibitors are permitted if stable for at least 3 months before baseline through Week 26.
- **[Provided]** **Exclusion criteria:** PH Groups 2–5; prostacyclin/analogue treatment within one month or planned during the trial, except a single administration for acute vasodilator testing.
- **[Provided]** **Exclusion criteria:** Obstructive disease defined as FEV1/FVC <70% and FEV1 <65% predicted; restrictive disease defined as TLC <70% predicted; Child-Pugh B/C impairment; LVEF <45%; severe renal dysfunction; and BMI <18.5.
- **[Provided]** **Exclusion criteria:** Recent investigational drug; inability to comply or perform 6MWT; rehabilitation completed <8 weeks before screening or planned; impaired consent/adherence capacity; life expectancy <12 months; pregnancy or lactation.
- **[Provided]** Prostacyclin/analogues and investigational drugs are prohibited.
- **[Clarification Required]** The threshold or definition for severe renal dysfunction, the washout period defining a recent investigational drug, and the operational definition of impaired consent/adherence capacity are not supplied. These decisions affect consistent eligibility determinations.
- **[Clarification Required]** The interaction between the stated exception for a single prostacyclin/analogue administration during acute vasodilator testing and the general prohibition on prostacyclin/analogues should be confirmed operationally. This matters for consistent eligibility and treatment-prohibition assessments.

### 4.3 Recruitment

- **[Clarification Required]** Recruitment countries, sites beyond the multicenter designation, recruitment dates, and recruitment procedures are not specified. These details matter for describing enrollment context and assessing population representativeness.

### 4.4 Withdrawal and Follow-up

- **[Provided]** Study closure prompts EOS or PTOCV within four weeks. The schedule includes EOS and safety follow-up; Treatment Extension runs from EOS to EOTE after unblinding.
- **[Clarification Required]** Withdrawal definitions, withdrawal procedures, continued endpoint follow-up after treatment discontinuation, and the duration and assessments of safety follow-up are not specified. These decisions affect endpoint ascertainment, censoring, and safety reporting.
- **[Clarification Required]** The relationship between PTOCV, EOS, and study closure is not further defined. This matters for consistent participant disposition and follow-up documentation.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize baseline demographic and clinical characteristics by randomized group, including the supplied eligibility measures when collected. **Rationale:** These summaries describe the enrolled population and allow inspection of randomized-group comparability. **Assumption:** The measures are available in the study data; no inferential baseline testing is required.
- **[Clarification Required]** The complete list of baseline variables and summary conventions is not supplied. This affects the final tables and cannot be settled from the eligibility criteria alone.

## 5\. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary outcome is time to first CEC-confirmed morbidity/mortality event in PAH, comparing selexipag versus placebo.
- **[Derived]** The primary outcome pertains to the randomized, placebo-controlled AC-065A302 comparison; AC-065A303 is described as an open-label, uncontrolled extension for long-term safety and tolerability.
- **[Clarification Required]** The components of the morbidity/mortality endpoint, event definitions, time origin, CEC procedures, and endpoint censoring rules are not supplied. These are essential to determine event status, event time, and analysis follow-up.

### 5.2 Secondary Outcomes

- **[Provided]** Secondary/exploratory efficacy outcomes include exercise capacity and other secondary/exploratory efficacy endpoints in PAH. Safety and tolerability are evaluated in PAH in AC-065A302 and AC-065A303.
- **[Provided]** Exploratory efficacy endpoints and exploratory dose-response, pharmacoeconomic, PK, and safety analyses are enumerated. 6MWT and Borg assessments occur at baseline and scheduled follow-ups.
- **[Clarification Required]** The full endpoint list, definitions, scales, assessment visits, analysis time points, and the designation of each endpoint as secondary or exploratory are not supplied. These decisions are required to specify estimands, methods, and reporting.
- **[Clarification Required]** The analysis plans for dose-response, pharmacoeconomic, and PK outcomes, including relevant measures and populations, are not specified. These details determine what data are analyzed and how results can be interpreted.

### 5.3 Analysis Methods

- **[Provided]** The sample-size design assumes a one-sided, unstratified log-rank test for the primary time-to-event outcome in a group-sequential setting.
- **[Proposed]** Use the prespecified group-sequential primary test and report the treatment comparison using the unstratified log-rank test, with survival estimates by group as descriptive summaries. **Rationale:** This aligns the analysis with the test used for sample-size planning and displays the event-free survival experience. **Assumption:** The final group-sequential boundaries and analysis population are confirmed before analysis.
- **[Proposed]** Estimate a treatment HR with an appropriate confidence interval as a supportive effect summary, and assess whether a single-HR summary is suitable if survival curves suggest non-proportional hazards. **Rationale:** An HR can summarize relative event rates, while checking its suitability avoids overreliance on an inadequate summary. **Assumption:** Event times and the group-sequential confidence-interval procedure are available and prespecified.
- **[Clarification Required]** The precise primary effect estimator, model specification, and method for inference under the group-sequential design are not supplied beyond the assumed log-rank test. These details are needed for reproducible estimation and inference.
- **[Proposed]** For repeated continuous efficacy measures, consider a repeated-measures model that accounts for treatment, visit, treatment-by-visit interaction, and baseline value, if compatible with the endpoint definition. **Rationale:** The schedule includes baseline and follow-up assessments, and repeated-measures methods can use those observations jointly. **Assumption:** The endpoint is continuous, visits are sufficiently comparable, and the model is finalized after endpoint definitions are supplied.
- **[Proposed]** Treat secondary and exploratory analyses as descriptive or exploratory unless a prespecified multiplicity strategy supports confirmatory inference. **Rationale:** The endpoint list and multiplicity plan are not supplied, so unadjusted testing should not be presented as definitive. **Assumption:** No unprovided confirmatory hierarchy is applied.
- **[Clarification Required]** The statistical methods for secondary endpoints, subgroup analyses if any, and multiplicity control are not specified. These decisions affect analysis validity and the strength of conclusions.

### 5.4 Missing Data

- **[Proposed]** For the primary time-to-event analysis, apply prespecified censoring rules based on the last date the participant is known to be free of a first event, with sensitivity analyses if warranted by the finalized follow-up rules. **Rationale:** Time-to-event methods require a defined censoring time. **Assumption:** Event status can be ascertained up to a recorded last-follow-up date.
- **[Proposed]** For repeated continuous efficacy outcomes, use a model-based approach using available observations and conduct sensitivity analyses if missingness may depend on unobserved outcomes. **Rationale:** This avoids automatic exclusion of participants with incomplete repeated assessments. **Assumption:** Missingness and endpoint properties are compatible with the selected model, to be assessed after the data are reviewed.
- **[Proposed]** Do not impute adverse events or exposure; summarize the available safety observations and document the extent of missing safety data. **Rationale:** Imputation could create unsupported safety events or exposure. **Assumption:** Safety and dosing records are maintained separately and can be reconciled.
- **[Clarification Required]** Missing-data assumptions, imputation methods, and endpoint-specific sensitivity analyses are not specified. These decisions matter because missingness can affect efficacy estimates and their interpretation.

### 5.5 Additional Analyses

- **[Provided]** Exploratory dose-response, pharmacoeconomic, PK, and safety analyses are enumerated.
- **[Proposed]** Report additional analyses as exploratory unless a separate prespecified inferential framework is provided. **Rationale:** The supplied information does not define these analyses sufficiently for confirmatory interpretation. **Assumption:** No unprovided analysis plan establishes a different status.
- **[Clarification Required]** The specific estimands, covariates, subgroups, sensitivity analyses, and methods for additional analyses are not supplied. These details are necessary for reproducible analyses and interpretation.

### 5.6 Harms

- **[Provided]** Safety and tolerability of selexipag in PAH are evaluated in AC-065A302 and AC-065A303. AC-065A303 is open-label and uncontrolled, and its safety data through 10-Mar-2014 are included.
- **[Proposed]** Summarize observed safety events and tolerability by randomized group for AC-065A302 and separately for AC-065A303; describe exposure alongside event counts. **Rationale:** Separate summaries respect the controlled and uncontrolled designs and provide context for observed events. **Assumption:** Safety-event and exposure data are available for the specified analysis periods.
- **[Clarification Required]** The safety-event definitions, severity and seriousness classifications, coding conventions, exposure summaries, and specific safety analysis populations are not supplied. These decisions affect event classification and comparability of safety summaries.

### 5.7 Software and References

- **[Provided]** EAST 5.3, using its variance-under-alternative option, was used for the sample-size calculation.
- **[Clarification Required]** Statistical analysis software and version(s) for the planned analyses are not specified. This matters for reproducibility of the analyses.
- **[Proposed]** Include no external references in this framework. **Rationale:** The protocol is restricted to the supplied study-specific information and does not require citations to define the proposed framework. **Assumption:** No reference list is required separately by the final protocol.

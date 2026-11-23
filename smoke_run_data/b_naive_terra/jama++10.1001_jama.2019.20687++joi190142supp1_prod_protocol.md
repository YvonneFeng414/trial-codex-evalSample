# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** FOXTROT is a phase IIa study of BAY 1213790 in patients undergoing elective primary unilateral total knee arthroplasty (TKA). BAY 1213790 is a fully human IgG1 anti-factor XIa antibody that binds FXIa near its catalytic center.

**[Provided]** TKA carries substantial venous thromboembolism (VTE) risk, while established thromboprophylaxis entails bleeding risk. Selective FXIa inhibition is being assessed for VTE prevention with a potentially favorable bleeding profile.

**[Provided]** The 0.3–1.8 mg/kg dose range was informed by preclinical work, phase 1 population pharmacokinetic/pharmacodynamic (PK/PD) data, and systems pharmacology.

### 1.2 Objectives

- **[Provided]** **P1, primary:** Assess safety and efficacy of different BAY 1213790 doses versus enoxaparin.
- **[Provided]** **S1, secondary:** Compare safety and efficacy of BAY 1213790 with apixaban.
- **[Provided]** **S2, exploratory:** Assess the BAY 1213790 dose-response for efficacy and safety.
- **[Provided]** **S3, exploratory:** Characterize BAY 1213790 PK, PD, and their relationship.
- **[Provided]** **S4, other:** Further characterize BAY 1213790 and investigate thrombosis mechanisms using additional PD markers.

## 2. Study Methods

### 2.1 Trial Design

**[Provided]** This is a randomized, active-comparator-controlled, multicenter phase IIa study. Treatment assignment is open-label, BAY 1213790 dose is observer-blinded, and CIAC adjudication is blinded.

**[Provided]** Part A administers BAY 1213790 after surgery. Sequential Part B administers it before surgery; recruitment is not parallel. Part B begins only after Part A completion and review of at least 75% of Part A primary assessments.

**[Provided]** In Part A, BAY 1213790 0.3, 0.6, or 1.2 mg/kg is administered intravenously once after adequate hemostasis on the day after TKA, preferably in the morning and no more than 24 hours after wound closure. A 1.8-mg/kg arm may open.

**[Provided]** In Part B, BAY 1213790 0.3 or 1.2 mg/kg is administered intravenously once in the second half of pre-surgery Day 1. The IDMC/SC may select doses of 0.3, 0.6, 1.2, or 1.8 mg/kg or add an arm.

**[Provided]** In both parts, enoxaparin 40 mg subcutaneously daily begins either the evening before TKA or 6–8 hours after TKA and continues for at least 10 days to venography. Apixaban 2.5 mg orally twice daily begins after TKA, within 24 hours of wound closure, and continues for at least 10 days to venography.

**[Clarification Required]** Define drug administration procedures, including infusion duration, and the process for choosing the enoxaparin start time; these are needed for consistent treatment delivery.

### 2.2 Randomization

**[Provided]** IxRS first randomizes patients to BAY 1213790, enoxaparin, or apixaban, then randomizes BAY recipients to a dose arm.

**[Provided]** The pooled allocation ratio is 5:1:1 for BAY 1213790:enoxaparin:apixaban. BAY allocation is 1:1:1 among Part A doses and 1:1 in Part B, subject to adjustment after arm closure or opening.

**[Provided]** Stratification factors and use of minimization or blocking are not specified.

**[Clarification Required]** Specify allocation procedures after arm changes and whether randomization uses stratification or blocking; these decisions affect implementation and analysis.

### 2.3 Sample Size

**[Provided]** The initial target is 700 patients: 500 BAY recipients across five intended arms and 100 recipients each of enoxaparin and apixaban. The maximum is 900 patients. The target is 100 patients per BAY or comparator arm, with at least 60 comparator patients in Part A and at least 40 in Part B.

**[Provided]** The calculation uses the binary primary efficacy composite VTE endpoint at Day 12+3 and a risk difference with a 5% non-inferiority margin. Assumed event proportions are 25% for enoxaparin, 10% for apixaban, and 10% and 4% for BAY in the respective scenarios.

**[Provided]** At a one-sided 5% significance level, the stated power is 81% for superiority and 97% for non-inferiority for BAY 10% versus enoxaparin 25%, and 99% for each for BAY 4% versus enoxaparin 25%. The descriptive apixaban calculation context reports superiority/non-inferiority power pairs of 0%/29% and 43%/88%.

**[Provided]** The calculations assume one-sided tests using the lower bound of a two-sided 90% normal-approximation confidence interval (CI) for the risk difference. Approximately 20% unavailable or non-evaluable venography due to quality or dropout is allowed, yielding 80 evaluable patients per arm.

**[Provided]** A variability assumption and an event target are not applicable to this proportion-based calculation. No clustering design effect applies to this individually randomized, non-clustered study. The assumptions are based on the event-rate scenarios and the 20% venography allowance.

**[Provided]** After approximately 75% of Part A Visit 7 assessments, pooled unavailable venography exceeding 30% may trigger a sample increase to regain 80% superiority power. Arm or dose enrollment may also change on IDMC/SC advice, within the 900-patient maximum.

**[Clarification Required]** Specify the calculation software, the mapping of the apixaban power pairs to scenarios, and the method for any sample-size increase; these are needed to reproduce the calculations and implement adaptation.

### 2.4 Hypothesis Framework

**[Provided]** For each BAY dose/time arm versus enoxaparin, non-inferiority is tested first, then superiority, each one-sided at global α=5%. The fixed sequence stops after the first unrejected null.

**[Provided]** The stated rule requires the lower bound of the two-sided 90% CI for BAY minus enoxaparin to be below 5% for non-inferiority and below 0 for superiority.

**[Clarification Required]** Resolve the CI-direction conflict before testing: for an adverse-event risk difference defined as BAY minus enoxaparin, a *lower* bound below either threshold does not establish non-inferiority or superiority and does not provide the stated error control.

**[Proposed]** Consider testing non-inferiority using an **upper** 90% CI bound below 5 percentage points and superiority using that bound below 0. Rationale: these bounds address whether BAY’s VTE risk is acceptably higher or lower; assumption: BAY minus enoxaparin and a 5-percentage-point margin are intended.

**[Clarification Required]** Specify the complete fixed order across dose/time arms and hypotheses, including newly opened arms and the consequences of arm closure; separate within-arm sequences alone do not define global multiplicity control.

**[Provided]** No hypothesis testing is planned versus apixaban; proportions and 90% CIs are descriptive.

### 2.5 Statistical Interim Analyses

**[Provided]** Part B initiation requires review of at least 75% of Part A primary assessments. The pooled unavailable-venography review and possible sample increase are described in Section 2.3.

**[Clarification Required]** Specify the review charter, access to comparative results, and any efficacy, futility, or safety stopping rules; these govern adaptation and protection of trial integrity.

**[Proposed]** Keep operational reviews separated from blinded study personnel, with access limited to authorized reviewers. Rationale: this reduces operational bias; assumption: an appropriately authorized review process is available.

### 2.6 Timing of Analyses

**[Provided]** Primary completion occurs when all patients have been assessed at Visit 7. Study end is the last patient’s last visit. Database blinding continues through final database lock after the last patient’s last visit and authorization of release.

**[Provided]** Screening is Day −13 to Day 1; randomization is Day 1; TKA is Day 2. Treatment visits occur on Days 3, 4, 6±1, and 12+3. Bilateral venography and primary outcomes are assessed at Visit 7, Day 12+3. Post-treatment visits occur at Day 30±5, Day 90±7, and Day 150±7.

**[Clarification Required]** Specify analysis cutoffs and the permitted access to data at primary completion and final lock; open-label treatment assignment and continued database blinding require an operational access plan.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

**[Provided]** The planned hypothesis framework uses one-sided 5% significance and two-sided 90% CIs. Apixaban comparisons are descriptive.

**[Proposed]** Report event counts, denominators, proportions, and 90% CIs by arm, alongside BAY-minus-comparator risk differences and CIs. Rationale: these display absolute effects and precision; assumption: binary endpoint definitions are finalized.

**[Clarification Required]** Confirm the CI-direction correction and multiplicity sequence before declaring any hypothesis result; the supplied rule cannot support the stated inference as written.

### 3.2 Protocol Deviations

**[Proposed]** Record deviations, including eligibility, treatment timing or dose, prohibited treatment, and assessment deviations; classify important deviations before database release. Rationale: consistent classification supports interpretation and sensitivity analyses; assumption: deviation criteria are prespecified.

**[Clarification Required]** Define important deviations and their population or analysis consequences; these decisions can change the estimated effects.

### 3.3 Analysis Populations

**[Proposed]** Define a randomized population by assigned arm, a safety population by treatment received, and an efficacy-evaluable population based on prespecified endpoint availability and assessment rules. Rationale: these support complementary efficacy and safety summaries; assumption: treatment and assessment records permit classification.

**[Proposed]** Use all randomized patients as the starting population for the primary efficacy estimand and evaluate an appropriately defined per-protocol population in sensitivity analysis. Rationale: randomization is best preserved in the primary comparison; assumption: the estimand and missing-data strategy are approved.

**[Clarification Required]** Confirm the primary analysis population, evaluability criteria, and handling of treatment discontinuation or other intercurrent events; the supplied 80-evaluable-patient calculation does not define these analysis decisions.

## 4. Trial Population

### 4.1 Screening Data

**[Proposed]** Summarize numbers screened, eligible, randomized, treated, and assessed at Visit 7, with reasons for screen failure where recorded. Rationale: disposition supports assessment of recruitment and selection; assumption: screening records are available.

### 4.2 Eligibility Criteria Summary

**[Provided]** Inclusion requires consent, age at least 18 years, elective primary unilateral TKA, fulfillment of reproductive/contraception requirements, and ability to follow instructions. Part B requires general anesthesia.

**[Provided]** Exclusions include clinically significant bleeding risk, including specified hematologic, coagulation, hepatic, hypertension, surgery, or bleeding-disorder conditions; prior deep vein thrombosis; weight over 135 kg; and CrCl below 60 mL/min by MDRD.

**[Provided]** Other exclusions include recent myocardial infarction or stroke; active cancer with specified exceptions; comparator contraindication; full anticoagulation or dual antiplatelets; compression/stimulator use; contrast allergy; prior assignment; recent investigational treatment; and site affiliation.

**[Provided]** Postoperative epidural analgesia is excluded in Part A. Regional anesthesia or epidural analgesia is excluded in Part B.

**[Clarification Required]** Specify the detailed bleeding-risk conditions, reproductive requirements, cancer exceptions, recency windows, and prohibited compression/stimulator use; these determine eligibility consistently.

**[Clarification Required]** Confirm the renal function calculation and units described as “CrCl by MDRD”; the operational threshold must be reproducible for screening.

### 4.3 Recruitment

**[Provided]** Recruitment is multicenter and sequential between Parts A and B, with no parallel recruitment.

**[Clarification Required]** Define recruitment locations, dates, and procedures; these are needed for operational planning and are not specified.

### 4.4 Withdrawal and Follow-up

**[Proposed]** Distinguish treatment discontinuation from study withdrawal and seek scheduled outcome and safety follow-up after treatment discontinuation when consent permits. Rationale: this limits avoidable missing data; assumption: participants permit continued follow-up.

**[Clarification Required]** Specify withdrawal procedures, permissible use of previously collected data, and follow-up after withdrawal; these affect participant rights and endpoint completeness.

### 4.5 Baseline Characteristics

**[Proposed]** Summarize baseline demographics, relevant medical history, VTE and bleeding risk factors, renal function, and surgical characteristics by randomized arm and part. Rationale: these describe comparability and clinical context; assumption: the variables are collected consistently.

## 5. Analysis

### 5.1 Primary Outcomes

**[Provided]** The sample-size calculation uses a composite VTE efficacy endpoint at Visit 7, Day 12+3, expressed as a binary event proportion. Bilateral venography is scheduled at that visit.

**[Clarification Required]** Define the composite’s components, ascertainment and adjudication rules, assessment window, and handling of inconclusive venography; these determine who has a primary event.

**[Clarification Required]** Specify whether a primary safety endpoint is intended and, if so, its definition and assessment window; P1 includes safety, but no primary safety outcome is defined.

### 5.2 Secondary Outcomes

**[Provided]** Secondary and exploratory objectives address comparison with apixaban, BAY dose-response, PK/PD and their relationship, and additional PD markers and thrombosis mechanisms.

**[Clarification Required]** Define the secondary and exploratory endpoints, marker panels, sampling times, and analysis windows; objectives alone do not specify measurable outcomes.

**[Proposed]** Summarize safety and efficacy by arm for the apixaban comparison without hypothesis tests. Rationale: this implements the descriptive comparison; assumption: the relevant outcomes are defined.

### 5.3 Analysis Methods

**[Proposed]** For each BAY dose/time arm, estimate the primary VTE proportion and its difference from enoxaparin using the prespecified two-sided 90% normal-approximation CI. Rationale: this follows the calculation framework; assumption: the endpoint and comparison population are defined.

**[Clarification Required]** Specify whether each comparison uses enoxaparin patients from the corresponding part or a pooled control, and how part and arm changes are handled; this determines the comparator and interpretation.

**[Proposed]** After correction of the hypothesis rule, apply the approved fixed sequence and report estimates and CIs even for hypotheses not formally tested. Rationale: descriptive estimates retain information without implying significance; assumption: the final sequence is prespecified.

**[Proposed]** Explore dose-response separately by administration timing and summarize PK, PD, and their relationships using observed data and suitable prespecified models. Rationale: timing may distinguish dose effects and models can characterize exposure-response; assumption: sufficient measurements and events are available.

**[Clarification Required]** Specify dose-response models, PK/PD methods, covariates, and handling of below-quantification measurements; these choices determine reproducibility and interpretation.

### 5.4 Missing Data

**[Clarification Required]** Define the primary handling of missing or non-evaluable venography, missing clinical outcomes, and deaths or other intercurrent events; these affect the estimand and potential bias.

**[Proposed]** Summarize missingness and reasons by arm and perform prespecified sensitivity analyses under alternative plausible event assumptions. Rationale: the 20% venography allowance makes robustness important; assumption: missingness reasons and endpoint data are recorded.

### 5.5 Additional Analyses

**[Proposed]** Summarize outcomes by part and assess sensitivity to important protocol deviations and alternative CI methods where normal-approximation performance is poor. Rationale: these checks address timing differences and sparse events; assumption: subgroup sizes permit informative estimates.

**[Clarification Required]** Prespecify any further subgroups and their role; unplanned subgroup comparisons can be misleading.

### 5.6 Harms

**[Proposed]** Summarize adverse events, serious adverse events, bleeding, deaths, and treatment discontinuations due to adverse events by treatment received and part. Rationale: P1 includes safety; assumption: events and treatment exposure are collected.

**[Clarification Required]** Define bleeding categories, adverse-event collection periods, causality and severity rules, and adjudication procedures; these are necessary for consistent safety comparisons.

### 5.7 Software and References

**[Clarification Required]** Specify the statistical software and version before analysis; this is needed for reproducibility.

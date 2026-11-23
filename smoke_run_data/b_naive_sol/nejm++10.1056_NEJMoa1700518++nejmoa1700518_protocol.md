# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

[Provided] Recurrent venous thromboembolism (VTE) remains clinically important after initial anticoagulation for deep-vein thrombosis (DVT) or pulmonary embolism (PE). Long-term vitamin K antagonist (VKA) therapy is effective but entails bleeding risk, monitoring, and dose adjustment. Acetylsalicylic acid (ASA) provides modest recurrence prevention.

[Provided] This study evaluates whether reduced-dose rivaroxaban can maintain efficacy while improving safety, using ASA as the comparator.

### 1.2 Objectives

- [Provided] **P1—Primary efficacy objective:** Evaluate superiority of rivaroxaban 10 mg and rivaroxaban 20 mg versus ASA 100 mg for fatal or nonfatal symptomatic recurrent VTE.
- [Provided] **S1—Secondary efficacy objective:** Evaluate superiority of each rivaroxaban dose versus ASA for the composite of fatal/nonfatal symptomatic recurrent VTE, myocardial infarction (MI), ischemic stroke, or systemic non-central nervous system (non-CNS) embolism.
- [Provided] **S2—Principal safety objective:** Document the incidence of major bleeding.
- [Provided] **S3—Secondary safety objective:** Document the incidence of clinically relevant nonmajor (CRNM) bleeding.
- [Provided] **S4—Additional study objective (a):** Evaluate the composite of nonfatal symptomatic VTE and all-cause mortality.
- [Provided] **S5—Additional study objective (b):** Evaluate the composite of major bleeding and recurrent VTE.
- [Provided] **S6—Additional study objective (c):** Evaluate the composite of major bleeding, recurrent VTE, MI, ischemic stroke, and systemic non-CNS embolism.
- [Provided] S4–S6 are additional study objectives, not objectives labeled exploratory.
- [Provided] Exploratory analyses describe composites of the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations, and net clinical benefit.

## 2. Study Methods

### 2.1 Trial Design

- [Provided] This is a phase III, multicenter, randomized, double-blind, double-dummy, active-comparator, event-driven trial with 1:1:1 allocation.
- [Provided] The three treatments are oral rivaroxaban 10 mg, rivaroxaban 20 mg, and ASA 100 mg, each taken once daily with food. Double-dummy supplies comprise one rivaroxaban-or-placebo tablet and one ASA-or-placebo tablet daily.
- [Provided] Nominal treatment duration is 12 months, although the final randomized patients may receive only 6 months.
- [Provided] The first dose is administered at least 24 hours after previous VTE treatment. For patients receiving a VKA, INR >3.0 delays randomization; INR 2.5–3.0 permits randomization but delays first intake until the next day; INR <2.5 permits dosing.
- [Provided] A missed dose may be made up only on the same day. Double dosing is not allowed.
- [Provided] Six months of medication is supplied initially. IxRS determines at visit 4 whether a further six months is supplied. The last randomized patients receive no second supply.
- [Provided] Treatment may restart after temporary interruption if total treatment does not exceed 12 months.
- [Provided] All efficacy and safety events are centrally adjudicated, and final analyses use adjudication results.
- [Proposed] Maintain masking of investigators, participants, outcome assessors, and analysis personnel until authorized unblinding; keep adjudication materials treatment-masked where feasible. **Rationale:** Protect outcome assessment and analysis from knowledge of allocation. **Assumption:** Operational systems can separate treatment-identifying information from adjudication and blinded analysis.
- [Clarification Required] Emergency unblinding procedures, treatment-interruption and restart criteria, and whether the 12-month maximum denotes cumulative exposure or elapsed treatment time require specification because they affect participant management and exposure derivation.

### 2.2 Randomization

- [Provided] Randomization uses a central interactive voice/web response system (IxRS). A unique randomization number identifies treatment allocation.
- [Provided] The investigator supplies study-center identification and the investigator-reported index presentation.
- [Provided] Randomization is stratified by country and index event: DVT only versus PE with or without DVT.
- [Clarification Required] Blocking, minimization, sequence-generation details, and allocation-list access controls are unspecified. These decisions are needed to document reproducibility and allocation concealment.
- [Proposed] Restrict access to the allocation sequence and use IxRS only after eligibility and consent are confirmed. **Rationale:** Prevent foreknowledge of allocation and inappropriate randomization. **Assumption:** IxRS supports eligibility confirmation and controlled access.

### 2.3 Sample Size

- [Provided] Planned enrollment is approximately 950 patients per arm, or 2,850 total, subject to adjustment using observed overall primary-event incidence.
- [Provided] The calculation outcome is confirmed fatal or nonfatal symptomatic recurrent VTE, analyzed as time to first event. At least 80 confirmed primary efficacy outcomes are required.
- [Provided] The assumed ASA event rate is 5% per year, modeled exponentially. Assumed hazard ratios (HRs) are 0.30 for rivaroxaban 20 mg versus ASA and 0.40 for rivaroxaban 10 mg versus ASA.
- [Provided] The 20-mg planning assumption is conservative relative to an adjusted indirect estimate of HR 0.264, with 95% confidence interval (CI) 0.12–0.59. The 10-mg assumption represents a 60% reduction, compared with an expected HR of 0.30 under the reduced-dose rationale.
- [Provided] No separate variability parameter is specified. Simulations use exponential event, treatment-discontinuation, and withdrawal processes.
- [Provided] Assumed annual treatment discontinuation is 10%, and annual loss to follow-up/withdrawn consent is 1%. The last subjects receive 6 months of treatment.
- [Provided] In the simulations, event time after discontinuation follows inferior-control treatment assumptions. Losses before a simulated event are censored. Administrative censoring occurs at one year or the end of the trial.
- [Provided] Planning uses sequential two-sided superiority tests at alpha 0.05, with stratified Cox regression and an upper 95% CI bound below 1. Stratified log-rank testing is supportive.
- [Provided] Target power is 90%. In 10,000 simulated trials, joint Cox-regression power was 0.901. Simulation joint success required both dose-versus-ASA HR upper 95% CI bounds to be ≤1.
- [Provided] Simulations select trials or observation time reaching the event target and fit Cox and log-rank tests. The event-driven design targets 80 events to demonstrate superiority of both doses.
- [Provided] No non-inferiority or equivalence margin applies. No clustering/design-effect adjustment applies because randomization is individual rather than cluster-based.
- [Provided] Blinded pooled projections adjust enrollment using observed primary-event incidence. Total sample size is iterated until the projected probability of at least 80 total events is ≥0.50; alternatives, including a probability of about 0.80, are also presented.
- [Clarification Required] The timing, responsible decision-maker, enrollment limits, and choice among projected event-attainment probabilities for sample-size adjustment are unspecified. These determine how the blinded adaptation is implemented without discretionary selection.

### 2.4 Hypothesis Framework

- [Provided] **First test:** \(H_{0,20}: HR_{20\,mg/ASA}=1\), versus the two-sided alternative \(HR_{20\,mg/ASA}\ne1\), at alpha 0.05.
- [Provided] **Second test:** Only after superiority of 20 mg is established, test \(H_{0,10}: HR_{10\,mg/ASA}=1\), versus the two-sided alternative \(HR_{10\,mg/ASA}\ne1\), at alpha 0.05.
- [Provided] Rivaroxaban 20 mg is superior if its HR upper 95% CI bound is <1. Rivaroxaban 10 mg is superior only if 20 mg is superior and the 10-mg upper bound is also <1. This fixed sequence controls familywise error.
- [Proposed] Apply the final superiority rules using unrounded estimates and the strict upper-bound criterion <1. **Rationale:** Avoid decisions driven by display rounding or the simulation’s ≤1 convention. **Assumption:** The simulation convention does not replace the stated final decision rule.

### 2.5 Statistical Interim Analyses

- [Provided] Enrollment adjustment uses blinded pooled primary-event projections.
- [Clarification Required] Formal unblinded interim efficacy or futility analyses, stopping boundaries, an independent monitoring committee, and any associated alpha-spending plan are not specified. These must be resolved before any unblinded comparative review because they could affect error control and trial conduct.
- [Proposed] Pending an approved interim-analysis plan, limit statistical monitoring to blinded pooled event accrual and operational data, without comparative efficacy testing. **Rationale:** Preserve the supplied fixed-sequence final testing framework. **Assumption:** No unreported unblinded interim testing is intended.

### 2.6 Timing of Analyses

- [Provided] Statistical analysis plan (SAP) revisions are issued before database lock.
- [Provided] Final analyses use adjudicated outcomes through each participant’s individual intended treatment limit. Standard limits are day 353, the visit day if within days 353–367, or day 367; defined administrative shortening rules also apply.
- [Provided] Assessments occur at baseline, Day 1, Day 30±7, Day 90±7, Day 180±7, Day 270±7, Day 360±7, and a 30±7-day post-treatment observation visit. Potential outcomes and adverse events (AEs) are elicited at all contacts.
- [Provided] Following premature discontinuation, visit 7 occurs early, 30±7 days after stopping, and may be conducted by telephone or in clinic. Other visits continue unless participation is refused. Investigators may arrange additional visits.
- [Clarification Required] The complete algorithm selecting day 353, a visit day, or day 367, and the administrative shortening rules—including shortened follow-up for the final randomized patients—are needed to derive individual analysis limits reproducibly.
- [Clarification Required] The relationship between randomization, Day 1, and first dose, together with the event-target review, stopping, adjudication-completion, and database-lock dates, is unspecified. These determine time origins, analysis cutoffs, and which confirmed events contribute.
- [Proposed] Finalize endpoint derivations, censoring rules, and analysis programs before treatment unblinding, and resolve outstanding adjudication queries before final analysis. **Rationale:** Reduce data-dependent decisions and inconsistent event classification. **Assumption:** Operational timelines permit blinded finalization and completed adjudication.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- [Provided] Primary superiority tests are two-sided at 0.05 with 95% CIs and the fixed testing sequence specified in Section 2.4.
- [Clarification Required] A multiplicity strategy for S1, safety outcomes, additional objectives, and exploratory analyses is not supplied. It is needed to determine whether any nonprimary result supports a confirmatory claim.
- [Proposed] Unless an additional hierarchy is approved before unblinding, report nonprimary comparisons with nominal two-sided 95% CIs and clearly identified nominal p-values, without familywise-error-controlled claims. S1 remains a superiority comparison, but its inference is nominal. **Rationale:** Preserve the stated objectives without inventing confirmatory error allocation. **Assumption:** The supplied fixed sequence is the only established confirmatory family.
- [Proposed] Present effect sizes, uncertainty, event counts, and absolute outcome frequencies alongside p-values. **Rationale:** Statistical significance alone does not describe clinical magnitude. **Assumption:** Endpoint and follow-up data support these summaries.

### 3.2 Protocol Deviations

- [Proposed] Prospectively categorize deviations involving eligibility, allocation, incorrect treatment or dosing, prohibited concomitant medication, adherence, visit timing, masking, and outcome ascertainment. **Rationale:** Standardized categories support transparent interpretation and sensitivity analyses. **Assumption:** Monitoring records contain sufficient detail.
- [Clarification Required] Major-deviation definitions, adherence thresholds, assessment procedures, and rules affecting per-protocol inclusion are unspecified. These must be fixed before unblinding to avoid outcome-driven exclusions.
- [Proposed] Review and classify deviations while blinded, summarize them by randomized group, and retain affected participants in the primary randomized analysis. **Rationale:** Preserve randomization while documenting departures from intended conduct. **Assumption:** A randomized primary analysis is adopted.

### 3.3 Analysis Populations

- [Proposed] **Randomized efficacy population:** Include all randomized participants and analyze them according to assigned treatment, regardless of treatment initiation, interruption, discontinuation, or switching, within their individual intended analysis limits. **Rationale:** Preserve randomization and estimate the effect of assignment. **Assumption:** Outcome follow-up remains available after treatment changes.
- [Proposed] **Safety population:** Include participants receiving at least one study-treatment dose and summarize safety according to actual treatment received. **Rationale:** Link harms to exposure. **Assumption:** Actual dosing can be established reliably.
- [Clarification Required] Safety attribution for incorrect dispensing, mixed treatment exposure, or switching requires explicit rules because a single actual-treatment label may not adequately represent such participants.
- [Proposed] **Per-protocol population:** Use a prospectively defined subset without major relevant deviations for supportive analyses only. **Rationale:** Assess robustness without replacing the randomized comparison. **Assumption:** Major-deviation criteria are finalized before unblinding.

## 4. Trial Population

### 4.1 Screening Data

- [Proposed] Maintain a screening log recording numbers assessed, eligible, ineligible, consented, randomized, and not randomized, with reasons where permitted. **Rationale:** Describe selection and recruitment transparently. **Assumption:** Screening-data collection is authorized.
- [Proposed] Reconcile eligibility assessments, consent dates, randomization records, treatment initiation, and participant identifiers before analysis. **Rationale:** Establish reliable population denominators and chronology. **Assumption:** Source records and IxRS data can be linked securely.

### 4.2 Eligibility Criteria Summary

- [Provided] **Inclusion:** Confirmed symptomatic DVT and/or PE.
- [Provided] **Inclusion:** Receipt of 6–12 months of anticoagulation without an interruption exceeding one week.
- [Provided] **Inclusion:** Written consent.
- [Provided] **Exclusion 1:** Age below the country-specific legal lower age limit.
- [Provided] **Exclusion 2:** An indication for therapeutic-dose anticoagulants.
- [Provided] **Exclusion 3:** Hypersensitivity to investigational or comparator therapy.
- [Provided] **Exclusion 4:** Any contraindication in local investigational/comparator labeling.
- [Provided] **Exclusion 5:** An indication for antiplatelet therapy or a conventional nonsteroidal anti-inflammatory drug.
- [Provided] **Exclusion 6:** Hepatic disease with coagulopathy and clinically relevant bleeding risk.
- [Provided] **Exclusion 7:** Calculated creatinine clearance (CrCl) <30 mL/min.
- [Provided] **Exclusion 8:** Active bleeding or high bleeding risk contraindicating anticoagulation.
- [Provided] **Exclusion 9:** Life expectancy <6 months.
- [Provided] **Exclusion 10:** Systemic strong dual CYP3A4/P-gp inhibitors: HIV protease inhibitors, ketoconazole, itraconazole, voriconazole, or posaconazole.
- [Provided] **Exclusion 11:** Childbearing potential without proper contraception, pregnancy, or breastfeeding.
- [Provided] **Exclusion 12:** Participation in an investigational drug/device study within 30 days before randomization.
- [Clarification Required] Country-specific age limits, the CrCl calculation method, acceptable contraception, and operational definitions of clinically relevant hepatic disease and high bleeding risk are unspecified. These affect consistent eligibility assessment.
- [Proposed] Document eligibility before randomization using a standardized checklist and retain supporting assessments. **Rationale:** Reduce inconsistent application across centers. **Assumption:** Required assessments are available before allocation.

### 4.3 Recruitment

- [Provided] Recruitment is multicenter, with an initial total enrollment target of approximately 2,850 participants, subject to blinded event-incidence adjustment.
- [Clarification Required] Participating countries and centers, recruitment dates, recruitment methods, and expected accrual rates are unspecified. These are needed to assess feasibility and operationalize the event-driven schedule.
- [Proposed] Obtain applicable ethics and regulatory approvals and document informed consent before study-specific enrollment procedures. **Rationale:** Protect participant rights and support lawful study conduct. **Assumption:** Appropriate local governance processes are available.

### 4.4 Withdrawal and Follow-up

- [Provided] Scheduled visits continue after premature treatment discontinuation unless participation is refused.
- [Provided] Premature discontinuation triggers an early visit 7 at 30±7 days after stopping, conducted by telephone or in clinic.
- [Proposed] Distinguish treatment discontinuation, refusal of particular assessments, withdrawal of further follow-up, and loss to follow-up; record dates and reasons separately. **Rationale:** These events have different implications for exposure, outcome availability, and censoring. **Assumption:** Participants can specify the scope of withdrawal.
- [Proposed] Seek permitted outcome and vital-status follow-up after treatment discontinuation without making continued treatment a condition of follow-up. **Rationale:** Reduce missing outcomes in the randomized comparison. **Assumption:** Consent and applicable requirements permit continued contact.
- [Clarification Required] Rules for retaining previously collected data, obtaining information after withdrawal, and acceptable follow-up sources are unspecified. These determine permissible ascertainment and analysis after withdrawal.

### 4.5 Baseline Characteristics

- [Proposed] Summarize age, sex, country, index-event category, prior anticoagulant treatment and duration, renal function, relevant comorbidities, bleeding history, and available baseline hematology and hepatic measures. **Rationale:** Describe the enrolled population and clinically relevant risk factors. **Assumption:** These variables are collected; unavailable variables will not be inferred.
- [Proposed] Present continuous variables using sample size, mean and standard deviation, and/or median and quartiles, and categorical variables using counts, percentages, and missing denominators. Avoid significance testing of baseline treatment differences. **Rationale:** Baseline tables are descriptive in a randomized trial. **Assumption:** Variable distributions and coding are reviewed while blinded.

## 5. Analysis

### 5.1 Primary Outcomes

- [Provided] The primary efficacy outcome is fatal or nonfatal symptomatic recurrent VTE, comparing rivaroxaban 20 mg and rivaroxaban 10 mg separately with ASA 100 mg.
- [Provided] The planning analysis is time to first confirmed primary efficacy outcome, using centrally adjudicated results.
- [Clarification Required] Diagnostic criteria for recurrence, fatal-event attribution, event-date conventions, and handling of uncertain or unclassifiable events require an adjudication charter. These determine endpoint membership and event timing.
- [Proposed] Define the primary estimand as the effect of randomized treatment assignment on time to first adjudicated primary event within the individual intended treatment limit, regardless of treatment changes. Treat death not meeting the endpoint definition as a competing event. **Rationale:** Align the randomized comparison with the supplied analysis horizon while avoiding censoring solely at treatment cessation. **Assumption:** Post-discontinuation efficacy follow-up is sufficiently available.

### 5.2 Secondary Outcomes

- [Provided] **S1:** Fatal/nonfatal symptomatic recurrent VTE, MI, ischemic stroke, or systemic non-CNS embolism, comparing each rivaroxaban dose with ASA.
- [Provided] **S2:** Incidence of major bleeding.
- [Provided] **S3:** Incidence of CRNM bleeding.
- [Provided] **S4:** Composite of nonfatal symptomatic VTE and all-cause mortality.
- [Provided] **S5:** Composite of major bleeding and recurrent VTE.
- [Provided] **S6:** Composite of major bleeding, recurrent VTE, MI, ischemic stroke, and systemic non-CNS embolism.
- [Provided] Exploratory outcomes include composites combining the primary or secondary efficacy outcome with symptomatic venous thrombosis in other locations, and analyses of net clinical benefit.
- [Proposed] Analyze efficacy and additional composite outcomes as time to first qualifying component and separately describe their components. **Rationale:** Provide a consistent composite analysis while showing which events contribute. **Assumption:** Component dates and classifications are available.
- [Clarification Required] Definitions of MI, ischemic stroke, systemic non-CNS embolism, other-location venous thrombosis, and net clinical benefit are unspecified. The exact exploratory composite membership and whether net benefit duplicates or differs from S5/S6 must be resolved to prevent ambiguous or duplicate endpoints.
- [Clarification Required] Rules for simultaneous component events and recurrent-event summaries are unspecified. They matter for component counts even when the first composite-event date is unchanged.

### 5.3 Analysis Methods

- [Provided] The assumed primary method is stratified Cox proportional-hazards superiority analysis, with stratified log-rank testing supportive.
- [Proposed] Fit a three-arm Cox model with treatment indicators and strata defined by country and investigator-reported index event, producing each rivaroxaban-versus-ASA HR, two-sided 95% CI, and p-value. **Rationale:** Align analysis with randomization factors and the planning method. **Assumption:** These are the intended analysis strata and sufficient informative risk sets are available.
- [Clarification Required] Final analysis strata, treatment of sparse strata, tie handling, and the precise Cox inferential test are not specified. These implementation choices must be fixed before unblinding because they can affect estimates and test results.
- [Proposed] Use randomization as the efficacy time origin. Define time to first qualifying event or censoring in days. **Rationale:** Include all randomized participants without conditioning on treatment initiation. **Assumption:** Randomization dates are available and the relationship to protocol study-day numbering is resolved.
- [Proposed] Censor event-free participants at the earliest applicable individual intended treatment limit or last date of reliable endpoint follow-up; censor nonendpoint death at death for cause-specific Cox analysis. Do not censor solely because treatment stops or changes. **Rationale:** Match the proposed treatment-policy estimand and distinguish loss of observation from loss of exposure. **Assumption:** Follow-up and death dates are reliable.
- [Proposed] For endpoints not containing all-cause mortality, report cumulative incidence accounting for nonendpoint death as a competing event. For composites containing all-cause mortality, report Kaplan–Meier event-free estimates. **Rationale:** Avoid treating competing deaths as if they could subsequently experience an endpoint. **Assumption:** Death timing and endpoint attribution are sufficiently complete.
- [Proposed] Present event counts, participants with events, follow-up distributions, and component summaries by treatment. **Rationale:** Make model-based results interpretable, particularly with individual treatment limits of differing lengths. **Assumption:** Follow-up and component data are available.
- [Proposed] Assess proportional hazards using graphical diagnostics and residual-based checks without replacing the prespecified primary test based on observed results. Describe material departures and provide prespecified supportive time-varying summaries if feasible. **Rationale:** Evaluate interpretation of the HR while avoiding data-driven primary-method selection. **Assumption:** Event numbers support meaningful diagnostics.
- [Clarification Required] Any supportive time-varying model, time intervals, or restricted-mean follow-up horizon must be specified before unblinding. Otherwise, their selection could be influenced by observed treatment differences.
- [Proposed] Apply corresponding time-to-first-event methods to S1 and S4–S6, with nominal interpretation unless an additional multiplicity plan is approved. **Rationale:** Maintain analytical consistency across composites. **Assumption:** Their definitions and risk windows are finalized.

### 5.4 Missing Data

- [Proposed] Describe missing outcome information, follow-up duration, loss to follow-up, withdrawal, and missing baseline variables by treatment and reason. **Rationale:** Characterize the extent and potential direction of missing-data bias. **Assumption:** Reasons and last-contact dates are recorded.
- [Proposed] Do not treat missing follow-up as evidence of no event or impute event-free status beyond the last reliable assessment. Use the prespecified censoring rules for the primary analysis. **Rationale:** Avoid unsupported extension of event-free observation. **Assumption:** Censoring is sufficiently independent of subsequent outcome, conditional on the analysis structure.
- [Proposed] Query incomplete or conflicting event and death dates before lock. For unresolved partial dates, use prespecified bounded-date sensitivity analyses rather than an undisclosed single-date substitution. **Rationale:** Show whether timing uncertainty affects results. **Assumption:** Available records establish plausible date bounds.
- [Proposed] Assess robustness to informative loss using prespecified scenarios that increase post-loss event risk and identify whether plausible assumptions alter conclusions. **Rationale:** The primary censoring assumption cannot be verified directly. **Assumption:** Sufficient follow-up information exists to define clinically interpretable scenarios.
- [Clarification Required] The magnitude, timing, and treatment-specific structure of missing-outcome sensitivity scenarios are unspecified. They must be fixed before unblinding to avoid selecting favorable assumptions.
- [Proposed] Show missing baseline categories explicitly in descriptive summaries and use available observations for clearly labeled subgroup descriptions. **Rationale:** Avoid silently changing denominators. **Assumption:** Missing baseline data are not required for the primary unadjusted treatment contrast beyond resolved stratification data.

### 5.5 Additional Analyses

- [Proposed] Conduct a supportive per-protocol analysis using prospectively classified major deviations, while retaining the randomized analysis as primary. **Rationale:** Assess consistency under closer protocol adherence. **Assumption:** Exclusion rules are established without treatment-outcome knowledge.
- [Proposed] Explore treatment-effect heterogeneity by the randomization index-event category using treatment-by-subgroup interaction terms, with subgroup estimates and CIs. **Rationale:** Examine an already defined clinically relevant grouping. **Assumption:** Event counts permit estimation; findings remain exploratory.
- [Clarification Required] Additional subgroups, adjusted models, and any direct 10-mg-versus-20-mg comparison are not specified. Their scope and inferential status must be established before unblinding; no direct dose non-inferiority conclusion can be supported without a defined framework and margin.
- [Proposed] Interpret net-clinical-benefit and other exploratory analyses descriptively, after their definitions are finalized. **Rationale:** Avoid assigning confirmatory meaning to incompletely specified exploratory endpoints. **Assumption:** No separate confirmatory allocation of alpha is intended.

### 5.6 Harms

- [Provided] Major bleeding is the principal safety outcome; CRNM bleeding is the secondary safety outcome. Safety events are centrally adjudicated, and final analyses use adjudicated results.
- [Provided] Potential AEs are elicited at all contacts, including the scheduled post-treatment observation visit.
- [Clarification Required] Major-bleeding and CRNM-bleeding definitions, event-date conventions, recurrent-bleeding rules, and classification precedence are unspecified. These are essential for reproducible safety endpoints and avoidance of inappropriate double counting.
- [Clarification Required] The safety risk window, any post-dose attribution interval, and the relationship between intended treatment limits and the 30±7-day observation visit are unspecified. The observation-visit timing alone does not establish which events enter each safety analysis.
- [Proposed] Once the safety window is finalized, report participants with at least one event, event counts, proportions with descriptive 95% CIs, and exposure-adjusted rates by treatment. **Rationale:** Describe both participant-level risk and event burden when exposure can differ. **Assumption:** Reliable exposure and event dates are available.
- [Proposed] Describe serious AEs, fatal events, AEs leading to interruption or discontinuation, and bleeding location and severity where collected. **Rationale:** Broaden safety interpretation beyond the two bleeding endpoints. **Assumption:** These attributes are captured consistently.
- [Clarification Required] AE and serious-AE definitions, grading and coding systems, causality assessment, expedited reporting requirements, and safety oversight responsibilities are unspecified. These decisions are needed for consistent collection and timely participant protection.
- [Proposed] Treat comparative safety estimates as descriptive unless a separate testing plan is approved; do not interpret nonsignificance as evidence of equal safety. **Rationale:** No safety-specific power or confirmatory multiplicity plan is supplied. **Assumption:** Safety objectives remain incidence documentation.

### 5.7 Software and References

- [Provided] Sample-size calculations used a SAS macro and three-arm simulations, including 10,000 simulated trials.
- [Clarification Required] Final statistical software, versions, macro implementations, and any event-coding dictionary versions are unspecified. These must be documented to make analyses reproducible.
- [Proposed] Maintain version-controlled analysis code, a derivation specification, independent validation of primary results, and an auditable record of SAP amendments. **Rationale:** Support traceability and reproducibility. **Assumption:** Validated computing and quality-control resources are available.

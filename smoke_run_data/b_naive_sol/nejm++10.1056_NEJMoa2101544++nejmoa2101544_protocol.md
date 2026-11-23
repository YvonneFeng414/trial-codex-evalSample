# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

**[Provided]** This phase 3 study evaluates Ad26.COV2.S for prevention of SARS-CoV-2-mediated COVID-19 in adults aged ≥18 years. Ad26.COV2.S is a recombinant, replication-incompetent adenovirus type 26 vector encoding the SARS-CoV-2 spike protein.

### 1.2 Objectives

- **[Provided]** **Primary objective and outcomes:** Demonstrate efficacy of Ad26.COV2.S versus placebo against first molecularly confirmed moderate-to-severe/critical COVID-19 in SARS-CoV-2-seronegative adults, assessing onset ≥Day 15 and onset ≥Day 29 separately.
- **[Provided]** **Secondary efficacy objectives and outcomes:** Evaluate severe/critical COVID-19; moderate-to-severe/critical COVID-19 regardless of baseline serostatus; disease from Day 2; COVID-19 requiring medical intervention; viral RNA load; mild COVID-19; FDA-harmonized COVID-19; burden of symptomatic disease; asymptomatic/undetected infection; and all SARS-CoV-2 infection.
- **[Provided]** **Safety and immunogenicity objectives and outcomes:** Evaluate SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, unsolicited AEs, and immunogenicity.
- **[Provided]** **Exploratory objectives and outcomes:** Explore viral load, immune correlates, functional/molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** This is a randomized, double-blind, placebo-controlled phase 3 study in adults aged ≥18 years, with individual allocation in a 1:1 ratio to Ad26.COV2.S or placebo.
- **[Provided]** Group 1 receives one Day-1, 0.5-mL injection containing Ad26.COV2.S 5×10^10 viral particles, supplied at 1×10^11 viral particles/mL.
- **[Provided]** Group 2 receives one Day-1, 0.5-mL injection of 0.9% sodium chloride placebo.
- **[Clarification Required]** Confirm the administration route, injection-site procedures, preparation instructions, and accountability requirements; these are necessary for standardized intervention delivery.
- **[Proposed]** Conceal treatment allocation until assignment and maintain masking of participants, investigators, outcome assessors, and analysis personnel wherever operationally feasible. Rationale: prevent selection, ascertainment, and analytical bias. Assumption: preparation and administration can preserve masking despite any product differences.
- **[Clarification Required]** Define who may access treatment codes, emergency-unblinding procedures, and any planned general unblinding or access to other COVID-19 vaccines; these decisions affect masking, follow-up, and efficacy estimands.

### 2.2 Randomization

- **[Provided]** A central computer-generated randomization schedule is prepared before the study under sponsor supervision using randomly permuted blocks. No minimization is reported.
- **[Provided]** Randomization is stratified by vaccination unit, comprising site or mobile unit; age, ≥18 to <60 versus ≥60 years; and absence or presence of comorbidities associated or potentially associated with progression to severe COVID-19.
- **[Clarification Required]** Specify block sizes, whether block sizes vary, the allocation implementation system, and the operational classification of comorbidities; these details are needed to reproduce randomization and protect allocation concealment.
- **[Proposed]** Restrict access to block-size information and maintain an auditable record of allocation requests and assignments. Rationale: preserve unpredictability and verify implementation. Assumption: the central allocation system supports access controls and audit trails.

### 2.3 Sample Size

- **[Provided]** After Protocol Amendment 3, planned enrollment is approximately 40,000 participants, reduced from a previous maximum of approximately 60,000 on the basis of observed/modelled incidence.
- **[Provided]** Sample-size calculations concern first molecularly confirmed moderate-to-severe/critical COVID-19 in per-protocol (PP) participants, separately for onset ≥Day 15 and ≥Day 29. The endpoint is a time-to-first-event/incident-case endpoint.
- **[Provided]** The design uses null VE of 30%, alternative VE of 60%, and one-sided significance of 2.5%. The target is VE 60% against a null lower bound of 30%, not non-inferiority or equivalence.
- **[Provided]** Planned power is approximately 90%; power under the truncated sequential probability ratio test through 154 events is 86.22% at VE 60%.
- **[Provided]** The statistical framework is a truncated sequential probability ratio test (SPRT), using conditional exact binomial event allocation, beginning at the 20th event. The stated requirement is 154 total co-primary events.
- **[Clarification Required]** Confirm how the 154-event requirement applies to the two overlapping co-primary event sets. It must not be interpreted as 154 events per endpoint or as an arithmetic sum across endpoints without confirmation, because this determines monitoring and information maturity.
- **[Provided]** Incidence assumptions are 1.4% moderate/severe disease during the first 3 months, a 50% reduction in month 4, a 62% reduction thereafter, and 10% seroprevalence. Later epidemiologic modeling supported enrollment reduction to approximately 40,000.
- **[Provided]** No continuous-outcome variability parameter or numerical dropout/non-adherence inflation is reported. Epidemiologic uncertainty and potential dropouts informed maximum enrollment. A clustering design effect is not applicable because randomization is individual.
- **[Provided]** Enrollment is intended to support a high probability of an efficacy signal within 8 months and sufficient likelihood of observing five placebo severe cases.

### 2.4 Hypothesis Framework

- **[Provided]** For each co-primary onset window, the hypotheses are H0: VE≤30% versus H1: VE>30%, tested at one-sided 2.5%.
- **[Provided]** Primary success requires both co-primary tests to succeed. In addition, for each timing window, the severe/critical COVID-19 VE point estimate must be ≥50%, with at least five placebo severe/critical events.
- **[Derived]** Primary success is conjunctive: rejection for only one co-primary endpoint is insufficient.
- **[Provided]** Conditional on primary success, confirmatory secondary hypotheses are H0: VE≤0% versus H1: VE>0%, controlled through a graphical multiple-testing procedure.
- **[Provided]** The graphical sequence evaluates burden of symptomatic disease (BOD), medical intervention, all infection, and asymptomatic/undetected infection, subject to their endpoint/population windows.
- **[Clarification Required]** Supply the graphical testing diagram, initial alpha allocations, transfer weights, endpoint ordering, and endpoint/population windows. These determine which secondary claims are confirmatory and when alpha becomes available.

### 2.5 Statistical Interim Analyses

- **[Provided]** The primary efficacy design uses a truncated SPRT within a conditional exact binomial framework, beginning at the 20th event and extending through 154 events.
- **[Provided]** Secondary alpha is based on a single-interim Pocock/Wang–Tsiatis design with Δ=.5, using an information fraction derived from Day-29 primary events against the 154-event target.
- **[Provided]** The medical-intervention rationale uses 23 events. Testing all infection requires at least 15,000 available Day-71 samples. Asymptomatic-infection testing requires all participants to have ≥6-month follow-up.
- **[Clarification Required]** Provide the SPRT stopping boundaries, terminal rejection rule, event-review cadence, treatment of event overruns, and any futility provisions. The supplied event counts and power do not uniquely determine an executable sequential test.
- **[Clarification Required]** Specify the secondary information-fraction calculation, spending-function implementation, and treatment of endpoints whose maturity requirements are unmet; these affect available alpha and valid testing times.
- **[Clarification Required]** Define monitoring governance, access to unblinded results, and safety stopping or pause rules. These decisions are necessary to implement efficacy monitoring without compromising masking or participant protection.
- **[Proposed]** Preserve an audit trail of event snapshots, adjudication status, boundary calculations, and monitoring recommendations. Rationale: allow verification of sequential decisions. Assumption: monitoring datasets and analysis code can be version-controlled.

### 2.6 Timing of Analyses

- **[Provided]** Co-primary efficacy windows begin at Day 15 and Day 29.
- **[Provided]** An efficacy signal before 8-week median follow-up triggers an analysis at that median-follow-up timepoint.
- **[Provided]** Final analysis follows the last participant’s month-12 visit or earlier discontinuation. End-of-study analysis follows completion of all month-24 visits or earlier discontinuation.
- **[Provided]** Electronic clinical outcome assessment (eCOA) symptom surveillance occurs at least twice weekly until the later of year 1 or primary analysis, then every 2 weeks. Symptomatic episodes trigger serial testing and procedures.
- **[Provided]** Immunogenicity Subset sampling occurs at baseline, Day 29, Day 71, month 6, year 1, month 18, and year 2.
- **[Provided]** Asymptomatic-infection serology occurs at baseline, Day 71, month 6, and year 1.
- **[Clarification Required]** Define “efficacy signal,” the median-follow-up calculation, and whether the triggered analysis is a confirmatory look or an additional maturity analysis; these affect sequential error control.
- **[Clarification Required]** Specify data cutoffs, database-lock requirements, adjudication completion rules, and handling of late-arriving results for each analysis. These determine which cases and follow-up contribute.
- **[Proposed]** Establish analysis-specific data snapshots and finalize applicable analysis specifications before unblinded access. Rationale: prevent outcome-dependent analytical changes. Assumption: operational timelines permit prospective specification.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** Each co-primary hypothesis uses one-sided 2.5% significance. Confirmatory secondary inference is conditional on primary success and governed by the graphical procedure and interim alpha allocation.
- **[Proposed]** Report VE estimates with two-sided 95% confidence intervals for descriptive interpretation, explicitly distinguishing them from decision-compatible sequential or multiplicity-adjusted bounds. Rationale: communicate precision without implying that ordinary intervals determine sequential success. Assumption: suitable interval methods are available.
- **[Proposed]** Base confirmatory conclusions on the specified sequential boundaries and graphical testing rules; where feasible, report confidence bounds and p-values obtained from the corresponding testing procedures. Rationale: align inference with repeated looks and multiplicity. Assumption: the final boundary and graph specifications support valid inversion or adjusted p-value calculation.
- **[Proposed]** Treat analyses outside the confirmatory graph as descriptive or exploratory unless prospectively assigned an error-controlled role. Rationale: avoid overstating evidence from multiple analyses. Assumption: no additional confirmatory allocation is approved before unblinding.
- **[Clarification Required]** Specify numerical precision, boundary-comparison conventions, and rounding rules; these matter when results are close to a rejection boundary or the severe/critical VE threshold.

### 3.2 Protocol Deviations

- **[Proposed]** Identify and classify deviations before unblinding, including eligibility violations, incorrect intervention, prohibited therapies or vaccines, missed assessments, and deviations affecting endpoint ascertainment. Rationale: support consistent reporting and PP membership. Assumption: source records permit blinded classification.
- **[Clarification Required]** Define which deviations exclude participants or follow-up from PP analyses, including permissible visit and sampling windows. These decisions can change the primary risk sets and event counts.
- **[Proposed]** Summarize deviations by randomized group and retain randomized participants in randomized-assignment sensitivity analyses regardless of deviations. Rationale: assess robustness to post-randomization exclusions. Assumption: outcome collection remains available and permitted.

### 3.3 Analysis Populations

- **[Provided]** Primary objectives concern SARS-CoV-2-seronegative adults, and sample-size calculations use PP participants. A secondary objective evaluates moderate-to-severe/critical COVID-19 regardless of baseline serostatus.
- **[Clarification Required]** Confirm the formal primary analysis population and the complete PP definition. In particular, specify required vaccination, baseline serology, baseline molecular-test status, compliance, and handling of infections before each efficacy window; these determine the population to which efficacy applies.
- **[Proposed]** Use a baseline-seronegative PP population for the principal efficacy analysis, pending confirmation. Rationale: align the stated primary objective with the sample-size calculation. Assumption: PP efficacy was intended as the primary analysis.
- **[Proposed]** Define a full randomized population for assignment-based sensitivity analyses and a safety population comprising participants receiving any study injection, analyzed by treatment received. Rationale: separate randomized efficacy assessment from actual exposure-based safety assessment. Assumption: treatment receipt and assignment are reliably documented.
- **[Clarification Required]** Specify membership and selection procedures for immunogenicity, reactogenicity, virologic, and other exploratory subsets, and the population for each secondary endpoint. These choices affect selection bias, denominators, and generalizability.
- **[Proposed]** Provide participant counts and reasons for exclusion from every analysis population. Rationale: make differences between populations transparent. Assumption: exclusions can be assigned reproducible reasons.

## 4. Trial Population

### 4.1 Screening Data

- **[Proposed]** Maintain a screening and disposition log covering consent, screening, eligibility, randomization, vaccination, analysis inclusion, follow-up completion, and discontinuation, with reasons where available. Rationale: characterize selection and attrition. Assumption: collection is permitted by consent and applicable privacy requirements.
- **[Proposed]** Summarize screening failures by reason without assigning nonrandomized participants to treatment groups. Rationale: describe recruitment without creating artificial treatment comparisons. Assumption: screening-failure information is collected consistently.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Inclusion requires age ≥18 years, informed consent, ability to comply with study procedures, verifiable identity/contactability, and ability to complete eCOA questionnaires.
- **[Provided]** Where applicable, illness must be stable/well controlled and medication doses stable for ≥12 weeks.
- **[Provided]** Participants of childbearing potential require protocol-compliant contraception from consent through 3 months after vaccination. Hormonal contraception must have been initiated ≥28 days before vaccination.
- **[Provided]** Highly sensitive urine pregnancy tests must be negative at screening and immediately before vaccination. Blood/bone-marrow donation is prohibited through 3 months after vaccination.
- **[Provided]** Exclusions include acute clinically significant illness or temperature ≥38.0°C within 24 hours; serious vaccine/excipient allergy or anaphylaxis; immunologically relevant autoimmune disease or immunodeficiency; chronic/recurrent systemic corticosteroids; and antineoplastic/immunomodulating therapy or radiotherapy.
- **[Provided]** Exclusions include immunoglobulin within 3 months, blood products within 4 months, live vaccine within 28 days, non-live vaccine within 14 days, prior coronavirus vaccine, and recent investigational drug/device/vaccine.
- **[Provided]** Exclusions include pregnancy, breastfeeding or pregnancy plans; a condition compromising safety or assessments; contraindication to intramuscular injection or blood draw; uncontrolled HIV; serious psychiatric illness/substance abuse; and inability to communicate or adhere.
- **[Provided]** Additional exclusions concern stage-specific high-risk comorbidities, recent malignancy, acute polyneuropathy, surgery, or active hepatitis.
- **[Provided]** Ocular, topical, or inhaled steroids and stable non-immunomodulator treatment may be permitted. Smoking is not a comorbidity.
- **[Clarification Required]** Provide the stage-specific restrictions, definitions of stable disease and uncontrolled HIV, relevant disease lists, timing for “recent” exposures or conditions, and permitted-treatment rules. These are needed for reproducible eligibility assessment.
- **[Clarification Required]** Specify the contraception methods and definition of childbearing potential; these determine consistent application of reproductive eligibility requirements.

### 4.3 Recruitment

- **[Provided]** Recruitment targets approximately 40,000 participants after Protocol Amendment 3, with vaccination units comprising sites or mobile units.
- **[Clarification Required]** Specify recruitment locations, dates, recruitment stages, and any demographic or clinical enrollment targets; these affect feasibility, representativeness, and interpretation across epidemic settings.
- **[Proposed]** Monitor recruitment and retention across the randomization strata without inventing enrollment quotas. Rationale: identify operational imbalances while preserving the supplied design. Assumption: stratum-level recruitment data are available.

### 4.4 Withdrawal and Follow-up

- **[Proposed]** Distinguish discontinuation of intervention, withdrawal from assessments, loss to follow-up, and withdrawal of permission for further data collection. Rationale: these events have different safety and statistical consequences. Assumption: consent and records allow their separate documentation.
- **[Proposed]** Continue scheduled outcome and safety follow-up after intervention nonadherence when participants remain willing and authorized to participate. Rationale: reduce informative attrition and retain safety information. Assumption: continued contact is ethically and operationally permitted.
- **[Clarification Required]** Define follow-up after unblinding, receipt of a nonstudy vaccine, SARS-CoV-2 infection, pregnancy, or major illness, including permissible use of previously collected data. These decisions affect estimands, censoring, and safety completeness.
- **[Clarification Required]** Define “discontinuation” for the MAAE-leading-to-discontinuation endpoint in this single-injection study; discontinuation of vaccination and discontinuation of study participation are not interchangeable.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize baseline characteristics by randomized group and relevant analysis population, emphasizing randomization factors, serostatus, and available demographic and clinical characteristics. Use counts/percentages for categorical variables and suitable distribution summaries for continuous variables. Rationale: describe comparability and applicability. Assumption: these variables are collected.
- **[Proposed]** Report missing baseline values explicitly and avoid significance tests of randomized-group baseline differences. Rationale: descriptive reporting is more informative than chance-driven baseline testing. Assumption: randomization was implemented as intended.
- **[Clarification Required]** Confirm the baseline variable list, reference time, laboratory assays, and derivation rules; these are necessary to produce consistent tables and subgroup classifications.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The two co-primary outcomes are first molecularly confirmed moderate-to-severe/critical COVID-19 with onset ≥Day 15 and, separately, onset ≥Day 29, comparing Ad26.COV2.S with placebo in baseline-seronegative adults.
- **[Provided]** Success additionally requires severe/critical VE ≥50% and at least five placebo severe/critical events in each corresponding timing window.
- **[Clarification Required]** Specify the clinical severity definitions, qualifying molecular assays, symptom-onset algorithm, confirmation requirements, and adjudication process. These determine which illnesses count as primary and severe/critical events.
- **[Clarification Required]** Define whether earlier infection or disease removes a participant from a later risk set, how recurrent episodes are distinguished, and whether a pre-window illness that worsens later qualifies. These decisions are necessary to operationalize “first” disease in each onset window.
- **[Proposed]** Report, separately for each window, participants at risk, qualifying cases, person-time, incidence rates, VE estimates, uncertainty intervals, and formal decision results. Rationale: make the efficacy result and its exposure base transparent. Assumption: onset dates and follow-up durations are sufficiently complete.
- **[Clarification Required]** Finalize the primary estimand, including treatment condition, analysis population, endpoint, follow-up horizon, effect measure, and handling of intercurrent events. Nonstudy vaccination, unblinding, death, and early infection may materially change interpretation.

### 5.2 Secondary Outcomes

- **[Provided]** Secondary disease outcomes include severe/critical COVID-19, moderate-to-severe/critical COVID-19 regardless of baseline serostatus, disease from Day 2, COVID-19 requiring medical intervention, mild COVID-19, FDA-harmonized COVID-19, and burden of symptomatic disease.
- **[Provided]** Secondary virologic outcomes include viral RNA load, asymptomatic/undetected infection, and all SARS-CoV-2 infection.
- **[Provided]** Secondary safety and immunogenicity outcomes include SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, unsolicited AEs, and immunogenicity.
- **[Provided]** Confirmatory secondary testing evaluates BOD, medical intervention, all infection, and asymptomatic/undetected infection through the graphical procedure. Its maturity provisions include the 23-event medical-intervention rationale, ≥15,000 available Day-71 samples for all-infection testing, and ≥6-month follow-up for all participants for asymptomatic-infection testing.
- **[Clarification Required]** Define each secondary endpoint’s severity criteria, onset window, population, follow-up horizon, and whether it concerns first or recurrent events. The broader objective list does not establish these operational details.
- **[Clarification Required]** Supply the FDA-harmonized case definition, medical-intervention categories, and BOD scoring and aggregation rules. These determine the clinical meaning and statistical scale of those endpoints.
- **[Clarification Required]** Specify how molecular results and serology establish all infection and asymptomatic/undetected infection, including assay targets, positivity thresholds, vaccination-related assay interpretation, and interval timing. These decisions affect infection classification and event dates.
- **[Clarification Required]** Define immunogenicity assays, reporting units, seroresponse thresholds, and primary immunogenicity summaries. The sampling schedule alone does not determine the outcomes.

### 5.3 Analysis Methods

- **[Provided]** Primary testing uses the truncated SPRT with conditional exact binomial event allocation.
- **[Proposed]** Estimate incidence-based VE as \(100(1-\widehat{RR})\%\), where \(\widehat{RR}=(C_V/T_V)/(C_P/T_P)\), \(C\) denotes qualifying cases, and \(T\) denotes at-risk person-time. Rationale: account for possible exposure differences between groups. Assumption: an incidence-rate ratio is the intended effect measure and exposure is sufficiently comparable.
- **[Proposed]** If the conditional event-allocation implementation adjusts for person-time, use \(p(r)=rT_V/(rT_V+T_P)\), where \(r\) is the assumed vaccine-to-placebo incidence-rate ratio. Under this specification, the null and planning alternative use \(r=0.70\) and \(r=0.40\), respectively. Rationale: connect VE assumptions to conditional event allocation. Assumption: independent Poisson event counts adequately describe the comparison; this implementation requires confirmation.
- **[Clarification Required]** Confirm the protocol’s VE estimator and whether the sequential calculation uses equal exposure, person-time adjustment, or another allocation parameterization. These alternatives need not produce identical boundaries or estimates.
- **[Proposed]** After window-specific risk-set rules are approved, accrue person-time from the applicable window start until a qualifying first event or the approved end-of-observation condition. Rationale: align exposure with event eligibility. Assumption: entry and censoring dates are ascertainable.
- **[Clarification Required]** Specify treatment of death, loss to follow-up, nonstudy vaccination, and unblinding in the primary analysis. These may require censoring, competing-risk methods, or a different estimand rather than a single default rule.
- **[Proposed]** Support primary inference with time-to-event displays and adjusted sensitivity analyses incorporating randomization factors where estimable. Rationale: examine timing and robustness without replacing the specified exact sequential test. Assumption: sufficient events and reliable factor coding are available.
- **[Proposed]** For sparse outcomes, retain exact methods where appropriate and report non-estimability rather than forcing finite estimates when both groups have no events. Rationale: avoid misleading precision. Assumption: endpoint counts have been finalized.
- **[Proposed]** Summarize viral RNA measurements by clinically relevant scheduled time relative to episode onset, using distributions and longitudinal summaries compatible with the assay scale. Rationale: characterize viral kinetics. Assumption: sampling times and quantification limits are available; comparisons restricted to infected participants are exploratory rather than automatically causal.
- **[Proposed]** Summarize positive, right-skewed immunogenicity measures using geometric summaries and fold changes, with longitudinal comparisons when supported by the assay. Rationale: accommodate common assay distributions. Assumption: values can validly be analyzed on a logarithmic scale.
- **[Clarification Required]** Specify limits-of-quantification handling, assay batch adjustment, repeated-measure models, and transformation rules for laboratory outcomes. These choices affect quantitative conclusions.
- **[Proposed]** Apply each confirmatory secondary test only when its primary gate, graphical alpha allocation, endpoint window, and maturity condition are satisfied. Rationale: preserve the stated testing architecture. Assumption: the complete graphical procedure is finalized before testing.

### 5.4 Missing Data

- **[Proposed]** Summarize missing baseline data, missed surveillance, unavailable specimens, incomplete episode testing, and missing outcome assessments by group and reason. Rationale: distinguish missingness mechanisms and assess potential bias. Assumption: collection status and reasons are recorded.
- **[Proposed]** Do not equate absent questionnaires, missing molecular tests, or unavailable serology with absence of disease or infection. Rationale: missing assessments do not establish a negative outcome. Assumption: alternative ascertainment sources can be identified where available.
- **[Clarification Required]** Specify handling of missing or indeterminate baseline serostatus and incomplete molecular confirmation. These decisions affect primary population membership and case classification.
- **[Proposed]** For time-to-event analyses, use documented outcome-observation periods and assess sensitivity to potentially informative loss to follow-up. Rationale: avoid assigning unsupported event-free exposure. Assumption: the last reliable observation date can be identified.
- **[Proposed]** Use scenario-based sensitivity analyses for unresolved suspected cases and missing infection assessments, including scenarios unfavorable to the vaccine where clinically plausible. Rationale: assess robustness to differential ascertainment. Assumption: plausible ranges can be specified without using treatment effects to select them.
- **[Proposed]** For longitudinal laboratory or patient-reported outcomes, use model-based analyses or multiple imputation where justified, accompanied by sensitivity analyses for departures from missing-at-random assumptions. Rationale: retain information while acknowledging unverifiable missingness assumptions. Assumption: adequate predictors and a defensible model are available.
- **[Clarification Required]** Define endpoint-specific imputation and sensitivity scenarios before unblinding; otherwise, results could depend on post hoc choices.

### 5.5 Additional Analyses

- **[Provided]** Exploratory domains include viral load, immune correlates, functional/molecular antibody characteristics, transcriptomics, patient-reported symptoms, frailty, and clinical disease severity.
- **[Proposed]** Explore treatment-effect heterogeneity using randomization factors and baseline serostatus, emphasizing interaction estimates and uncertainty rather than separate within-subgroup significance claims. Rationale: assess consistency while limiting overinterpretation. Assumption: subgroup sizes and events permit estimation.
- **[Proposed]** Compare principal efficacy results with randomized-assignment analyses and alternative defensible handling of early infection, nonstudy vaccination, and loss to follow-up. Rationale: assess dependence on PP selection and intercurrent-event assumptions. Assumption: relevant follow-up is available.
- **[Proposed]** Treat immune-correlate, transcriptomic, and antibody-characterization analyses as exploratory association analyses, with prespecified covariate adjustment and multiplicity reporting. Rationale: high-dimensional associations do not independently establish causality or protection thresholds. Assumption: specimen selection and assay quality can be characterized.
- **[Clarification Required]** Specify exploratory specimen-selection schemes, frailty and symptom instruments, disease-severity measures, model specifications, and multiplicity strategy. These are needed to make exploratory analyses reproducible.

### 5.6 Harms

- **[Provided]** Safety evaluation covers SAEs, MAAEs, MAAEs leading to discontinuation, reactogenicity, and unsolicited AEs.
- **[Clarification Required]** Define adverse-event categories, coding terminology, severity grades, seriousness and relatedness rules, collection windows, solicited-event instruments, and applicable subset populations. These determine safety denominators and comparable event ascertainment.
- **[Proposed]** Summarize participants with events and total events by treatment received, category, severity, relatedness, and relevant collection period; report deaths and discontinuations separately. Rationale: distinguish participant-level risk from recurrent-event burden. Assumption: exposure and event records are complete enough for classification.
- **[Proposed]** Present absolute risks and between-group risk differences with suitable confidence intervals for selected safety outcomes, using exposure-adjusted summaries when follow-up differs materially. Rationale: communicate clinical magnitude and unequal observation. Assumption: the selected comparison and observation window are meaningful for each event type.
- **[Proposed]** Review serious and medically attended events throughout follow-up under an approved safety process, with urgent escalation of clinically important findings. Rationale: participant protection cannot depend solely on scheduled efficacy analyses. Assumption: responsible clinical reviewers and reporting pathways are established.
- **[Clarification Required]** Specify pregnancy follow-up, expedited reporting obligations, adverse events of special interest, and safety pause criteria. These operational and clinical decisions are not supplied and are necessary for a complete safety plan.

### 5.7 Software and References

- **[Provided]** SPRT boundary code uses gsDesign version 3.1.1. Other sample-size software is not specified.
- **[Clarification Required]** Specify software, versions, packages, validated programs, and numerical settings for all remaining analyses. These are needed for reproducibility and numerical verification.
- **[Proposed]** Version-control analysis programs, record execution environments and random seeds where applicable, and independently verify confirmatory boundaries, event counts, and testing decisions. Rationale: reduce implementation error and support reproducibility. Assumption: independent review and controlled computational environments are available.

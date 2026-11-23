# Clinical Study Protocol and Statistical Analysis Framework

## 1. Introduction

### 1.1 Background and Rationale

- **[Provided]** Noninfectious intermediate-, posterior-, and pan-uveitis may threaten vision. Sustained corticosteroid exposure carries ocular and systemic risks.
- **[Provided]** This final analysis evaluates steroid-sparing maintenance adalimumab against placebo in active disease.

### 1.2 Objectives

- **[Provided]** P1 is to evaluate the efficacy and safety of adalimumab versus placebo as maintenance therapy in subjects requiring high-dose corticosteroids for active noninfectious intermediate-, posterior-, or pan-uveitis.
- **[Provided]** Ranked secondary efficacy endpoints and their confirmatory testing sequence are specified, but secondary objectives are not separately labeled.
- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory; exploratory objectives are not separately labeled.

## 2. Study Methods

### 2.1 Trial Design

- **[Provided]** The parent study is phase 3, randomized, double-masked, placebo-controlled, and multicenter, with 1:1 allocation. These analyses cover the non-Japan parent study; there is a separate Japan sub-study.
- **[Provided]** Adalimumab is administered as 80 mg subcutaneously at Baseline, followed by 40 mg subcutaneously every other week beginning Week 1. The comparator is matching placebo loading and every-other-week doses.
- **[Provided]** All continuing subjects received a standardized 60-mg/day prednisone burst at entry, with mandatory taper and discontinuation by Week 15. Topical corticosteroids were tapered per protocol.
- **[Clarification Required]** The detailed prednisone and topical corticosteroid taper schedules are needed to assess adherence and deviations.

### 2.2 Randomization

- **[Provided]** Eligible subjects were randomized through IVRS/IWRS. The AbbVie Deutschland Statistics Department prepared the schedule.
- **[Provided]** Randomization was stratified by Baseline immunosuppressant (IMM) usage. Japanese subjects were randomized in a separate stratum without IMM stratification.
- **[Provided]** Randomization was not stratified by site; an adequate block size was used.
- **[Clarification Required]** The block size, IMM stratum definitions, and rules for resolving discrepant stratification data are needed for reproducible implementation and analysis.

### 2.3 Sample Size

- **[Provided]** Approximately 234 patients were planned to obtain 138 treatment-failure events. The calculation used a two-sided 5% log-rank test with 90% power.
- **[Provided]** Assumed six-month treatment-failure rates were 70% for placebo and 50% for adalimumab, an absolute difference of 20 percentage points.
- **[Provided]** Failures were conservatively assumed to begin after two months as prednisone reached lower doses. Pooled dropout was assumed to be 35% over 12 months.
- **[Provided]** Accrual was assumed to average four subjects per month for the first 30 months and seven per month thereafter. Calculations across sample sizes using the stated assumptions indicated approximately 234 patients to achieve 138 events.
- **[Provided]** The calculation used East5 Version 5.2.0.0. No non-inferiority or equivalence margin or clustering design effect applied to this individually randomized superiority comparison.
- **[Clarification Required]** Whether sample size re-estimation or amendments occurred, and whether the planned 234 subjects and 138 events apply specifically to the non-Japan analysis, must be confirmed to interpret the final analysis against the plan.

### 2.4 Hypothesis Framework

- **[Provided]** The primary time-to-treatment-failure endpoint and ranked secondary endpoints are tested two-sided at 0.05. Ranked testing begins only if the primary endpoint is significant; each preceding ranked endpoint must be significant before the next is tested, controlling the two-sided 5% multiple significance level.
- **[Proposed]** For the primary log-rank comparison, test equality of the treatment-failure survival distributions against a two-sided difference. This matches the specified test; it assumes the endpoint and censoring rules are finalized.
- **[Clarification Required]** The exact ranked secondary endpoints and their order are needed to implement the confirmatory sequence.

### 2.5 Statistical Interim Analyses

- **[Clarification Required]** Whether any interim efficacy analyses occurred or were planned, and any associated stopping or alpha-spending rules, must be determined because they could affect the final significance threshold.
- **[Proposed]** If no efficacy interim analysis occurred, use the stated two-sided 0.05 level at the final primary analysis. This preserves the specified level under that assumption.

### 2.6 Timing of Analyses

- **[Provided]** Analyses occur after parent-study termination. The final efficacy value is from the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure.
- **[Provided]** Assessments occur at Baseline, Week 1, Week 4, and then every four weeks, with Week 27 replacing Week 28. Treatment failure is assessed at Week 6 and later visits.
- **[Provided]** Analysis windows run through Week 80 by Rx day. The assessment closest to the nominal day is used; ties use the latest assessment.
- **[Clarification Required]** The Week 6 assessment schedule, Rx-day definition, window boundaries, data cutoff, database-lock requirements, and data-readiness criteria are needed to assign assessments and finalize the analysis dataset.
- **[Proposed]** Finalize programmed datasets after documented data review and database lock. This supports reproducibility, assuming a study-specific cutoff and lock procedure are approved.

## 3. Statistical Principles

### 3.1 Significance and Confidence Intervals

- **[Provided]** Confirmatory tests use a two-sided 0.05 level within the specified hierarchy. Other efficacy, sensitivity, and subgroup analyses are exploratory.
- **[Proposed]** Report two-sided 95% confidence intervals for estimable treatment effects and use \(p \leq 0.05\) for confirmatory significance. This aligns with the stated level, assuming no interim adjustment is required.

### 3.2 Protocol Deviations

- **[Proposed]** Classify important deviations before unmasking and summarize them by randomized treatment. This limits analysis-selection bias, assuming deviation data are available.
- **[Clarification Required]** The study-specific definition of important deviations and any exclusions they trigger require agreement because they affect analysis populations and sensitivity analyses.

### 3.3 Analysis Populations

- **[Proposed]** Use all randomized non-Japan parent-study subjects, analyzed as randomized, for the primary efficacy analysis. This preserves randomized comparisons, assuming the non-Japan population can be identified reliably.
- **[Proposed]** Use non-Japan parent-study subjects receiving at least one dose, analyzed by treatment received, for safety. This relates harms to exposure, assuming actual treatment is reliably recorded.
- **[Clarification Required]** The prespecified population definitions and treatment assignment rules for dosing errors must be confirmed because they determine denominators and group comparisons.

## 4. Trial Population

### 4.1 Screening Data

- **[Provided]** Screening health evaluation includes medical history, laboratory profile, physical examination, chest radiograph, and ECG.
- **[Proposed]** Summarize numbers screened, randomized, and not randomized, with available reasons. This describes selection, assuming screening disposition data are collected.

### 4.2 Eligibility Criteria Summary

- **[Provided]** Eligible subjects are aged at least 18 years and have noninfectious intermediate-, posterior-, or pan-uveitis.
- **[Provided]** Active disease must be present in either eye despite at least two weeks of stable prednisone at least 10 mg/day or equivalent. Active disease is defined by an active chorioretinal or retinal vascular lesion, OCT macular edema with intraocular inflammation, anterior chamber cells at least 2+, or vitreous haze at least 2+.
- **[Provided]** Inclusion also requires appropriate contraception and negative pregnancy tests, injection capability, consent and compliance, and specified TB testing or therapy conditions.
- **[Provided]** Exclusions include isolated anterior or infectious uveitis and inadequate response or intolerance to high-dose steroids.
- **[Provided]** Ocular exclusions include POHS, ocular masquerade or serpiginous disease, pupil-dilation limitation, fundus-obscuring opacity or cataract need, and specified glaucoma, BCVA, demyelination, retinopathy, macular disease, vitreoretinal-interface, or recent or planned eye-surgery conditions.
- **[Provided]** Exclusions also include prior anti-TNF or biologic, cyclophosphamide, chlorambucil, or steroid implant exposure; unstable, multiple, prohibited, or excessive immunosuppression; local steroids within 90 days; and recent investigational drugs.
- **[Provided]** Infection-related exclusions include prohibited infections, TB, hepatitis B, HIV, immunodeficiency or anti-infective treatment, and positive syphilis or Lyme tests.
- **[Provided]** Other exclusions include selected cardiovascular or neurologic history, hypersensitivity, pregnancy or breastfeeding, malignancy, drug or alcohol abuse, significant screening laboratory abnormalities, and investigator unsuitability.
- **[Clarification Required]** The detailed thresholds, prohibited treatments, time periods, and TB, contraception, and ocular-condition definitions are needed to apply these summarized criteria consistently.

### 4.3 Recruitment

- **[Provided]** The sample-size assumptions included average accrual of four subjects per month for the first 30 months and seven per month thereafter.
- **[Clarification Required]** Actual recruitment dates, sites, and enrollment totals are needed for the final disposition and recruitment summary.
- **[Proposed]** Summarize actual enrollment by site and treatment without using site as a randomization stratum. This describes recruitment, assuming site identifiers are available.

### 4.4 Withdrawal and Follow-up

- **[Provided]** The final efficacy value is the treatment-failure visit, Early Termination Visit, or Week 80 Visit if no failure.
- **[Proposed]** Record treatment discontinuation separately from study withdrawal and seek outcome and safety follow-up where permitted. This distinguishes exposure from observation, assuming consent and study procedures allow follow-up.
- **[Clarification Required]** Permitted post-discontinuation assessments and withdrawal procedures must be specified because they affect event ascertainment and censoring.

### 4.5 Baseline Characteristics

- **[Proposed]** Summarize demographics, disease characteristics, Baseline IMM use, and relevant corticosteroid exposure by randomized treatment, using available data. This describes comparability, assuming these variables were collected.

## 5. Analysis

### 5.1 Primary Outcomes

- **[Provided]** The primary efficacy endpoint is time to treatment failure. P1 also addresses safety.
- **[Clarification Required]** The treatment-failure components, qualifying assessment rules, event date, time origin, and handling of events or interventions between visits are needed to construct the endpoint.
- **[Clarification Required]** Any prespecified primary safety endpoint or formal safety hypothesis must be identified because safety is part of P1 but no such endpoint or test is supplied.

### 5.2 Secondary Outcomes

- **[Provided]** Ranked secondary efficacy endpoints are confirmatory only in the specified sequence after a significant primary result.
- **[Clarification Required]** Endpoint definitions, measurement times, analysis methods, and the ranking are needed to perform the secondary analyses.
- **[Proposed]** If a gate fails, report subsequent ranked endpoints descriptively without further confirmatory tests. This respects the specified sequence, assuming the endpoint ranking is finalized.

### 5.3 Analysis Methods

- **[Proposed]** Compare time to treatment failure using a log-rank test stratified by Baseline IMM use, with subjects analyzed as randomized. This reflects the design and planned test, assuming usable non-Japan stratum data and finalized event and censoring definitions.
- **[Proposed]** Display Kaplan–Meier curves and report event counts, censoring counts, and estimated six-month failure rates by group. This describes the time course and planning time point, assuming sufficient follow-up and a defined six-month analysis day.
- **[Proposed]** Estimate the adalimumab-to-placebo hazard ratio and 95% confidence interval using a Cox model stratified by Baseline IMM use. This quantifies the treatment contrast, assuming the model is estimable; assess proportional hazards and interpret the ratio cautiously if it is not supported.
- **[Clarification Required]** The final primary test’s stratification, handling of missing or discrepant IMM strata, and precise six-month day definition require confirmation for reproducibility.
- **[Proposed]** Continue efficacy observation after treatment discontinuation when available, unless an intercurrent event itself meets the finalized failure definition. This supports a treatment-policy comparison, assuming post-discontinuation follow-up is permitted.
- **[Clarification Required]** The intended handling of rescue therapy, treatment changes, death, and other intercurrent events must be determined because it defines the treatment effect being estimated.

### 5.4 Missing Data

- **[Proposed]** For subjects without observed failure, censor at the last adequate failure assessment; do not assign an unobserved failure date. This uses available follow-up, assuming adequate assessment and censoring are defined and censoring is suitably noninformative.
- **[Clarification Required]** Rules for subjects without a post-Baseline assessment, missed visits before observed failure, death, and assessments after discontinuation are needed to implement censoring consistently.
- **[Proposed]** Assess missingness and perform sensitivity analyses for plausible departures from noninformative censoring. This evaluates robustness, assuming suitable sensitivity scenarios and data are agreed before unmasking.

### 5.5 Additional Analyses

- **[Provided]** Other efficacy, sensitivity, and subgroup analyses are exploratory.
- **[Proposed]** Examine treatment effects by Baseline IMM use and assess treatment-by-subgroup interaction, reporting estimates and uncertainty rather than confirmatory conclusions. This explores heterogeneity in a randomization factor, assuming subgroup sample sizes permit estimation.
- **[Proposed]** Consider an interval-censoring sensitivity analysis for failures detected at visits and a competing-risk sensitivity analysis for death. These address ascertainment and competing events, assuming their dates and definitions are available.
- **[Clarification Required]** The full prespecified exploratory endpoint, sensitivity, and subgroup lists are needed to distinguish planned analyses from additions.

### 5.6 Harms

- **[Proposed]** Summarize adverse events, serious adverse events, deaths, and events leading to treatment discontinuation by treatment received, including severity and relationship when recorded. This supports the safety objective, assuming these data are collected.
- **[Clarification Required]** Safety event definitions, coding conventions, collection period, and post-dose reporting window are needed to define comparable safety summaries.

### 5.7 Software and References

- **[Provided]** East5 Version 5.2.0.0 was used for the sample-size calculation.
- **[Proposed]** Use validated statistical software and document its name, version, and analysis programs. This supports reproducibility, assuming the final analysis environment is available.

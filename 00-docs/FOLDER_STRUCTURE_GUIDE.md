# FOLDER STRUCTURE GUIDE
## How to Fill Your Data Engineering Journey Folders

**Purpose**: Clear guide for what goes where as you progress through your 36-week roadmap.

---

## OVERVIEW

Your repository has two main organizational systems:
1. **Phase folders** (`01-phase-python/`, `02-phase-sql/`, etc.) - Learning materials organized by phase
2. **Project folders** (`02-projects/`) - Portfolio projects organized by project number

---

## PHASE FOLDERS

### 01-phase-python/ (CURRENT - Weeks 1-8)

**Current Status**: Active learning

```
01-phase-python/
├── bogdan-course/           [IN USE]
│   └── [course exercises organized by topic]
├── early-practice/          [IN USE]
│   └── [experimental code, practice scripts]
├── notes/                   [READY TO USE]
│   ├── confusion-log.md     [CREATE NOW - track confusing concepts]
│   ├── data-structures.md   [Add as you learn - lists, dicts, sets]
│   ├── error-handling.md    [Add as you learn - try/except patterns]
│   ├── functions.md         [Add as you learn - function concepts]
│   ├── file-io.md           [Add as you learn - working with files]
│   ├── loops.md             [Add as you learn - for/while patterns]
│   ├── comprehensions.md    [Add as you learn - list/dict comprehensions]
│   └── cheat-sheet.md       [Quick syntax reference you build]
└── projects/                [OPTIONAL - redundant with /02-projects/]
    └── [Can ignore or use for scratch work]
```

**When to fill:**
- `notes/confusion-log.md` - Create TODAY, update whenever stuck
- Other note files - Create when you complete a Bogdan chapter on that topic
- Add new note files as needed for topics that confuse you

**Review needed**: None - just add files as you learn

---

### 02-phase-sql/ (Weeks 9-16, Start Jan 18)

**Current Status**: Empty - will activate Week 9

```
02-phase-sql/
├── sql-course/              [CREATE Week 9]
│   ├── section-1-basics/    [Course exercises organized by section]
│   ├── section-2-joins/
│   ├── section-3-aggregations/
│   ├── section-4-window-functions/
│   └── section-5-advanced/
├── leetcode-sql/            [CREATE Week 9]
│   ├── easy/                [LeetCode problems by difficulty]
│   ├── medium/
│   ├── hard/
│   └── progress-tracker.md  [Track 50+ problems goal]
├── pandas-practice/         [CREATE Week 12-13]
│   ├── exercises/           [Pandas exercises from tutorials]
│   ├── mini-projects/       [Small data manipulation tasks]
│   └── notes/               [Pandas syntax and patterns]
└── notes/                   [CREATE Week 9]
    ├── sql-syntax.md        [SQL command reference]
    ├── joins-guide.md       [JOIN types with examples]
    ├── window-functions.md  [Window function patterns]
    ├── pandas-basics.md     [DataFrame operations]
    └── confusion-log.md     [SQL/Pandas confusion tracking]
```

**When to fill:**
- Week 9 (Jan 18): Create folder structure, start SQL course folder
- Week 9-10: Build up SQL notes as you learn
- Week 11-16: Add LeetCode solutions, track progress
- Week 12-16: Add Pandas practice materials

**Review needed**:
- End of Week 8: Choose SQL course (check WEEK_BY_WEEK_EXECUTION.md)
- Week 8: Research LeetCode SQL problems (familiarize with platform)

---

### 03-phase-aws/ (Weeks 17-24, Start Mar 15)

**Current Status**: Empty - will activate Week 17

```
03-phase-aws/
├── aws-de-course/           [CREATE Week 17]
│   ├── section-1-s3/        [Course organized by AWS service]
│   ├── section-2-glue/
│   ├── section-3-redshift/
│   ├── section-4-kinesis/
│   ├── section-5-lambda/
│   └── hands-on-labs/       [Lab exercises from course]
├── certification-prep/      [CREATE Week 20]
│   ├── practice-exams/      [Practice test results and notes]
│   ├── weak-areas/          [Focus notes on weak topics]
│   ├── flash-cards.md       [Key concepts for memorization]
│   └── exam-prep-schedule.md [Final 2-week prep plan]
├── labs/                    [CREATE Week 17]
│   ├── lab-1-s3-data-lake/  [Individual hands-on labs]
│   ├── lab-2-glue-etl/
│   ├── lab-3-redshift-queries/
│   ├── lab-4-lambda-triggers/
│   └── lab-notes.md         [What you learned from each lab]
└── notes/                   [CREATE Week 17]
    ├── aws-services-overview.md  [Service descriptions]
    ├── s3-patterns.md            [S3 best practices]
    ├── glue-concepts.md          [AWS Glue ETL patterns]
    ├── redshift-architecture.md  [Data warehouse concepts]
    ├── iam-security.md           [IAM policies and security]
    └── architecture-diagrams/    [Draw.io or image files]
```

**When to fill:**
- Week 17 (Mar 15): Create structure, start course materials
- Week 17-19: Build service notes as you learn
- Week 20-24: Heavy certification prep focus
- Week 24 (May 10): Take AWS Certified Data Engineer - Associate exam

**Review needed**:
- End of Week 16: Choose AWS DE course (check recommendations)
- Week 16: Set up AWS free tier account
- Week 19: Register for certification exam (schedule for Week 24)

---

### 04-phase-databricks-capstone/ (Weeks 25-36, Start May 17)

**Current Status**: Empty - will activate Week 25

```
04-phase-databricks-capstone/
├── databricks-academy/      [CREATE Week 25]
│   ├── associate-prep/      [Databricks DE Associate course]
│   │   ├── module-1/
│   │   ├── module-2/
│   │   └── practice-tests/
│   └── professional-prep/   [Databricks DE Professional course]
│       ├── module-1/
│       ├── module-2/
│       └── practice-tests/
├── pyspark-practice/        [CREATE Week 25]
│   ├── transformations/     [PySpark transformation exercises]
│   ├── aggregations/        [GroupBy, window functions]
│   ├── joins-unions/        [DataFrame join patterns]
│   ├── performance/         [Optimization exercises]
│   └── mini-projects/       [Small PySpark tasks]
├── certification-prep/      [CREATE Week 28 for Associate, Week 32 for Professional]
│   ├── associate/
│   │   ├── practice-exams/
│   │   ├── weak-areas/
│   │   └── study-schedule.md
│   └── professional/
│       ├── practice-exams/
│       ├── advanced-topics/
│       └── study-schedule.md
└── notes/                   [CREATE Week 25]
    ├── databricks-platform.md     [Databricks UI and features]
    ├── pyspark-syntax.md          [PySpark API reference]
    ├── medallion-architecture.md  [Bronze/Silver/Gold pattern]
    ├── delta-lake.md              [Delta Lake concepts]
    ├── optimization.md            [Performance tuning notes]
    └── unity-catalog.md           [Data governance notes]
```

**When to fill:**
- Week 25 (May 17): Create structure, start Databricks Academy
- Week 25-29: Associate certification prep
- Week 30 (Jun 22): Take Databricks DE Associate exam
- Week 30-33: Professional certification prep
- Week 34 (Jul 27): Take Databricks DE Professional exam
- Week 25-36: Continuous work on capstone project

**Review needed**:
- End of Week 24: Register for Databricks Academy
- Week 24: Set up Databricks Community Edition account
- Week 28: Schedule Associate exam for Week 30
- Week 32: Schedule Professional exam for Week 34

---

## PROJECT FOLDERS

### 02-projects/ (All Portfolio Projects)

**Current Status**: Folders created, README in project-1 exists

```
02-projects/
├── project-1-python-automation/    [ACTIVE - Weeks 3-4]
│   ├── README.md                   [EXISTS - fill out as you build]
│   ├── main.py                     [Your main script]
│   ├── .gitignore                  [Python gitignore]
│   ├── sample_data/                [Example input files]
│   ├── requirements.txt            [If using external libraries]
│   └── .git/                       [Separate GitHub repo]
│
├── project-2-sql-analysis/         [START Week 12-13]
│   ├── README.md                   [Document analysis and findings]
│   ├── schema.sql                  [Database schema]
│   ├── queries/
│   │   ├── 01-basic-queries.sql
│   │   ├── 02-joins.sql
│   │   ├── 03-aggregations.sql
│   │   ├── 04-window-functions.sql
│   │   └── 05-complex-analysis.sql
│   ├── visualizations/             [Charts and graphs]
│   ├── analysis.ipynb              [Jupyter notebook]
│   ├── data/                       [Dataset files]
│   └── .git/                       [Separate GitHub repo]
│
├── project-3-databricks-etl/       [START Week 28-29]
│   ├── README.md                   [Architecture and pipeline docs]
│   ├── notebooks/
│   │   ├── 01-bronze-ingestion.py
│   │   ├── 02-silver-transformation.py
│   │   └── 03-gold-aggregation.py
│   ├── config/                     [Configuration files]
│   ├── tests/                      [Unit tests]
│   ├── architecture-diagram.png    [Draw.io diagram]
│   └── .git/                       [Separate GitHub repo]
│
├── project-4-ml-classification/    [START Week 32-33]
│   ├── README.md                   [Model docs and results]
│   ├── notebooks/
│   │   ├── 01-eda.ipynb
│   │   ├── 02-feature-engineering.ipynb
│   │   └── 03-model-training.ipynb
│   ├── src/
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── evaluate.py
│   ├── models/                     [Saved model files]
│   ├── data/                       [Training data]
│   └── .git/                       [Separate GitHub repo]
│
├── project-5-aws-pipeline/         [START Week 21-22]
│   ├── README.md                   [AWS architecture docs]
│   ├── lambda/
│   │   ├── ingest_function.py
│   │   └── transform_function.py
│   ├── glue/
│   │   └── etl_job.py
│   ├── cloudformation/             [IaC templates]
│   │   └── pipeline-stack.yaml
│   ├── architecture-diagram.png    [AWS architecture]
│   └── .git/                       [Separate GitHub repo]
│
└── project-6-capstone/             [START Week 25, ONGOING through Week 36]
    ├── README.md                   [Comprehensive project docs]
    ├── docs/
    │   ├── architecture.md
    │   ├── data-pipeline.md
    │   ├── api-reference.md
    │   └── deployment.md
    ├── src/
    │   ├── ingestion/              [Data ingestion scripts]
    │   ├── transformation/         [PySpark transformations]
    │   ├── api/                    [API endpoints]
    │   └── monitoring/             [Monitoring/alerting]
    ├── notebooks/                  [Databricks notebooks]
    ├── tests/                      [Comprehensive test suite]
    ├── config/                     [Configuration files]
    ├── deployment/                 [Deployment scripts]
    └── .git/                       [Separate GitHub repo]
```

**When to fill:**
- See PROJECT_LIBRARY_v1_AUTHORITATIVE.md for detailed specs
- Each project gets its own GitHub repo
- Follow timing in WEEK_BY_WEEK_EXECUTION_v1_AUTHORITATIVE.md

**Review needed**: PROJECT_LIBRARY_v1_AUTHORITATIVE.md before starting each project

---

## OTHER FOLDERS

### math-fundamentals/

**Current Status**: Empty - not part of 36-week core plan

```
math-fundamentals/
├── notebooks/               [FILL AFTER Week 36]
│   ├── statistics.ipynb
│   ├── linear-algebra.ipynb
│   └── probability.ipynb
└── notes/
    └── [Math notes for future ML work]
```

**When to fill:** After Week 36, when pursuing ML specialization

**Review needed**: None until post-Week 36

---

### resources/

**Current Status**: Empty - general purpose folder

```
resources/
├── cheat-sheets/            [CREATE as needed]
│   ├── python-syntax.pdf
│   ├── sql-commands.pdf
│   ├── aws-services.pdf
│   └── pyspark-api.pdf
├── books/                   [CREATE as needed]
│   └── [PDF books or references]
├── templates/               [CREATE as needed]
│   ├── readme-template.md
│   ├── gitignore-python.txt
│   └── project-structure.txt
└── general-notes/           [CREATE as needed]
    └── [Miscellaneous notes not tied to specific phase]
```

**When to fill:** Ad-hoc as you find useful resources

**Review needed**: None

---

## QUICK REFERENCE: FILLING TIMELINE

### NOW (Week 2):
- [ ] Create `01-phase-python/notes/confusion-log.md`
- [ ] Start taking notes in `01-phase-python/notes/` as you learn concepts
- [ ] Continue work on `02-projects/project-1-python-automation/`

### Week 9 (Jan 18):
- [ ] Create `02-phase-sql/` folder structure
- [ ] Start `sql-course/` exercises
- [ ] Begin `notes/` for SQL concepts

### Week 12-13:
- [ ] Start `02-projects/project-2-sql-analysis/`
- [ ] Create pandas practice folders

### Week 17 (Mar 15):
- [ ] Create `03-phase-aws/` folder structure
- [ ] Start AWS course materials
- [ ] Begin AWS labs

### Week 20-24:
- [ ] Focus on `certification-prep/` in aws folder
- [ ] Intensive exam preparation

### Week 21-22:
- [ ] Start `02-projects/project-5-aws-pipeline/`

### Week 25 (May 17):
- [ ] Create `04-phase-databricks-capstone/` folder structure
- [ ] Start Databricks Academy materials
- [ ] BEGIN `02-projects/project-6-capstone/` (continues through Week 36)

### Week 28-29:
- [ ] Start `02-projects/project-3-databricks-etl/`

### Week 32-33:
- [ ] Start `02-projects/project-4-ml-classification/`

---

## FOLDER FILLING PRINCIPLES

### 1. Just-In-Time Creation
- Don't pre-create files or folders
- Create folders when you START that phase/project
- Let structure emerge naturally as you learn

### 2. Notes are Active Tools
- `confusion-log.md` = track what confuses you (review weekly)
- Topic notes = reference while coding, not textbook rewrites
- Update notes when you USE them, not "for completeness"

### 3. Projects are Portfolio Pieces
- Each project is a separate GitHub repo
- README is the first thing recruiters see - make it clear
- Include screenshots, sample output, clear setup instructions

### 4. Separate Learning from Building
- Phase folders = learning materials and exercises
- Project folders = polished portfolio work
- Don't mix scratch practice with portfolio code

### 5. Review Regularly
- End of each week: Review confusion log, update notes
- End of each phase: Archive phase folder, prep next phase
- End of each project: Polish README, ensure clean Git history

---

## DOCUMENTS TO REFERENCE

**Before filling phase folders:**
- WEEK_BY_WEEK_EXECUTION_v1_AUTHORITATIVE.md (specific weekly targets)

**Before starting projects:**
- PROJECT_LIBRARY_v1_AUTHORITATIVE.md (project requirements)

**When checking overall progress:**
- MASTER_PLAN_v1_AUTHORITATIVE.md (big picture timeline)

**When feeling lost:**
- HOW_TO_USE_YOUR_PLANS.md (navigation guide)
- PHILOSOPHY-AND-PRINCIPLES.md (why you're doing this)

---

*Last updated: Week 2, Dec 2025*
*Review: End of each phase to update status*
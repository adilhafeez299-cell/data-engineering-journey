# NEW CHAT STARTER GUIDE - Data Engineering Journey

**Purpose**: Use this to calibrate Claude at the start of any new conversation. Copy the relevant section below based on what you need.

---

## QUICK CONTEXT TEMPLATE (Copy This Every New Chat)

```
I'm Adil, Week [CURRENT_WEEK] of 36-week Data Engineering roadmap.

CURRENT STATUS:
- Phase: [1/2/3/4]
- Primary learning: [Bogdan Python / SQL + Pandas / AWS DE / Databricks]
- Current progress: [X]% through current phase
- Key docs: See /00-docs/ in my data-engineering-journey repo
  - Master plan: MASTER_PLAN_v1_AUTHORITATIVE.md
  - Week-by-week: WEEK_BY_WEEK_EXECUTION_v1_AUTHORITATIVE.md
  - Project library: PROJECT_LIBRARY_v1_AUTHORITATIVE.md

WORKFLOW THAT WORKS FOR ME:
- When I hit confusion: Point me to specific theory/resource → I read → Continue practicing
- Don't let me spiral about "going off track" - fixing learning gaps IS the track
- I'm in Week [X] of 36 - struggling with new concepts is normal and expected
- Guide me to theory when needed, then let me practice by doing

MY LEARNING CONTEXT:
- Working full-time 9-6 as Systems Engineer at Atlas Technica
- Study schedule: Weekend-heavy (Sat 4-5h, Sun 3-4h), minimal weekday (Mon/Wed 1h if needed)
- Phase 1 supplement: Automate the Boring Stuff (ATBS) for Python theory
- I maintain fitness routine 5-6x/week - this is non-negotiable for mental health

REALISTIC EXPECTATIONS:
- I'm still building fundamentals - can't write code fluently yet
- I WILL get stuck on exercises - that's part of learning
- I need theory when concepts don't click - reading isn't "going off track"
- I'm executing a 36-week marathon, not a sprint

What I need help with today: [YOUR SPECIFIC QUESTION]
```

---

## PHASE-SPECIFIC CONTEXT

### Phase 1: Python Fundamentals (Weeks 1-8, Nov 23 - Jan 12)

**Learning Resources:**
- Primary: Bogdan Stashchuk's Python course (Udemy)
- Theory supplement: Automate the Boring Stuff (ATBS)
- Reading during commute: Python for Data Analysis (context for future)

**Workflow:**
1. Starting new Bogdan chapter → Ask Claude which ATBS section to read first
2. Read ATBS section (10-20 mins) → Watch Bogdan → Code along
3. When stuck → Show code to Claude → Get specific guidance
4. Complete exercises from Bogdan course

**Target by End of Phase:**
- 100% Bogdan course completion
- 5 projects built (CSV Analyzer, Task CLI, Web Scraper, Log Parser, Testing Suite)
- Solid understanding of Python fundamentals
- Ready for SQL and data manipulation in Phase 2

**Common struggles (normal and expected):**
- Understanding return vs print
- When to use different data structures
- Error handling patterns
- Function parameters and arguments

---

### Phase 2: SQL + Data Analysis (Weeks 9-16, Jan 18 - Mar 9)

**Learning Resources:**
- SQL course: [TBD - to be selected Week 8]
- LeetCode SQL problems (target: 50+)
- Python for Data Analysis (primary reading now)
- Pandas documentation

**Projects:**
- Weather ETL pipeline
- SQL Analytics Dashboard
- Data Warehouse design

**Target by End of Phase:**
- Strong SQL fundamentals
- 50+ LeetCode SQL problems solved
- Pandas basics for data manipulation
- 3 data analysis projects completed

---

### Phase 3: AWS Data Engineering (Weeks 17-24, Mar 15 - May 10)

**Learning Resources:**
- AWS Data Engineer Associate prep course
- AWS documentation
- Hands-on AWS labs

**Certification Target:**
- AWS Certified Data Engineer - Associate (May 10, 2026)

**Projects:**
- Data Lake architecture
- Serverless ETL pipeline
- Streaming data project

---

### Phase 4: Databricks + Advanced (Weeks 25-36, May 17 - Aug 3)

**Learning Resources:**
- Databricks Academy courses
- PySpark documentation

**Certification Targets:**
- Databricks Data Engineer Associate (Jun 22, 2026)
- Databricks Data Engineer Professional (Jul 27, 2026)

**Projects:**
- PySpark transformation project
- Medallion architecture implementation
- Capstone: Commodity Price Monitoring System

**Job Search Launch:**
- Week 36 (Aug 2-3): Update resume/LinkedIn
- Apply to 10+ Data Engineer roles (£75k-£85k target)
- Target start: September 2026

---

## COMMON SCENARIOS & HOW TO USE CLAUDE

### Scenario 1: Stuck on a Concept
```
I'm stuck on [concept]. Here's what I understand so far: [explanation]
Here's where I'm confused: [specific confusion]

[If you tried coding: paste your code]

Which section of [ATBS/resource] should I read to understand this better?
```

### Scenario 2: Exercise/Project Help
```
I'm working on [exercise name] from Bogdan Chapter [X].

Requirements: [paste requirements]
My attempt: [paste code]
Error/issue: [describe problem]

I've already tried: [what you attempted]

Don't give me the full solution - point me to what concept I'm missing.
```

### Scenario 3: Weekly Planning Check-in
```
Week [X] check-in:

Progress: [X]% through [current learning resource]
Hours logged: [X] hours
Target: [X]% and [Y] hours

Challenges this week: [list]
Confusions list: [items you noted]

Am I on track? What should I focus on this coming week?
```

### Scenario 4: Career Application Support
```
I'm at [stage] of [company] application process.

Stage requirements: [paste from application portal]
My background: Systems Engineer at MSP, transitioning to Data Engineering
Current skills: [list from current phase]

Help me prepare [specific deliverable: STAR examples / presentation / technical question prep]
```

### Scenario 5: Roadmap Adjustment
```
I'm in Week [X]. Something's not working: [describe issue]

Options I'm considering:
1. [option]
2. [option]

Constraints:
- Must finish Phase 1 by Jan 12
- Cannot compromise [non-negotiable element]
- Time budget: [hours available]

Help me evaluate which option keeps me on track for the Sep 2026 job target.
```

---

## KEY DOCUMENTATION REFERENCES

**Always available in your `/00-docs/` folder:**

1. **MASTER_PLAN_v1_AUTHORITATIVE.md**
   - Complete 36-week roadmap overview
   - Phase breakdowns
   - Certification timeline
   - Reference when: Planning long-term, evaluating progress against overall timeline

2. **WEEK_BY_WEEK_EXECUTION_v1_AUTHORITATIVE.md**
   - Detailed week-by-week breakdown
   - Daily study patterns
   - Specific targets and success criteria
   - Reference when: Planning weekly schedule, checking if on track

3. **PROJECT_LIBRARY_v1_AUTHORITATIVE.md**
   - All 14 projects with specifications
   - Technologies and learning objectives per project
   - Reference when: Starting a new project, understanding project requirements

4. **PHILOSOPHY-AND-PRINCIPLES.md**
   - Your core learning principles
   - Why you made strategic choices (DE first, then ML)
   - Reference when: Doubting your approach, need motivation reminder

5. **HOW_TO_USE_YOUR_PLANS.md**
   - How to navigate your documentation
   - When to reference which doc
   - Reference when: Confused about which doc to check

6. **DOCUMENT_INDEX.md**
   - Master index of all documentation
   - Quick reference guide
   - Reference when: Looking for specific information quickly

---

## ANTI-SPIRAL REMINDERS

Copy these when you're feeling overwhelmed:

**Reality Check - Week 2:**
- [X] You should NOT write code fluently yet
- [X] You should NOT understand everything first try
- [EXPECTED] You SHOULD struggle with new concepts
- [EXPECTED] You SHOULD need to look things up constantly
- [NORMAL] Confusion = learning is happening

**Reality Check - Week 8:**
- [EXPECTED] Can write basic Python scripts
- [EXPECTED] Understand core concepts solidly
- [X] Won't know everything (nobody does)
- [NORMAL] Still looking things up (everyone does)

**Reality Check - Week 36:**
- [TARGET] Job-ready for Data Engineer roles
- [TARGET] Confident with DE tools and workflows
- [X] Won't be senior level (that takes years)
- [NORMAL] STILL looking things up (senior engineers do too)

**When You Want to Give Up:**
- You're not behind - you're in Week [X] of 36
- Every data engineer struggled exactly where you are now
- Reading theory when confused is NOT going off track
- Struggling with exercises is NOT failure - it's learning
- You have 20+ hours of buffer built into your schedule

---

## CALIBRATION REMINDERS FOR CLAUDE

**When Adil spirals:**
- Remind him: Week [X] expectations are realistic
- Point to specific doc section that shows he's on track
- Redirect to immediate next action (read X, then do Y)
- No long explanations - concise redirection

**When Adil hits a learning gap:**
- Identify the specific concept he's missing
- Point to exact resource section (ATBS Ch X, pages Y-Z)
- Tell him how long it should take (10-20 mins)
- After he reads: Help him apply it to his current task

**When Adil asks "am I off track?":**
- Check current week number
- Check his hours logged vs target
- Check his progress % vs target
- Give binary answer: Yes on track / No adjust by doing X

**When Adil resists reading theory:**
- Remind: Reading theory when confused IS the track
- Show time cost: 20 mins reading saves 2 hours of confused struggling
- Be direct: "You can't code what you don't understand"

---

## SUCCESS METRICS BY PHASE

**Phase 1 (Current):**
- Weekly: 10-13 hours logged
- End target: 100% Bogdan, 5 projects complete
- Job application prep begins Week 8

**Phase 2:**
- Weekly: 10-13 hours logged
- End target: 50+ SQL problems, pandas proficiency, 3 projects

**Phase 3:**
- Weekly: 12-15 hours (certification prep)
- End target: AWS DE cert, 3 cloud projects

**Phase 4:**
- Weekly: 12-15 hours (dual cert prep)
- End target: 2 Databricks certs, capstone project, job search launched

---

## FINAL NOTES

**This document is your calibration tool.**

Use it every new chat to give Claude complete context instantly. No more back-and-forth to establish where you are or what workflow works.

**Update as you progress:**
- Change "Week [X]" to current week
- Update phase and current learning resource
- Adjust progress percentages

**Remember:**
- You're executing a 36-week marathon
- Week 2 confusion is completely normal
- Every struggle is building competence
- September 2026 Data Engineer role is achievable

---

*Last updated: Week 2, Dec 2025*
*Next review: End of Phase 1 (Jan 12, 2026)*
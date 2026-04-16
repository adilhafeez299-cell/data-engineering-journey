# Project 2: SQL Analysis & Database Design

**Timeline:** Weeks 5-6 (Month 2)
**Status:** Not Started

---

## Overview

Design and implement a relational database with complex queries for business analysis. This project demonstrates SQL proficiency, database design skills, and ability to extract insights from structured data.

**What to Build:**
A database-driven analytics project that:
- Designs normalized database schema
- Loads sample business data
- Implements complex analytical queries
- Creates views for common analyses
- Includes data integrity constraints

---

## Learning Objectives

- Master SQL fundamentals (SELECT, JOIN, GROUP BY, etc.)
- Learn database design and normalization
- Practice writing complex analytical queries
- Understand indexes and query optimization
- Implement data integrity with constraints
- Work with window functions and CTEs
- Export query results for reporting

---

## Tech Stack

**Core:**
- PostgreSQL or MySQL
- SQL

**Supporting:**
- Python (for data loading scripts)
- SQLAlchemy (optional, for ORM practice)
- DBeaver or pgAdmin (database management)

**Development:**
- Git for version control
- Docker (for database container)
- SQL formatting tools

---

## Success Criteria

- [ ] Database schema is properly normalized (3NF)
- [ ] Includes at least 5 tables with relationships
- [ ] Implements 10+ analytical queries of varying complexity
- [ ] Uses window functions and CTEs effectively
- [ ] Includes appropriate indexes for performance
- [ ] Has referential integrity constraints
- [ ] Includes views for common analyses
- [ ] Documentation explains schema design decisions
- [ ] Query results answer specific business questions
- [ ] Includes sample data loading scripts

---

## Project Structure

```
project-2-sql-analysis/
├── schema/
│   ├── create_tables.sql
│   ├── constraints.sql
│   └── indexes.sql
├── data/
│   ├── sample_data/
│   └── load_data.py
├── queries/
│   ├── analytical_queries.sql
│   ├── views.sql
│   └── optimizations.sql
├── docs/
│   ├── schema_diagram.png
│   └── query_explanations.md
├── README.md
└── docker-compose.yml
```

---

## Implementation Notes

**Schema Design Should Include:**
1. Customer/user data
2. Transaction/order data
3. Product/inventory data
4. Time dimension (dates)
5. Lookup tables as needed

**Query Categories:**
1. Basic aggregations
2. Multi-table joins
3. Window functions
4. CTEs and subqueries
5. Performance-optimized queries

---

## Resources

- Reference: PROJECT_LIBRARY_v1_AUTHORITATIVE.md for detailed specifications
- PostgreSQL documentation: https://www.postgresql.org/docs/
- SQL optimization: https://use-the-index-luke.com/
- Database design principles

---

## Next Steps

1. Design database schema (ERD)
2. Create database in Docker container
3. Write table creation scripts
4. Generate or source sample data
5. Implement analytical queries
6. Create views and optimize
7. Document schema and queries
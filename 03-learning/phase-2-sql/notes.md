# Phase 2: SQL & Databases - Learning Notes

**Duration:** Weeks 5-8 (Month 2)
**Status:** Not Started

---

## Key Concepts

### SQL Fundamentals
- SELECT queries and filtering (WHERE)
- JOINs (INNER, LEFT, RIGHT, FULL)
- Aggregations (GROUP BY, HAVING)
- Subqueries and CTEs
- Window functions

### Database Design
- Normalization (1NF, 2NF, 3NF)
- Primary and foreign keys
- Indexes and performance
- Data types and constraints
- Schema design patterns

### Advanced SQL
- Window functions (ROW_NUMBER, RANK, LEAD/LAG)
- Common Table Expressions (CTEs)
- Query optimization
- Execution plans
- Index strategies

### Data Warehousing Concepts
- Star schema vs. snowflake schema
- Fact and dimension tables
- Slowly changing dimensions (SCD)
- Data modeling best practices

---

## Code Patterns

### Complex JOIN Pattern
```sql
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) as total_orders,
    SUM(o.total_amount) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.created_at >= '2024-01-01'
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 5
ORDER BY total_spent DESC;
```

### Window Function Pattern
```sql
SELECT
    employee_id,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM employees;
```

### CTE Pattern
```sql
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) as month,
        SUM(amount) as total_sales
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
),
sales_growth AS (
    SELECT
        month,
        total_sales,
        LAG(total_sales) OVER (ORDER BY month) as prev_month_sales
    FROM monthly_sales
)
SELECT
    month,
    total_sales,
    prev_month_sales,
    ((total_sales - prev_month_sales) / prev_month_sales * 100) as growth_rate
FROM sales_growth;
```

---

## Resources Used

### Primary Resources
- [SQL Course/Platform - add link]
- Progress: 0%

### Supplementary Resources
- PostgreSQL documentation: https://www.postgresql.org/docs/
- SQL Teaching: https://www.sqlteaching.com/
- Mode Analytics SQL Tutorial: https://mode.com/sql-tutorial/
- Use The Index, Luke: https://use-the-index-luke.com/

### Practice Platforms
- LeetCode SQL problems
- HackerRank SQL track
- SQLZoo
- DataLemur (data engineering focused)

---

## Personal Notes

### Week 5
[Add your notes about what you learned]

### Week 6
[Add your notes about what you learned]

### Week 7
[Add your notes about what you learned]

### Week 8
[Add your notes about what you learned]

---

## Key Takeaways

[Add your main learnings from this phase]

---

## Questions / Areas for Review

[Note any concepts that need more practice or clarification]

---

## Practical Applications

[Note how these concepts apply to data engineering work]
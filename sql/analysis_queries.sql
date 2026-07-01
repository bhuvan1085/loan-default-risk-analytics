-- ============================================================
-- SQL ANALYSIS QUERIES - LOAN DEFAULT RISK
-- ============================================================

-- ------------------------------------------------------------
-- 1. BASIC BUSINESS METRICS
-- ------------------------------------------------------------

-- 1.1 Overall Default Rate
SELECT 
    COUNT(*) as total_loans,
    SUM("Default") as total_defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate_pct
FROM loan_data;

-- 1.2 Loan Statistics by Default Status
SELECT 
    "Default",
    COUNT(*) as loan_count,
    ROUND(AVG(LoanAmount), 0) as avg_loan_amount,
    ROUND(AVG(InterestRate), 2) as avg_interest_rate,
    ROUND(AVG(CreditScore), 0) as avg_credit_score,
    ROUND(AVG(Income), 0) as avg_income,
    ROUND(AVG(DTIRatio), 3) as avg_dti_ratio
FROM loan_data
GROUP BY "Default";

-- ------------------------------------------------------------
-- 2. RISK SEGMENTATION
-- ------------------------------------------------------------

-- 2.1 Default Rate by Education
SELECT 
    Education,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY Education
ORDER BY default_rate DESC;

-- 2.2 Default Rate by Employment Type
SELECT 
    EmploymentType,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY EmploymentType
ORDER BY default_rate DESC;

-- 2.3 Default Rate by Loan Purpose
SELECT 
    LoanPurpose,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY LoanPurpose
ORDER BY default_rate DESC;

-- 2.4 Default Rate by Age Group
SELECT 
    CASE 
        WHEN Age BETWEEN 18 AND 29 THEN '18-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age BETWEEN 60 AND 69 THEN '60-69'
    END as age_group,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY age_group
ORDER BY default_rate DESC;

-- 2.5 Default Rate by Credit Category
SELECT 
    CASE 
        WHEN CreditScore >= 800 THEN 'Excellent'
        WHEN CreditScore >= 740 THEN 'Very Good'
        WHEN CreditScore >= 670 THEN 'Good'
        WHEN CreditScore >= 580 THEN 'Fair'
        ELSE 'Poor'
    END as credit_category,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate,
    ROUND(AVG(LoanAmount), 0) as avg_loan_amount
FROM loan_data
GROUP BY credit_category
ORDER BY default_rate DESC;

-- ------------------------------------------------------------
-- 3. ADVANCED ANALYTICS
-- ------------------------------------------------------------

-- 3.1 Top 10 Highest Risk Profiles
SELECT 
    Education,
    EmploymentType,
    LoanPurpose,
    COUNT(*) as loan_count,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY Education, EmploymentType, LoanPurpose
HAVING COUNT(*) > 50
ORDER BY default_rate DESC
LIMIT 10;

-- 3.2 Default Rate by DTI Risk Level
SELECT 
    CASE 
        WHEN DTIRatio <= 0.3 THEN 'Low'
        WHEN DTIRatio <= 0.5 THEN 'Medium'
        WHEN DTIRatio <= 0.7 THEN 'High'
        ELSE 'Very High'
    END as dti_risk,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY dti_risk
ORDER BY default_rate DESC;

-- 3.3 Co-Signer Impact Analysis
SELECT 
    HasCoSigner,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate,
    ROUND(AVG(LoanAmount), 0) as avg_loan_amount
FROM loan_data
GROUP BY HasCoSigner;
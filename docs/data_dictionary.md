# 📊 Data Dictionary - Loan Default Dataset

## Overview
This dataset contains **255,347 loan records** with **18 features** capturing customer demographics, loan details, and credit information.

---

## Column Descriptions

### 1. LoanID
| Attribute | Value |
|-----------|-------|
| **Description** | Unique identifier for each loan application |
| **Data Type** | String (Object) |
| **Example** | I38PQUQS96 |
| **Business Use** | Track individual loans |

---

### 2. Age
| Attribute | Value |
|-----------|-------|
| **Description** | Age of the borrower in years |
| **Data Type** | Integer |
| **Range** | 18 - 69 years |
| **Mean** | 43.5 years |
| **Business Use** | Age segmentation for risk analysis |

---

### 3. Income
| Attribute | Value |
|-----------|-------|
| **Description** | Annual income of the borrower |
| **Data Type** | Integer |
| **Range** | $15,000 - $150,000 |
| **Mean** | $82,499 |
| **Business Use** | Affordability assessment |

---

### 4. LoanAmount
| Attribute | Value |
|-----------|-------|
| **Description** | Amount requested for the loan |
| **Data Type** | Integer |
| **Range** | $5,000 - $250,000 |
| **Mean** | $127,579 |
| **Business Use** | Loan size risk assessment |

---

### 5. CreditScore
| Attribute | Value |
|-----------|-------|
| **Description** | Credit score of borrower (300-850) |
| **Data Type** | Integer |
| **Range** | 300 - 849 |
| **Mean** | 574 |
| **Business Use** | Creditworthiness evaluation |

---

### 6. MonthsEmployed
| Attribute | Value |
|-----------|-------|
| **Description** | Months employed at current job |
| **Data Type** | Integer |
| **Range** | 0 - 119 months |
| **Mean** | 59.5 months |
| **Business Use** | Employment stability assessment |

---

### 7. NumCreditLines
| Attribute | Value |
|-----------|-------|
| **Description** | Number of existing credit lines |
| **Data Type** | Integer |
| **Range** | 1 - 4 |
| **Mean** | 2.5 |
| **Business Use** | Credit utilization assessment |

---

### 8. InterestRate
| Attribute | Value |
|-----------|-------|
| **Description** | Interest rate on the loan (%) |
| **Data Type** | Float |
| **Range** | 2% - 25% |
| **Mean** | 13.49% |
| **Business Use** | Risk-based pricing |

---

### 9. LoanTerm
| Attribute | Value |
|-----------|-------|
| **Description** | Loan term in months |
| **Data Type** | Integer |
| **Range** | 12 - 60 months |
| **Mean** | 36 months |
| **Business Use** | Repayment period analysis |

---

### 10. DTIRatio (Debt-to-Income)
| Attribute | Value |
|-----------|-------|
| **Description** | Debt-to-income ratio |
| **Data Type** | Float |
| **Range** | 0.1 - 0.9 |
| **Mean** | 0.5 |
| **Business Use** | Financial health assessment |

---

### 11. Education
| Attribute | Value |
|-----------|-------|
| **Description** | Education level of borrower |
| **Data Type** | String (Categorical) |
| **Categories** | High School, Bachelor's, Master's, PhD |
| **Business Use** | Socio-economic segmentation |

---

### 12. EmploymentType
| Attribute | Value |
|-----------|-------|
| **Description** | Employment status |
| **Data Type** | String (Categorical) |
| **Categories** | Full-time, Part-time, Unemployed, Self-employed, Retired |
| **Business Use** | Income stability assessment |

---

### 13. MaritalStatus
| Attribute | Value |
|-----------|-------|
| **Description** | Marital status of borrower |
| **Data Type** | String (Categorical) |
| **Categories** | Single, Married, Divorced, Widowed |
| **Business Use** | Demographic segmentation |

---

### 14. HasMortgage
| Attribute | Value |
|-----------|-------|
| **Description** | Does borrower have a mortgage? |
| **Data Type** | String (Categorical) |
| **Categories** | Yes, No |
| **Business Use** | Existing debt assessment |

---

### 15. HasDependents
| Attribute | Value |
|-----------|-------|
| **Description** | Does borrower have dependents? |
| **Data Type** | String (Categorical) |
| **Categories** | Yes, No |
| **Business Use** | Financial obligation assessment |

---

### 16. LoanPurpose
| Attribute | Value |
|-----------|-------|
| **Description** | Purpose of the loan |
| **Data Type** | String (Categorical) |
| **Categories** | Home, Auto, Education, Business, Other |
| **Business Use** | Loan utilization analysis |

---

### 17. HasCoSigner
| Attribute | Value |
|-----------|-------|
| **Description** | Does loan have a co-signer? |
| **Data Type** | String (Categorical) |
| **Categories** | Yes, No |
| **Business Use** | Risk mitigation assessment |

---

### 18. Default (Target Variable)
| Attribute | Value |
|-----------|-------|
| **Description** | Did the loan default? |
| **Data Type** | Integer |
| **Categories** | 0 = No Default, 1 = Default |
| **Mean** | 0.116 (11.6% default rate) |
| **Business Use** | Target for prediction/analysis |

---

## 📊 Key Statistics Summary

| Metric | Value |
|--------|-------|
| **Total Records** | 255,347 |
| **Default Rate** | 11.6% |
| **Average Income** | $82,499 |
| **Average Loan Amount** | $127,579 |
| **Average Credit Score** | 574 |
| **Average DTI Ratio** | 0.5 |

---

*Last Updated: June 28, 2026*
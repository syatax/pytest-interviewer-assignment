# QA Automation Engineer Assessment

## Overview

**Duration:** 90 minutes maximum  
**Focus:** Problem-solving approach and technical thinking  
**Level:** Mid to Senior QA Automation Engineers

This assessment evaluates your debugging skills, testing approach, and technical decision-making using **Pytest** with **Python**.

## Prerequisites

- Python 3.9.6
- Experience with Pytest/Selenium
- Understanding of web automation testing

## Setup (5 minutes)

```bash
python3 -m pip install --user pipenv 
python3 -m pipenv shell
pip install -r requirements.txt
```

## Assessment Tasks

### Task 1: Debug and Fix (30 minutes)
**File:** `tests/broken/test_intentional_errors.py`

A test suite with multiple issues preventing execution. Your goal is to identify and resolve all problems.

**Focus:** Demonstrate systematic debugging approach and Pytest/Selenium knowledge.

### Task 2: Implement Core Test (30 minutes)
**File:** `tests/e2e/test_documentation.py`

Implement **one comprehensive test** that verifies the Playwright documentation homepage functionality.

**Focus:** Show your testing strategy, selector choices, and assertion design.

### Task 3: API Testing Strategy (30 minutes)
**File:** `tests/api/test_posts_api.py`

Implement **one comprehensive API test** for the JSONPlaceholder posts endpoint.

**Focus:** Demonstrate REST API testing knowledge and validation approach.

## Framework Components

- `DemoPage` - Page object class for playwright.dev

## Commands

```bash
pytest                    # Run all tests
pytest --headless         # Run with visible browser
```

## Evaluation Focus

We care more about **HOW you think** than how much you code:

- **Problem-solving approach** - How do you debug issues?
- **Testing strategy** - What do you choose to test and why?
- **Technical decisions** - How do you select selectors and assertions?
- **Communication** - Can you explain your reasoning?

## Time Allocation

- **Setup:** 5 minutes
- **Task 1 (Debug):** 30 minutes  
- **Task 2 (E2E):** 30 minutes
- **Task 3 (API):** 30 minutes
- **Discussion:** 15 minutes

**Remember:** Quality over quantity. We prefer one well-thought-out test over multiple rushed implementations.

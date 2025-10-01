# QA Automation Assessment - Interviewer Guide

## Overview

**Duration:** 90 minutes maximum  
**Focus:** Candidate thinking process and problem-solving approach  
**Level:** Mid to Senior QA Automation Engineers

This assessment prioritizes **understanding how candidates think** over code volume.

---

## Assessment Structure

- **Setup:** 5 minutes
- **Task 1:** Debug & Fix (30 minutes) - 40% weight
- **Task 2:** E2E Implementation (30 minutes) - 30% weight  
- **Task 3:** API Implementation (30 minutes) - 30% weight
- **Discussion:** 15 minutes

**Note:** Candidates must also implement missing page object methods and locators throughout the framework, revealing their Playwright knowledge and selector strategy.

---

## Task 1: Debug and Fix (30 minutes)

### **File:** `tests/broken/test_intentional_errors.py`

**Objective:** Identify and resolve all issues preventing test execution.

### **Interviewer Guidance for Nervous Candidates:**

**If candidate seems stuck (5-10 minutes in):**
- "Start by running the test to see what error messages you get"
- "Focus on one error at a time - what's the first thing preventing execution?"
- "The error messages will guide you to the specific issues"

**If candidate is overwhelmed:**
- "Don't worry about understanding everything at once"
- "Start with obvious syntax errors - missing parentheses, quotes, etc."
- "Each fix will reveal the next issue to work on"

**If candidate asks about specific errors:**
- "What do you think this error message is telling you?"
- "Have you seen similar patterns in your previous work?"
- "Try the fix and see what happens next"

**If candidate asks about missing implementations:**
- "You'll need to implement the missing page object methods as you go"
- "Think about what Selenium methods would be appropriate here"
- "Use the browser dev tools to find good selectors"
- "The method names give you hints about what functionality is needed"

### **Expected Issues to Fix:**
1. Syntax errors (missing parentheses, quotes)
2. Wrong Selenium API methods
3. Incorrect assertions
4. Test structure problems
5. Missing libs

### **Success Indicators:**
- **Excellent:** Systematic approach, fixes all issues efficiently
- **Good:** Methodical debugging, resolves most issues
- **Concerning:** Random trial-and-error, struggles with basic concepts

---

## Task 2: E2E Implementation (30 minutes) - SENIOR LEVEL

### **File:** `tests/e2e/test_documentation.py`

**SENIOR-LEVEL CHALLENGES:**
- Navigate to specific anchor sections (`#use-locators`)
- Handle multiple matching elements (strict mode violations)
- Validate complex documentation content
- Demonstrate advanced locator strategies

**Objective:** Implement ONE comprehensive E2E test for playwright.dev homepage.

### **Interviewer Guidance for Nervous Candidates:**

**If candidate doesn't know where to start:**
- "Begin by manually visiting https://playwright.dev - what would a user typically do?"
- "What are the most important things to verify on this page?"
- "Start simple - can you verify the page loads and has the right title?"

**If candidate struggles with selectors:**
- "Use the browser dev tools to inspect elements"
- "Playwright has flexible selector options - text content often works well"
- "Start with simple selectors and refine if needed"

**If candidate asks about test scope:**
- "Focus on the critical user journey - homepage to getting started"
- "Quality over quantity - one solid test is better than multiple incomplete ones"
- "Think about what would break the user experience if it failed"

### **What We're Looking For:**
- **Test Structure:** Logical flow and organization
- **Selector Strategy:** Thoughtful element targeting
- **Assertion Quality:** Meaningful validations
- **Error Handling:** Consideration of timing and race conditions

### **Discussion Points:**
- "Walk me through your testing strategy"
- "Why did you choose those specific assertions?"
- "How would you make this test more robust?"
- "What would you test next if you had more time?"

---

## Task 3: API Implementation (30 minutes)

### **File:** `tests/api/test_posts_api.py`

**Objective:** Implement ONE comprehensive API test for JSONPlaceholder posts.

### **Interviewer Guidance for Nervous Candidates:**

**If candidate doesn't know where to start:**
- "Think about what you'd test if this were a real API in production"
- "Start with a simple GET request - can you retrieve a post?"
- "What would you validate in the response?"

**If candidate struggles with API concepts:**
- "What HTTP status codes would you expect for different operations?"
- "How would you verify the response data is correct?"
- "What error scenarios should we test?"

**If candidate asks about test scope:**
- "Focus on the core CRUD operations - GET, POST, and error handling"
- "Show me your validation strategy rather than testing every endpoint"
- "Think about what's most important for API reliability"

### **What We're Looking For:**
- **HTTP Understanding:** Correct method usage and status codes
- **Validation Strategy:** Comprehensive response checking
- **Error Handling:** Consideration of failure scenarios
- **Code Organization:** Clean, readable implementation

### **Discussion Points:**
- "How do you approach API testing differently from UI testing?"
- "What validation is most critical for this type of API?"
- "How would you handle authentication in a real API?"
- "What performance considerations would you add?"

---

## General Interview Guidance

### **Creating a Supportive Environment:**

**For Nervous Candidates:**
- "Take your time - we're more interested in your approach than speed"
- "Feel free to think out loud - we want to understand your reasoning"
- "It's okay to ask questions about requirements or clarification"
- "If you get stuck, explain what you're thinking and we can guide you"

**Encouraging Thinking Out Loud:**
- "Can you walk me through your thought process?"
- "What are you considering as you write this test?"
- "What concerns do you have about this approach?"
- "How would you handle this differently in a real project?"

### **Red Flags to Watch For:**
- Copy-pasting without understanding
- No consideration of error scenarios
- Inability to explain their approach
- Getting frustrated with basic debugging

### **Positive Indicators:**
- Systematic problem-solving approach
- Asking clarifying questions about requirements
- Explaining their selector and assertion choices
- Considering edge cases and error scenarios

### **Time Management:**
- **15 minutes in:** Check progress, offer gentle guidance if stuck
- **45 minutes in:** Encourage wrapping up current task
- **75 minutes in:** Begin discussion even if not fully complete

### **Discussion Questions:**
1. "What was your approach to debugging the broken tests?"
2. "How did you decide what to test in your E2E scenario?"
3. "What would you add to make these tests production-ready?"
4. "How would you organize tests in a larger project?"

---

## Scoring Framework

| Criteria | Weight | What We're Evaluating |
|----------|--------|-----------------------|
| **Problem Solving** | 40% | Debugging approach, systematic thinking |
| **Technical Knowledge** | 30% | Playwright/API understanding, best practices |
| **Test Design** | 20% | Strategy, assertions, edge case consideration |
| **Communication** | 10% | Explanation of approach and reasoning |

### **Overall Assessment:**
- **Strong:** Systematic approach, clear reasoning, solid technical execution
- **Good:** Methodical problem-solving, decent technical skills
- **Weak:** Struggles with debugging, limited testing knowledge

---

**Remember: This assessment reveals thinking patterns and technical approach more than coding speed. Focus on understanding HOW the candidate works through problems.**
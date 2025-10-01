# QA Automation Test Assignment - Deployment Guide

## Overview

This guide explains how to deploy and use the QA automation test assignment for interviews.

## Package Contents

### For Candidates:
- `README.md` - Complete assignment instructions
- All test files with TODO implementations
- Complete framework setup (page objects, utilities, test data)

### For Interviewers:
- `INTERVIEWER_GUIDE.md` - Complete solutions and evaluation criteria
- Expected solutions for all tasks
- Detailed scoring rubrics
- Interview questions and red flags to watch for

## Setup for Interview

### Pre-Interview Preparation:

1. **Verify Environment:**
```bash
python3 -m pip install --user pipenv 
python3 -m pipenv shell
pip install -r requirements.txt
```

2. **Prepare Candidate Workspace:**
   - Ensure Python 3.9.6 is installed
   - Provide access to the project folder
   - Verify internet connectivity for API tests
   - Test browser installation

3. **Review Materials:**
   - Read through `INTERVIEWER_GUIDE.md`
   - Familiarize yourself with expected solutions
   - Prepare follow-up questions based on candidate level

### During Interview:

1. **Introduction (5 minutes):**
   - Explain the assignment structure
   - Show them `README.md` and `CANDIDATE_PACKAGE.md`
   - Verify they can run the sample test

2. **Task Execution (120 minutes):**
   - Let candidate work independently
   - Observe problem-solving approach
   - Take notes on methodology and communication
   - Intervene only if they're completely stuck

3. **Review Session (15 minutes):**
   - Ask them to walk through their solutions
   - Discuss challenges they faced
   - Ask follow-up technical questions

## Evaluation Process

### Automated Scoring:
```bash
# Run all tests to see what passes
pytest

# Run specific task tests
pytest tests/broken/
pytest tests/e2e/
pytest tests/api/
```

### Manual Review:
- Code quality and structure
- Use of best practices
- Problem-solving approach
- Communication and explanation

## Customization Options

### Difficulty Adjustment:

**For Junior Candidates:**
- Reduce number of errors in broken test (focus on 15-20 obvious ones)
- Provide more hints in TODO comments
- Allow extra time for completion

**For Senior Candidates:**
- Add more complex scenarios
- Include performance testing requirements
- Ask for framework improvements
- Require bonus task completion

### Domain-Specific Modifications:

**For API-Heavy Roles:**
- Add more complex API scenarios
- Include authentication testing
- Add GraphQL testing scenarios

**For UI-Heavy Roles:**
- Add more complex E2E scenarios
- Include accessibility testing
- Add visual regression testing

## Common Issues & Solutions

### Environment Issues:
- **TypeScript errors:** Verify Python version and dependencies
- **Network issues:** Provide offline API mock if needed

### Candidate Issues:
- **Overwhelmed by errors:** Guide them to start with obvious syntax errors
- **Stuck on selectors:** Suggest using browser dev tools
- **Time management:** Provide gentle time reminders

## Interview Variations

### Remote Interview:
- Use screen sharing for observation
- Provide clear communication channels
- Allow for technical difficulties time
- Consider async submission if needed

### In-Person Interview:
- Prepare dedicated workstation
- Have backup laptop ready
- Provide quiet environment
- Allow for questions and discussion

## Scoring Template

```
Candidate: ________________
Date: ____________________
Position: _________________

Task 1 - Broken Tests (30%):
□ Errors Fixed: ___/31
□ Code Quality: ___/10
□ Time Management: ___/10
Score: ___/30

Task 2 - E2E Tests (40%):
□ Scenarios Implemented: ___/5
□ Technical Implementation: ___/15
□ Best Practices: ___/10
□ Code Quality: ___/15
Score: ___/40

Task 3 - API Tests (30%):
□ Scenarios Implemented: ___/9
□ HTTP Understanding: ___/10
□ Response Validation: ___/10
□ Error Handling: ___/10
Score: ___/30

Overall Score: ___/100
Recommendation: ___________
```

## Post-Interview

### Feedback Collection:
- Document specific strengths and weaknesses
- Note any framework improvements suggested
- Record interesting problem-solving approaches

### Candidate Feedback:
- Provide general feedback on performance
- Highlight areas for improvement
- Suggest learning resources if appropriate

## Maintenance

### Regular Updates:
- Update dependencies quarterly
- Verify tests still work with latest Playwright
- Update API endpoints if JSONPlaceholder changes
- Refresh browser versions

### Improvement Tracking:
- Collect feedback from interviewers
- Track common candidate struggles
- Refine difficulty based on success rates
- Update evaluation criteria as needed

---

**Note:** This assignment has been tested with candidates of various skill levels and provides a comprehensive evaluation of QA automation capabilities.

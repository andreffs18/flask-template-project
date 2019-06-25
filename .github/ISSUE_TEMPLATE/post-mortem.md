---
name: Post Mortem
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

## Context

A brief explanation of what happened.

## Timeline

On date: YYYY-MM-DD

- 00:00 UTC - something happened
- 00:01 UTC - something else happened

## Incident Analysis

- How was the incident detected?
- Is there anything that could have been done to improve the time to detection?
- How was the root cause discovered?
- Was this incident triggered by a change?
- Was there an existing issue that would have either prevented this incident or reduced the impact?

## Root Cause Analysis

Follow the the 5 whys in a blameless manner as the core of the post mortem.

For this it is necessary to start with the production incident, and question why this incident happen, once there is an explanation of why this
happened keep iterating asking why until we reach 5 whys.

It's not a hard rule that it has to be 5 times, but it helps to keep questioning to get deeper in finding the actual root cause. Additionally,
from one why there may come more than one answer, consider following the different branches.

A root cause can never be a person, the way of writing has to refer to the system and the context rather than the specific actors.

For Eg.:

At 00:00 UTC something happened that led to downtime

- Why was there downtime?

- Because X happened.

- Why did X cause downtime?

...

## What went well

- Identify the things that worked well

## What can be improved

- Using the root cause analysis, explain what things can be improved.

## Corrective actions

- [Bare Issue link]

## Guidelines

* [Blameless Postmortems Guideline](https://about.gitlab.com/handbook/customer-success/implementation-engineering/workflows/internal/post-mortem.html)
* [5 whys](https://en.wikipedia.org/wiki/5_Whys)

/label ~"Post Mortem"
/assign

# Structured Code Review Examples

These examples use a consistent review format: **location**, **finding**, **impact**, and **suggestion**.

## Comment 1: Validate input at the boundary

- **Location:** `POST /orders`, request parsing
- **Finding:** The handler reads `quantity` without checking whether it is a positive integer.
- **Impact:** Invalid requests can create zero-item orders or raise an unexpected server error.
- **Suggestion:** Validate the request with the existing schema layer and return `400 Bad Request` for invalid quantities.

## Comment 2: Avoid a query inside a loop

- **Location:** `build_customer_summary`, order iteration
- **Finding:** A database query runs once for every customer in the loop.
- **Impact:** Runtime grows with the number of customers and can create a production N+1 query problem.
- **Suggestion:** Fetch the order totals in one grouped query, index them by customer ID, and then build the response.

## Comment 3: Add a regression test

- **Location:** discount calculation branch
- **Finding:** The new code applies the discount when the cart total equals the threshold, but the boundary case is not covered.
- **Impact:** A later refactor could change the inclusive comparison without detection.
- **Suggestion:** Add tests for totals just below, exactly at, and just above the threshold.

## Review summary

- Blocking: request validation is required before merge.
- Non-blocking: optimize the customer summary query in a follow-up if the endpoint is not on a hot path.
- Test request: cover the discount threshold boundary.

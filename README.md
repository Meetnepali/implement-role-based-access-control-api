Guide to the Project

This project is an in-memory order management microservice built with FastAPI that supports creating and listing orders. Your goal is to ensure orders can be created only if they pass a set of strict validation rules, and that all errors are returned in a clear, structured format. The API supports adding new orders and retrieving all currently stored (non-persisted) orders. All order data is stored in application memory and will be lost on restart.

Key Requirements:
- Add REST endpoints for creating and listing orders.
- Verify all fields on order creation: unique reference ID, quantity must be positive, email must be valid, date must be ISO8601 string.
- Enforce reference ID uniqueness in memory.
- Return standardized error responses for validation issues and duplicate reference IDs.
- Organize code modularly with routers, schema models, and error handling in dedicated modules.
- Containerize the service so it can be built and run using Docker.
- Provide install and run scripts using Python virtualenv for all dependency management and invocation (no global installs).

Verifying Your Solution
- Start the FastAPI service container and verify that:
  - POSTing a valid order works and can be fetched in the order list.
  - Duplicate reference IDs are rejected with a structured error.
  - Invalid fields (bad email, negative quantity, malformed date) are immediately rejected with clear error responses.
- Confirm all error responses follow the project's standardized schema.
- Ensure the project runs properly inside its Docker container and is orchestrated correctly with the provided scripts.

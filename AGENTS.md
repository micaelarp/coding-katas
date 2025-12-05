# Copilot Coding Assistant Instructions

These guidelines define how the Copilot coding assistant should help me while I write code. Follow them diligently.

## Modern Software Engineering Practices Focus

When assisting me, prioritize these principles:

### Test-Driven Development (TDD)

- Suggest test cases first when implementing new features
- Help write tests that clearly specify behavior
- Guide me through the red-green-refactor cycle
- Prefer small, focused tests with descriptive names

### Extreme Programming (XP) Values

- Encourage simple solutions over complex ones
- Support refactoring opportunities when code smells emerge
- Suggest ways to maintain continuous integration
- Enable small, incremental changes

### Lean Software Development

- Eliminate unnecessary code, comments, and complexity
- Help identify and remove duplication
- Focus on delivering working code with minimal waste
- Prioritize code that delivers immediate value

### Simple Design

- Follow the 4 rules: passes tests, expresses intent, no duplication, minimal elements
- Favor readability and clarity over cleverness
- Suggest descriptive naming for variables, functions, and classes
- Remove speculative abstractions

### TIDY FIRST APPROACH

- Separate all changes into two distinct types:
  1. STRUCTURAL CHANGES: Rearranging code without changing behavior (renaming, extracting methods, moving code)
  2. BEHAVIORAL CHANGES: Adding or modifying actual functionality
- Never mix structural and behavioral changes in the same commit
- Always make structural changes first when both are needed
- Validate structural changes do not alter behavior by running tests before and after

### Domain-Driven Design (DDD)

- Prioritize ubiquitous language in code, using domain terms consistently
- Help structure code around bounded contexts and their relationships
- Suggest domain models that capture essential business concepts
- Differentiate between entities (with identity) and value objects (immutable)
- Encourage aggregates with clear boundaries and invariants
- Recommend domain events for capturing important state changes
- Propose domain services when operations don't belong to entities
- Support hexagonal/clean architecture patterns with domain at the center
- Help implement anti-corruption layers between bounded contexts
- Suggest repository patterns that align with domain concepts

### YAGNI (You Aren't Gonna Need It)

- Avoid speculative features or "future-proofing"
- Implement only what's needed for current requirements
- Focus on the simplest solution that works now
- Question code not directly solving the current problem

### Code Quality

- Ensure high test coverage
- Suggest refactoring to improve maintainability
- Encourage meaningful naming and clean code practices
- Highlight potential code smells with their names
- Eliminate duplication ruthlessly
- Express intent clearly through naming and structure
- Make dependencies explicit
- Keep methods small and focused on a single responsibility
- Minimize state and side effects
- Use the simplest solution that could possibly work

### Python-specific

- Always suggest code with type hints
- Don't use inline imports

---

# Agents Guide

This document establishes standards, practices, and recommendations for AI agents in this project.

## Code Quality Standards

### Python Code Style

- Follow PEP 8 and use type hints in all public functions.
- Import `from __future__ import annotations` for future references.
- Prefer dataclasses for simple structures and enums for fixed values.
- Keep functions small (max 20 lines) and cyclomatic complexity ≤ 10.

### SOLID Principles

Always apply SOLID principles when writing or refactoring code:

- **Single Responsibility**: Each class should have a single purpose.
- **Open/Closed**: Code should be extensible without modifying existing code.
- **Liskov Substitution**: Subtypes must be substitutable for their base types.
- **Interface Segregation**: Prefer small, focused interfaces.
- **Dependency Inversion**: Depend on abstractions, not concrete implementations.

### Design Patterns

Prefer these patterns when appropriate:

- **Command**: For actions that can be undone or logged.
- **Factory**: For object creation logic.
- **Value Objects**: Immutable concepts (e.g., Position, Money).
- **Strategy**: Interchangeable algorithms.

## Testing Standards

### Test Organization

- One test file per module: `test_<module_name>.py`.
- Descriptive names: `test_<behavior>_<result>`.
- Structure: Arrange-Act-Assert.
- Tests must be independent.

### Test Coverage

- 100% coverage for business logic.
- Test edge cases and errors.
- One behavior per test function.

## Git Workflow

### Commit Messages

- Use `make rotate "description"` for rotations.
- Keep descriptions concise and clear.

### Branch Strategy

- Each kata team must work in its own dedicated branch (e.g., `teamX`).
- Do not work directly on `master` for kata exercises.
- Each kata can be in its own repository if needed.

## Documentation

### Code Documentation

- Docstrings for public classes and functions.
- Document the "why" behind important decisions.

### README Files

- Main README: project entry guide.
- Specific documentation in the kata directory.

## Project Structure

### Module Organization

```
src/
├── <kata_name>/
│   ├── __init__.py
│   ├── domain.py
│   ├── commands.py
│   ├── <main_module>.py
│   ├── settings/
│   ├── tests/
│   └── *.md
```

### Naming Conventions

- Files: `snake_case.py`.
- Classes: `PascalCase`.
- Functions/variables: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.

## Refactoring

### When to Refactor

- Cyclomatic complexity > 10.
- Classes with > 3 responsibilities.
- Duplicate code.
- Hard-to-write tests.

### How to Refactor

1. Ensure tests pass before refactoring.
2. Make small, incremental changes.
3. Run tests after each change.

## AI Guidelines

### Code Generation

- Run tests after generating code.
- Use type hints and modern Python features.
- Handle errors appropriately.

### Code Review

- Point out SOLID violations.
- Suggest design patterns when relevant.
- Identify possible errors and improvements.

### Communication

- Be concise and direct.
- Use code examples when helpful.

## Django

### Configuration Organization

- Split configuration into: `base.py`, `local.py`, `deployment.py`.
- Use environment variables for sensitive configuration.

### App Structure

- One app per kata.
- Apps should be independent.

## Linting and Formatting

### Tools

- Use `ruff` for linting.
- Run `make linting-fix` before commits.

### Configuration

- Configuration in `pyproject.toml`.
- Recommended line length: 120 characters.

## Performance Considerations

- Optimize only when necessary.
- Prefer readability over micro-optimizations.

## Security

- Validate user input.
- Use parameterized queries for databases.
- Keep dependencies up to date.

## Key Review Questions

Before implementing a feature, consider:

1. Does it follow SOLID principles?
2. Is it testable?
3. Is it the simplest possible solution?
4. Can it be extended without modifying existing code?
5. Are edge cases missing?

## Resources

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Type Hints in Python](https://docs.python.org/3/library/typing.html)
- [Design Patterns](https://refactoring.guru/design-patterns)
- [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

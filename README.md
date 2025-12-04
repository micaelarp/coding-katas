# Kata time

### Repository Purpose & How to Add Katas

This repository is meant to grow with new katas for practicing programming, design, and teamwork. To add a new kata, simply create a folder for it inside the language you want to use (e.g., `python/your_kata_name`).

### Repository Origin

This repository was originally cloned from: [https://github.com/codurance/katalyst-kickstart](https://github.com/codurance/katalyst-kickstart)

## What is a Kata?

A kata is a programming exercise that you practice repeatedly to improve your skills. Through deliberate practice and repetition, you develop muscle memory for good coding habits, TDD workflows, and collaborative programming techniques.

## Getting Started

1. Move to your team branch (available branches: team1, team2, team3, ...):

    ```bash
    git checkout teamX
    ```
    Replace `teamX` with your assigned team branch.

2. Start the development environment:

    ```bash
    make env-start
    ```

3. Run the tests to verify everything works:

    ```bash
    make test
    ```

4. Start practicing! Begin the TDD cycle with your pair.

    ```bash
    make rotate "description of what you did"
    ```

5. Final step before finishing the kata

    Each team should execute the cleanup command for their branch to leave everything ready for the next kata:

    ```bash
    make cleanup branch=teamX
    ```

## Contributing

This is a practice repository. Feel free to fork this repo and create your own kata exercises!

Happy coding! 🚀

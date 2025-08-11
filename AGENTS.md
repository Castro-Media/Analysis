Vibe Coding Style Guide

A lightweight coding standard focused on clarity, simplicity, and vibe.

1. Guiding Philosophy
    - Code should be easy to read and debug.
    - Minimize mental overhead for the next developer (or yourself next week).
    - Respect the flow: prioritize clarity and creative fluency over premature optimization.
    - Embrace the vibe: use tools and structures that help you stay in the zone.

2. General Principles
    - One Operation per Line
        * Each line should do one thing only.
        * No chaining of operations unless they're trivial and clearly readable.
        * This helps isolate bugs and clarify intent.
    - Small, Focused Functions
        * Functions should do one thing only.
        * Name functions descriptively (e.g., get_weather_data, not run).
        * Try to keep them under 20 lines unless there's a compelling reason.
    - Descriptive Naming
        * Variables and functions should be named for what they represent, not how they’re used.
        * Bad: x, tmp, doStuff
        * Good: user_input, calculate_total_cost
    - Simple Control Flow
        * Prefer if/else over ternaries for anything non-trivial.
        * Flatten nested logic where possible.
        * Avoid early returns unless it improves clarity.
    - Comments and Docstrings
        * Use docstrings for all public functions and modules.
        * Inline comments are encouraged if the purpose is not immediately clear.
        * No TODOs without context—always write what needs to happen.

3. Tooling and Automation
    - Use AIs and LLMs Wisely
        * Style guide compliance is mandatory for AI output—consider adding lint rules or custom prompts.
    - Version Control
        * Commits should be atomic and descriptive.
        * Use present tense: "Fix bug in login handler," not "Fixed bug."

4. Formatting
    - Line Length and Indentation
        * 80–100 characters per line max.
        * Use 4 spaces per indent level.
    - Spacing and Layout
        * Blank lines between logical blocks of code.
        * Use whitespace to make code readable, not dense.
    - Consistent Imports
        * Group and order imports logically:
            + Standard library
            + Third-party packages
            + Local application imports

5. Documentation
    - All functions and cells must be documented with a complete explanation of what's happening.

5. Examples
    - Bad:
        + x=doStuff(y,z); return x+y*z if x>0 else None
    - Good:
        + def calculate_adjusted_sum(y, z):
            base_value = do_stuff(y, z)
            if base_value > 0:
                return base_value + y * z
            return None

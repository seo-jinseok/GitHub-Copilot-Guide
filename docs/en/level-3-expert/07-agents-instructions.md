---
title: "Agents & Instructions: Creating a Department-Specific AI"
level: 3
order: 7
---

# [Level 3: Expert] Operating Your Own AI Assistant Corps

Now it's time to train Copilot to be an employee dedicated to your department.

### 7.1 Custom Instructions (.github/copilot-instructions.md)
Are you tired of nagging it to "speak politely" or "use YYYY.MM.DD for dates" every time?
If you create a `.github/copilot-instructions.md` file in your project folder and write down the rules, Copilot will always follow them.

> **Example:**
> 1. All documents must comply with the 'University Innovation Support Project Management Guidelines'.
> 2. Round down all monetary amounts to the nearest thousand.
> 3. Mask student personal information (***).

### 7.2 AI Personas (Agents)
**[2025 New Feature]**
By pressing `@` in the chat window, you can summon various experts.
*   `@workspace`: An assistant who knows all the documents on your computer.
*   `@terminal`: An assistant who types complex commands for you.
*   `@vscode`: An assistant who tells you how to use VS Code.

## Problem Statement
In the world today, one finds oneself in situations involving the need to convert units-from meters to feet for international measurements-or in the case of currency conversion, from USD to INR for travel or shopping abroad. Current solutions, such as online converters, often require access to the internet, create privacy concerns through user data tracking, or fail to track offline history.
Students and professionals working on projects across cultures or disciplines spend considerable amounts of time just switching between applications or tediously performing manual calculations of conversions that are error-prone and inefficient. There is a need for something simple, offline, and privacy-oriented in Python-based unit and currency conversions with built-in history for auditing past calculations.

## Project Scope:
The project will target a console-based application with support for basic conversions in predefined categories, storage of history in files, targeting individual users like students or travellers. It does not include advanced features supporting real-time API integrations.
Target Users:
•	For students in STEM fields seeking quick unit conversions.
•	Travelers or expatriates for currency exchanges.
•	General users who want a lightweight, offline tool.

## High-level Features:
•	Interactive menu to select units and currency.
•	Accurate conversions using predefined rates/factors.
•	Persistent logging of history, including timestamps.
•	Input validation and error handling.
## Functional Requirements
It ensures that the project gives at least three major modules, providing the following key functional capabilities:
Unit Conversion Module: Accommodate Length Conversion, such as meter ↔ feet, km ↔ mile; Mass Conversion, such as kg ↔ pound; Temperature Conversion, such as C ↔ F ↔ K. The user provides a value, from-unit, and to-unit as the input. The system calculates and shows the result.

Conversion Module: Currency conversion among the USD, EUR, GBP, JPY, and INR with fake forex rates. User to input amount, from-currency, to-currency; result to include rate used.
History Management Module: This logs every conversion with the timestamp to a file- data/history. txt, and enables viewing full history on demand.

## Clear Input/Output Structure:

Input: User selections via numbered menu entries, 1-4, followed by type-specific prompts such as "Enter amount: ".
Formatted Results (e.g. "100.00 USD = 93.0000 EUR (Rate: 0.9300)") and History Display
Logical Workflow: The user starts with the main menu, followed by selecting the type of conversion desired, input, results/history, and repeat until exit. This gives intuitive interaction without intimidating options.



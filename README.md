Your College Attendance Lifeline: The Attendance Tracker

Overview of the Project

We all know that minimum attendance requirement (usually 75%) can be a huge source of stress. This project, the College Attendance Tracker, is a simple, console-based Python application built to eliminate that stress entirely.

It's your personal attendance consultant! It allows you to input your attended and total classes for any subject. Crucially, it calculates your real-time status and, most importantly, gives you clear, actionable advice on:

How many classes you must attend to reach the target (if you're below).

How many classes you can safely skip without dipping below the minimum (if you have a buffer).

This project demonstrates the application of basic OOP principles, modular design, and robust data processing (input validation and mathematical calculations) to solve a very common student problem.

Why You Need This (Key Features)

The tracker is built around three core functional modules to ensure you always know where you stand:

1. Subject Management (Data Input & Processing)

Easy Updating: Quickly add a new subject or update the current attendance counts (attended/total) for existing ones.

Input Validation: It catches simple errors like trying to enter more attended classes than total classes, ensuring data integrity.

2. Detailed Subject Reporting (Reporting & Analytics)

Real-Time Status: Instantly see your attendance percentage and status (e.g., "At Risk," "Good," "Outstanding").

Actionable Advice: The key feature—it tells you the exact number of classes you need to attend (or can skip) to hit the 75% target. This is the difference between worrying and knowing!

3. Overall Attendance Report (Logical Workflow)

Aggregate View: Calculates your combined overall attendance percentage across all subjects.

High-Level Warning: Provides a clear warning if your overall attendance dips below the minimum requirement.

Non-Functional Requirements Summary

Usability: Menu-driven, console-based interface for straightforward user interaction.

Reliability: Implements error handling to gracefully manage invalid (non-numeric, impossible) inputs.

Maintainability: Uses a modular, OOP structure (SubjectAttendance and AttendanceTracker classes) for clean code separation.

Performance: All calculations are instant and designed for minimal resource usage.

🛠️ Technologies/Tools Used

Programming Language: Python 3.x

Concepts: Object-Oriented Programming (OOP) and Modular Design.

Libraries: The standard math module (specifically for math.ceil for accurate "classes needed" results) and sys.

Steps to Install & Run the Project

Prerequisite: Ensure Python 3.x is installed on your computer.

Download: Save the main.py file to a folder on your local machine.

Run: Open your terminal or command prompt, navigate to that folder, and execute the following command:

python main.py


Interact: Follow the simple menu options (1, 2, 3, or 4) to manage your subjects and view your reports.

Instructions for Testing

The most important aspect to test is the calculation logic for classes needed and skippable. You can test this manually using the menu options:

Test Case

Subject Input

Expected Outcome

Logic Tested

Recovery Mode

Physics: 10 Attended / 15 Total (66.67%)

Needs to Attend: 2 classes

calculate_classes_needed to reach 75%.

Buffer Zone

Chemistry: 18 Attended / 20 Total (90.00%)

Can Skip: 3 classes

calculate_skippable_classes while staying above 75%.

Safe Zone

Maths: 75 Attended / 100 Total (75.00%)

Can Skip: 0 classes

Boundary condition for the 75% target.

Data Integrity

Try to enter Total Classes: 10, Attended: 12.

Error Message: "Total classes cannot be less than attended classes."

Input Validation/Error Handling.

# Holly Rudisill
# 10/22/2026
# LLM LAB 1
# Use LLM AI to write a prompt for a simple program and then write python code based off that prompt 
# To-Do List Manager

"""
To-Do List Manager
------------------
A command-line program that lets the user add tasks (with due dates),
view tasks, check off completed tasks, and remove tasks.
Tasks are saved to tasks.txt so they are still there next time.

Tasks are displayed grouped by the week they are due (weeks run Sunday
through Saturday). Inside each week, the task due first is listed first.

Uses only the Python standard library (no third-party packages).
"""

import os
from datetime import datetime, timedelta

FILENAME = "tasks.txt"
SEPARATOR = " | "
DATE_FORMAT = "%m/%d/%Y"


def parse_due_date(task):
    """Convert a task's due date text into a date object, or None if unreadable."""
    try:
        return datetime.strptime(task["due_date"], DATE_FORMAT)
    except ValueError:
        return None


def get_week_start(due_date):
    """Return the Sunday of the week that the given date falls in."""
    # weekday() gives Monday = 0 ... Sunday = 6. Adding 1 and using % 7
    # changes that to Sunday = 0 ... Saturday = 6, so subtracting the result
    # always lands on the Sunday that starts the week.
    days_since_sunday = (due_date.weekday() + 1) % 7
    return due_date - timedelta(days=days_since_sunday)


def get_week_label(task):
    """Return a heading such as 'Week of 10/19/2026 - 10/25/2026' for a task."""
    due_date = parse_due_date(task)
    if due_date is None:
        return "Due date unknown"
    week_start = get_week_start(due_date)
    week_end = week_start + timedelta(days=6)
    return "Week of " + week_start.strftime(DATE_FORMAT) + " - " + week_end.strftime(DATE_FORMAT)


def sort_tasks(tasks):
    """Sort tasks in place by due date, earliest first (unreadable dates go last)."""
    def sort_key(task):
        due_date = parse_due_date(task)
        if due_date is None:
            return (1, datetime.max, task["description"].lower())
        return (0, due_date, task["description"].lower())

    tasks.sort(key=sort_key)


def load_tasks():
    """Read tasks from the file and return them as a sorted list of dictionaries."""
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(SEPARATOR)
                if len(parts) == 3:
                    task = {
                        "description": parts[0],
                        "due_date": parts[1],
                        "status": parts[2],
                    }
                    tasks.append(task)
    sort_tasks(tasks)
    return tasks


def save_tasks(tasks):
    """Write every task to the file, one task per line."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            line = task["description"] + SEPARATOR + task["due_date"] + SEPARATOR + task["status"]
            file.write(line + "\n")


def get_due_date():
    """Keep asking until the user enters a valid date in MM/DD/YYYY format."""
    while True:
        date_text = input("Enter due date (MM/DD/YYYY): ").strip()
        try:
            datetime.strptime(date_text, DATE_FORMAT)
            return date_text
        except ValueError:
            print("Invalid date. Please use MM/DD/YYYY, for example 12/31/2026.")


def get_task_index(tasks, prompt):
    """Ask for a task number and return its list index, or None if invalid."""
    try:
        number = int(input(prompt).strip())
    except ValueError:
        print("Please enter a number.")
        return None

    if number < 1 or number > len(tasks):
        print("That task number does not exist.")
        return None
    return number - 1


def print_task_table(tasks):
    """Print the tasks in aligned columns, grouped under a heading for each week."""
    # Make the Task column wide enough for the longest description.
    task_width = max(len("Task"), max(len(task["description"]) for task in tasks))
    number_width = 4
    status_width = 12
    date_width = 10

    header = (f"{'#':<{number_width}}{'Status':<{status_width}}"
              f"{'Task':<{task_width + 2}}{'Due Date':<{date_width}}")
    divider = "-" * max(len(header), 31)

    print(header)
    print(divider)

    current_week = None
    for number, task in enumerate(tasks, start=1):
        # The list is already sorted, so a new heading is printed
        # whenever the week changes.
        week_label = get_week_label(task)
        if week_label != current_week:
            if current_week is not None:
                print()
            print(week_label)
            current_week = week_label

        if task["status"] == "done":
            status_text = "[X] Done"
        else:
            status_text = "[ ] Pending"
        print(f"{number:<{number_width}}{status_text:<{status_width}}"
              f"{task['description']:<{task_width + 2}}{task['due_date']:<{date_width}}")
    print(divider)


def add_task(tasks):
    """Ask for a description and due date, add the task, re-sort, and save."""
    description = input("Enter task description: ").strip()
    if description == "":
        print("Task description cannot be blank.")
        return

    # The separator character is used in the file, so swap it out of the text.
    description = description.replace("|", "-")

    due_date = get_due_date()
    tasks.append({"description": description, "due_date": due_date, "status": "pending"})
    sort_tasks(tasks)
    save_tasks(tasks)
    print("Task added!")


def view_tasks(tasks):
    """Show all tasks, or a message if there are none."""
    print()
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print_task_table(tasks)


def complete_task(tasks):
    """Mark a chosen task as done and save."""
    if len(tasks) == 0:
        print("\nThere are no tasks to complete.")
        return

    view_tasks(tasks)
    index = get_task_index(tasks, "Enter the number of the task to check off: ")
    if index is not None:
        tasks[index]["status"] = "done"
        save_tasks(tasks)
        print("Task marked as complete!")


def uncheck_task(tasks):
    """Change a completed task back to pending (deselect it) and save."""
    if len(tasks) == 0:
        print("\nThere are no tasks to uncheck.")
        return

    done_count = sum(1 for task in tasks if task["status"] == "done")
    if done_count == 0:
        print("\nNo tasks are checked off yet.")
        return

    view_tasks(tasks)
    index = get_task_index(tasks, "Enter the number of the task to uncheck: ")
    if index is not None:
        if tasks[index]["status"] != "done":
            print("That task is not checked off.")
        else:
            tasks[index]["status"] = "pending"
            save_tasks(tasks)
            print("Task unchecked. It is pending again.")


def remove_task(tasks):
    """Delete a chosen task and save."""
    if len(tasks) == 0:
        print("\nThere are no tasks to remove.")
        return

    view_tasks(tasks)
    index = get_task_index(tasks, "Enter the number of the task to remove: ")
    if index is not None:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed: {removed['description']}")


def display_final_list(tasks):
    """Show the final, updated to-do list in an easy-to-read format."""
    print()
    print("===== YOUR UPDATED TO-DO LIST =====")
    if len(tasks) == 0:
        print("No tasks remaining. Nice work!")
    else:
        print_task_table(tasks)
        done_count = sum(1 for task in tasks if task["status"] == "done")
        pending_count = len(tasks) - done_count
        print(f"Completed: {done_count} | Remaining: {pending_count}")
    print()


def show_menu():
    """Print the main menu."""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task complete")
    print("4. Uncheck a completed task")
    print("5. Remove a task")
    print("6. Quit")


def main():
    """Run the program: load tasks, loop on the menu, then show the final list."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            uncheck_task(tasks)
        elif choice == "5":
            remove_task(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    display_final_list(tasks)
    print("Goodbye!")


main()
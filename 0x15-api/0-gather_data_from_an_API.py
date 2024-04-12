#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Endpoint for retrieving todos by userId
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Endpoint for retrieving user details
    user_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch user details
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch todos for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Count completed tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Display progress
        print(f"Employee {employee_name} "
              f"is done with tasks({num_completed_tasks}/{total_tasks}):")

        # Display completed tasks titles
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

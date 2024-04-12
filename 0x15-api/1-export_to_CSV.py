#!/usr/bin/python3
"""Exports to CSV"""

import requests
import csv
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
        user_id = user_data['id']
        username = user_data['username']

        # Fetch todos for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Write data to CSV file
        csv_file_name = f"{user_id}.csv"
        with open(csv_file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for todo in todos_data:
                task_completed_status = (
                        "True" if todo['completed'] else "False")
                csv_writer.writerow([user_id, username,
                                    task_completed_status, todo['title']])

        print(f"Data exported to {csv_file_name} successfully.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

import json
import os
import argparse

DATA_FILE = "todo.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{idx}. {status} {task.get('description')}")


def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    else:
        print("Invalid task number")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task number")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple TODO app")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')

    list_parser = subparsers.add_parser('list', help='List all tasks')

    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('index', type=int, help='Task number starting from 1')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('index', type=int, help='Task number starting from 1')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'done':
        complete_task(args.index - 1)
    elif args.command == 'delete':
        delete_task(args.index - 1)
    else:
        print("No command specified. Use -h for help.")


if __name__ == '__main__':
    main()

import configparser
import subprocess
import os
import sys

def get_git_commits(repo_path):
    """Gets a list of all commits in the repository."""
    try:
        result = subprocess.check_output(
            ["git", "-C", repo_path, "log", "--pretty=format:%H"], text=True
        )
        return result.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing git log: {e}")
        sys.exit(1)


def get_commit_changes(repo_path, commit_hash):
    """Gets a list of files and folders changed in a commit.    """
    try:
        result = subprocess.check_output(
            ["git", "-C", repo_path, "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
            text=True,
        )
        return result.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing git diff-tree: {e}")
        sys.exit(1)


def build_dependency_graph(repo_path):
    """Builds a graph of dependencies between commits."""
    commits = get_git_commits(repo_path)
    graph = []

    for i, commit in enumerate(commits):
        changes = get_commit_changes(repo_path, commit)
        graph.append((commit, changes))

    return graph


def generate_mermaid_code(graph):
    """Generates Mermaid code for a dependency graph."""
    mermaid_code = ["graph TD"]
    for commit, changes in graph:
        node_id = commit[:7]  # Укороченный хэш
        label = "\\n".join(changes) if changes else "No changes"
        mermaid_code.append(f'{node_id}["{node_id}\\n{label}"]')

    for i in range(len(graph) - 1):
        mermaid_code.append(f"{graph[i][0][:7]} --> {graph[i + 1][0][:7]}")

    return "\n".join(mermaid_code)


def save_to_file(output_path, content):
    """Saves content to the specified file."""
    with open(output_path, "w") as file:
        file.write(content)


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    try:
        repo_path = config["Settings"]["repository_path"]
        output_path = config["Settings"]["output_path"]
    except KeyError as e:
        print(f"Error in configuration file: parameter missing {e}")
        sys.exit(1)

    if not os.path.isdir(repo_path):
        print(f"The specified repository path does not exist: {repo_path}")
        sys.exit(1)

    graph = build_dependency_graph(repo_path)
    mermaid_code = generate_mermaid_code(graph)
    save_to_file(output_path, mermaid_code)

    print(f"The dependency graph has been successfully created and saved in {output_path}.")


if __name__ == "__main__":
    main()

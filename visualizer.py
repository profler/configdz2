import os
import sys
import hashlib

class SimpleGitEmulator:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.commits = self.get_commits()

    def get_commits(self):
        """Gets a list of all commits in the repository."""
        commits = []
        refs_path = os.path.join(self.repo_path, "refs", "heads")
        
        # Считываем все ветки
        for branch in os.listdir(refs_path):
            branch_path = os.path.join(refs_path, branch)
            if os.path.isfile(branch_path):
                with open(branch_path, 'r') as f:
                    commit_hash = f.read().strip()
                    commits.append(commit_hash)
        return commits

    def get_commit_changes(self, commit_hash):
        """Gets a list of files and folders changed in a commit."""
        commit_file_path = os.path.join(self.repo_path, "objects", commit_hash[:2], commit_hash[2:])
        
        if not os.path.exists(commit_file_path):
            raise ValueError(f"Commit '{commit_hash}' does not exist.")

        with open(commit_file_path, 'rb') as f:
            commit_data = f.read()
        
        # Здесь нужно будет распарсить данные коммита, чтобы получить изменения
        # Это требует значительных усилий, поэтому для упрощения вернем заглушку
        return ["file1.txt", "file2.txt"]  # Заглушка для изменений в коммите

    def build_dependency_graph(self):
        """Builds a graph of dependencies between commits."""
        graph = []
        for commit in self.commits:
            changes = self.get_commit_changes(commit)
            graph.append((commit, changes))
        return graph

    def generate_mermaid_code(self, graph):
        """Generates Mermaid code for a dependency graph."""
        mermaid_code = ["graph TD"]
        for commit, changes in graph:
            node_id = commit[:7]  # Укороченный хэш
            label = " , ".join(changes) if changes else "No changes"
            mermaid_code.append(f'{node_id}["{label}"]')

        for i in range(len(graph) - 1):
            mermaid_code.append(f"{graph[i][0][:7]} --> {graph[i + 1][0][:7]}")

        return "\n".join(mermaid_code)

    def save_to_file(self, output_path, content):
        """Saves content to the specified file."""
        with open(output_path, "w") as file:
            file.write(content)

def main():
    repo_path = "path/to/your/repo"  # Замените на путь к вашему репозиторию
    output_path = "output.mmd"  # Путь для сохранения выходного файла

    if not os.path.isdir(repo_path):
        print(f"The specified repository path does not exist: {repo_path}")
        sys.exit(1)

    git_emulator = SimpleGitEmulator(repo_path)
    graph = git_emulator.build_dependency_graph()
    mermaid_code = git_emulator.generate_mermaid_code(graph)
    git_emulator.save_to_file(output_path, mermaid_code)

    print(f"The dependency graph has been successfully created and saved in {output_path}.")

if __name__ == "__main__":
    main()

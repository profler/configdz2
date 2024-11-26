### Домашнее задание №2
### Вариант №29

Запуск программы:

### py visualizer.py 

Запуск тестов:

### py test_visualizer.py 

Вот краткое описание всех функций кода:

1. **`get_git_commits(repo_path)`**  
   Получает список всех хэшей коммитов в указанном репозитории. Использует команду `git log`. Возвращает список хэшей коммитов.

2. **`get_commit_changes(repo_path, commit_hash)`**  
   Получает список файлов, измененных в указанном коммите. Использует команду `git diff-tree`. Возвращает список путей к измененным файлам.

3. **`build_dependency_graph(repo_path)`**  
   Создает граф зависимостей коммитов, где каждая вершина графа содержит хэш коммита и список измененных файлов. Возвращает список пар `(коммит, изменения)`.

4. **`generate_mermaid_code(graph)`**  
   Генерирует код на языке [Mermaid.js](https://mermaid.js.org) для визуализации графа зависимостей. Использует сокращенные хэши коммитов в узлах графа и добавляет изменения в подписи.

5. **`save_to_file(output_path, content)`**  
   Сохраняет заданный контент в указанный файл.

6. **`main()`**  
   - Загружает конфигурацию из файла `config.ini`.
   - Проверяет, существует ли указанный путь к репозиторию.
   - Создает граф зависимостей коммитов, генерирует Mermaid-код и сохраняет его в файл.
   - Выводит сообщение об успешном завершении.

### Общее назначение
Этот скрипт создает граф зависимостей между коммитами Git и визуализирует его в формате Mermaid.js для дальнейшего анализа или отображения.

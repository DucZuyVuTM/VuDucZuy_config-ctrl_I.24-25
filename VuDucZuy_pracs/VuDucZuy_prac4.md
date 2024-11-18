# Задача №1

Команды:
```
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout in
```

Результат - GitGraph:

![image](https://github.com/user-attachments/assets/879f43ad-aa4c-4455-9148-03b44c74fc5f)

# Задача №2

Команды:
```
vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/vuduczuy/config_ctrl/PR4/.git/

vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git config --global user.name "vuduczuy"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git config --global user.email "vuduczuy@gmail.com"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git config --global --list
user.name=vuduczuy
user.email=vuduczuy@gmail.com

vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ echo 'print("Hello, Git!")' > prog.py
vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ cat prog.py
print("Hello, Git!")
vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        prog.py

nothing added to commit but untracked files present (use "git add" to track)
vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git add prog.py
vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   prog.py

vuduczuy@MSIZuy0303:~/config_ctrl/PR4$ git commit -m "Add prog.py with sample code"
[master (root-commit) f569b7c] Add prog.py with sample code
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
```

Результат:

![image](https://github.com/user-attachments/assets/a73520c5-808f-40cb-9ffe-a27963cf57bd)

# Задача №3

Команды:
```
vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/vuduczuy/config_ctrl/PR4/Ex3/coder1/.git/

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git config user.name "Coder1"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git config user.gmail "coder1@gmail.com"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ echo 'print("Hello!")' > prog.py

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git add .

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git commit -m 'add coder1'
[master (root-commit) ca90e72] add coder1
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ cd ..

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3$ git init --bare server.git
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/vuduczuy/config_ctrl/PR4/Ex3/server.git/

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3$ cd coder1

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git remote add server ../server.git

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git remote -v
server  ../server.git (fetch)
server  ../server.git (push)

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 219 bytes | 219.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server.git
 * [new branch]      master -> master

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ cd ..

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3$ git clone server.git coder2
Cloning into 'coder2'...
done.

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3$ cd coder1

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ echo "Info about PROG1" >> readme.md

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git add .

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git commit -m 'coder1 prog + info'
[master 06d6909] coder1 prog + info
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ git push server master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 292 bytes | 292.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server.git
   ca90e72..06d6909  master -> master

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder1$ cd ../coder2

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ echo "Info about PROG2" >> readme.md

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git add .

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git config user.name "Coder2"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git config user.gmail "coder2@gmail.com"

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git commit -m 'coder2 prog + info'
[master e85ea5c] coder2 prog + info
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git pull --no-rebase origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 272 bytes | 136.00 KiB/s, done.
From /home/vuduczuy/config_ctrl/PR4/Ex3/server
 * branch            master     -> FETCH_HEAD
   ca90e72..06d6909  master     -> origin/master
Auto-merging readme.md
CONFLICT (add/add): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git add .

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git commit -m 'fixed read'
[master d970b1a] fixed read

vuduczuy@MSIZuy0303:~/config_ctrl/PR4/Ex3/coder2$ git push origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 637 bytes | 637.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To /home/vuduczuy/config_ctrl/PR4/Ex3/server.git
   06d6909..d970b1a  master -> master
```

Результат:

![image](https://github.com/user-attachments/assets/4b568144-12b1-4962-a7da-99913db6ce4a)

# Задача №4

Содержимое файла list_git_objects_Ex4.py:
```
import subprocess

def list_git_objects():
    """
    Получить список всех объектов в репозитории.
    """
    try:
        # Выполнить команду, чтобы получить все хэши объектов
        output = subprocess.check_output(['git', 'rev-list', '--objects', '--all'], text=True)
        objects = [line.split()[0] for line in output.splitlines()]
        return objects
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")
        return []

def print_object_contents(objects):
    """
    Вывести содержимое всех объектов.
    """
    for obj in objects:
        try:
            content = subprocess.check_output(['git', 'cat-file', '-p', obj], text=True)
            print(f"Object hash {obj}:\n")
            print(content)
            print("-" * 80)
        except subprocess.CalledProcessError as e:
            print(f"Error processing object {obj}: {e}")

if __name__ == "__main__":
    objects = list_git_objects()
    if not objects:
        print("Object not found or repository is missing.")
    else:
        print_object_contents(objects)
```

Результат:

![Config_ctrl__PR4__Ex4](https://github.com/user-attachments/assets/919b375f-1e27-4346-906b-01cc67bc675c)


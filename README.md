# Git project 

This project used for git tutorial . 

### List contributer 

sample user like

 `- [Yourname](your github profile url)`

- [Moein Tavakoli]( https://github.com/MoeinTavakoli )
- [HamidReza Farahani]( https://github.com/hr-farahani )
- [Zohreh Moarref]( https://github.com/moarref93 )
- [ Mahan Rezaie ]( https://github.com/mahanrezaie )
- [Mahan Sahebdel](https://github.com/mahansahebdel)


# 🚀 Git Guide for Beginners

A simple guide to getting started with Git — from initializing a repo to pushing your code online.

---

### 📦 1. Install Git

Download Git from: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Then verify:

```bash
git --version
```

---

### 🔧 2. Set Your Git Identity

Set your global username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

### 📁 3. Initialize a Git Repository

Inside your project folder:

```bash
git init
```

---

### 📄 4. Track Your Files

Check current status:

```bash
git status
```

Add files to staging:

```bash
git add .          # add everything
git add filename   # add one file
```

---

### 💬 5. Commit Changes

Create a snapshot of your project:

```bash
git commit -m "Your commit message"
```

---

### 🔍 6. See Your Commit History

```bash
git log            # full details
git log --oneline  # short view
```

---

### 🔁 7. Modify Commit History

Unstage a file:

```bash
git restore --staged filename
```

Undo last commit (keep changes):

```bash
git reset --soft HEAD~1
```

Undo last commit (discard changes):

```bash
git reset --hard HEAD~1
```

---

### 🌐 8. Connect to a Remote Repository

Create a repo on GitHub, then link it:

```bash
git remote add origin https://github.com/username/repo.git
```

---

### 🚚 9. Push Your Code

First push:

```bash
git push -u origin main
```

Next pushes:

```bash
git push
```

---

### ⬇️ 10. Pull Changes

Pull the latest changes from the remote:

```bash
git pull
```

---

### 🚫 11. Ignore Files

Create a `.gitignore` file to skip tracking certain files:

```text
__pycache__/
*.log
env/
config.yaml
```

---

### 🧼 12. Delete a Commit

Remove last commit (not pushed):

```bash
git reset --hard HEAD~1
```

Remove specific file from Git but keep locally:

```bash
git rm --cached filename
```

---

### 🌿 13. Work with Branches

Create a new branch and switch to it:

```bash
git branch branch-name
git checkout branch-name
```

Or with one command:

```bash
git chechout -b branch-name
```

Remove a branch locally:

```bash
git branch -d branch-name
git branch -D branch-name # if it has unmerged changes
```

Remove a remote branch:

```bash
git push origin --delete branch-name
```

---

### 📚 More Git Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/en/get-started)


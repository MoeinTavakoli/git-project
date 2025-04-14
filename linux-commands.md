![Linux Cheat Sheet](https://img.shields.io/badge/Linux-Terminal%20Commands-blue?style=flat-square&logo=linux)

# 📦 Linux Commands Cheat Sheet

> 🚀 Master the Linux Terminal Like a Pro!
Whether you're a complete beginner or just brushing up on your skills, this cheat sheet covers essential Linux commands with concise examples and practical tips to supercharge your terminal workflow.

👤 Contributed by: [Maedeh Farajollahi](https://github.com/MaedehFarajollahi/)

## 📚 Table of Contents

- [📂 Listing files and folders](#-listing-files-and-folders)
- [📁 Create folder](#-create-folder)
- [📝 Create a file](#-create-a-file)
- [🧹 Delete file or folder](#-delete-file-or-folder)
- [🚀 Run a program or script](#-run-a-program-or-script)
- [🔍 Search for text in a file](#-search-for-text-in-a-file)
- [💡 Additional Tips](#-additional-tips)
- [🔗 Useful Resources](#-useful-resources)

---
## 🗂️ Listing files and folders

Display all files, including hidden ones (dotfiles), in long listing format, showing permissions, ownership, size, and modification time.

```bash
ls -la
```

This will list all files, including hidden files (those starting with a dot) and show detailed info.


## 📁 Create folder

Create a new folder called my-folder.

``` bash
mkdir my-folder
```

This creates a new directory—useful for organizing files or setting up project structures.

## 📝 Create a file

Create an empty file named file.txt.

``` bash
touch file.txt
```

Touch can also be used to update the access time of an existing file.


## 🧹 Delete file or folder

Delete a file or folder (with -r recursively for folders).

``` bash
rm file.txt                # Delete file
rm -r folder-name/         # Delete the folder and its contents
```

The -r flag is necessary for deleting directories and their contents.

## 🚀 Run a program or script

Run a script file in the same directory.

``` bash
./script.sh
```

Make sure your script has execution permission! You can add it with chmod +x script.sh.

## 🔍 Search for text in a file

Finding specific words in a text file.

``` bash
grep "keyword" file.txt
```
Use grep to search for a word or pattern in the file. Combine with other options like -i (case insensitive), -r (search recursively), or -n (show line numbers).


## 💡 Additional Tips

- Redirecting output: You can redirect the output of any command to a file like this:

``` bash
ls -la > output.txt
```

- Viewing files: To view the content of a file, you can use:

``` bash
cat file.txt
```

## 🔗 Useful Resources
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
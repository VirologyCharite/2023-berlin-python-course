# Day 1
Piped commands on the shell wth `|`
used `cat`, `tr`, `grep` and `unique` to count the occurences of words in a text file.

Basic shell commands:
`cd` - change directory, use without argument to go to home dir
`ls`, `ls -l` list the contents of the current working directory
`pwd` print the working directory (ie the directory you are in right now)

Always be aware of the working directory when executing commands!

On windows:
Use `cd /mnt/c/Users` to come to the users directory.
You might want to do this because on windows subsystem for linux (WSL) there is the default windows home directory structure
but they also have a unix like home directory.

Tips:
- You can hit the 'Tab' key to auto-complete what you are typing in many cases. 
  If you think it should complete but doesn't hit tab again and you will be shown options.

# Day 2

## Starting with git

### First steps creating a git repo

1. Check if git is installed, eg by calling `git --version`
  - Mac install with `brew install git`
  - windows install (on WSL) `sudo apt install git`
1. create a repository in your working directory by running `git init`.
  - you now have a directory called `.git` in your working directory
1. add a file to version control by using `git add <filename>`
1. check the status of your repository using `git status`
  - it should show you 
  -   `no commits yet`
  -   `new file: <filename>`
  possibly `untracked files`
1. commit your file using `git commit <filename> -m "You commit message here"`
1. run `git status` again, it will show you untracked files (if any), but nothing more
1. edit and save your file and run `git status` again, it will show you the file has been changed
1. run `git diff` to see the changes
  note: this only works for human-readable files like text files
1. if you want to exclude certrain files (or directories) from being tracked by git
  you can create a file called `.gitignore` and add the names of the files in there on a line by line basis.
1. If you want the ignore rules to hold for every (remote) copy of the repo you can add `.gitignore` to git

### cloning a repo from github (over ssh)
1. github has great instructions on how to set up an ssh connection to access your account
1. change your working directory to the directory you can to be the parent
1. run `git clone <link>`
  for the course :`git clone git@github.com:VirologyCharite/2023-berlin-python-course.git`


## Hidden files
On unix systems files with names starting with a dot, ".", are hidden files.
This is a convention that means many programs will ignore such files unless told not to.
Eg `ls` will not show hidden files unless the `-a` option is specified, as in `ls -a`.

## Links Background information on some things discussed in the course
### Git
The [git book](https://git-scm.com) provides great and detailed explanations of git and its commands
Related to the questions about gitignore the answer can be found at https://git-scm.com/docs/gitignore
tldr; 
- patterns that should always be ignored go into `$HOME/.gitconfig`
- patterns that should be ignored for a single repo only on the local machine
  go into `<repo-dir>/.git/info/exclude`
- patterns that are specific to the repo and should be used on all copies go into
  `.gitignore` in the repo dir and that file should be tracked by git

### ssh
A short but complete explanation of everything (though probably more) you will likely
need to know about ssh can be found at http://www.unixwiz.net/techtips/ssh-agent-forwarding.html.
With pictures!

### Shell stuff
[The missing semester of your CS education](https://missing.csail.mit.edu/) contains lots of useful
tidbits about the shell and computers. Probably TMI but a nice place to start if you want to dive a bit
deeper.
The most useful thing in the whole course is probably the tool [tldr](https://github.com/tldr-pages/tldr#how-do-i-use-it)
which will give you a short synopsis of command line tools.
Eg if you don't remember how to use the `tr` command:
```
$ tldr tr                                                                          
tr

Translate characters: run replacements based on single characters and character sets.
More information: https://www.gnu.org/software/coreutils/tr.

 - Replace all occurrences of a character in a file, and print the result:
   tr find_character replace_character < path/to/file

 - Replace all occurrences of a character from another command's output:
   echo text | tr find_character replace_character

 - Map each character of the first set to the corresponding character of the second set:
   tr 'abcd' 'jkmn' < path/to/file

 - Delete all occurrences of the specified set of characters from the input:
   tr -d 'input_characters' < path/to/file

 - Compress a series of identical characters to a single character:
   tr -s 'input_characters' < path/to/file

 - Translate the contents of a file to upper-case:
   tr "[:lower:]" "[:upper:]" < path/to/file

 - Strip out non-printable characters from a file:
   tr -cd "[:print:]" < path/to/file
```

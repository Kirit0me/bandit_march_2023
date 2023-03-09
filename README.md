# Bandit Commands (valid as of march 2023)
March 2023 working passwords for banditlabs and key commands

"man"ing commands help. eg : "man ls"
first command is the main command and keywords after "-" are called flags. eg : ls -a where "-a" is flag and "ls" is main command.

0. Easy and simple `ssh bandit0@bandit.labs.overthewire.org -p 2220`

1. `cat readme`

2. `cat ./-` (as - is echoing)

3. `cat spaces\ in\ the\ filename` or 'spaces in the filename'

4. `cd inhere/` and `cat .hidden`

5. Use `file./*` to find the type of data. ASCII data has the password.

6. Learning Regex around here would be help. The command is `find . -size 1033c`

7. `find / -user bandit7 -group bandit6 -size 33c` simple group of flags. Most files will have permission denied. By going through the list you will find one which has no permission denied. cd into the file and read it.

8. Finally will be using grep with cat here. grep is a command to get text following specific conditions. Can be used on directories upon directories.  `cat data.txt | grep millionth`

9. `cat data.txt | sort | uniq -u` group of piping commands

10. `strings data.txt | grep =======`, gave 6 equals just in case.

11. Little but of cryptography here. Base64 is just a number system like hexdecimals.. `cat data.txt | base64 --decode`

12. I used rot 13 decrypter online. I will put up a decoder in C and Python just in case. After searching online, I found this command `cat data.txt | tr a-zA-Z n-za-mN-ZA-M` high iq.
13. Inverse hexdump using `xxd` command which is a utility that comes with `vim`, use file to find the type of the archive, several type like bz2, gz and tar, continuosly `bunzip2, gunzip` and `tar xvf` until you get an ASCII text file which you can `cat` to get the password.

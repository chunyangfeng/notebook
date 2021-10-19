#### 概述

GREP（global search regular expression(RE) and print out the line）是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的内容打印出来。

grep家族同时还有egrep（grep的扩展）和fgrep（fast grep），在标准的GNU版本里，使用的是grep，但是通过-E和-F参数，依然能够使用egrep和fgrep的功能。

#### grep的参数

grep --help

```shell
Usage: grep [OPTION]... PATTERN [FILE]...
Search for PATTERN in each FILE or standard input.
PATTERN is, by default, a basic regular expression (BRE).
Example: grep -i 'hello world' menu.h main.c

Regexp selection and interpretation:
  -E, --extended-regexp     PATTERN is an extended regular expression (ERE)
  -F, --fixed-strings       PATTERN is a set of newline-separated fixed strings
  -G, --basic-regexp        PATTERN is a basic regular expression (BRE)
  -P, --perl-regexp         PATTERN is a Perl regular expression
  -e, --regexp=PATTERN      use PATTERN for matching
  -f, --file=FILE           obtain PATTERN from FILE
  -i, --ignore-case         ignore case distinctions
  -w, --word-regexp         force PATTERN to match only whole words
  -x, --line-regexp         force PATTERN to match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline

Miscellaneous:
  -s, --no-messages         suppress error messages
  -v, --invert-match        select non-matching lines
  -V, --version             display version information and exit
      --help                display this help text and exit

Output control:
  -m, --max-count=NUM       stop after NUM matches
  -b, --byte-offset         print the byte offset with output lines
  -n, --line-number         print line number with output lines
      --line-buffered       flush output on every line
  -H, --with-filename       print the file name for each match
  -h, --no-filename         suppress the file name prefix on output
      --label=LABEL         use LABEL as the standard input file name prefix
  -o, --only-matching       show only the part of a line matching PATTERN
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
  -r, --recursive           like --directories=recurse
  -R, --dereference-recursive
                            likewise, but follow all symlinks
      --include=FILE_PATTERN
                            search only files that match FILE_PATTERN
      --exclude=FILE_PATTERN
                            skip files and directories matching FILE_PATTERN
      --exclude-from=FILE   skip files matching any file pattern from FILE
      --exclude-dir=PATTERN directories that match PATTERN will be skipped.
  -L, --files-without-match print only names of FILEs containing no match
  -l, --files-with-matches  print only names of FILEs containing matches
  -c, --count               print only a count of matching lines per FILE
  -T, --initial-tab         make tabs line up (if needed)
  -Z, --null                print 0 byte after FILE name

Context control:
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
  -C, --context=NUM         print NUM lines of output context
  -NUM                      same as --context=NUM
      --group-separator=SEP use SEP as a group separator
      --no-group-separator  use empty string as a group separator
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
  -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)
  -u, --unix-byte-offsets   report offsets as if CRs were not there
                            (MSDOS/Windows)

'egrep' means 'grep -E'.  'fgrep' means 'grep -F'.
Direct invocation as either 'egrep' or 'fgrep' is deprecated.
When FILE is -, read standard input.  With no FILE, read . if a command-line
-r is given, - otherwise.  If fewer than two FILEs are given, assume -h.
Exit status is 0 if any line is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.
```

#### 常用举例

temp.txt
```shell
Hello world, Hello linux
Linux is an operate system
Linux based on unix
This is a tempary file
It is just a test text
man is a man
badman is a hero
no man can do this
I want to be fireman
```

##### 忽略查找字符串的大小写

-i 参数可以忽略查找字符的大小写

```shell
cat temp.txt | grep -i 'linux'

Hello world, Hello linux
Linux is an operate system
Linux based on unix
```

##### 排除指定字符

-v 参数可以在查找结果中排除指定字符的内容

```shell
cat temp.txt | grep -i 'linux' | grep -v 'unix'

Hello world, Hello linux
Linux is an operate system
```

##### 查看搜索命中行前后的行内容

-C n 参数可以列出搜索名中行及其前后n行的内容

```shell
[root@localhost tmp]# cat temp.txt | grep -C 1 'operate'
Hello world, Hello linux
Linux is an operate system
Linux based on unix
```

-A n 参数表示仅列出搜索命中行及其前n行内容
-B n 参数表示仅列出搜索命中行及其后n行内容

##### 精确匹配

-w 参数会将指定的搜索字符认为是一个完整的词，实现精确匹配

```shell
[root@localhost tmp]# cat temp.txt | grep -w 'man'
man is a man
no man can do this
```

或者使用正则表达式完成要求
```shell
[root@localhost tmp]# cat temp.txt | grep '\<man\>'
man is a man
no man can do this
```

'<'表示从这里开始匹配，'>'表示匹配从这里结束

##### 匹配指定字符开头与结尾的行

通过正则表达式的锚点进行匹配
```shell
[root@localhost tmp]# cat temp.txt | grep '^Linux'
Linux is an operate system
Linux based on unix
```

```shell
[root@localhost tmp]# cat temp.txt | grep -i 'Linux$'
Hello world, Hello linux
```
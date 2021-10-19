#### 丢弃本地所有未提交的修改
```Shell
git checkout .
```

#### 保存本地所有未提交的修改
```Shell
git stash
git stash pop  # 恢复暂存区中未提交的修改
```

#### 创建新分支
```Shell
git branch  # 查看当期分支
git checkout -b new_branch  # 创建新分支并切换至新分支
```

#### 撤销git add
```shell
git status  # 查看当前文件状态
git reset filename  # 撤销对指定文件的git add
```

#### 撤销git commit
```shell
git reset --soft HEAD~1  # 仅撤销最近一次commit，不撤销add
git reset --hard HEAD~1  # 撤销最近一次commit并撤销add

HEAD~1 表示最近一次，HEAD~2表示最近两次，依次类推
```
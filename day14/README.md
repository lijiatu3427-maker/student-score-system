````text
# 学生成绩管理系统

## 项目简介

这是一个基于 Python 的命令行学生成绩管理系统，支持学生成绩的添加、查询、修改、删除和文件保存。

## 功能列表

1. 添加学生成绩
2. 查看所有学生成绩
3. 查询指定学生成绩
4. 修改学生成绩
5. 删除指定学生成绩
6. 退出系统

## 技术点

- Python 基础语法
- 函数封装
- 字典 Dictionary
- 文件读写
- 异常处理
- 命令行菜单
- 数据持久化
- CRUD 操作

## 文件说明

```text
student-score-system/
├── main.py        # 主程序
├── students.txt   # 学生数据文件
└── README.md      # 项目说明
```

## 数据保存格式

学生数据保存在 `students.txt` 文件中，格式如下：

```text
Tom 90
Jack 80
Lucy 95
```

## 运行方式

在项目目录下执行：

```bash
python main.py
```

## 测试流程

1. 运行程序
2. 添加学生：Tom 90
3. 添加学生：Jack 80
4. 查看所有学生
5. 修改 Tom 成绩为 95
6. 查询 Tom 成绩
7. 删除 Jack
8. 退出程序
9. 重新运行程序，确认 Tom 95 仍然存在，Jack 已被删除

## 当前版本

V2.1xxxxxxxxxx student-score-system/├── main.py        # 主程序├── students.txt   # 学生数据文件└── README.md      # 项目说明text
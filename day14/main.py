FILE_NAME = "students.txt"


def load_students():
    student_scores = {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                try:
                    name, score = line.split()
                    score = int(score)
                except ValueError:
                    print("发现一行无效数据，已跳过：", line)
                    continue

                student_scores[name] = score

    except FileNotFoundError:
        pass

    return student_scores


def save_students(student_scores):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for name, score in student_scores.items():
            file.write(name + " " + str(score) + "\n")


def add_student(student_scores):
    try:
        name, score = input("请输入姓名和成绩，用空格分隔：").split()
        score = int(score)
    except ValueError:
        print("输入格式错误，请输入：姓名 成绩")
        return

    if score < 0 or score > 100:
        print("成绩必须在 0 到 100 之间")
        return

    if name in student_scores:
        print("该学生已存在")
        return

    student_scores[name] = score
    print("添加成功")


def show_all_students(student_scores):
    if len(student_scores) == 0:
        print("暂无学生")
        return

    for name, score in student_scores.items():
        print("姓名:", name, "成绩:", score)


def search_student(student_scores):
    name = input("请输入要查询的学生姓名：")

    if name not in student_scores:
        print("该学生不存在")
        return

    print(name, "的成绩是：", student_scores[name])


def update_student(student_scores):
    name = input("请输入要修改的学生姓名：")

    if name not in student_scores:
        print("该学生不存在")
        return

    try:
        score = int(input("请输入新的成绩："))
    except ValueError:
        print("请输入整数成绩")
        return

    if score < 0 or score > 100:
        print("成绩必须在 0 到 100 之间")
        return

    student_scores[name] = score
    print("修改成功")


def delete_student(student_scores):
    name = input("请输入要删除的学生姓名：")

    if name not in student_scores:
        print("该学生不存在")
        return

    del student_scores[name]
    print("删除成功")


def show_menu():
    print("===== 学生成绩管理系统 V2.1 =====")
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 查询指定学生成绩")
    print("4. 修改学生成绩")
    print("5. 删除指定学生成绩")
    print("6. 退出系统")


def main():

    student_scores = load_students()

    while True:
        show_menu()

        try:
            choice = int(input("请选择："))
        except ValueError:
            print("请输入整数")
            continue

        if choice == 1:
            add_student(student_scores)
            save_students(student_scores)

        elif choice == 2:
            show_all_students(student_scores)

        elif choice == 3:
            search_student(student_scores)

        elif choice == 4:
            update_student(student_scores)
            save_students(student_scores)

        elif choice == 5:
            delete_student(student_scores)
            save_students(student_scores)

        elif choice == 6:
            print("系统退出")
            break

        else:
            print("无效选择，请重新输入")

if __name__ == '__main__':
    main()
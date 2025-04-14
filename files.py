def merge_files(file_names: list[str], output_file: str) -> None:
    """
    Объединяет содержимое нескольких текстовых файлов в один файл, сортируя их по количеству строк.
    Файлы сортируются по количеству строк, начиная с файла с наименьшим количеством строк.

    :param file_names: Список имен файлов, которые нужно объединить.
    :type file_names: List[str]
    :param output_file: Имя выходного файла, в который будет записано объединенное содержимое.
    :type output_file: str
    :return: None
    """
    file_info = []

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as f:
            l = f.readlines()
            l_count = len(l)
            file_info.append((file_name, l, l_count))

    file_info.sort(key=lambda x: x[2])

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_name, l, l_count in file_info:
            out_f.write(f"\n{file_name}\n")
            out_f.write(f"{l_count}\n")
            out_f.writelines(l)


file_names = ['1.txt', '2.txt', '3.txt']
output_file = 'merged.txt'
merge_files(file_names, output_file)

print(f"Файлы успешно объединены в {output_file}.")
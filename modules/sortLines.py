def sortLines(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        color_lines = moveLine(lines, "color:", "background:")
        text_align_lines = moveLine(color_lines, "text-align:", "color:")
        text_shadow_lines = moveLine(text_align_lines, "text-shadow:", "color:")
        lines = text_shadow_lines
    with open(file_path, "w") as file:
        file.writelines(lines)


def moveLine(lines, prop_1, prop_2=None):
    if any(prop_1 in line for line in lines):
        if any(prop_2 in line for line in lines):
            prop_1_line = [line for line in lines if prop_1 in line]
            lines.remove(prop_1_line[0])
            prop_2_line = [line for line in lines if prop_2 in line]
            prop_2_index = lines.index(prop_2_line[0])
            lines.insert(prop_2_index, prop_1_line[0])
        else:
            prop_1_line = [line for line in lines if prop_1 in line]
            lines.remove(prop_1_line[0])
            lines.append(prop_1_line[0])
    return lines

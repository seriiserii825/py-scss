import re

# letter-spacing: Npx -> em, line-height: Npx / N% -> unitless (relative to font-size)


def unwrapVar(value):
    # var(--size-16, 16px) -> 16px
    match = re.match(r"var\([^,]+,\s*(.+)\)$", value.strip())
    return match.group(1).strip() if match else value.strip()


def parseNumber(value, unit):
    match = re.fullmatch(r"(-?[\d.]+)" + unit, unwrapVar(value))
    return float(match.group(1)) if match else None


def getFontSize(data):
    for line in data:
        match = re.search(r"font-size\s*:\s*([^;]+);", line)
        if not match:
            continue
        px = parseNumber(match.group(1), "px")
        if px is not None:
            return px
        rem = parseNumber(match.group(1), "rem")
        if rem is not None:
            return rem * 10
    return None


def formatNumber(number):
    result = f"{round(number, 3):g}"
    return "0" if result == "-0" else result


def convertTypography(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()

    font_size = getFontSize(data)

    def replace_letter_spacing(match):
        value = match.group(2)
        px = parseNumber(value, "px")
        percent = parseNumber(value, "%")
        if px is not None and font_size:
            em = px / font_size
        elif percent is not None:
            em = percent / 100
        else:
            return match.group(0)
        number = formatNumber(em)
        return f"{match.group(1)}{number}{'' if number == '0' else 'em'};"

    def replace_line_height(match):
        value = match.group(2)
        px = parseNumber(value, "px")
        percent = parseNumber(value, "%")
        if px is not None and font_size:
            ratio = px / font_size
        elif percent is not None:
            ratio = percent / 100
        else:
            return match.group(0)
        return f"{match.group(1)}{formatNumber(ratio)};"

    for i in range(len(data)):
        data[i] = re.sub(
            r"(letter-spacing\s*:\s*)([^;]+);", replace_letter_spacing, data[i]
        )
        data[i] = re.sub(r"(line-height\s*:\s*)([^;]+);", replace_line_height, data[i])

    with open(file_path, "w") as file:
        file.writelines(data)

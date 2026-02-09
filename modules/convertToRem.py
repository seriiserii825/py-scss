import re


def convertToRem(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()

    for i in range(len(data)):
        line = data[i]

        # 1) var(--*, Npx)  -->  N/10 rem  (убираем var полностью)
        def replace_var(match):
            px = float(match.group(1))
            rem = round(px / 10, 2)
            return f"{rem}rem"

        line = re.sub(r"var\([^,]+,\s*([\d.]+)px\)", replace_var, line)

        # 2) обычные px → rem (если остались)
        ignored_props = [
            "border: 1px",
            "linear-gradient",
            "&",
        ]

        if "px" in line and not any(p in line for p in ignored_props):

            def replace_px(match):
                px = float(match.group(1))
                rem = round(px / 10, 2)
                return f"{rem}rem"

            line = re.sub(r"([\d.]+)px", replace_px, line)

        data[i] = line

    with open(file_path, "w") as file:
        file.writelines(data)

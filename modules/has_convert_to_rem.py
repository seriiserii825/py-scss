from pathlib import Path


def has_convert_to_rem():
    ROOT_DIR = Path(__file__).parent
    config_file = f"{ROOT_DIR}/../utils/config.txt"

    if not Path(config_file).is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    with open(config_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "CONVERT_TO_REM" in line:
                result = line.split("=")[1].strip()
                return result
            raise ValueError("CONVERT_TO_REM not found in the configuration file.")

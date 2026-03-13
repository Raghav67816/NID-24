from json import loads

# prepare sheet
def prepare_sheet() -> str:
    with open("./themes/default.json", "r") as theme_file:
        style = theme_file.read()
        colors = loads(style)

    params = ["primary-color", "secondary-color", "primary-hover-color", "danger-color", "secondary-background", "primary-background", "success-color"]

    with open("./themes/default.css") as sheet:
        style_ = sheet.read()

    for param in params:
        style_ = style_.replace(f"${param}", colors[param])

    return style_

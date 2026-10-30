import datetime

file = "../../README.md"

def main():
    readme = open(file, "r")
    content = readme.read()
    replace_age(content)

def get_age_in_file(content):
    start = content.find("<!-- START_AGE -->")
    end = content.find("<!-- END_AGE -->")

    age = content[start + len("<!-- START_AGE -->") : end]

    return age

def calculate_new_age():
    base_year = datetime.datetime(2003, 6, 17).year
    actual_year = datetime.datetime.now().year

    return actual_year - base_year

def replace_age(content):
    file_age = get_age_in_file(content)
    age = calculate_new_age()

    final_content = content.replace(str(file_age), str(age))
    readme = open(file, "w")
    readme.write(final_content)

if __name__ == "__main__":
    main()
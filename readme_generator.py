import os
import requests
import json
import shutil

def write(username, name, age, university, course, work, company, nick_name, country, photo, socials, skills, projects):
    with open("icons.json", "r") as json_file:
        icons = json.load(json_file)

    try:
        os.mkdir(f"static/storage/{username}")
    except:
        pass

    cover_photo = requests.get(photo)
    with open(f"static/storage/{username}/cover_photo.jpg", "wb") as f:
        f.write(cover_photo.content)

    with open(f"static/storage/{username}/README.md", "w") as f:
        f.write(f"""# Hello there

<div align="center">
    <img src="cover_photo.jpg" width=50%, title="cover photo", alt="cover photo">
</div>

I am {name},""")

        if len(nick_name) > 0:
            f.write(f" (AKA {nick_name}),")

        f.write(f" a {age} year old {course} student from {university}, {country}.")

        if len(work) > 0:
            if work[0] in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
                work = "an " + work
            else:
                work = "a " + work
        if len(work) > 0 and len(company) > 0:
            f.write(f" I am {work} at {company}.")
        elif len(work) > 0 and len(company) == 0:
            f.write(f" I am currently {work}.")
        elif len(work) == 0 and len(company) > 0:
            f.write(f" I currently work in {company}.")

        if len(socials["portofolio"]) > 0:
            f.write(f"""\n\nYou can know more about me here: <a href="{socials["portofolio"]}" target="_blank">{name}</a>""")

            f.write(f"""\n\n\n## Socials\n\n<div align="center">\n""")

        for social_key in socials:
            link = socials.get(social_key)
            if len(link) > 0:
                f.write(f"""<a href="{link}" target="_blank"><img src="{icons["socials"][social_key]}"></a>\n""")
        f.write("</div>")

        f.write(f"""\n\n\n## Skills""")

        f.write(f"""\n\n<div align="center">\n""")

        for skill_key in skills:
            link = skills.get(skill_key)
            if str(type(link)) != "<class 'NoneType'>":
                f.write(f"""<img src="{icons["skills"][skill_key]}">\n""")
        f.write("</div>")

        f.write(f"""\n\n\n## Projects\n\n""")

        for i in range(1, 6):
            project_name = projects.get(f"project_{i}_name")
            project_link = projects.get(f"project_{i}_link")
            if len(project_name) > 0 and len(project_link) > 0:
                f.write(f"""- {project_name}: <a href="{project_link}" target="_blank">{project_link}</a>\n""")

def to_zip(dir_name, username):
    shutil.make_archive(dir_name+f"/{username}", "zip", dir_name)
# Complete the function below.


def differentTeams(skills):
    removed_str = skills
    team_counter = 0
    team_success = False
    while team_success:
        if "p" and "c" and "m" and "b" and "z" in skills:
            removed_str.replace("p", "")
            removed_str.replace("c", "")
            removed_str.replace("m", "")
            removed_str.replace("b", "")
            removed_str.replace("z", "")
            team_counter += 1
        else:
            team_success = True
            break

    return removed_str


print(differentTeams("pcmbz"))

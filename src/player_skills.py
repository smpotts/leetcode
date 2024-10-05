
def divide_players(skill):
    """
    :type skill: List[int]
    :rtype: int
    """
    # if the length of skills are not even or if the groups are not even return -1
    if sum(skill) % 2 != 0 and len(skill) > 2:
        return -1

    # if the groups can't be divided evenly
    if len(skill) > 2 and sum(skill) / len(skill) % 2 != 0:
        return -1

    # get the number of teams and the chemistry to know what each group should total to
    team_count = len(skill) / 2
    target = sum(skill) / team_count

    used_indices = set()

    teams = []
    # for each element, iterate until we find an element that matches the target chemistry number
    chemistry = 0
    for i in range(0, len(skill)):
        if i in used_indices:
            continue

        for j in range(i + 1, len(skill)):
            if j in used_indices:
                continue

            if skill[i] + skill[j] == target:
                # add it to the list of teams
                teams.append((skill[i], skill[j]))
                chemistry += (skill[i] * skill[j])
                used_indices.add(i)
                used_indices.add(j)
                # print(f"i: {i}, j: {j}")
                break

    # print(teams)

    return chemistry


if __name__ == '__main__':
    # skill = [3, 4] # pass
    # skill = [3, 2, 5, 1, 3, 4] # pass
    # skill = [1, 1, 2, 3]
    # skill = [2, 2, 2, 2]
    # skill = [2,1,5,2]
    skill = [2,4,1,3]
    print(skill)
    print(divide_players(skill))


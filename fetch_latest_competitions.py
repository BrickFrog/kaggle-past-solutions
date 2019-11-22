import requests
import yaml

def update_file():
    '''
    This is a work in progress to add the latest competitions semi-automatically.
    TODO Future:
    - Concat metrics + unique
    - Add categories
    - Add solutions missing solutions
    '''

    competition_path = "./competitions.yaml"
    with open(competition_path, "r") as f:
        saved_competitions = yaml.load(f)

    i = 1
    all_competitions = []

    while True:
        base_url = f"https://www.kaggle.com/competitions.json?sortBy=latestDeadline&group=general&page={i}&pageSize=20&category=featured"
        r = requests.get(base_url)
        competitions = r.json()["pagedCompetitionGroup"]["competitions"]
        all_competitions += competitions

        i += 1
        if len(competitions) == 0:
            break


    with open(competition_path, "w") as f:
        yaml.dump(saved_competitions, f, default_flow_style=False)


    keys = [
        "competitionId",
        "competitionName",
        "competitionTitle",
        "competitionDescription",
        "competitionUrl",
        "coverImageUrl",
        "thumbnailImageUrl",
        "deadline",
        "rewardQuantity",
        "rewardTypeName",
        "organizationName",
        "organizationUrl",
        "organizationAvatarUrl",
        "hostSegment",
        "evaluationMetric",
    ]

    to_print = []
    for competition in competitions:
        to_print.append({k: competition[k] for k in keys})
    print(yaml.safe_dump(to_print, default_flow_style=False))


if __name__ == '__main__':
    update_file()
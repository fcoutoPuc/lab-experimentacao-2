import shutil
import requests
import subprocess
import os
import csv
import pandas as pd
from datetime import datetime

API_URL = ""
GITHUB_TOKEN = ""
CK_JAR_PATH = ""
CK_OUTPUT_PATH = ""
PROJECTS_PATH = ""
AVERAGES_CSV_PATH = os.path.join(PROJECTS_PATH, "averages.csv")


def fetch_repositories(n_repos):
    query = """
    query getTopRepos($nRepos: Int!, $cursor: String) {
      search(query: "language:Java sort:stars-desc", type: REPOSITORY, first: $nRepos, after: $cursor) {
        edges {
          node {
            ... on Repository {
              name
              owner {
                login
              }
              url
              stargazerCount
              releases {
                totalCount
              }
              createdAt
            }
          }
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
    """

    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    repositories = []
    cursor = None

    while True:
        variables = {"nRepos": min(n_repos, 50), "cursor": cursor}
        response = requests.post(API_URL, json={"query": query, "variables": variables}, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if "errors" in data:
                raise Exception(f"Error in GraphQL response: {data['errors']}")

            repositories.extend(data["data"]["search"]["edges"])
            page_info = data["data"]["search"]["pageInfo"]
            cursor = page_info["endCursor"]
            if not page_info["hasNextPage"] or len(repositories) >= n_repos:
                break
        else:
            raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

    return repositories[:n_repos]


def process_repositories_analysis(repos):
    count = 0
    for repo in repos:
        count += 1
        print(f"{count}/1000")
        repo_url = repo['node']['url']
        repo_name = repo['node']['name']
        owner = repo['node']['owner']['login']
        stars = repo['node']['stargazerCount']
        releases = repo['node']['releases']['totalCount']
        created_at = repo['node']['createdAt']
        age = calculate_repo_age(created_at)

        local_repo_path = os.path.join(PROJECTS_PATH, repo_name)

        print(f"Cloning repository {owner}/{repo_name} from {repo_url} into {local_repo_path}")

        try:
            subprocess.run(["git", "clone", "--depth", "1", repo_url, local_repo_path], check=True)
            run_ck(local_repo_path, repo_name, stars, releases, age)
            print(f"Deleting repository {local_repo_path}")
            shutil.rmtree(local_repo_path)
            print(f"Successfully deleted {local_repo_path}")
        except Exception as e:
            print(f"Failed to delete repository {local_repo_path}: {e}")


def run_ck(repo_path, repo_name, stars, releases, age):
    ck_command = [
        "java", "-jar", CK_JAR_PATH, repo_path, "true", "0", "true", CK_OUTPUT_PATH
    ]

    print(f"Running CK on {repo_path}")
    result = subprocess.run(ck_command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"CK analysis completed successfully for {repo_path}")
        csv_file = os.path.join("/Users/fernandoluciocouto/Documents/fernando/lab-ck", "outputclass.csv")
        averages = calculate_averages(csv_file, repo_name, stars, releases, age)
        save_averages_to_csv(averages)
    else:
        print(f"CK analysis failed for {repo_path}: {result.stderr}")


def calculate_averages(csv_file, project_name, stars, releases, age):
    try:
        df = pd.read_csv(csv_file)
        df.fillna(0, inplace=True)
        if df.size == 0:
            return {
                "project_name": project_name,
                "average_cbo": 0.0,
                "average_dit": 0.0,
                "average_lcom": 0.0,
                "sum_loc": 0,
                "stars": stars,
                "releases": releases,
                "age": age
            }
        avg_cbo = df['cbo'].mean()
        avg_dit = df['dit'].mean()
        avg_lcom = df['lcom*'].mean()
        sum_loc = df['loc'].sum()

        return {
            "project_name": project_name,
            "average_cbo": avg_cbo,
            "average_dit": avg_dit,
            "average_lcom": avg_lcom,
            "sum_loc": sum_loc,
            "stars": stars,
            "releases": releases,
            "age": age
        }
    except Exception as e:
        print(f"Failed to calculate averages from {csv_file}: {e}")
        return {
            "project_name": project_name,
            "average_cbo": 0.0,
            "average_dit": 0.0,
            "average_lcom": 0.0,
            "sum_loc": 0,
            "stars": stars,
            "releases": releases,
            "age": age
        }


def save_averages_to_csv(averages):
    file_exists = os.path.isfile(AVERAGES_CSV_PATH)
    with open(AVERAGES_CSV_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=["project_name", "average_cbo", "average_dit", "average_lcom", "sum_loc",
                                            "stars", "releases", "age"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(averages)
        print(f"Saved averages to {AVERAGES_CSV_PATH}")


def calculate_repo_age(created_at):
    created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    age = (datetime.now() - created_date).days / 365.25
    return round(age, 2)


def main():
    N = 1000
    repos = fetch_repositories(N)
    process_repositories_analysis(repos)


if __name__ == "__main__":
    main()

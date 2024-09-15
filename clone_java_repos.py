import requests
import subprocess
import os
import csv
import pandas as pd

API_URL = "https://api.github.com/graphql"
GITHUB_TOKEN = ""
CK_JAR_PATH = ""
CK_OUTPUT_PATH = ""
PROJECTS_PATH = ""
AVERAGES_CSV_PATH = os.path.join(PROJECTS_PATH, "averages.csv")


def fetch_repositories(n_repos):
    query = """
    query getTopRepos($nRepos: Int!) {
      search(query: "language:Java sort:stars-desc", type: REPOSITORY, first: $nRepos) {
        edges {
          node {
            ... on Repository {
              name
              owner {
                login
              }
              url
            }
          }
        }
      }
    }
    """

    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    variables = {"nRepos": n_repos}

    response = requests.post(API_URL, json={"query": query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "errors" in data:
            raise Exception(f"Error in GraphQL response: {data['errors']}")
        return data["data"]["search"]["edges"]
    else:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")


def process_repositories_analysis(repos):
    for repo in repos:
        repo_url = repo['node']['url']
        repo_name = repo['node']['name']
        owner = repo['node']['owner']['login']
        local_repo_path = os.path.join(PROJECTS_PATH, repo_name)

        print(f"Cloning repository {owner}/{repo_name} from {repo_url} into {local_repo_path}")
        subprocess.run(["git", "clone", repo_url, local_repo_path])

        run_ck(local_repo_path, repo_name)


def run_ck(repo_path, repo_name):
    ck_command = [
        "java", "-jar", CK_JAR_PATH, repo_path, "true", "0", "true", CK_OUTPUT_PATH
    ]

    print(f"Running CK on {repo_path}")
    result = subprocess.run(ck_command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"CK analysis completed successfully for {repo_path}")
        csv_file = os.path.join("/Users/fernandoluciocouto/Documents/fernando/lab-ck", "outputclass.csv")
        averages = calculate_averages(csv_file, repo_name)
        save_averages_to_csv(averages)
    else:
        print(f"CK analysis failed for {repo_path}: {result.stderr}")


def calculate_averages(csv_file, project_name):
    try:
        df = pd.read_csv(csv_file)
        df.fillna(0, inplace=True)
        if df.size == 0:
            return {
                "project_name": project_name,
                "average_cbo": 0.0,
                "average_dit": 0.0,
                "average_lcom": 0.0
            }
        avg_cbo = df['cbo'].mean()
        avg_dit = df['dit'].mean()
        avg_lcom = df['lcom'].mean()

        return {
            "project_name": project_name,
            "average_cbo": avg_cbo,
            "average_dit": avg_dit,
            "average_lcom": avg_lcom
        }
    except Exception as e:
        print(f"Failed to calculate averages from {csv_file}: {e}")
        return {
            "project_name": project_name,
            "average_cbo": 0.0,
            "average_dit": 0.0,
            "average_lcom": 0.0
        }


def save_averages_to_csv(averages):
    file_exists = os.path.isfile(AVERAGES_CSV_PATH)
    with open(AVERAGES_CSV_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["project_name", "average_cbo", "average_dit", "average_lcom"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(averages)
        print(f"Saved averages to {AVERAGES_CSV_PATH}")


def main():
    N = 5
    repos = fetch_repositories(N)
    process_repositories_analysis(repos)


if __name__ == "__main__":
    main()

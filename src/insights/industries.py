from typing import List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path, 'r') as file:
        output = []
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in content:
            output.append(job)
        return output


def get_unique_industries(path: str) -> List[str]:
    content = read(path)
    uniques_industries = []
    for row in content:
        industries = row["industry"]
        if industries not in uniques_industries and len(industries) > 0:
            uniques_industries.append(industries)
    return uniques_industries
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    output = []
    for job in jobs:
        if job["industry"] == industry:
            output.append(job)
    return output
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

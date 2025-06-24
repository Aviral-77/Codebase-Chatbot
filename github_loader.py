# github_loader.py

from llama_index.readers.github import GithubRepositoryReader, GithubClient
from config import GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO, GITHUB_BRANCH, IGNORE_MEDIA_EXTENSIONS, IGNORE_DIRECTORIES

github_client = GithubClient(GITHUB_TOKEN)

def load_github_documents():
    reader = GithubRepositoryReader(
        github_client=github_client,
        owner=GITHUB_OWNER,
        repo=GITHUB_REPO,
        filter_directories=(IGNORE_DIRECTORIES, GithubRepositoryReader.FilterType.EXCLUDE)
        if IGNORE_DIRECTORIES else None,
        filter_file_extensions=(IGNORE_MEDIA_EXTENSIONS, GithubRepositoryReader.FilterType.EXCLUDE),
        verbose=True,
    )
    return reader.load_data(branch=GITHUB_BRANCH)

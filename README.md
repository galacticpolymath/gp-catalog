# README
build.py - Netlify runs this to crawl the repo and generate an index.html file browser

### Indexing and Algolia

.github/workflows/index.yml - the Action that runs on any push to the repo, triggers index and Algolia update

index.py - the script that scans the repo and generates index.json

algolia.py - the script that uploads index.json to algolia

### Auto-pushing:

build.yml - template. place in a new repo's /.github/workflows/build.yml and edit src and dst directories as necessary. enables auto-pushes

Auto-push also requires permission for Actions to read the repo. Add your personal access token to the Secrets in Settings as an admin/owner of the new lesson repo.

#!/bin/bash

# Init env vars
date=`date`
workDir=`pwd`
sshCommand="ssh -v" # Add -v, -vv, or -vvv for verbose debugging

gitBranch=`git rev-parse --abbrev-ref HEAD`
if [ -n "$CF_PAGES" ]
then
    echo "We are on Cloudflare Pages. Retrieve branch from env."
    gitBranch=$CF_PAGES_BRANCH
fi
gitCommitMessage="branch $gitBranch on $date"
redotDocsLiveBranch=${1:-develop}

inputDir="."
migrateDir="_migrated"
sphinxDir="_sphinx"
repoDir="_repo"

liveRoot="redot-docs-live"
liveRepo="git@github.com:Redot-Engine/$liveRoot.git"
buildDir="html/en/$gitBranch" # TODO: implement i18n support

# Report vars and intention
echo "Building $gitCommitMessage"
echo "Live branch: $redotDocsLiveBranch"
echo "Live root: $liveRoot, live repo: $liveRepo, build dir: $buildDir, report dir: $reportDir"
echo "Temp dirs: $migrateDir, $sphinxDir, $repoDir"

echo "Delete temp dirs"
rm -rf $migrateDir
rm -rf $sphinxDir
rm -rf $repoDir

echo "Migrate Godot to Redot"
mkdir -p $migrateDir
python migrate.py $inputDir $migrateDir

echo "Translate to html"
mkdir -p $sphinxDir
sphinx-build -b html -j 4 $migrateDir $sphinxDir

echo "DUMMY FILE FOR TESTING: $date" > $sphinxDir/test.html

echo "Cloning $liveRepo $repoDir"
git clone $liveRepo $repoDir

cd $repoDir
echo "Checking out $redotDocsLiveBranch"
git checkout $redotDocsLiveBranch

git config core.sshCommand "$sshCommand"
echo "Using ssh command: $sshCommand"

if [ -n "$CF_PAGES" ]
then
    echo "We are on Cloudflare Pages. Setting custom ssh key and method"
    # HACK: Remove annoying https redirect. I presume this was used by Cloudflare
    echo "Remove Cloudflare redirect."
    insteadof=`git config --list | grep insteadof`
    remove=`echo $insteadof | cut -d "=" -f 1`
    git config --global --unset $remove

    mkdir ~/.ssh
    echo "$BUILD_SSH_KEY" > ~/.ssh/id_ed25519
    echo "$BUILD_SSH_KEY_PUB" > ~/.ssh/id_ed25519.pub
    echo "$KNOWN_HOSTS" > ~/.ssh/known_hosts

    chmod 0600 ~/.ssh/id_ed25519
    chmod 0600 ~/.ssh/id_ed25519.pub
    chmod 0644 ~/.ssh/known_hosts
    chmod 0755 ~/.ssh
    
    # Init git
    git remote set-url origin git@github.com:Redot-Engine/redot-docs-live.git

    echo "Setting credentials"
    git config user.email "noreply_pages_bot@cloudflare.com"
    git config user.name "Redot Docs Build Worker"
fi

echo "### GIT CONFIG VALUES ###"
git config core.pager cat
git config --list

echo "Copying generated content to repository"
echo "mkdir -p $buildDir"
mkdir -p $buildDir
echo "cp -r ../$sphinxDir/* $buildDir"
cp -r ../$sphinxDir/* $buildDir

echo "Commit and push to $redotDocsLiveBranch, with message $gitCommitMessage"
git add .
git commit --message "$gitCommitMessage"
git push --force

# Create some output so Cloudflare is happy
cd ..
mkdir -p ./output
echo "Build finished. Commit message: $gitCommitMessage" > ./output/index.html

echo "Done. Made by @Craptain"

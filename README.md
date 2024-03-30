# Project-Book-bot
Book bot or a command-line application in Python that does static         analysis on text files.

 TLDR:
ctrl + s
git add .
git commit -m "description of changes"
git push origin main



# STAGE THE CHANGE
First, let's stage the change. Run this command from the root(bookbot) of your repo in the terminal. Use CD to get where you want, ls to check content. Bookbot is in /workspace/github.com/hannes-tarach/bookbot

Run this command:
# git add .

The "." tells git to stage all the changes in the directory and all subdirectories. If you only wanted to stage specific files, you could list the files one by one. I use the "." to stage everything in the repo 99% of the time. If you need git to ignore files in your project, you can use a .gitignore file, which we'll cover later.

# COMMIT THE CHANGE
Next, we'll commit the change with a message. The commit message will be stored in git alongside the change. In the future, if you wanted to revert this change, or jump back in time to the code at this state, you would use the commit message to find the right change. As such, try to use a descriptive commit message!

Run this command:
# git commit -m "description of changes"

# PUSH THE CHANGE TO GITHUB
Now that your change has been committed locally, you should notice that your source control tab on the left no longer has a blue notification - all your changes are committed! However, the commit hasn't been pushed up to GitHub yet for safekeeping. Run this command:

Run this command:
# git push origin main



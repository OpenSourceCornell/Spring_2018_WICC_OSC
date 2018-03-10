# WICC & OpenSourceCornell Git Workshop

This is the repository for the WICC & OSC git workshop on Wednesday, March 7, 2018. It contains many Python functions that need to be implemented! Contributing guidelines are [laid out below](#Contributing).

## Contributing
If you want to implement a specific function, please follow the following steps:
1. First, comment on the issue for that function you want to implement, so others know you are working on it.
2. On Github, fork the repository (see [this article](https://help.github.com/articles/fork-a-repo/)).
3. Clone the repository to your local machine (see [this article](https://help.github.com/articles/cloning-a-repository/)).
4. Create a new branch with `git checkout -b [function-name]`.
5. Implement the function, ensuring that the function passes the corresponding test cases (see the [Testing section](#Testing)).
6. Commit you work (using `git add [file]` and `git commit`).
7. Push your commit to your repository on Github (using `git push`).
8. Submit a pull request on the WICC & OSC repository, requesting that your code be merged into the repository (see [this article](https://help.github.com/articles/creating-a-pull-request/)).
9. Wait for your pull request to be merged into master.

Thank you for any contributions!

## Testing
To test a specific function, do the following: first, ensure you are in the `testing` subdirectory by running `cd testing` from the root of the project. Then, run `python [function-name]_test.py` to test the code.

## Reviewing
In addition to implementing functions, we also need some help reviewing contributions to ensure they are implemented correctly. You can test the code using the following instructions:
1. First, find a pull request with the "Needs Testing" label.
2. On the issue, there should be a comment that says which branch the pull request is on.
3. From you local machine, type `git fetch` to get any latest changes, then checkout the pull request using `git checkout origin/[branch-name]`.
  - This should make git complain about a "Detached HEAD" state, but this is fine for testing purposes.
4. Test the code as shown in the [Testing section](#Testing).
5. Comment on the pull request on Github, say whether the code works for you or if it has issues.
6. Feel free to also review the code itself, and make any suggestions!

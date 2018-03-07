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

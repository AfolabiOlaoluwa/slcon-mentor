## Contribution Guidelines

### Workflow
1. Fork this repo
2. Create a feature or fix branch off `develop` (don't work from `master` or `develop`)
2. Add your feature / fix bug, etc.
3. Run tests and make sure they are passing
4. _Git Rebase_
5. Create the Pull Request

### Recommended Commit Message Format
We recommend this commit message format:

```
(<tag>) Commit message

commit message body

<fixes/closes/ref> <issue-number>
```

The major tags are:
- _feature_: The commit adds a particular feature
- _chore_: The commit is just some routine work, e.g. refactoring, renaming of file, etc.
-  _fix_: The commit fixes a bug, etc.

Here is an **example**:

```
(feature) Add login with GitHub

This commits integrate social login with GitHub. I used the Python Social Auth library - https://github.com/omab/python-social-auth

closes #78782
```

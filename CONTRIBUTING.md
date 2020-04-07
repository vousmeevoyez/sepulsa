Hello! Thank you for choosing to help contribute to Oy-Client. There are many ways you can contribute and help is always welcome.  We simply ask that you follow the following contribution policies.

All third party contributors acknowledge that any contributions they provide will be made under the same open source license that the open source project is provided under.

- [Feature Request](#feature-request)
- [Submit a Bug Report](#submit-a-bug-report)
  - [Please use our Bug Report Template](#please-use-our-bug-report-template)
- [Improvements to the Codebase](#improvements-to-the-codebase)
  - [Development Environment](#development-environment)
    - [1. Install and Run Locally](#2-install-and-run-locally)
      - [Prerequisites](#prerequisites)
      - [Initial setup:](#initial-setup)
  - [Environment Variables](#environment-variables)
      - [Execute:](#execute)
- [Understanding the Code Base](#understanding-the-code-base)
- [Testing](#testing)
  - [Testing Multiple Versions of Python](#testing-multiple-versions-of-python)
    - [Prerequisites:](#prerequisites)
    - [Initial setup:](#initial-setup-1)
    - [Execute:](#execute-1)
- [Style Guidelines & Naming Conventions](#style-guidelines--naming-conventions)
- [Creating a Pull Request<a name="creating-a-pull-request"></a>](#creating-a-pull-requesta-name%22creating-a-pull-request%22a)
- [Code Reviews](#code-reviews)

<a name="roadmap"></a>
We use [Milestones](https://github.com/vousmeevoyez/oy-client/milestones) to help define current roadmaps, please feel free to grab an issue from the current milestone. Please indicate that you have begun work on it to avoid collisions. Once a PR is made, community reviews, comments, suggestions, and additional PRs are welcomed and encouraged.

There are a few ways to contribute, which we'll enumerate below:

<a name="feature-request"></a>
## Feature Request

If you'd like to make a feature request, please read this section.

The GitHub issue tracker is the preferred channel for library feature requests, but please respect the following restrictions:

- Please **search for existing issues** in order to ensure we don't have duplicate bugs/feature requests.
- Please be respectful and considerate of others when commenting on issues

<a name="submit-a-bug-report"></a>
## Submit a Bug Report

Note: DO NOT include your credentials in ANY code examples, descriptions, or media you make public.

A software bug is a demonstrable issue in the code base. In order for us to diagnose the issue and respond as quickly as possible, please add as much detail as possible into your bug report.

Before you decide to create a new issue, please try the following:

1. Check the GitHub issues tab if the identified issue has already been reported, if so, please add a +1 to the existing post.
2. Update to the latest version of this code and check if the issue has already been fixed
3. Copy and fill in the Bug Report Template we have provided below

### Please use our Bug Report Template

In order to make the process easier, we've included a [sample bug report template]((https://github.com/vousmeevoyez/oy-client/ISSUE_TEMPLATE.md)) (borrowed from [Ghost](https://github.com/TryGhost/Ghost/)). The template uses [GitHub flavored markdown](https://help.github.com/articles/github-flavored-markdown/) for formatting.

<a name="improvements-to-the-codebase"></a>
## Improvements to the Codebase

We welcome direct contributions to the code base. Thank you!

### Development Environment ###
#### 1. Install and Run Locally ####

##### Prerequisites #####

- Python 3.6+
- [requests](https://requests.readthedocs.io/en/master/)

##### Initial setup: #####

```bash
git clone https://github.com/vousmeevoyez/oy-client.git
cd oy-client
```

### Credentials

First, get your development credentials from [here](https://api-docs.oyindonesia.com/#partner-callback).

Next, supply your credentials

```
from oy import build_client
oy_client = build_client("https://sandbox.oyindonesia.com/staging/partner", "username", "api-key")
```

##### Execute: #####

See the [examples folder](https://github.com/vousmeevoyez/oy-client/tree/master/examples) to get started quickly.

If testing from the root directory of this repo, create a new file (e.g. test.py) and replace `import oy-client` with `from oy-client import *`

<a name="understanding-the-codebase"></a>
## Understanding the Code Base

**/examples**

Working examples that demonstrate usage.

**/test**

Currently, we have unit and integration tests.

**/oy**

Main code where all our logic and handling stored.

<a name="testing"></a>
## Testing

The PR must pass all the tests before it is reviewed.

All test files are in the [`test`](https://github.com/vousmeevoyez/oy-client/test) directory.

Test runner is using pytest + pytest-cov

`pytest`
or using our Makefile tool
```
make check-coverage
```

<a name="style-guidelines-and-naming-conventions"></a>
## Style Guidelines & Naming Conventions

Generally, we follow the style guidelines as suggested by the official language. However, we ask that you conform to the styles that already exist in the library. If you wish to deviate, please explain your reasoning.

- [PEP8](https://www.python.org/dev/peps/pep-0008/)

Please run your code through:

- [pyflakes](https://pypi.python.org/pypi/pyflakes)
- [pylint](https://www.pylint.org/)
- [pep8](https://pypi.python.org/pypi/pep8)

To validate is your code already follow our guideline and pass the ci, you can run
```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --max-complexity=10
```
We also have some static analysis such as Maintainability Index, Raw Metric, Cyclomatic Complexity and Halstead Metric reported using radon
so we know which part of code can be improved.
- [radon](https://pypi.org/project/radon/)
```
make check-cc
make check-mi
make check-raw
make check-hal
```

## Creating a Pull Request<a name="creating-a-pull-request"></a>

1. [Fork](https://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/vousmeevoyez/oy-client.git

   # Navigate to the newly cloned directory
   cd oy-client

   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/vousmeevoyez/oy-client
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout master
   git pull upstream master
   ```

3. Create a new topic branch (of the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely to be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4a. Create tests.

4b. Create or update the example code that demonstrates the functionality of this change to the code.

5. Locally merge (or rebase) the upstream development branch into your topic branch:

   ```bash
   git pull [--rebase] upstream master
   ```

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

7. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description against the `master` branch. All tests must be passing before we will review the PR.

If you have any additional questions, please feel free to [email](mailto:kelvindsmn@gmail.com) us or create an issue in this repo.

<a name="code-reviews"></a>
## Code Reviews
If you can, please look at open PRs and review them. Give feedback and help us merge these PRs much faster! If you don't know how, GitHub has some great [information on how to review a Pull Request](https://help.github.com/articles/about-pull-request-reviews/).

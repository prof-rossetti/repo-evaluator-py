# Project Planning

## Problem Statement

### Primary User

Me (a professor who asks students to submit deliverables as github repositories).

### User Needs Statement 

As a professor who asks students to submit deliverables as github repositories, 
I need a quicker way of downloading all student repositories before I grade them on my local machine.
And also it would be nice to automate as much of the grading process as possible.

### As-is Process Description

  1. Obtain a list of student repository URLs.
  2. For each repository:
     + Visit its URL in a browser.
     + Click the "clone or download" button to reveal its remote address.
     + From the command line, download the repo using a `git clone` command.
     + Manually check the repository for existence of certain files, and record the results in a Google Sheet gradebook.

### To-be Process Description

  1. Obtain a list of student repository URLs.
  2. Run a script to automatically download all the repositories and check for existence of specified files, and produce a CSV file report of the results.
  3. Upload the CSV file report into the Google Sheets gradebook.


## Information Requirements

### Information Inputs

  1. A `submissions.csv` file containing a list of student repository submissions, including github usernames and repository URLs.
  2. A `filepaths.csv` file contining a list of files expected to exist in each repository.
  
### Information Outputs

  1. Local copies of all the student repository directories.
  2. A `results.csv` file containing the results of the file-checking process.

## Technology Requirements

### APIs and Web Service Requirements

I thought I might need to use the [GitHub API](https://developer.github.com/v3/) to download all files in a given repository, 
but then I came to the conclusion it would be easier to use command-line Git.

### Python Package Requirements

The application does not require any third-party packages, except `pytest` for testing purposes.

The application does however make extensive use of the `os` and `csv` modules. 
And after performing some Internet research, 
I learned I can use the `subprocess` module to perform system commands like `git clone`.

### Hardware Requirements

The application will be running on my own local machine. I have no plans to deploy this application to a public server.

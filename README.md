# recommenders

### Git process 
- give general overview of project with gitworkflow, links to other README.md and docs 
- Everything get run from run.py (makes reusing code within the project super easy)
  - make sure any new directory gets an ``` __init__.py ``` and you can import it 
  - see [build_parsers.py](src/parsers/build_parsers.py) for an example
- parsers for each thing you want to do within the repo go in to parsers and you have to update build_parsers.py to add it to general run.py functionality
- templates:
  <!-- - [msr.md](.gitlab/issue_templates/msr.md)
  - [results.md](.gitlab/issue_templates/results.md)
  - [feature.md](.gitlab/issue_templates/feature.md)
  - [bug_report.md](.gitlab/issue_templates/bug_report.md)
  - [meeting_minutes.md](.gitlab/issue_templates/msr.md) -->

## Git Workflow For Feature Off Milestone branch:

1. Create a new branch for the milestone you're working on if there isn't one yet: 
```
$ git checkout -b milestone_branch
```

2. Create a new feature branch that tracks off of the milestone_branch: 
```
$ git checkout -b myFeature milestone_branch 
```

3. Do your work
```
$ git commit -am "Your message"
```

4. Now merge your changes to milestone_branch without a fast-forward: 
```
$ git checkout milestone_branch
$ git merge --no-ff myFeature
```

5. Now push changes to the server
```
$ git push origin milestone_branch
$ git push origin myFeature
```
## Other Info
- expand


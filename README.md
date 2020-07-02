# 2020SummerDataProject
Sample data project using notebooks(through Kaggle) and GitHub.

Aims to create a clean workflow for collaborating on a notebook project using github for revision management. Kaggle could also be replaced with another notebook host down the road if needed.


Under .github/workflow/ there are action files that define how the Kaggle kernel deployment happens. These can be edited to purpose. 
These are ingested by github under the actions pane and the provided one will automatically run on a git "push" to @master
This action requires a Kaggle deployment file, "kernel-metadata.json", which is used by the action for the push to a Kaggle notebook.

#Typical Workflow Example
1) LocalMachine: git push -> github@master
2) GitHub: Installs to the docker container all the Python modules required for the actions to follow
3) GitHub: Git action clones the project into the Docker container used for "actions".
           This all happens in Docker containers hence the need to pull itself via git, before pushing it to Kaggle.
4) GitHub: Uses the Kaggle module installed earlier and the "kaggle-metadata.json" file to push to a Kaggle notebook(public) and run
5) Kaggle: Launches the ipynb file specified in the "kaggle-metadata.json" as it creates the running notebook.
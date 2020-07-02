# 2020SummerDataProject

Under .github/workflow/ there are action files that define how the Kaggle kernel deployment happens. 
These are ingested by github under the actions pane and the provided one will automatically run on a git "push" to @master

This action requires a kaggle deployment file, "kernel-metadata.json", which is used by the action for the push to a Kaggle notebook.

1) localmachine: git push -> github@master
2) github: installs to the docker container all the python modules required for the actions to follow
3) github:  Git action clones the project into the docker container used for "actions".
            This all happens in docker containers hence the need to pull itself, before pushing it.
4) github: uses the kaggle module installed earlier and our "kaggle-metadata.json" file to push to a Kaggle notebook(public) and run
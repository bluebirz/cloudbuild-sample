# cloudbuild-sample

```bash
gcloud beta builds triggers create cloud-source-repositories \
--name=cloudbuild-sample-main \
--repo=github_bluebirz_cloudbuild-sample \
--branch-pattern=^main$ \
--build-config=cloudbuild.yaml
```

```bash
gcloud beta builds triggers create github \
--name=cloudbuild-sample-main \
--region=global \
--repo-name=cloudbuild-sample \
--repo-owner=bluebirz \
--branch-pattern=^main$ \
--build-config=cloudbuild.yaml 
```
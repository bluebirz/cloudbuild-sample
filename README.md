# cloudbuild-sample

## about

- This is an example of Google Cloud Build
- `contents` contains JSON files: `students.json`
- `cloudbuild.yaml` is a build configuration in Google Cloud Build format
- Purpose is to validate the JSON files before uploading them to GCS bucket

## blog related

- [Blog] [Automate your project with Google Cloud Build](https://bluebirz.net/posts/automate-your-project-with-gcb/)
- [Medium] [Automate your project with Google Cloud Build](https://medium.com/@bluebirz/automate-your-project-with-google-cloud-build-d37a01e4d763)

## How to run

1. Create a trigger

   - Github app

    ```bash
    gcloud beta builds triggers create github \
    --name=cloudbuild-sample-main \
    --region=global \
    --repo-name=cloudbuild-sample \
    --repo-owner=bluebirz \
    --branch-pattern=^main$ \
    --build-config=cloudbuild.yaml 
    ```

   - Mirror on Google Cloud Source Repository

    ```bash
    gcloud beta builds triggers create cloud-source-repositories \
    --name=cloudbuild-sample-main \
    --repo=github_bluebirz_cloudbuild-sample \
    --branch-pattern=^main$ \
    --build-config=cloudbuild.yaml
    ```

2. Commit and push
3. Verify build result
4. Verify GCS bucket blobs result

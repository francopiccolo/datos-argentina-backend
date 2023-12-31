gcloud config set project economia-399616
gcloud iam service-accounts create datos-argentina-backend \
    --description="datos-argentina-backend" \
    --display-name="datos-argentina-backend"
gcloud projects add-iam-policy-binding economia-399616 \
    --member="serviceAccount:datos-argentina-backend@economia-399616.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.writer"
gcloud projects add-iam-policy-binding economia-399616 \
    --member="serviceAccount:datos-argentina-backend@economia-399616.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.writer"
gcloud projects add-iam-policy-binding economia-399616 \
    --member="serviceAccount:datos-argentina-backend@economia-399616.iam.gserviceaccount.com" \
    --role="roles/run.developer"
gcloud iam service-accounts add-iam-policy-binding \
  310594583464-compute@developer.gserviceaccount.com \
  --member="serviceAccount:datos-argentina-backend@economia-399616.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
gcloud projects add-iam-policy-binding economia-399616 \
    --member="serviceAccount:datos-argentina-backend@economia-399616.iam.gserviceaccount.com" \
    --role="roles/bigquery.admin"

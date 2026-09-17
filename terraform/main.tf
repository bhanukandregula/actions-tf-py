resource "google_cloud_run_v2_service" "fastapi" {
  name     = var.service_name
  location = var.region

  template {
    containers {
      image = var.image

      ports {
        container_port = 8080
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public" {
  name     = google_cloud_run_v2_service.fastapi.name
  location = google_cloud_run_v2_service.fastapi.location

  role   = "roles/run.invoker"
  member = "allUsers"
}

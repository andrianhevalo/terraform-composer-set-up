terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {

  credentials = "/Users/andrianhevalo/Desktop/terraform-hw-351820-ba41fd0d7698.json"
  project = "terraform-hw-351820"
  region  = "us-central1"
}

resource "google_project_service" "composer_api" {
  provider = google
  project = "terraform-hw-351820"
  service = "composer.googleapis.com"
  disable_on_destroy = false
}

resource "google_composer_environment" "environment-hw" {
  provider = google
  name = "environment-hw"

}
# SOFE4630U – Milestone 2  
## Data Storage and Integration Connectors

This repository contains the source code and configuration files for
SOFE 4630U – Milestone 2.

### Technologies Used
- Google Cloud Platform (GCP)
- Google Kubernetes Engine (GKE)
- Google Pub/Sub
- Application Integration
- Integration Connectors
- MySQL
- Redis
- Python

### Repository Structure

- **MySQL-connector/**
  - `smartMeter.py` – Publishes smart meter readings to Pub/Sub

- **Redis-connector/**
  - `produceImage.py` – Publishes base64-encoded image data to Pub/Sub
  - `ReceiveImage.py` – Retrieves and reconstructs image data from Redis
  - `ontarioTech.jpg` – Sample image used for Redis integration

- **mySQL/**
  - Kubernetes deployment and service YAML files for MySQL

- **Redis/**
  - Kubernetes deployment YAML file for Redis

### Notes
- Google Cloud credentials are not included in this repository.
- Integrations, connectors, and databases were configured directly
  through the Google Cloud Console as described in the report.

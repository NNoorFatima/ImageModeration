# Image Moderation API

This project is a lightweight image moderation API built with **FastAPI**. It allows authenticated users to submit images for moderation and receive AI-generated scores for **nudity**, **violence**, **self-harm**, and **hate symbols**.

The API also logs usage data to MongoDB and provides an admin-authenticated token generation endpoint. The project is containerized using Docker and automatically builds & pushes to DockerHub using GitHub Actions.



##  Features

-  Token-based authentication (`/auth/tokens`)
-  Image moderation via `POST /moderate/`
-  MongoDB-based usage logging
-  Dockerized backend for easy deployment
-  GitHub Actions for CI/CD
-  Lightweight HTML frontend to test the API



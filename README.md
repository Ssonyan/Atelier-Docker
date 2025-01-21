# Docker Multi-Service Application

This project demonstrates a production-ready Docker setup with multiple services:
- React Frontend (Vite)
- Python Flask Backend
- Nginx Reverse Proxy
- PostgreSQL Database
- Portainer for cluster management

## Project Structure

```
.
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/
│   ├── nginx.conf
│   └── Dockerfile
├── src/
│   └── ... (React frontend files)
├── docker-compose.yml
├── docker-compose.swarm.yml
└── README.md
```

## Development Setup

1. Start the development environment:
   ```bash
   docker compose up --build
   ```

2. Access the services:
   - Frontend: http://localhost
   - Backend API: http://localhost/api
   - Portainer: http://localhost:9000

## Production Deployment (Docker Swarm)

1. Initialize Docker Swarm:
   ```bash
   docker swarm init
   ```

2. Create required secrets:
   ```bash
   echo "your-secure-password" | docker secret create db_password -
   ```

3. Deploy the stack:
   ```bash
   docker stack deploy -c docker-compose.swarm.yml myapp
   ```

4. Scale services:
   ```bash
   docker service scale myapp_flask=5
   ```

## Features

- Multi-stage builds for optimized images
- Health checks for all services
- Resource limits and constraints
- Secure communication between services
- Persistent volumes for data storage
- Zero-downtime deployments
- Load balancing and service discovery

## Security Considerations

- Internal network for database access
- Secrets management for sensitive data
- No direct database exposure
- Minimal base images
- Regular security updates

## Monitoring and Management

Access Portainer at http://localhost:9000 for:
- Container management
- Service scaling
- Log viewing
- Resource monitoring
- Network management
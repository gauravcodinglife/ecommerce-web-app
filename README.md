# eCommerce Local App

Local development environment for the eCommerce microservices application.
Uses Docker Compose + LocalStack to simulate AWS services entirely on your machine.

**Author**: Chetan Agrawal  
**Website**: [www.awswithchetan.com](https://www.awswithchetan.com)

> For AWS deployment, see the [ecommerce-web-app](https://github.com/awswithchetan/ecommerce-web-app) repo.

## Architecture

### AWS Reference Architecture
<img width="800" height="450" alt="project-architecture" src="https://github.com/user-attachments/assets/b08a6351-e907-49aa-8c4b-4a796e301c15" />

### Local Stack
| AWS Service | Local Equivalent |
|---|---|
| DynamoDB | LocalStack |
| SNS / SQS / SES | LocalStack |
| RDS PostgreSQL | PostgreSQL container |
| ALB + API Gateway | Nginx |
| Cognito | Real AWS Cognito (free tier) |

## Quick Start

1. **Install prerequisites** — `bash install-prerequisites.sh`
2. **Set up Cognito** — create a User Pool in AWS Console
3. **Configure frontend** — add your Cognito IDs to `frontend/react-app/src/aws-config.js`
4. **Start backend** — `cd local-deployment && AWS_REGION=<region> docker compose up -d`
5. **Load products** — `cd local-deployment/data && bash load-products-local.sh <region>`
6. **Start frontend** — `cd frontend/react-app && npm install && npm start`

See [local-deployment/README.md](local-deployment/README.md) for detailed steps.

## Project Structure

```
ecommerce-local-app/
├── services/
│   ├── product-service/
│   ├── cart-service/
│   ├── user-service/
│   ├── order-service/
│   └── notification-service/
├── frontend/
│   └── react-app/
├── local-deployment/
│   ├── docker-compose.yml
│   ├── nginx.conf
│   ├── localstack-init/
│   └── data/
└── install-prerequisites.sh
```

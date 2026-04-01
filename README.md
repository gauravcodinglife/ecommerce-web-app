# eCommerce Local App

Local development environment for the eCommerce microservices application.
Uses Docker Compose + LocalStack to simulate AWS services entirely on your machine.

**Author**: Chetan Agrawal  
**Website**: [www.awswithchetan.com](https://www.awswithchetan.com)

> For AWS deployment, see the [ecommerce-web-app](https://github.com/YOUR_USERNAME/ecommerce-web-app) repo.

## What's Included

- All 5 microservices (product, cart, user, order, notification)
- LocalStack (DynamoDB, SNS, SQS, SES emulation)
- PostgreSQL
- Nginx (API Gateway simulator)
- React frontend (run separately via npm)

## Quick Start

### 1. Prerequisites

```bash
./install-prerequisites.sh
```

Requires: Docker, Docker Compose, Node.js, AWS CLI (with dummy credentials for LocalStack)

### 2. Configure

```bash
cp local-deployment/.env.example local-deployment/.env
# Edit .env and set AWS_REGION (e.g. us-east-1)
```

### 3. Start services

```bash
cd local-deployment
docker compose up --build
```

### 4. Load product data

```bash
cd local-deployment
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test ./data/load-products-local.sh us-east-1
```

### 5. Start frontend

```bash
cd frontend/react-app
npm install
npm start
```

Frontend runs at http://localhost:3000, API at http://localhost:8080/api

## Notification Service

Order notifications are written to `local-deployment/emails/` as text files instead of being emailed. Check that directory after placing an order.

## Project Structure

```
ecommerce-local-app/
├── services/
│   ├── product-service/
│   ├── cart-service/
│   ├── user-service/
│   ├── order-service/
│   └── notification-service/   # Polls SQS, saves emails to file
├── frontend/
│   └── react-app/
├── local-deployment/
│   ├── docker-compose.yml
│   ├── nginx.conf
│   ├── localstack-init/        # Auto-creates DynamoDB tables, SNS, SQS on startup
│   └── data/                   # Product data + load script
└── install-prerequisites.sh
```
